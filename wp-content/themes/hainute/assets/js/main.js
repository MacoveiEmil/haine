/* Hainute theme JS — gallery swap + filter auto-submit. Vanilla, no deps. */

document.addEventListener('DOMContentLoaded', function () {

	// Product gallery: click a thumbnail to swap the main image.
	document.querySelectorAll('[data-gallery]').forEach(function (gallery) {
		var main = gallery.querySelector('.gallery-main img');
		if (!main) return;

		gallery.querySelectorAll('.gallery-thumb').forEach(function (thumb) {
			thumb.addEventListener('click', function () {
				main.removeAttribute('srcset'); main.src = thumb.getAttribute('data-full');
				gallery.querySelectorAll('.gallery-thumb').forEach(function (t) {
					t.classList.remove('is-active');
				});
				thumb.classList.add('is-active');
			});
		});
	});

	// Meniu mobil: hamburger deschide/închide nav-ul (rămâne în DOM, doar ascuns vizual).
	(function () {
		var header = document.querySelector('.site-header');
		var toggle = header && header.querySelector('.nav-toggle');
		if (!header || !toggle) return;
		toggle.addEventListener('click', function () {
			var open = header.classList.toggle('nav-open');
			toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
		});
		// Închide meniul când dai click pe un link.
		header.querySelectorAll('.site-nav a').forEach(function (a) {
			a.addEventListener('click', function () {
				header.classList.remove('nav-open');
				toggle.setAttribute('aria-expanded', 'false');
			});
		});
	})();

	// Descriere „citește mai mult": dacă e lungă, o pliem vizual (conținutul RĂMÂNE
	// în HTML pentru SEO) și adăugăm un buton de extindere.
	document.querySelectorAll('.product-description').forEach(function (desc) {
		if (desc.scrollHeight <= 200) return; // scurtă — nu plia
		desc.classList.add('is-collapsible');
		var btn = document.createElement('button');
		btn.type = 'button';
		btn.className = 'desc-toggle';
		btn.setAttribute('aria-expanded', 'false');
		btn.textContent = 'Citește mai mult';
		// Descriere + buton într-un singur container: părintele e o grilă pe 2
		// coloane (descriere | specificații), iar butonul nu trebuie să fie o celulă.
		var wrap = document.createElement('div');
		wrap.className = 'desc-wrap';
		desc.parentNode.insertBefore(wrap, desc);
		wrap.appendChild(desc);
		wrap.appendChild(btn);
		btn.addEventListener('click', function () {
			var open = desc.classList.toggle('is-expanded');
			btn.setAttribute('aria-expanded', open ? 'true' : 'false');
			btn.textContent = open ? 'Arată mai puțin' : 'Citește mai mult';
		});
	});

	// Filtre pe mobil: butonul „Filtre și sortare" vine din server, iar CSS-ul le
	// pliază de la prima randare (fără salt de layout). JS doar deschide/închide.
	document.querySelectorAll('.filter-toggle').forEach(function (btn) {
		var form = document.getElementById(btn.getAttribute('aria-controls'));
		if (!form) return;
		btn.addEventListener('click', function () {
			var open = form.classList.toggle('is-open');
			btn.setAttribute('aria-expanded', open ? 'true' : 'false');
		});
	});

	// Filter bar: submit automatically when a select changes
	// (the "Filtrează" button stays as the no-JS fallback).
	document.querySelectorAll('[data-filter-bar] select, [data-filter-bar] input[type="checkbox"]').forEach(function (field) {
		field.addEventListener('change', function () {
			field.closest('form').submit();
		});
	});

	// Colour/variant selector: pick a swatch → swap the main product image and
	// update the "go to store" price + link to that exact colour.
	document.querySelectorAll('[data-variant-selector]').forEach(function (sel) {
		var mainImg = document.querySelector('[data-gallery] .gallery-main img');
		var priceEl = sel.querySelector('[data-variant-price]');
		var linkEl  = sel.querySelector('[data-variant-link]');

		var sizeChips = document.querySelector('[data-size-display] [data-size-chips]');

		sel.querySelectorAll('.variant-swatch').forEach(function (btn) {
			btn.addEventListener('click', function () {
				var img = btn.getAttribute('data-image');
				var url = btn.getAttribute('data-url');
				var price = btn.getAttribute('data-price');
				var sizes = btn.getAttribute('data-sizes');

				if (mainImg && img) { mainImg.removeAttribute('srcset'); mainImg.src = img; }
				if (priceEl && price) priceEl.textContent = price;
				if (linkEl && url) linkEl.setAttribute('href', url);

				// Mărimile culorii selectate.
				if (sizeChips && sizes !== null) {
					var list = sizes.split(',').map(function (s) { return s.trim(); }).filter(Boolean);
					if (list.length) {
						sizeChips.innerHTML = list.map(function (s) {
							return '<li class="size-chip">' + s.replace(/[<>&]/g, '') + '</li>';
						}).join('');
					}
				}

				sel.querySelectorAll('.variant-swatch').forEach(function (b) {
					b.classList.remove('is-active');
				});
				btn.classList.add('is-active');
			});
		});
	});

	// Shop matrix: UN rând per magazin. Culoarea + mărimea aleasă schimbă dinamic
	// linkul și prețul fiecărui magazin (ruta către pagina exactă a variantei).
	document.querySelectorAll('[data-shop-matrix]').forEach(function (m) {
		var mainImg = document.querySelector('[data-gallery] .gallery-main img');
		var rows = [].slice.call(m.querySelectorAll('.sm-listings .offer'));
		var sizeBtns = [].slice.call(m.querySelectorAll('.sm-size'));
		var colorBtns = [].slice.call(m.querySelectorAll('.sm-color'));
		var state = { color: null, size: null };
		var alt = m.querySelector('[data-size-alt]');
		var altDefault = alt ? !alt.hidden : false;
		rows.forEach(function (li, i) { li._idx = i; li._rank = 0; });

		function fmt(p) { return (Math.round(p * 100) / 100).toFixed(2).replace('.', ',') + ' lei'; }
		function variantsOf(li) { try { return JSON.parse(li.getAttribute('data-variants') || '[]'); } catch (e) { return []; } }
		// Activează/dezactivează butonul „Vezi în magazin": fără link funcțional când
		// mărimea aleasă nu e disponibilă la acel magazin.
		// Fără mărime/stoc la acel magazin → butonul nu rămâne mort: duce la aceeași
		// categorie (gen + mărimea aleasă), ca la linkul „Vezi … în mărimea X".
		function altUrl() {
			var altBox = m.querySelector('[data-size-alt]');
			if (!altBox) return '';
			var u = new URL(altBox.getAttribute('data-base'), location.href);
			if (state.size) u.searchParams.set('marime', state.size);
			return u.toString();
		}
		function setCta(a, enabled, url) {
			if (!a) return;
			if (!a.dataset.label) a.dataset.label = a.textContent;
			a.classList.remove('is-disabled');
			a.removeAttribute('aria-disabled');
			if (enabled && url) {
				a.setAttribute('href', url);
				a.setAttribute('target', '_blank');
				a.setAttribute('rel', 'sponsored nofollow noopener');
				a.classList.remove('is-alt');
				a.textContent = a.dataset.label;
				return;
			}
			var alt = altUrl();
			if (alt) {
				a.setAttribute('href', alt);
				a.removeAttribute('target');
				a.removeAttribute('rel');
				a.classList.add('is-alt');
				a.textContent = 'Vezi alternative \u2192';
			} else {
				a.removeAttribute('href');
				a.classList.add('is-disabled');
				a.setAttribute('aria-disabled', 'true');
			}
		}

		// Sub-ofertele unui magazin care corespund culorii active (externii n-au
		// culoare la noi → intră mereu).
		function poolFor(li) {
			var vs = variantsOf(li);
			var pool = vs.filter(function (v) { return !state.color || v.color === state.color || v.color === ''; });
			return pool.length ? pool : (vs.some(function (v) { return v.color === ''; }) ? vs : []);
		}
		// Varianta potrivită culorii + mărimii selectate (pt link/preț).
		function pick(li) {
			// Variantele cu stoc primele (sort stabil), apoi restul.
			var pool = poolFor(li).slice().sort(function (a, b) { return (b.in_stock ? 1 : 0) - (a.in_stock ? 1 : 0); });
			if (!pool.length) return null;
			if (state.size) {
				// Un magazin cu mărimi NECUNOSCUTE (listă goală — încă necrawluit) NU
				// poate fi declarat „fără mărimea asta"; rămâne disponibil. Doar cele cu
				// mărimi cunoscute se filtrează pe mărimea selectată.
				var ws = pool.filter(function (v) { return !v.sizes.length || v.sizes.indexOf(state.size) >= 0; });
				return ws.length ? ws[0] : null;
			}
			return pool[0];
		}

		function apply() {
			// Mărimile disponibile pentru culoarea activă (din toate magazinele).
			var avail = {};
			rows.forEach(function (li) { poolFor(li).forEach(function (v) { if (v.in_stock) v.sizes.forEach(function (s) { if (s) avail[s] = 1; }); }); });
			// Dacă NICIUN magazin nu are date de mărime pt culoarea activă (încă
			// necrawluită), nu tăiem nimic — mărimi „necunoscute", nu „indisponibile".
			var known = Object.keys(avail).length > 0;
			sizeBtns.forEach(function (b) {
				if (b.classList.contains('sm-unavail')) { return; } // permanent indisponibilă (tăiată)
				var s = b.getAttribute('data-size');
				var off = known && !avail[s];
				b.classList.toggle('sm-off', off);
				// (o mărime „off" rămâne selectabilă: arată alternativa, nu blochează)
			});

			rows.forEach(function (li) {
				var p = pick(li);
				var priceEl = li.querySelector('.offer-price'), linkEl = li.querySelector('.offer-cta'), statusEl = li.querySelector('.offer-status-label');
				li._rank = (!p || !p.in_stock) ? 2 : (state.size && !p.sizes.length ? 1 : 0);
				if (!p) {
					// O singură stare pentru „nu se poate cumpăra aici": același stil și același
					// text, fie că magazinul n-are stoc deloc, fie că n-are mărimea aleasă.
					li.classList.add('stock-out'); li.classList.remove('stock-in');
					if (statusEl) statusEl.textContent = 'Indisponibil';
				} else {
					if (priceEl) priceEl.textContent = fmt(p.price);
					// Mărimile acestui magazin nu sunt (încă) verificate → nu promitem nimic.
					if (statusEl) statusEl.textContent = !p.in_stock ? 'Indisponibil' : (state.size && !p.sizes.length ? 'Mărime neconfirmată' : 'Disponibil');
					li.classList.toggle('sm-unconfirmed', !!(p.in_stock && state.size && !p.sizes.length));
					li.classList.toggle('stock-out', !p.in_stock); li.classList.toggle('stock-in', p.in_stock);
				}
				// Linkul e activ doar dacă produsul e cumpărabil la mărimea aleasă.
				// Fără mărime selectată → link general. Cu mărime indisponibilă la acel
				// magazin (fără variantă sau fără stoc) → link dezactivat.
				setCta(linkEl, !!(p && p.in_stock), p ? p.url : ''); // fără stoc → alternative, nu magazinul
				});

				// Magazinele care AU mărimea aleasă primele, apoi cele neconfirmate, apoi
				// restul (ordine stabilă, nu după preț).
				var list = rows.length ? rows[0].parentNode : null;
				if (list) {
					rows.slice().sort(function (a, b) { return (a._rank - b._rank) || (a._idx - b._idx); }).forEach(function (li) { list.appendChild(li); });
				}

				// Fără fundătură: mărime epuizată peste tot → link spre alte produse din
				// aceeași categorie, în mărimea aleasă.
				if (alt) {
					var none = state.size && !rows.some(function (li) { return li._rank === 0; });
					if (state.size) {
						alt.hidden = !none;
						var a = alt.querySelector('.sm-alt-link'), msg = alt.querySelector('[data-size-alt-msg]');
						if (none && a) {
							var u = new URL(alt.getAttribute('data-base'), location.href);
							u.searchParams.set('marime', state.size);
							a.href = u.toString();
							a.textContent = a.getAttribute('data-label') + ' în mărimea ' + state.size + ' →';
							if (msg) msg.textContent = 'Mărimea ' + state.size + ' nu e pe stoc în magazine acum.';
						}
					} else {
						alt.hidden = !altDefault;
					}
				}
				}

		// Galeria aparține culorii produsului nostru (prima). La altă culoare arătăm
		// poza variantei de la magazinul care o are și ascundem miniaturile (sunt ale
		// altei culori); la revenire refacem galeria. Fără poză → mesaj, nu poza greșită.
		var gallery = document.querySelector('[data-gallery]');
		var origSrc = mainImg ? mainImg.getAttribute('src') : '';
		var origSet = mainImg ? mainImg.getAttribute('srcset') : '';
		function showColorImage(b, isPrimary) {
			if (!mainImg || !gallery) return;
			var img = b.getAttribute('data-image');
			gallery.classList.remove('gallery--variant', 'gallery--noimg');
			var box = gallery.querySelector('.gallery-main');
			if (box) box.removeAttribute('data-noimg');
			if (isPrimary) {
				mainImg.src = origSrc;
				if (origSet) mainImg.setAttribute('srcset', origSet);
				return;
			}
			gallery.classList.add('gallery--variant');
			if (img) { mainImg.removeAttribute('srcset'); mainImg.src = img; }
			else { gallery.classList.add('gallery--noimg'); if (box) box.setAttribute('data-noimg', 'Poza variantei ' + (b.getAttribute('title') || '') + ' e pe site-ul magazinului'); }
		}
		var hasPrimary = colorBtns.some(function (x) { return x.hasAttribute('data-primary'); });
		colorBtns.forEach(function (b, i) {
			b.addEventListener('click', function () {
				state.color = b.getAttribute('data-color'); state.size = null;
				// Culoarea produsului nostru (data-primary) → galeria originală.
				showColorImage(b, hasPrimary ? b.hasAttribute('data-primary') : i === 0);
				colorBtns.forEach(function (x) { x.classList.remove('is-active'); });
				b.classList.add('is-active');
				sizeBtns.forEach(function (x) { x.classList.remove('is-active'); });
				apply();
			});
		});

		sizeBtns.forEach(function (b) {
			b.addEventListener('click', function () {
				var s = b.getAttribute('data-size');
				if (state.size === s) { state.size = null; b.classList.remove('is-active'); }
				else {
					state.size = s;
					sizeBtns.forEach(function (x) { x.classList.remove('is-active'); });
					b.classList.add('is-active');
				}
				apply();
			});
		});

		if (colorBtns.length) {
			state.color = colorBtns[0].getAttribute('data-color');
			colorBtns[0].classList.add('is-active');
			// Prima culoare (cu stoc) nu e a produsului nostru → arătăm direct poza ei.
			if (hasPrimary && !colorBtns[0].hasAttribute('data-primary')) showColorImage(colorBtns[0], false);
		}
		apply();
	});

	// Carousel: scroll the track by ~one viewport-width on arrow clicks.
	// CSS scroll-snap does the smooth stops; JS only nudges scrollLeft.
	document.querySelectorAll('[data-carousel]').forEach(function (carousel) {
		var track = carousel.querySelector('[data-carousel-track]');
		if (!track) return;

		var prev = carousel.querySelector('.carousel-prev');
		var next = carousel.querySelector('.carousel-next');

		function step() {
			var item = track.querySelector('.carousel-item');
			var w = item ? item.getBoundingClientRect().width + 16 : track.clientWidth * 0.8;
			return Math.max(w, track.clientWidth * 0.8);
		}
		function update() {
			if (prev) prev.disabled = track.scrollLeft <= 4;
			if (next) next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
		}

		if (prev) prev.addEventListener('click', function () {
			track.scrollBy({ left: -step(), behavior: 'smooth' });
		});
		if (next) next.addEventListener('click', function () {
			track.scrollBy({ left: step(), behavior: 'smooth' });
		});
		track.addEventListener('scroll', update, { passive: true });
		window.addEventListener('resize', update);
		update();
	});
});

