<?php
/**
 * Ajoute un schema Course sur la page Programme Yoga Maternité (ID 7018).
 *
 * À coller : Code Snippets → Ajouter → SANS la ligne <?php
 * Réglage  : "Run snippet everywhere"
 *
 * ------------------------------------------------------------------
 * POURQUOI
 * ------------------------------------------------------------------
 * Un « schema », c'est une fiche d'identité invisible que la page
 * transmet aux moteurs. Sans elle, Google et ChatGPT voient un texte ;
 * avec elle, ils voient : une formation, 84 heures, hybride, 1 050 €,
 * d'octobre 2026 à juin 2027, dispensée par l'École Yoga Doula.
 *
 * Aujourd'hui la page PYM n'en a aucune de ce type : elle est déclarée
 * comme un simple « Article ». La page Formation Yoga Doula, elle, a
 * bien un schema Course — c'est donc la page de la campagne d'octobre
 * qui est la moins bien équipée des deux.
 *
 * ------------------------------------------------------------------
 * ⚠️ DEUX CHOSES À FAIRE AVANT / APRÈS
 * ------------------------------------------------------------------
 * 1. AVANT : vérifier ta sauvegarde UpdraftPlus.
 *
 * 2. NE PAS FAIRE LES DEUX. Soit tu utilises ce snippet, soit tu
 *    ajoutes le schema Course à la main dans Rank Math (Schéma →
 *    Générateur → Course). Les deux ensemble = deux fiches
 *    concurrentes, et c'est pire que rien.
 *
 * 3. APRÈS : tester la page sur
 *    https://search.google.com/test/rich-results
 *    On doit voir « Course » détecté, sans erreur.
 *
 * ------------------------------------------------------------------
 * ⚠️ LES DEUX VALEURS À CORRIGER AVANT DE COLLER
 * ------------------------------------------------------------------
 * Cherche plus bas 'startDate' et 'endDate' : j'ai mis le 1er octobre
 * 2026 et le 30 juin 2027, qui sont des approximations tirées de la
 * page. Remplace-les par les vraies dates de ton calendrier.
 * Format obligatoire : AAAA-MM-JJ.
 */

add_action( 'wp_head', function () {

	// On n'agit que sur la page Programme Yoga Maternité, et nulle part ailleurs.
	if ( ! is_page( 7018 ) ) {
		return;
	}

	$schema = array(
		'@context'    => 'https://schema.org',
		'@type'       => 'Course',
		'name'        => 'Programme Yoga Maternité',
		'description' => "Formation à l'enseignement du yoga prénatal et postnatal. 84 heures en format hybride, combinant plateforme en ligne et rencontres en présentiel. Ouvert aux personnes venues de la périnatalité, de l'accompagnement ou du soin.",
		'url'         => 'https://yoga-doula.eu/formation-yoga-maternite/',
		'inLanguage'  => 'fr',

		// Qui délivre la formation.
		'provider'    => array(
			'@type' => 'EducationalOrganization',
			'name'  => 'École Internationale Yoga Doula',
			'url'   => 'https://yoga-doula.eu/',
		),

		// La session concrète : dates, format, durée, prix.
		'hasCourseInstance' => array(
			array(
				'@type'           => 'CourseInstance',
				'courseMode'      => 'Blended',   // hybride : en ligne + présentiel
				'courseWorkload'  => 'PT84H',     // 84 heures, en notation ISO 8601
				'startDate'       => '2026-10-01', // ⚠️ À CORRIGER
				'endDate'         => '2027-06-30', // ⚠️ À CORRIGER
				'inLanguage'      => 'fr',
				'location'        => array(
					'@type'   => 'Place',
					'name'    => 'France',
					'address' => array(
						'@type'          => 'PostalAddress',
						'addressCountry' => 'FR',
					),
				),
				'offers' => array(
					'@type'         => 'Offer',
					'price'         => '1050',
					'priceCurrency' => 'EUR',
					'category'      => 'Paid',
					'availability'  => 'https://schema.org/InStock',
					'url'           => 'https://yoga-doula.eu/formation-yoga-maternite/',
				),
			),
		),
	);

	echo "\n<!-- Schema Course — École Yoga Doula -->\n";
	echo '<script type="application/ld+json">'
		. wp_json_encode( $schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE )
		. "</script>\n";

}, 20 );
