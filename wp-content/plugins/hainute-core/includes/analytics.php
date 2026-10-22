<?php
/**
 * Monitorizare utilizatori: vizite (ce pagini), sursa traficului (facebook,
 * instagram, google...), click-uri pe magazine (afiliate + externe).
 *
 * Conversiile (comenzile) NU se pot urmări pe site-ul nostru — se întâmplă pe
 * site-ul magazinului. Ele vin din dashboard-ul rețelei de afiliere (CJ/2P/
 * Profitshare) sau printr-un postback dacă rețeaua îl suportă. Aici măsurăm ce
 * putem: intrări, sursă și click-uri outbound (intenția de cumpărare).
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function hainute_events_table() {
	global $wpdb;
	return $wpdb->prefix . 'hainute_events';
}

/** Creează tabelul de evenimente (o dată). */
function hainute_analytics_install() {
	global $wpdb;
	$table   = hainute_events_table();
	if ( get_option( 'hainute_events_installed' ) === '1' && $wpdb->get_var( "SHOW TABLES LIKE '$table'" ) === $table ) {
		return;
	}
	require_once ABSPATH . 'wp-admin/includes/upgrade.php';
	$charset = $wpdb->get_charset_collate();
	dbDelta(
		"CREATE TABLE $table (
			id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
			created_at DATETIME NOT NULL,
			session VARCHAR(40) NOT NULL DEFAULT '',
			type VARCHAR(20) NOT NULL DEFAULT 'view',
			source VARCHAR(40) NOT NULL DEFAULT '',
			referer VARCHAR(255) NOT NULL DEFAULT '',
			path VARCHAR(255) NOT NULL DEFAULT '',
			product_id BIGINT UNSIGNED NOT NULL DEFAULT 0,
			store VARCHAR(80) NOT NULL DEFAULT '',
			PRIMARY KEY (id),
			KEY created_at (created_at),
			KEY type (type),
			KEY source (source),
			KEY product_id (product_id)
		) $charset;"
	);
	update_option( 'hainute_events_installed', '1' );
}
add_action( 'init', 'hainute_analytics_install' );

/** Derivă sursa din utm_source sau din host-ul referer-ului. */
function hainute_analytics_source( $referer, $utm ) {
	$utm = strtolower( trim( (string) $utm ) );
	if ( '' !== $utm ) {
		return substr( preg_replace( '/[^a-z0-9_-]/', '', $utm ), 0, 40 );
	}
	$host = strtolower( (string) wp_parse_url( (string) $referer, PHP_URL_HOST ) );
	if ( '' === $host ) {
		return 'direct';
	}
	$map = array(
		'facebook' => 'facebook', 'fb.' => 'facebook', 'fb.me' => 'facebook', 'l.facebook' => 'facebook',
		'instagram' => 'instagram', 'l.instagram' => 'instagram',
		'google' => 'google', 'bing' => 'bing', 'yahoo' => 'yahoo', 'duckduckgo' => 'duckduckgo',
		'tiktok' => 'tiktok', 'youtube' => 'youtube', 'youtu.be' => 'youtube',
		't.co' => 'twitter', 'twitter' => 'twitter', 'x.com' => 'twitter',
		'pinterest' => 'pinterest', 'whatsapp' => 'whatsapp', 'telegram' => 'telegram', 't.me' => 'telegram',
	);
	foreach ( $map as $needle => $src ) {
		if ( false !== strpos( $host, $needle ) ) {
			return $src;
		}
	}
	// Referer din propriul site → intern (nu-l numărăm ca sursă nouă).
	if ( false !== strpos( $host, (string) wp_parse_url( home_url(), PHP_URL_HOST ) ) ) {
		return 'intern';
	}
	return substr( preg_replace( '/^www\./', '', $host ), 0, 40 );
}

/** REST: primește un eveniment de la front-end. Public (tracking). */
function hainute_analytics_register_routes() {
	register_rest_route(
		'hainute/v1',
		'/track',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_track',
			'permission_callback' => '__return_true',
		)
	);
}
add_action( 'rest_api_init', 'hainute_analytics_register_routes' );

function hainute_rest_track( WP_REST_Request $request ) {
	global $wpdb;
	$b       = $request->get_json_params();
	$type    = in_array( ( $b['type'] ?? '' ), array( 'view', 'click' ), true ) ? $b['type'] : 'view';
	$referer = (string) ( $request->get_header( 'referer' ) ?: ( $b['referer'] ?? '' ) );
	$source  = hainute_analytics_source( $b['referer'] ?? $referer, $b['utm'] ?? '' );
	$sid     = substr( preg_replace( '/[^a-zA-Z0-9]/', '', (string) ( $b['sid'] ?? '' ) ), 0, 40 );

	$wpdb->insert(
		hainute_events_table(),
		array(
			'created_at' => current_time( 'mysql' ),
			'session'    => $sid,
			'type'       => $type,
			'source'     => $source,
			'referer'    => substr( esc_url_raw( (string) ( $b['referer'] ?? $referer ) ), 0, 255 ),
			'path'       => substr( sanitize_text_field( (string) ( $b['path'] ?? '' ) ), 0, 255 ),
			'product_id' => (int) ( $b['product_id'] ?? 0 ),
			'store'      => substr( sanitize_text_field( (string) ( $b['store'] ?? '' ) ), 0, 80 ),
		)
	);
	return rest_ensure_response( array( 'ok' => true ) );
}