/* Mobil: căutarea din lupă + bara fixă „Vezi mărimile disponibile". */
document.addEventListener('DOMContentLoaded', function () {
	var header = document.querySelector('.site-header');
	var st = header && header.querySelector('.search-toggle');
	if (st) {
		st.addEventListener('click', function () {
			var open = header.classList.toggle('search-open');
			st.setAttribute('aria-expanded', open ? 'true' : 'false');
			if (open) {
				var f = header.querySelector('.search-field');
				if (f) f.focus();
			}
		});
	}

	// Bara apare după ce prețul a ieșit din ecran (în sus) și dispare cât timp
	// lista de magazine e vizibilă (acolo e deja tot ce oferă bara).
	var bar = document.querySelector('[data-sticky-cta]');
	var price = document.querySelector('.price-summary') || document.querySelector('.price-block');
	var offers = document.querySelector('.sm-listings') || document.getElementById('magazine');
	if (!bar || !price) return;
	var ticking = false;
	function sync() {
		ticking = false;
		var vh = window.innerHeight;
		var pr = price.getBoundingClientRect();
		var pricePassed = pr.bottom < 0;
		var offersVisible = false;
		if (offers) { var o = offers.getBoundingClientRect(); offersVisible = o.top < vh && o.bottom > 0; }
		var show = pricePassed && !offersVisible;
		bar.classList.toggle('is-visible', show);
		bar.setAttribute('aria-hidden', show ? 'false' : 'true');
		var btn = bar.querySelector('a');
		if (btn) btn.tabIndex = show ? 0 : -1;
	}
	function onScroll() { if (!ticking) { ticking = true; window.requestAnimationFrame(sync); } }
	window.addEventListener('scroll', onScroll, { passive: true });
	window.addEventListener('resize', onScroll);
	sync();
});

