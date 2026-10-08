<form role="search" method="get" class="search-form" action="<?php echo esc_url( home_url( '/' ) ); ?>">
	<input type="search" class="search-field" placeholder="<?php esc_attr_e( 'Caută un produs…', 'hainute' ); ?>"
		value="<?php echo esc_attr( get_search_query() ); ?>" name="s">
	<input type="hidden" name="post_type" value="product">
	<button type="submit" class="search-submit" aria-label="<?php esc_attr_e( 'Caută', 'hainute' ); ?>">
		<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
			<circle cx="11" cy="11" r="7"></circle>
			<line x1="21" y1="21" x2="16.5" y2="16.5"></line>
		</svg>
	</button>
</form>
