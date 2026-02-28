ANALYSE DES PERFORMANCES COMMERCIALES - AMAZON (POWER BI, PYTHON) 
 
Objectif : Analyser les performances commerciales afin d’identifier les leviers d’optimisation des ventes 
 
. Nettoyage, structuration et préparation des données de ventes à l’aide de Python (pandas), 

. Analyse des ventes selon plusieurs dimensions (produits, catégories, périodes) pour comprendre les dynamiques de performance, 

. Conception de tableaux de bord interactifs facilitant le suivi et la comparaison des performances commerciales, 

. Mise en place de KPI clés : chiffre d’affaires, volumes de ventes, produits les plus performants, 

. Identification des catégories à fort potentiel et des tendances de consommation afin de soutenir les décisions commerciales et stratégiques, 

<h1> les statistique de ventes </h1><br>
<H4> chaque article est mit en avant par :  </H4><br>
<ul>
  <li>son identifiant</li>
  <li> son nommation </li>
  <li> son nombre de vente </li>
  <li> son prix unitaire   </li>
  <li> son impacte sur le chiffre d'affaires final </li>
  <li> son impact sur le nombre total de vente </li>
</ul><br><br>
<img width="1223" height="757" alt="image" src="https://github.com/user-attachments/assets/1f0b4e1e-c4d1-4933-83f1-990c072bc241" /><br><br>
<H1> classification des articles en fonction de leur effectif vente ainsi que leur  poourcentages sur la vente globales </H1>
<img width="783" height="191" alt="image" src="https://github.com/user-attachments/assets/7cd187fa-789b-4230-9126-2fc9dd9dfe89" /><br><br>

<H1>Orientation comportement client  : Appétance Client par catégories </H1><br>


<img width="1277" height="751" alt="image" src="https://github.com/user-attachments/assets/892e1ad7-6d04-4490-a887-7eb52343543c" /><br><br>

<H1>Cathegories d'articles phares les plus reccurentes </H1>

<img width="705" height="318" alt="image" src="https://github.com/user-attachments/assets/592d6f52-c6b9-41ad-acf9-449305c5d8fb" /> <img width="390" height="371" alt="image" src="https://github.com/user-attachments/assets/1e68080e-f192-41ab-9483-22630cb1c9b9" />

<br><br>
<h1> Telecharger le projet </h1>

* dans le dossier data :
     - amazon_raw.csv : le dataset d'origine
     - amazonClean.csv : le dataset apres filtrage grace au script python
* dans le dossier python :
     - p.py le script ayant permis le filtrage
* dans le dossier analyse des performances :
     - tableau de bord.pbix le tableau de bord sous power bi presenté
* lors de l'ouverture du tableau de bord une erreur sur l'emplacement des données s'affichera ce qui est normal :  
     - dans power bi sur le ruban du haut dans la rubrique ACCEUIL cliquer sur transfomer les données
     - vous verez plusieurs tables
     - un message s'affichera vous demandant de modifier le chemin d'acces aux données
     - parcourer votre appareil pour selectionner le dataset <b>amazonClean.csv<b>