/* Admin: „Reverifică disponibilitatea acum" → coadă → worker → reîncărcare automată. */
document.addEventListener('DOMContentLoaded', function () {
	var box = document.querySelector('[data-recheck]');
	if (!box || !window.fetch) return;
	var btn = box.querySelector('.admin-recheck-btn');
	var st = box.querySelector('.admin-recheck-status');
	var id = box.getAttribute('data-recheck'), api = box.getAttribute('data-api'), nonce = box.getAttribute('data-nonce');
	var hdr = { 'X-WP-Nonce': nonce };
	btn.addEventListener('click', function () {
		btn.disabled = true;
		st.textContent = 'Se verifică la toate magazinele (de obicei ~1 minut)…';
		fetch(api + 'recheck', { method: 'POST', credentials: 'same-origin', headers: Object.assign({ 'Content-Type': 'application/json' }, hdr), body: JSON.stringify({ id: id }) })
			.then(function (r) { return r.json(); })
			.then(function (j) {
				if (!j || !j.ok) { throw new Error((j && j.message) || 'eroare'); }
				var since = j.queued, tries = 0;
				var t = setInterval(function () {
					tries++;
					fetch(api + 'recheck-status?id=' + id, { credentials: 'same-origin', headers: hdr })
						.then(function (r) { return r.json(); })
						.then(function (s) {
							if (s.done >= since) { clearInterval(t); st.textContent = 'Gata, reîncarc pagina…'; location.reload(); }
							else if (!s.worker || Date.now() / 1000 - s.worker > 120) { st.textContent = 'În coadă. Worker-ul de verificare nu rulează acum; pornește-l (tools/crawler/worker.js).'; }
							else if (tries > 72) { clearInterval(t); st.textContent = 'Durează mai mult decât de obicei; reîncarcă pagina mai târziu.'; btn.disabled = false; }
						});
				}, 5000);
			})
			.catch(function (e) { st.textContent = 'Nu am putut porni verificarea: ' + e.message; btn.disabled = false; });
	});
});

