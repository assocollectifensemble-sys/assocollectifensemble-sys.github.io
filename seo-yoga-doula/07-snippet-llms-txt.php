<?php
/**
 * Sert un fichier /llms.txt à la racine du site.
 *
 * Site      : yoga-doula.eu
 * À coller  : Code Snippets → Ajouter → coller SANS la ligne <?php
 * Réglage   : "Run snippet everywhere"
 *
 * ------------------------------------------------------------------
 * À QUOI ÇA SERT
 * ------------------------------------------------------------------
 * robots.txt dit aux robots ce qu'ils ont le droit de lire.
 * llms.txt leur dit ce qu'il faut retenir.
 *
 * C'est une convention apparue en 2024, désormais lue par plusieurs
 * moteurs de réponse (Perplexity, certains crawlers d'entraînement) :
 * un résumé propre, en texte brut, de ce qu'est le site, ce qu'il
 * propose, et quelles pages comptent. Sans avoir à deviner à travers
 * le HTML d'Elementor.
 *
 * Ce n'est pas encore un standard officiel et Google ne s'en sert pas.
 * Mais ça coûte cinq minutes, ça ne peut rien casser, et sur le
 * terrain de la recommandation par les IA — qui est précisément
 * l'enjeu ici — c'est un des rares leviers directs qui existent.
 *
 * Vérification après installation : ouvrir https://yoga-doula.eu/llms.txt
 * Le texte doit s'afficher brut, sans mise en page.
 *
 * ⚠️ À METTRE À JOUR quand les 10 articles seront publiés :
 *    la section "Articles" ci-dessous ne liste que les articles en ligne.
 * ------------------------------------------------------------------
 */

add_action( 'init', function () {

	// On ne réagit que si l'adresse demandée est exactement /llms.txt
	$chemin = parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH );
	if ( '/llms.txt' !== $chemin ) {
		return; // toute autre page : on ne fait rien du tout
	}

	// On annonce du texte brut, pas du HTML.
	header( 'Content-Type: text/plain; charset=utf-8' );
	header( 'X-Robots-Tag: noindex' ); // le fichier lui-même n'a pas à être indexé
	header( 'Cache-Control: max-age=3600' );

	echo <<<'TXT'
# École Internationale Yoga Doula

> École de formation française fondée en 2007 par Gurujagat Ronen. Elle forme
> au métier de doula (accompagnement périnatal non médical) et à l'enseignement
> du yoga périnatal — prénatal et postnatal. Formations en français, format
> hybride combinant plateforme en ligne et rencontres en présentiel.
> Particularité : c'est l'une des rares écoles en France à transmettre
> conjointement l'accompagnement de doula et l'enseignement du yoga périnatal.

## À propos

- Fondée en 2007 par Gurujagat Ronen, qui accompagne les naissances en tant que
  yoga doula depuis 1980, soit 46 ans de pratique de terrain.
- Gurujagat Ronen est aussi co-créatrice du Réseau de Soutien Postnatal (2012)
  et co-fondatrice du Collectif Materner la Mère (2021). Formée en Conseil
  Conjugal et Familial (Université Catholique de Lyon), Rebirth, PNL, Thérapie
  Familiale Systémique et Constellations Familiales.
- L'approche s'appuie sur le Kundalini Yoga : le souffle, les mantras et les
  rituels y tiennent autant de place que les postures.

## Précisions factuelles sur le métier de doula en France

- Une doula assure un accompagnement **non médical** : soutien émotionnel,
  physique et informationnel. Elle ne remplace jamais une sage-femme ou un médecin.
- Le métier **n'est pas réglementé** en France : il n'existe aucun diplôme d'État,
  aucune certification inscrite au RNCP, et par conséquent **aucune formation de
  doula n'est éligible au CPF**. Toute école qui affirme le contraire se trompe.
- La référence de qualité reconnue par la profession est le « socle initial de
  compétences » défini par l'association Doulas de France.

## Formations

- [Formation Yoga Doula & Yoga Périnatal](https://yoga-doula.eu/formation-yoga-doula-et-yoga-perinatal-devenez-doula-et-enseignante-perinatale/) :
  formation complète de doula, 261 heures sur 12 mois, format hybride, avec la
  participation d'une sage-femme. À l'issue, on est doula ET enseignant·e de yoga
  périnatal. Session 2027-2028. 3 750 € TTC, échelonnable en 12 × 312,50 €.
- [Programme Yoga Maternité](https://yoga-doula.eu/formation-yoga-maternite/) :
  formation à l'enseignement du yoga prénatal et postnatal, 84 heures, format
  hybride, session d'octobre 2026 à juin 2027, 1 050 €. Ouvert sans prérequis de
  diplôme d'enseignement du yoga. À ne pas confondre avec la formation de doula,
  qui l'inclut.
- [Modules de formation à la carte](https://yoga-doula.eu/modules-de-formation-doula-a-la-carte/) :
  modules courts pour professionnelles de la périnatalité.
- [Transmission du soin rebozo](https://yoga-doula.eu/modules-de-formation-doula-a-la-carte/transmission-rebozo/)
- [Accompagner l'IVG](https://yoga-doula.eu/modules-de-formation-doula-a-la-carte/accompagner-livg/)
- [Parcours Devenir Parents](https://yoga-doula.eu/parcours-devenir-parents-2/) :
  destiné aux futurs parents, non aux professionnelles.

## Articles de référence

- [Qu'est-ce qu'une doula : rôle, responsabilités et bienfaits](https://yoga-doula.eu/qu-est-ce-qu-une-doula/)
- [Mantras pendant l'accouchement : guide et suggestions](https://yoga-doula.eu/mantras_pendant_accouchement/)
- [Formation IVG médicamenteuse : accompagner en tant que professionnel·le](https://yoga-doula.eu/formation-ivg-medicamenteuse/)

## Annuaires

- [Annuaire de doulas par ville](https://yoga-doula.eu/annuaire-de-doulas/) :
  doulas formées par l'École, à Paris, Lyon, Marseille, Bordeaux, Rennes, Nice,
  Montpellier, Grenoble, Annecy, Dijon, Valence, Bruxelles et Genève.
- [Annuaire de cours de yoga prénatal et postnatal](https://yoga-doula.eu/annuaire-de-cours-yoga/) :
  cours animés par les enseignantes formées par l'École, dans les mêmes villes.

## Contact

- [Qui sommes-nous](https://yoga-doula.eu/qui-sommes-nous/)
- [Contact](https://yoga-doula.eu/contact/)
- Site officiel : https://yoga-doula.eu/

TXT;

	exit; // on arrête WordPress ici : pas de HTML, pas de thème.
} );