/** Scriptul de tracking pe front-end (beacon la vizită + click pe magazine). */
function hainute_analytics_enqueue() {
	if ( is_admin() ) {
		return;
	}
	$pid = ( is_singular( 'product' ) ) ? get_queried_object_id() : 0;
	// Google Analytics 4 cu Consent Mode v2 (avansat): doar pe site-ul live (nu în pre-lansare).
	// Fără acord: analytics_storage=denied, GA primește semnale anonime, fără cookie-uri (le folosește
	// pentru modelare); după „Accept”: granted, cu cookie-urile _ga. Reclamele rămân mereu denied.
	$ga = defined( 'HAINUTE_GA_ID' ) ? (string) HAINUTE_GA_ID : 'G-7LR8THNFJ4';
	if ( ( function_exists( 'hainute_is_test_host' ) && hainute_is_test_host() ) || ! preg_match( '/^G-[A-Z0-9]+$/', $ga ) ) {
		$ga = '';
	}
	$js  = "(function(){
		/* Cookie-urile de statistică (hnt_sid, hnt_src) DOAR cu acordul vizitatorului
		   (Legea 506/2004). Fără acord: evenimente anonime, fără nimic stocat în browser. */
		function ok(){return /(?:^|; )hnt_consent=1/.test(document.cookie);}
		var GA='".$ga."';
		function ga(){if(!GA||window.hntGa)return;window.hntGa=1;window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments);};
			gtag('consent','default',{analytics_storage:ok()?'granted':'denied',ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied'});
			gtag('set','ads_data_redaction',true);gtag('js',new Date());gtag('config',GA);
			var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+GA;document.head.appendChild(s);}
		/* La refuz: GA trece pe denied și ștergem cookie-urile _ga puse înainte (pe host și pe domeniul părinte). */
		function gaClean(){document.cookie.split('; ').forEach(function(k){var n=k.split('=')[0];if(/^_ga/.test(n)){var d=location.hostname.replace(/^www\./,'');document.cookie=n+'=;path=/;max-age=0';document.cookie=n+'=;path=/;max-age=0;domain=.'+d;}});}
		function gaConsent(c){if(!window.gtag)return;gtag('consent','update',{analytics_storage:c?'granted':'denied'});if(!c)gaClean();}
		ga();if(/(?:^|; )hnt_consent=0/.test(document.cookie))gaClean();
		function sid(){if(!ok())return '';var m=document.cookie.match(/hnt_sid=([^;]+)/);if(m)return m[1];var s=Math.random().toString(36).slice(2)+Date.now().toString(36);document.cookie='hnt_sid='+s+';path=/;max-age='+(60*60*24*30)+';SameSite=Lax';return s;}
		function firstSrc(ref,utm){var v=utm||ref||'';if(!ok())return v;var m=document.cookie.match(/hnt_src=([^;]+)/);if(m)return decodeURIComponent(m[1]);document.cookie='hnt_src='+encodeURIComponent(v)+';path=/;max-age='+(60*60*24*30)+';SameSite=Lax';return v;}
		function banner(){
			var old=document.getElementById('hnt-cookies');if(old)old.remove();
			var b=document.createElement('div');b.id='hnt-cookies';b.className='cookie-banner';b.setAttribute('role','dialog');b.setAttribute('aria-label','Cookie-uri');
			b.innerHTML='<p>Folosim cookie-uri de statistică (ale noastre și Google Analytics), ca să vedem ce pagini sunt utile. Le punem doar dacă ești de acord; fără acord, Google Analytics primește doar date anonime, fără cookie-uri. <a href=\"".esc_url( home_url( '/politica-cookies/' ) )."\">Politica de cookie-uri</a></p><div class=\"cookie-actions\"><button type=\"button\" data-c=\"0\">Refuz</button><button type=\"button\" data-c=\"1\">Accept</button></div>';
			b.addEventListener('click',function(e){var x=e.target.closest('[data-c]');if(!x)return;var c=x.getAttribute('data-c');document.cookie='hnt_consent='+c+';path=/;max-age='+(60*60*24*180)+';SameSite=Lax';if(c!=='1'){document.cookie='hnt_sid=;path=/;max-age=0';document.cookie='hnt_src=;path=/;max-age=0';}gaConsent(c==='1');b.remove();});
			document.body.appendChild(b);
		}
		if(!/(?:^|; )hnt_consent=/.test(document.cookie))banner();
		document.addEventListener('click',function(e){if(e.target.closest('[data-cookie-settings]')){e.preventDefault();banner();}});
		var params=new URLSearchParams(location.search);var utm=params.get('utm_source')||'';
		var src=firstSrc(document.referrer,utm);
		function send(d){d.sid=sid();d.utm=utm;d.referer=document.referrer;d.path=location.pathname;try{navigator.sendBeacon('".esc_url_raw( rest_url( 'hainute/v1/track' ) )."',new Blob([JSON.stringify(d)],{type:'application/json'}));}catch(e){}}
		send({type:'view',product_id:".$pid."});
		document.addEventListener('click',function(e){var a=e.target.closest('a.offer-cta');if(!a)return;var row=a.closest('[data-store-row]');var st=row?(row.querySelector('.offer-store')||{}).textContent:'';send({type:'click',product_id:".$pid.",store:(st||'').trim()});if(window.gtag)gtag('event','click_magazin',{magazin:(st||'').trim(),product_id:".$pid.",transport_type:'beacon'});},true);
	})();";
	wp_register_script( 'hainute-analytics', '', array(), HAINUTE_CORE_VERSION, true );
	wp_enqueue_script( 'hainute-analytics' );
	wp_add_inline_script( 'hainute-analytics', $js );
}
add_action( 'wp_enqueue_scripts', 'hainute_analytics_enqueue' );

