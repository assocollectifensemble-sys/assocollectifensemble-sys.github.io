<?php
/**
 * Expose les champs Rank Math à l'API REST de WordPress.
 *
 * Site      : yoga-doula.eu
 * À coller  : Code Snippets (déjà installé et actif) → Ajouter → coller SANS la ligne <?php
 * Exécution : "Run snippet everywhere"
 * Objectif  : permettre d'écrire le titre SEO, la méta description et le mot-clé
 *             principal Rank Math depuis le connecteur, au lieu de les saisir à la main.
 *
 * Sans ce snippet : WordPress rejette ces 3 champs et renvoie
 *   ignored_keys: ["rank_math_description","rank_math_focus_keyword","rank_math_title"]
 *
 * Réversible : désactiver le snippet en un clic. Aucune donnée n'est modifiée,
 * aucune table touchée. Le snippet ouvre juste une porte, il n'écrit rien lui-même.
 */

add_action( 'init', function () {

	// Les 3 champs Rank Math qu'on veut rendre accessibles.
	$champs = array(
		'rank_math_title',         // le titre bleu dans les résultats Google
		'rank_math_description',   // le paragraphe gris en dessous
		'rank_math_focus_keyword', // le mot-clé principal (sert au score Rank Math)
	);

	// On ouvre ces champs pour les articles ET les pages.
	$types = array( 'post', 'page' );

	foreach ( $types as $type ) {
		foreach ( $champs as $champ ) {

			register_post_meta( $type, $champ, array(

				// 'string' : le contenu du champ est du texte simple.
				'type'          => 'string',

				// true : une seule valeur par article (pas une liste).
				'single'        => true,

				// LA ligne qui débloque tout : rend le champ visible et
				// modifiable via l'API REST, donc via le connecteur.
				'show_in_rest'  => true,

				// Le garde-fou de sécurité. Seul un utilisateur ayant le droit
				// de modifier des articles peut écrire dans ces champs.
				// Un visiteur anonyme ne peut rien faire, même en connaissant l'URL.
				'auth_callback' => function () {
					return current_user_can( 'edit_posts' );
				},

				// Nettoie le texte reçu (supprime le HTML indésirable) avant
				// enregistrement en base.
				'sanitize_callback' => 'sanitize_text_field',
			) );
		}
	}
}, 20 ); // priorité 20 : on passe APRÈS Rank Math, qui s'enregistre plus tôt.
