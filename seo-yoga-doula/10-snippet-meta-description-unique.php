<?php
/**
 * Supprime la deuxième balise <meta name="description"> sur les articles.
 *
 * À coller : Code Snippets → Ajouter → SANS la ligne <?php
 * Réglage  : "Run snippet everywhere"
 *
 * ------------------------------------------------------------------
 * LE PROBLÈME
 * ------------------------------------------------------------------
 * Chaque article du blog envoie DEUX descriptions à Google au lieu d'une.
 * Vérifié le 7 août sur « Mantras pendant l'accouchement » :
 *
 *   1. "Quels sont les effets des mantras pendant la grossesse..."
 *      → celle de Rank Math. C'est la bonne.
 *   2. "Cet article explore les bienfaits des mantras..."
 *      → l'extrait de l'article, injecté par autre chose.
 *
 * Les PAGES (accueil, PYM) n'ont qu'une seule balise. Le défaut est
 * spécifique aux ARTICLES.
 *
 * Impact réel : faible. Google lit la première et ignore la seconde.
 * Mais pour un modèle d'IA qui lit l'en-tête de la page, deux
 * descriptions différentes, c'est du bruit — et on cherche justement
 * à être lisible par les IA.
 *
 * ------------------------------------------------------------------
 * COMMENT ÇA MARCHE, EN FRANÇAIS
 * ------------------------------------------------------------------
 * Au lieu de chercher quel plugin ou quel bout de thème produit la
 * balise en trop (ce qui demanderait de fouiller le code), on met en
 * pause l'écriture de l'en-tête, on relit ce qui a été écrit, on
 * garde la première description et on efface les suivantes, puis on
 * laisse repartir. Comme un filtre posé à la sortie.
 *
 * ------------------------------------------------------------------
 * ⚠️ AVANT DE COLLER
 * ------------------------------------------------------------------
 * 1. Vérifie ta sauvegarde UpdraftPlus.
 * 2. Après activation, ouvre n'importe quel article du site et
 *    regarde qu'il s'affiche normalement. C'est la seule chose qui
 *    pourrait mal se passer : si la page s'affiche blanche ou
 *    cassée, désactive le snippet — tout revient instantanément.
 * 3. Vide le cache (WP-Optimize → Cache → Purger) avant de vérifier.
 *
 * C'est le snippet le plus "invasif" des trois : il touche à la
 * fabrication de la page. Si tu ne devais en installer que deux,
 * garde llms.txt et le schema Course, et laisse celui-ci de côté —
 * son gain est réel mais modeste.
 */

// Étape 1 : au tout début de l'en-tête, on met l'écriture en pause.
add_action( 'wp_head', function () {
	if ( is_admin() || is_feed() ) {
		return;
	}
	ob_start();
}, -99999 );

// Étape 2 : à la toute fin de l'en-tête, on relit et on filtre.
add_action( 'wp_head', function () {
	if ( is_admin() || is_feed() ) {
		return;
	}

	// Sécurité : s'il n'y a rien en pause, on ne touche à rien.
	if ( ! ob_get_level() ) {
		return;
	}

	$entete = ob_get_clean();
	if ( ! is_string( $entete ) || '' === $entete ) {
		echo $entete;
		return;
	}

	$compteur = 0;

	$entete_filtre = preg_replace_callback(
		'#<meta[^>]+name=([\'"])description\1[^>]*>\s*#i',
		function ( $trouve ) use ( &$compteur ) {
			$compteur++;
			// On garde la première, on efface toutes les suivantes.
			return ( 1 === $compteur ) ? $trouve[0] : '';
		},
		$entete
	);

	// Si le filtrage a échoué pour une raison quelconque, on réaffiche
	// l'en-tête d'origine intact plutôt que de casser la page.
	echo ( null === $entete_filtre ) ? $entete : $entete_filtre;

}, 99999 );