// ---- Dashboard admin --------------------------------------------------------

function hainute_analytics_menu() {
	add_menu_page( __( 'Hainute Analytics', 'hainute' ), __( 'Analytics', 'hainute' ), 'manage_options', 'hainute-analytics', 'hainute_analytics_page', 'dashicons-chart-area', 58 );
}
add_action( 'admin_menu', 'hainute_analytics_menu' );

function hainute_analytics_page() {
	global $wpdb;
	$t    = hainute_events_table();
	$days = isset( $_GET['days'] ) ? max( 1, min( 365, (int) $_GET['days'] ) ) : 30;
	$since = gmdate( 'Y-m-d H:i:s', time() - $days * DAY_IN_SECONDS );

	$views  = (int) $wpdb->get_var( $wpdb->prepare( "SELECT COUNT(*) FROM $t WHERE type='view' AND created_at>=%s", $since ) );
	$vis    = (int) $wpdb->get_var( $wpdb->prepare( "SELECT COUNT(DISTINCT session) FROM $t WHERE created_at>=%s", $since ) );
	$clicks = (int) $wpdb->get_var( $wpdb->prepare( "SELECT COUNT(*) FROM $t WHERE type='click' AND created_at>=%s", $since ) );

	echo '<div class="wrap"><h1>' . esc_html__( 'Hainute — Analytics', 'hainute' ) . '</h1>';
	echo '<p>';
	foreach ( array( 7, 30, 90 ) as $d ) {
		echo '<a class="button ' . ( $d === $days ? 'button-primary' : '' ) . '" href="?page=hainute-analytics&days=' . $d . '">' . $d . ' zile</a> ';
	}
	echo '</p>';
	echo '<div style="display:flex;gap:16px;margin:16px 0">';
	foreach ( array( __( 'Vizite', 'hainute' ) => $views, __( 'Vizitatori unici', 'hainute' ) => $vis, __( 'Click-uri magazine', 'hainute' ) => $clicks ) as $lbl => $val ) {
		echo '<div style="background:#fff;border:1px solid #ccd0d4;padding:14px 22px;border-radius:8px"><div style="font-size:12px;color:#666">' . esc_html( $lbl ) . '</div><div style="font-size:26px;font-weight:700">' . esc_html( number_format_i18n( $val ) ) . '</div></div>';
	}
	echo '</div>';

	$blocks = array(
		__( 'Surse trafic', 'hainute' )       => $wpdb->get_results( $wpdb->prepare( "SELECT source AS k, COUNT(*) AS c FROM $t WHERE type='view' AND created_at>=%s GROUP BY source ORDER BY c DESC LIMIT 15", $since ) ),
		__( 'Top pagini', 'hainute' )          => $wpdb->get_results( $wpdb->prepare( "SELECT path AS k, COUNT(*) AS c FROM $t WHERE type='view' AND created_at>=%s GROUP BY path ORDER BY c DESC LIMIT 15", $since ) ),
		__( 'Click-uri per magazin', 'hainute' ) => $wpdb->get_results( $wpdb->prepare( "SELECT store AS k, COUNT(*) AS c FROM $t WHERE type='click' AND created_at>=%s GROUP BY store ORDER BY c DESC LIMIT 15", $since ) ),
	);
	echo '<div style="display:flex;gap:20px;flex-wrap:wrap">';
	foreach ( $blocks as $title => $rows ) {
		echo '<div style="flex:1;min-width:280px"><h2>' . esc_html( $title ) . '</h2><table class="widefat striped"><tbody>';
		if ( $rows ) {
			foreach ( $rows as $r ) {
				echo '<tr><td>' . esc_html( $r->k ?: '—' ) . '</td><td style="text-align:right;font-weight:600">' . esc_html( number_format_i18n( $r->c ) ) . '</td></tr>';
			}
		} else {
			echo '<tr><td>' . esc_html__( 'Încă fără date', 'hainute' ) . '</td></tr>';
		}
		echo '</tbody></table></div>';
	}
	echo '</div>';

	// Top produse click-uite.
	$tp = $wpdb->get_results( $wpdb->prepare( "SELECT product_id AS pid, COUNT(*) AS c FROM $t WHERE type='click' AND product_id>0 AND created_at>=%s GROUP BY product_id ORDER BY c DESC LIMIT 15", $since ) );
	echo '<h2 style="margin-top:24px">' . esc_html__( 'Top produse (click-uri către magazine)', 'hainute' ) . '</h2><table class="widefat striped"><tbody>';
	foreach ( $tp as $r ) {
		echo '<tr><td><a href="' . esc_url( get_edit_post_link( $r->pid ) ) . '">' . esc_html( get_the_title( $r->pid ) ?: ( '#' . $r->pid ) ) . '</a></td><td style="text-align:right;font-weight:600">' . esc_html( $r->c ) . '</td></tr>';
	}
	if ( ! $tp ) {
		echo '<tr><td>' . esc_html__( 'Încă fără click-uri', 'hainute' ) . '</td></tr>';
	}
	echo '</tbody></table>';

	echo '<p style="margin-top:20px;color:#666"><strong>' . esc_html__( 'Comenzile', 'hainute' ) . ':</strong> ' . esc_html__( 'nu se pot urmări pe site-ul nostru (se întâmplă pe site-ul magazinului). Le vezi în dashboard-ul rețelei de afiliere (CJ / 2Performant / Profitshare), corelate cu click-urile de aici.', 'hainute' ) . '</p>';
	echo '</div>';
}

