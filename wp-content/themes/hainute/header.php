<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<header class="site-header">
	<div class="container header-inner">
		<a class="site-logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">
			<img src="<?php echo esc_url( get_template_directory_uri() . '/assets/img/logo.png' ); ?>" width="242" height="88" alt="<?php bloginfo( 'name' ); ?>">
		</a>

		<button class="search-toggle" type="button" aria-expanded="false" aria-controls="header-search" aria-label="<?php esc_attr_e( 'Caută', 'hainute' ); ?>">
			<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
		</button>

		<button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="<?php esc_attr_e( 'Deschide meniul', 'hainute' ); ?>">
			<span></span><span></span><span></span>
		</button>

		<nav id="site-nav" class="site-nav" aria-label="<?php esc_attr_e( 'Meniu principal', 'hainute' ); ?>">
			<?php
			wp_nav_menu(
				array(
					'theme_location' => 'primary',
					'container'      => false,
					'fallback_cb'    => 'hainute_nav_fallback',
				)
			);
			?>
		</nav>

		<div class="header-search" id="header-search">
			<?php get_search_form(); ?>
		</div>
	</div>
</header>

<main class="site-main">