// Poză moartă la sursă (magazinul a șters-o): în galerie trecem la următoarea
// poză, altfel placeholder; pe carduri, placeholder. Nu lăsăm icon de poză ruptă.
(function () {
	function broken(img) {
		if (img.dataset.hnFail) return;
		img.dataset.hnFail = '1';
		var main = img.closest('.gallery-main');
		if (main) {
			var gallery = img.closest('[data-gallery]');
			var cur = img.getAttribute('src');
			var next = gallery ? [].slice.call(gallery.querySelectorAll('.gallery-thumb')).map(function (t) { return t.getAttribute('data-full'); }).filter(function (u) { return u && u !== cur && !(gallery.dataset.dead || '').split('|').includes(u); })[0] : null;
			if (gallery) gallery.dataset.dead = (gallery.dataset.dead || '') + '|' + cur;
			if (next) { delete img.dataset.hnFail; img.removeAttribute('srcset'); img.src = next; return; }
		}
		var thumb = img.closest('.gallery-thumb');
		if (thumb) { thumb.hidden = true; return; }
		var ph = document.createElement('span');
		ph.className = 'card-noimg';
		ph.setAttribute('role', 'img');
		ph.setAttribute('aria-label', img.getAttribute('alt') || '');
		img.replaceWith(ph);
	}
	document.addEventListener('error', function (e) { if (e.target && e.target.tagName === 'IMG') broken(e.target); }, true);
	// Poze care au eșuat înainte să se încarce scriptul: după load, le confirmăm cu o
	// încercare nouă (o poză încă în descărcare nu e „moartă").
	window.addEventListener('load', function () {
		document.querySelectorAll('img').forEach(function (img) {
			if (!img.complete || img.naturalWidth || !img.getAttribute('src') || img.loading === 'lazy') return;
			var probe = new Image();
			probe.onerror = function () { broken(img); };
			probe.src = img.currentSrc || img.src;
		});
	});
})();