/**
 * Politica de confidențialitate spunea „nu folosim Google Analytics", dar site-ul
 * folosește GA4 cu Consent Mode v2 (vezi hainute_analytics_enqueue). Corectăm pagina
 * din DB o singură dată, la prima cerere după publicare.
 */
function hainute_privacy_ga_fix() {
	if ( get_option( 'hainute_privacy_ga_v1' ) || ! add_option( 'hainute_privacy_ga_v1', time(), '', false ) ) {
		return;
	}
	$page = get_page_by_path( 'politica-de-confidentialitate' );
	if ( ! $page || false !== strpos( $page->post_content, 'Google Analytics 4' ) ) {
		return;
	}
	$c = str_replace(
		'(maximum 30 de zile pentru cookie-urile de statistică, puse doar cu acordul tău; nu folosim Google Analytics)',
		'(maximum 30 de zile pentru cookie-urile noastre de statistică, puse doar cu acordul tău; pentru Google Analytics, vezi mai sus)',
		$page->post_content
	);
	$par = '<p><strong>Google Analytics.</strong> Folosim Google Analytics 4 (serviciu Google) ca să vedem ce pagini sunt utile. Fără acordul dumneavoastră, Google Analytics nu pune cookie-uri în browser și primește doar semnale anonime despre vizită (de exemplu pagina vizitată), folosite de Google pentru statistici agregate. Numai dacă apăsați „Accept” în bannerul de cookie-uri, Google Analytics pune cookie-urile lui (<em>_ga</em>), ca să deosebească vizitele. Nu folosim aceste date pentru reclame: stocarea pentru publicitate rămâne mereu dezactivată. Vă puteți retrage oricând acordul din „Setări cookie-uri”, în subsolul paginii, iar cookie-urile <em>_ga</em> se șterg. Google poate prelucra datele și în afara Spațiului Economic European, cu garanțiile prevăzute de GDPR (Cadrul UE-SUA privind protecția datelor).</p>' . "\n";
	$pos = strpos( $c, '<h2>Temeiul legal' );
	if ( false === $pos ) {
		return; // structura paginii s-a schimbat: nu ghicim unde intră
	}
	$c = substr( $c, 0, $pos ) . $par . substr( $c, $pos );
	wp_update_post( array( 'ID' => $page->ID, 'post_content' => $c ) );
}
add_action( 'init', 'hainute_privacy_ga_fix', 21 );
