{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Gymnases', 'Sportifs']"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Import des librairies\n",
    "from pymongo import MongoClient\n",
    "#Connection au client Mongo\n",
    "client = MongoClient()\n",
    "#Instancier base de données \"Gym\"\n",
    "db = client.gym\n",
    "#Afficher toutes les collections de la base de données \"Gym\"\n",
    "db.list_collection_names()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Il y a 28 documents dans Gymnases\n",
      "\n",
      "Il y a 150 documents dans Sportifs\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#1.a) Le nombre de documents dans \"Gymnases\" des collections\n",
    "total_count_gym = db.Gymnases.count_documents({})\n",
    "print(\"Il y a\", total_count_gym, \"documents dans Gymnases\\n\")\n",
    "#1.b) Le nombre de documents dans \"Sportifs\" des collections\n",
    "total_count_sport = db.Sportifs.count_documents({})\n",
    "print(\"Il y a\", total_count_sport, \"documents dans Sportifs\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GYMNASE : \n",
      "{'_id': '566eec69662b388eba46429b', 'IdGymnase': 3, 'NomGymnase': 'SAINT EXUPERY', 'Adresse': '47 bvd des brumes', 'Ville': 'PIERREFITTE', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Mercredi', 'Horaire': 11.0, 'Duree': 30, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'jeudi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "\n",
      "SPORTIF : \n",
      "{'_id': '566eec5f662b388eba464203', 'IdSportif': 1, 'Nom': 'BOUTAHAR', 'Prenom': 'Abderahim', 'Sexe': 'm', 'Age': 30, 'Sports': {'Jouer': ['Volley ball', 'Tennis', 'Football'], 'Arbitrer': ['Basket ball', 'Volley ball', 'Hockey'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Hockey', 'Badmington']}}\n"
     ]
    }
   ],
   "source": [
    "#1.c) Afficher un document de \"Gymnases\"\n",
    "gymnases = db.Gymnases.find({\"_id\": \"566eec69662b388eba46429b\"})\n",
    "print(\"GYMNASE : \")\n",
    "for gymnase in gymnases:\n",
    "    print(gymnase)\n",
    "#1.d) Afficher un document de \"Sportifs\"\n",
    "sportifs = db.Sportifs.find({\"_id\": \"566eec5f662b388eba464203\"})\n",
    "print(\"\\nSPORTIF : \")\n",
    "for sportif in sportifs:\n",
    "    print(sportif)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec5f662b388eba464204', 'IdSportif': 2, 'Nom': 'KERVADEC', 'Prenom': 'Yann', 'Sexe': 'M', 'Age': 28, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Ping pong', 'Football'], 'Arbitrer': ['Hockey', 'Football'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Tennis', 'Hockey', 'Badmington', 'Ping pong', 'Boxe']}}\n"
     ]
    }
   ],
   "source": [
    "#2) Le conseiller du nom de \"KERVADEC\"\n",
    "kervadec = db.Sportifs.find({\"Nom\": \"KERVADEC\"})\n",
    "for nom in kervadec:\n",
    "    print(nom)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec5f662b388eba464206', 'IdSportif': 4, 'Nom': 'DORLEANS', 'Prenom': 'Jean-michel', 'Sexe': 'M', 'Age': 32, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Volley ball', 'Football'], 'Arbitrer': ['Basket ball', 'Volley ball', 'Ping pong', 'Boxe'], 'Entrainer': ['Basket ball', 'Ping pong', 'Boxe']}}\n",
      "{'_id': '566eec5f662b388eba46421d', 'IdSportif': 28, 'Nom': 'RABAHI', 'Prenom': 'Rabah', 'Sexe': 'M', 'Age': 40, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba46423d', 'IdSportif': 60, 'Nom': 'TIZEGHAT', 'Prenom': 'Benamar', 'Sexe': 'M', 'Age': 32, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Hand ball', 'Tennis', 'Football'], 'Arbitrer': 'Volley ball', 'Entrainer': ['Volley ball', 'Tennis', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba46423f', 'IdSportif': 62, 'Nom': 'BAZOUD', 'Prenom': 'Jérôme', 'Sexe': 'M', 'Age': 32, 'IdSportifConseiller': 3, 'Sports': {'Jouer': 'Football'}}\n",
      "{'_id': '566eec60662b388eba464253', 'IdSportif': 82, 'Nom': 'HOUEL', 'Prenom': 'Jean-louis', 'Sexe': 'M', 'Age': 40, 'IdSportifConseiller': 14, 'Sports': {'Jouer': 'Football'}}\n",
      "{'_id': '566eec60662b388eba464264', 'IdSportif': 99, 'Nom': 'BONE', 'Prenom': 'Guy', 'Sexe': 'M', 'Age': 32, 'Sports': {'Jouer': 'Football'}}\n"
     ]
    }
   ],
   "source": [
    "#3) Les sportifs qui ont ou 32ans ou 40 ans\n",
    "sportifs = db.Sportifs.find({\"$or\":[ {\"Age\":32}, {\"Age\":40}]})\n",
    "for age in sportifs:\n",
    "    print(age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec5f662b388eba464204', 'IdSportif': 2, 'Nom': 'KERVADEC', 'Prenom': 'Yann', 'Sexe': 'M', 'Age': 28, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Ping pong', 'Football'], 'Arbitrer': ['Hockey', 'Football'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Tennis', 'Hockey', 'Badmington', 'Ping pong', 'Boxe']}}\n",
      "{'_id': '566eec5f662b388eba464207', 'IdSportif': 5, 'Nom': 'COMES', 'Prenom': 'Sylvie', 'Sexe': 'F', 'Age': 22, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Badmington', 'Ping pong'], 'Arbitrer': 'Ping pong'}}\n",
      "{'_id': '566eec5f662b388eba464208', 'IdSportif': 6, 'Nom': 'RETALDI', 'Prenom': 'Sophie', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Ping pong'], 'Arbitrer': ['Basket ball', 'Hockey', 'Ping pong'], 'Entrainer': ['Hockey', 'Ping pong', 'Boxe']}}\n",
      "{'_id': '566eec5f662b388eba46420f', 'IdSportif': 14, 'Nom': 'CAILLIOT', 'Prenom': 'Stéphanie', 'Sexe': 'F', 'Age': 24, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Ping pong']}}\n",
      "{'_id': '566eec5f662b388eba464215', 'IdSportif': 20, 'Nom': 'TIENER', 'Prenom': 'Thomas', 'Sexe': 'M', 'Age': 25, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Ping pong', 'Football'], 'Arbitrer': 'Volley ball'}}\n",
      "{'_id': '566eec5f662b388eba464217', 'IdSportif': 22, 'Nom': 'LEDUFAUD', 'Prenom': 'Pierre', 'Sexe': 'M', 'Age': 25, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec5f662b388eba464219', 'IdSportif': 24, 'Nom': 'LEJEUNE', 'Prenom': 'Sylvaine', 'Sexe': 'F', 'Age': 23, 'IdSportifConseiller': 7, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Badmington', 'Ping pong']}}\n",
      "{'_id': '566eec5f662b388eba46421d', 'IdSportif': 28, 'Nom': 'RABAHI', 'Prenom': 'Rabah', 'Sexe': 'M', 'Age': 40, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec5f662b388eba464221', 'IdSportif': 32, 'Nom': 'VAN CAUTER', 'Prenom': 'Vincent', 'Sexe': 'M', 'Age': 23, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Badmington', 'Ping pong', 'Football'], 'Arbitrer': 'Ping pong', 'Entrainer': 'Ping pong'}}\n",
      "{'_id': '566eec60662b388eba464224', 'IdSportif': 35, 'Nom': 'TANQUE', 'Prenom': 'Yann', 'Sexe': 'M', 'Age': 24, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Ping pong', 'Football'], 'Arbitrer': 'Badmington', 'Entrainer': ['Badmington', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba464225', 'IdSportif': 36, 'Nom': 'DJELOUDANE', 'Prenom': 'Zinedine', 'Sexe': 'M', 'Age': 28, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Ping pong', 'Football'], 'Entrainer': 'Badmington'}}\n",
      "{'_id': '566eec60662b388eba464229', 'IdSportif': 40, 'Nom': 'VALIN', 'Prenom': 'Yann', 'Sexe': 'M', 'Age': 23, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Badmington', 'Ping pong', 'Football'], 'Entrainer': ['Badmington', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba46422d', 'IdSportif': 44, 'Nom': 'ADIBO', 'Prenom': 'Senamé', 'Sexe': 'M', 'Age': 28, 'IdSportifConseiller': 21, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464231', 'IdSportif': 48, 'Nom': 'HEDDI', 'Prenom': 'Zohra', 'Sexe': 'F', 'Age': 23, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong'], 'Entrainer': 'Badmington'}}\n",
      "{'_id': '566eec60662b388eba464232', 'IdSportif': 49, 'Nom': 'JOUVE', 'Prenom': 'Sandra', 'Sexe': 'F', 'Age': 24, 'IdSportifConseiller': 5, 'Sports': {'Jouer': ['Basket ball', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba464233', 'IdSportif': 50, 'Nom': 'KALOMBO', 'Prenom': 'Yannick', 'Sexe': 'M', 'Age': 22, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong', 'Football'], 'Entrainer': 'Badmington'}}\n",
      "{'_id': '566eec60662b388eba464234', 'IdSportif': 51, 'Nom': 'LOPEZ', 'Prenom': 'Thibaud', 'Sexe': 'M', 'Age': 24, 'IdSportifConseiller': 5, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464235', 'IdSportif': 52, 'Nom': 'DANDOIS', 'Prenom': 'Régis', 'Sexe': 'M', 'Age': 22, 'IdSportifConseiller': 5, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464236', 'IdSportif': 53, 'Nom': 'DEMMER', 'Prenom': 'Thomas', 'Sexe': 'M', 'Age': 22, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464239', 'IdSportif': 56, 'Nom': 'GUERRAOUI', 'Prenom': 'Zohra', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Ping pong'], 'Entrainer': 'Badmington'}}\n",
      "{'_id': '566eec60662b388eba46423b', 'IdSportif': 58, 'Nom': 'GUIGUI', 'Prenom': 'Vincent', 'Sexe': 'M', 'Age': 23, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong', 'Football'], 'Entrainer': ['Volley ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba46423c', 'IdSportif': 59, 'Nom': 'CLERICE', 'Prenom': 'Stéphanie', 'Sexe': 'F', 'Age': 23, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong'], 'Arbitrer': 'Tennis', 'Entrainer': ['Volley ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba464240', 'IdSportif': 63, 'Nom': 'AMAND', 'Prenom': 'Patrick', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464246', 'IdSportif': 69, 'Nom': 'MARIE', 'Prenom': 'Paule', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 7, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba46424e', 'IdSportif': 77, 'Nom': 'HEON', 'Prenom': 'Philippe', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464251', 'IdSportif': 80, 'Nom': 'HOCHET', 'Prenom': 'Pierre', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464256', 'IdSportif': 85, 'Nom': 'HAMARD', 'Prenom': 'Romain', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464259', 'IdSportif': 88, 'Nom': 'LEJEUNE', 'Prenom': 'Richard', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 8, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba46425c', 'IdSportif': 91, 'Nom': 'LECHEVALIER', 'Prenom': 'Patrick', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 98, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba46425f', 'IdSportif': 94, 'Nom': 'LEROUX', 'Prenom': 'Paule', 'Sexe': 'M', 'Age': 36, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Ping pong', 'Football'], 'Arbitrer': 'Basket ball'}}\n",
      "{'_id': '566eec60662b388eba464263', 'IdSportif': 98, 'Nom': 'RICHARD', 'Prenom': 'William', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Ping pong', 'Football'], 'Arbitrer': 'Basket ball'}}\n",
      "{'_id': '566eec60662b388eba46426a', 'IdSportif': 105, 'Nom': 'STILO', 'Prenom': 'Philippe', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Ping pong', 'Football'], 'Arbitrer': 'Basket ball'}}\n",
      "{'_id': '566eec60662b388eba46426d', 'IdSportif': 108, 'Nom': 'LAURENCE', 'Prenom': 'Serge', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba46426e', 'IdSportif': 109, 'Nom': 'SAUVAGE', 'Prenom': 'Patrick', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 5, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464277', 'IdSportif': 118, 'Nom': 'FROMENT', 'Prenom': 'Philippe', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba46427c', 'IdSportif': 123, 'Nom': 'LETHIMONNIER', 'Prenom': 'Victor', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 6, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba46427e', 'IdSportif': 125, 'Nom': 'JALON', 'Prenom': 'Patrick', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464282', 'IdSportif': 129, 'Nom': 'DABON', 'Prenom': 'Richard', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464285', 'IdSportif': 132, 'Nom': 'DORON', 'Prenom': 'Yannick', 'Sexe': 'M', 'Age': 30, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464296', 'IdSportif': 149, 'Nom': 'BELZ', 'Prenom': 'Sylvianne', 'Sexe': 'F', 'Age': 27, 'IdSportifConseiller': 7, 'Sports': {'Jouer': 'Basket ball', 'Arbitrer': 'Basket ball', 'Entrainer': 'Basket ball'}}\n",
      "{'_id': '566eec60662b388eba464298', 'IdSportif': 151, 'Nom': 'HENRY', 'Prenom': 'Maël', 'Sexe': 'M', 'Age': 25, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Hand ball'], 'Arbitrer': ['Basket ball', 'Hand ball'], 'Entrainer': ['Basket ball', 'Hand ball']}}\n"
     ]
    }
   ],
   "source": [
    "#4) Les sportifs jouant au basket ball\n",
    "basketball = db.Sportifs.find({\"Sports.Jouer\": {\"$in\" :[\"Basket ball\"]}})\n",
    "for sport in basketball:\n",
    "    print(sport)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec5f662b388eba464205', 'IdSportif': 3, 'Nom': 'HUE', 'Prenom': 'Pascale', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Volley ball', 'Ping pong'], 'Arbitrer': ['Volley ball', 'Badmington', 'Ping pong'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Badmington']}}\n",
      "{'_id': '566eec5f662b388eba464206', 'IdSportif': 4, 'Nom': 'DORLEANS', 'Prenom': 'Jean-michel', 'Sexe': 'M', 'Age': 32, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Volley ball', 'Football'], 'Arbitrer': ['Basket ball', 'Volley ball', 'Ping pong', 'Boxe'], 'Entrainer': ['Basket ball', 'Ping pong', 'Boxe']}}\n",
      "{'_id': '566eec5f662b388eba464207', 'IdSportif': 5, 'Nom': 'COMES', 'Prenom': 'Sylvie', 'Sexe': 'F', 'Age': 22, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Badmington', 'Ping pong'], 'Arbitrer': 'Ping pong'}}\n",
      "{'_id': '566eec5f662b388eba464208', 'IdSportif': 6, 'Nom': 'RETALDI', 'Prenom': 'Sophie', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Ping pong'], 'Arbitrer': ['Basket ball', 'Hockey', 'Ping pong'], 'Entrainer': ['Hockey', 'Ping pong', 'Boxe']}}\n",
      "{'_id': '566eec5f662b388eba46420a', 'IdSportif': 9, 'Nom': 'ANTUNES', 'Prenom': 'Gaêlle', 'Sexe': 'F', 'Age': 23, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Volley ball', 'Tennis', 'Badmington']}}\n",
      "{'_id': '566eec5f662b388eba46420f', 'IdSportif': 14, 'Nom': 'CAILLIOT', 'Prenom': 'Stéphanie', 'Sexe': 'F', 'Age': 24, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Ping pong']}}\n",
      "{'_id': '566eec5f662b388eba464213', 'IdSportif': 18, 'Nom': 'HOSNI', 'Prenom': 'Leila', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 5, 'Sports': {'Jouer': 'Volley ball'}}\n",
      "{'_id': '566eec5f662b388eba464219', 'IdSportif': 24, 'Nom': 'LEJEUNE', 'Prenom': 'Sylvaine', 'Sexe': 'F', 'Age': 23, 'IdSportifConseiller': 7, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Badmington', 'Ping pong']}}\n",
      "{'_id': '566eec5f662b388eba46421b', 'IdSportif': 26, 'Nom': 'MICHEL', 'Prenom': 'Frédérique', 'Sexe': 'F', 'Age': 23, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Volley ball', 'Hand ball', 'Tennis', 'Badmington']}}\n",
      "{'_id': '566eec5f662b388eba46421d', 'IdSportif': 28, 'Nom': 'RABAHI', 'Prenom': 'Rabah', 'Sexe': 'M', 'Age': 40, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Ping pong', 'Football']}}\n",
      "{'_id': '566eec5f662b388eba46421e', 'IdSportif': 29, 'Nom': 'ROUSSEL', 'Prenom': 'Nadège', 'Sexe': 'F', 'Age': 22, 'IdSportifConseiller': 5, 'Sports': {'Jouer': ['Volley ball', 'Hand ball', 'Badmington', 'Ping pong'], 'Arbitrer': 'Ping pong', 'Entrainer': 'Ping pong'}}\n",
      "{'_id': '566eec60662b388eba464226', 'IdSportif': 37, 'Nom': 'LAZZARI', 'Prenom': 'Magali', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 44, 'Sports': {'Jouer': 'Volley ball'}}\n",
      "{'_id': '566eec60662b388eba46422a', 'IdSportif': 41, 'Nom': 'DELOVINA', 'Prenom': 'Elina', 'Sexe': 'F', 'Age': 22, 'IdSportifConseiller': 7, 'Sports': {'Jouer': ['Tennis', 'Badmington']}}\n",
      "{'_id': '566eec60662b388eba46422c', 'IdSportif': 43, 'Nom': 'MATHIEU', 'Prenom': 'Denise', 'Sexe': 'F', 'Age': 23, 'IdSportifConseiller': 6, 'Sports': {'Jouer': ['Hand ball', 'Tennis', 'Badmington']}}\n",
      "{'_id': '566eec60662b388eba464230', 'IdSportif': 47, 'Nom': 'GROEN', 'Prenom': 'Céline', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 2, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba464231', 'IdSportif': 48, 'Nom': 'HEDDI', 'Prenom': 'Zohra', 'Sexe': 'F', 'Age': 23, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong'], 'Entrainer': 'Badmington'}}\n",
      "{'_id': '566eec60662b388eba464232', 'IdSportif': 49, 'Nom': 'JOUVE', 'Prenom': 'Sandra', 'Sexe': 'F', 'Age': 24, 'IdSportifConseiller': 5, 'Sports': {'Jouer': ['Basket ball', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba464239', 'IdSportif': 56, 'Nom': 'GUERRAOUI', 'Prenom': 'Zohra', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Ping pong'], 'Entrainer': 'Badmington'}}\n",
      "{'_id': '566eec60662b388eba46423c', 'IdSportif': 59, 'Nom': 'CLERICE', 'Prenom': 'Stéphanie', 'Sexe': 'F', 'Age': 23, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong'], 'Arbitrer': 'Tennis', 'Entrainer': ['Volley ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba46423d', 'IdSportif': 60, 'Nom': 'TIZEGHAT', 'Prenom': 'Benamar', 'Sexe': 'M', 'Age': 32, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Hand ball', 'Tennis', 'Football'], 'Arbitrer': 'Volley ball', 'Entrainer': ['Volley ball', 'Tennis', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba46423f', 'IdSportif': 62, 'Nom': 'BAZOUD', 'Prenom': 'Jérôme', 'Sexe': 'M', 'Age': 32, 'IdSportifConseiller': 3, 'Sports': {'Jouer': 'Football'}}\n",
      "{'_id': '566eec60662b388eba464241', 'IdSportif': 64, 'Nom': 'LANOE', 'Prenom': 'Françoise', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 2, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba464244', 'IdSportif': 67, 'Nom': 'VONTHRON', 'Prenom': 'Dominique', 'Sexe': 'F', 'Age': 26, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Hand ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba464245', 'IdSportif': 68, 'Nom': 'REGNAULD', 'Prenom': 'Jeanne', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 2, 'Sports': {'Jouer': 'Hand ball'}}\n",
      "{'_id': '566eec60662b388eba464246', 'IdSportif': 69, 'Nom': 'MARIE', 'Prenom': 'Paule', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 7, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba46424c', 'IdSportif': 75, 'Nom': 'SARRAZIN', 'Prenom': 'Noëlle', 'Sexe': 'F', 'Age': 39, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Hand ball', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba46424d', 'IdSportif': 76, 'Nom': 'HALGATTE', 'Prenom': 'Claude', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 21, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba464252', 'IdSportif': 81, 'Nom': 'DROULLON', 'Prenom': 'Joëlle', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 1}\n",
      "{'_id': '566eec60662b388eba464253', 'IdSportif': 82, 'Nom': 'HOUEL', 'Prenom': 'Jean-louis', 'Sexe': 'M', 'Age': 40, 'IdSportifConseiller': 14, 'Sports': {'Jouer': 'Football'}}\n",
      "{'_id': '566eec60662b388eba46425f', 'IdSportif': 94, 'Nom': 'LEROUX', 'Prenom': 'Paule', 'Sexe': 'M', 'Age': 36, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Ping pong', 'Football'], 'Arbitrer': 'Basket ball'}}\n",
      "{'_id': '566eec60662b388eba464264', 'IdSportif': 99, 'Nom': 'BONE', 'Prenom': 'Guy', 'Sexe': 'M', 'Age': 32, 'Sports': {'Jouer': 'Football'}}\n",
      "{'_id': '566eec60662b388eba464269', 'IdSportif': 104, 'Nom': 'SEHIER', 'Prenom': 'Dominique', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Hand ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba464273', 'IdSportif': 114, 'Nom': 'MICHEL', 'Prenom': 'Danielle', 'Sexe': 'F', 'Age': 22, 'IdSportifConseiller': 5, 'Sports': {'Jouer': ['Hand ball', 'Tennis', 'Badmington']}}\n",
      "{'_id': '566eec60662b388eba464275', 'IdSportif': 116, 'Nom': 'BELUAU', 'Prenom': 'Gilberte', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 8}\n",
      "{'_id': '566eec60662b388eba464276', 'IdSportif': 117, 'Nom': 'FERREIRA', 'Prenom': 'Martine', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 2}\n",
      "{'_id': '566eec60662b388eba46427b', 'IdSportif': 122, 'Nom': 'BECQUET', 'Prenom': 'Erika', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 6, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba46427d', 'IdSportif': 124, 'Nom': 'SWERTVAEGER', 'Prenom': 'Michelle', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 2, 'Sports': {'Jouer': 'Hand ball'}}\n",
      "{'_id': '566eec60662b388eba464284', 'IdSportif': 131, 'Nom': 'GALLOIS', 'Prenom': 'Michelle', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 2}\n",
      "{'_id': '566eec60662b388eba464289', 'IdSportif': 136, 'Nom': 'LABOULAIS', 'Prenom': 'Chloé', 'Sexe': 'F', 'Age': 26, 'IdSportifConseiller': 2, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba46428a', 'IdSportif': 137, 'Nom': 'DUDOUIT', 'Prenom': 'Chloé', 'Sexe': 'F', 'Age': 26, 'IdSportifConseiller': 2, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba46428b', 'IdSportif': 138, 'Nom': 'MADELAINE', 'Prenom': 'Chloé', 'Sexe': 'F', 'Age': 26, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Hand ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba46428c', 'IdSportif': 139, 'Nom': 'BESNARD', 'Prenom': 'Chloé', 'Sexe': 'F', 'Age': 26, 'IdSportifConseiller': 4, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba46428d', 'IdSportif': 140, 'Nom': 'BELZ', 'Prenom': 'Chloé', 'Sexe': 'F', 'Age': 26, 'IdSportifConseiller': 7, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba46428e', 'IdSportif': 141, 'Nom': 'BONNET', 'Prenom': 'Chloé', 'Sexe': 'F', 'Age': 26, 'IdSportifConseiller': 5, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba46428f', 'IdSportif': 142, 'Nom': 'CORNET', 'Prenom': 'Chloé', 'Sexe': 'F', 'Age': 26, 'IdSportifConseiller': 1, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba464290', 'IdSportif': 143, 'Nom': 'BEUZELIN', 'Prenom': 'Chloé', 'Sexe': 'F', 'Age': 26, 'IdSportifConseiller': 5, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba464291', 'IdSportif': 144, 'Nom': 'GRANDIDIER', 'Prenom': 'Chloé', 'Sexe': 'F', 'Age': 26, 'IdSportifConseiller': 2, 'Sports': {'Jouer': 'Tennis'}}\n",
      "{'_id': '566eec60662b388eba464292', 'IdSportif': 145, 'Nom': 'LENEVEU', 'Prenom': 'Marie', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 2}\n",
      "{'_id': '566eec60662b388eba464294', 'IdSportif': 147, 'Nom': 'CLERICE', 'Prenom': 'Alice', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 2}\n",
      "{'_id': '566eec60662b388eba464295', 'IdSportif': 148, 'Nom': 'COMES', 'Prenom': 'Marie', 'Sexe': 'F', 'Age': 27, 'IdSportifConseiller': 1}\n",
      "{'_id': '566eec60662b388eba464296', 'IdSportif': 149, 'Nom': 'BELZ', 'Prenom': 'Sylvianne', 'Sexe': 'F', 'Age': 27, 'IdSportifConseiller': 7, 'Sports': {'Jouer': 'Basket ball', 'Arbitrer': 'Basket ball', 'Entrainer': 'Basket ball'}}\n"
     ]
    }
   ],
   "source": [
    "#5) Les sportifs qui ont ou 32ans ou plus ou de sexe féminin\n",
    "sportifs = db.Sportifs.find( { \"$or\": [ { \"Age\": { \"$gte\": 32 } }, { \"Sexe\": \"F\" } ] } )\n",
    "for sportif in sportifs:\n",
    "    print(sportif)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Il y a 44 sportifs féminin\n"
     ]
    }
   ],
   "source": [
    "#6) Le nombre de sportives féminines\n",
    "total_count_sexe_femme = db.Sportifs.count_documents({\"Sexe\": \"F\"})\n",
    "print(\"Il y a\", total_count_sexe_femme, \"sportifs féminin\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'IdSportif': 1, 'Nom': 'BOUTAHAR', 'Prenom': 'Abderahim'}\n",
      "{'IdSportif': 2, 'Nom': 'KERVADEC', 'Prenom': 'Yann'}\n",
      "{'IdSportif': 3, 'Nom': 'HUE', 'Prenom': 'Pascale'}\n",
      "{'IdSportif': 5, 'Nom': 'COMES', 'Prenom': 'Sylvie'}\n",
      "{'IdSportif': 6, 'Nom': 'RETALDI', 'Prenom': 'Sophie'}\n",
      "{'IdSportif': 7, 'Nom': 'GOMEZ', 'Prenom': 'Diego'}\n",
      "{'IdSportif': 9, 'Nom': 'ANTUNES', 'Prenom': 'Gaêlle'}\n",
      "{'IdSportif': 10, 'Nom': 'BLANDET', 'Prenom': 'Arnaud'}\n",
      "{'IdSportif': 11, 'Nom': 'BONNET', 'Prenom': 'Christophe'}\n",
      "{'IdSportif': 12, 'Nom': 'BORREL', 'Prenom': 'Benoît'}\n",
      "{'IdSportif': 13, 'Nom': 'BOYON', 'Prenom': 'Julien'}\n",
      "{'IdSportif': 14, 'Nom': 'CAILLIOT', 'Prenom': 'Stéphanie'}\n",
      "{'IdSportif': 15, 'Nom': 'CHAMPENOIS', 'Prenom': 'Cédric'}\n",
      "{'IdSportif': 16, 'Nom': 'COLAS', 'Prenom': 'Michaël'}\n",
      "{'IdSportif': 17, 'Nom': 'COLOMB', 'Prenom': 'Michaël'}\n",
      "{'IdSportif': 18, 'Nom': 'HOSNI', 'Prenom': 'Leila'}\n",
      "{'IdSportif': 19, 'Nom': 'TESTEMONT', 'Prenom': 'Laurent'}\n",
      "{'IdSportif': 20, 'Nom': 'TIENER', 'Prenom': 'Thomas'}\n",
      "{'IdSportif': 21, 'Nom': 'LE BOUCHER', 'Prenom': 'Denis'}\n",
      "{'IdSportif': 22, 'Nom': 'LEDUFAUD', 'Prenom': 'Pierre'}\n",
      "{'IdSportif': 23, 'Nom': 'LEGRAND', 'Prenom': 'David'}\n",
      "{'IdSportif': 24, 'Nom': 'LEJEUNE', 'Prenom': 'Sylvaine'}\n",
      "{'IdSportif': 25, 'Nom': 'MARTORA', 'Prenom': 'Fabrice'}\n",
      "{'IdSportif': 26, 'Nom': 'MICHEL', 'Prenom': 'Frédérique'}\n",
      "{'IdSportif': 27, 'Nom': 'NIELLEZ', 'Prenom': 'Christophe'}\n",
      "{'IdSportif': 29, 'Nom': 'ROUSSEL', 'Prenom': 'Nadège'}\n",
      "{'IdSportif': 30, 'Nom': 'SCHINK', 'Prenom': 'Nicolas'}\n",
      "{'IdSportif': 31, 'Nom': 'STEMPUT', 'Prenom': 'Mathieu'}\n",
      "{'IdSportif': 32, 'Nom': 'VAN CAUTER', 'Prenom': 'Vincent'}\n",
      "{'IdSportif': 33, 'Nom': 'RAMPNOUX', 'Prenom': 'Jean françois'}\n",
      "{'IdSportif': 34, 'Nom': 'LHERPINIERE', 'Prenom': 'Olivier'}\n",
      "{'IdSportif': 35, 'Nom': 'TANQUE', 'Prenom': 'Yann'}\n",
      "{'IdSportif': 36, 'Nom': 'DJELOUDANE', 'Prenom': 'Zinedine'}\n",
      "{'IdSportif': 37, 'Nom': 'LAZZARI', 'Prenom': 'Magali'}\n",
      "{'IdSportif': 38, 'Nom': 'VASSEMON', 'Prenom': 'Laurent'}\n",
      "{'IdSportif': 39, 'Nom': 'MOREL', 'Prenom': 'Mathieu'}\n",
      "{'IdSportif': 40, 'Nom': 'VALIN', 'Prenom': 'Yann'}\n",
      "{'IdSportif': 41, 'Nom': 'DELOVINA', 'Prenom': 'Elina'}\n",
      "{'IdSportif': 42, 'Nom': 'LEHOUX', 'Prenom': 'Bruno'}\n",
      "{'IdSportif': 43, 'Nom': 'MATHIEU', 'Prenom': 'Denise'}\n",
      "{'IdSportif': 44, 'Nom': 'ADIBO', 'Prenom': 'Senamé'}\n",
      "{'IdSportif': 45, 'Nom': 'CHAVANT', 'Prenom': 'Christophe'}\n",
      "{'IdSportif': 46, 'Nom': 'DAUXIAN', 'Prenom': 'Cédric'}\n",
      "{'IdSportif': 47, 'Nom': 'GROEN', 'Prenom': 'Céline'}\n",
      "{'IdSportif': 48, 'Nom': 'HEDDI', 'Prenom': 'Zohra'}\n",
      "{'IdSportif': 49, 'Nom': 'JOUVE', 'Prenom': 'Sandra'}\n",
      "{'IdSportif': 50, 'Nom': 'KALOMBO', 'Prenom': 'Yannick'}\n",
      "{'IdSportif': 51, 'Nom': 'LOPEZ', 'Prenom': 'Thibaud'}\n",
      "{'IdSportif': 52, 'Nom': 'DANDOIS', 'Prenom': 'Régis'}\n",
      "{'IdSportif': 53, 'Nom': 'DEMMER', 'Prenom': 'Thomas'}\n",
      "{'IdSportif': 54, 'Nom': 'ELKABBADJ', 'Prenom': 'Mohammed'}\n",
      "{'IdSportif': 55, 'Nom': 'FEROLDI', 'Prenom': 'Olivier'}\n",
      "{'IdSportif': 56, 'Nom': 'GUERRAOUI', 'Prenom': 'Zohra'}\n",
      "{'IdSportif': 57, 'Nom': 'BOISSEAU', 'Prenom': 'Eric'}\n",
      "{'IdSportif': 58, 'Nom': 'GUIGUI', 'Prenom': 'Vincent'}\n",
      "{'IdSportif': 59, 'Nom': 'CLERICE', 'Prenom': 'Stéphanie'}\n",
      "{'IdSportif': 61, 'Nom': 'LAZARRE', 'Prenom': 'Jean'}\n",
      "{'IdSportif': 63, 'Nom': 'AMAND', 'Prenom': 'Patrick'}\n",
      "{'IdSportif': 64, 'Nom': 'LANOE', 'Prenom': 'Françoise'}\n",
      "{'IdSportif': 65, 'Nom': 'CHESNIER', 'Prenom': 'Marc'}\n",
      "{'IdSportif': 66, 'Nom': 'DURIEU', 'Prenom': 'Loïc'}\n",
      "{'IdSportif': 67, 'Nom': 'VONTHRON', 'Prenom': 'Dominique'}\n",
      "{'IdSportif': 68, 'Nom': 'REGNAULD', 'Prenom': 'Jeanne'}\n",
      "{'IdSportif': 69, 'Nom': 'MARIE', 'Prenom': 'Paule'}\n",
      "{'IdSportif': 70, 'Nom': 'BELLAMY', 'Prenom': 'Norbert'}\n",
      "{'IdSportif': 71, 'Nom': 'DELAROCHE', 'Prenom': 'Bertrand'}\n",
      "{'IdSportif': 72, 'Nom': 'MARTEL', 'Prenom': 'Bernard'}\n",
      "{'IdSportif': 73, 'Nom': 'DALLIER', 'Prenom': 'Didier'}\n",
      "{'IdSportif': 74, 'Nom': 'AUVRAY', 'Prenom': 'Alain'}\n",
      "{'IdSportif': 76, 'Nom': 'HALGATTE', 'Prenom': 'Claude'}\n",
      "{'IdSportif': 77, 'Nom': 'HEON', 'Prenom': 'Philippe'}\n",
      "{'IdSportif': 78, 'Nom': 'CHAUVIN', 'Prenom': 'Julien'}\n",
      "{'IdSportif': 79, 'Nom': 'HENRY', 'Prenom': 'Jacky'}\n",
      "{'IdSportif': 80, 'Nom': 'HOCHET', 'Prenom': 'Pierre'}\n",
      "{'IdSportif': 81, 'Nom': 'DROULLON', 'Prenom': 'Joëlle'}\n",
      "{'IdSportif': 83, 'Nom': 'LEROUX', 'Prenom': 'André'}\n",
      "{'IdSportif': 84, 'Nom': 'SALLAÏ', 'Prenom': 'Miloud'}\n",
      "{'IdSportif': 85, 'Nom': 'HAMARD', 'Prenom': 'Romain'}\n",
      "{'IdSportif': 86, 'Nom': 'GALLOT', 'Prenom': 'Bernard'}\n",
      "{'IdSportif': 87, 'Nom': 'COUESBOT', 'Prenom': 'Daniel'}\n",
      "{'IdSportif': 88, 'Nom': 'LEJEUNE', 'Prenom': 'Richard'}\n",
      "{'IdSportif': 89, 'Nom': 'RIQUIER', 'Prenom': 'Jean-pierre'}\n",
      "{'IdSportif': 90, 'Nom': 'DUREL', 'Prenom': 'Eric'}\n",
      "{'IdSportif': 91, 'Nom': 'LECHEVALIER', 'Prenom': 'Patrick'}\n",
      "{'IdSportif': 92, 'Nom': 'HERVIEU', 'Prenom': 'Jean-François'}\n",
      "{'IdSportif': 93, 'Nom': 'CAUCHARD', 'Prenom': 'Georges'}\n",
      "{'IdSportif': 95, 'Nom': 'EUSTACHE', 'Prenom': 'Marcel'}\n",
      "{'IdSportif': 96, 'Nom': 'JANY', 'Prenom': 'Claude'}\n",
      "{'IdSportif': 97, 'Nom': 'BONHOMME', 'Prenom': 'Bruno'}\n",
      "{'IdSportif': 98, 'Nom': 'RICHARD', 'Prenom': 'William'}\n",
      "{'IdSportif': 100, 'Nom': 'LESOIF', 'Prenom': 'Jacques'}\n",
      "{'IdSportif': 101, 'Nom': 'SWERTVAEGER', 'Prenom': 'Eric'}\n",
      "{'IdSportif': 102, 'Nom': 'DUVAL', 'Prenom': 'Alain'}\n",
      "{'IdSportif': 103, 'Nom': 'LEMENOREL', 'Prenom': 'Claude'}\n",
      "{'IdSportif': 104, 'Nom': 'SEHIER', 'Prenom': 'Dominique'}\n",
      "{'IdSportif': 105, 'Nom': 'STILO', 'Prenom': 'Philippe'}\n",
      "{'IdSportif': 106, 'Nom': 'LE BANNARD', 'Prenom': 'Gérard'}\n",
      "{'IdSportif': 107, 'Nom': 'BORNE', 'Prenom': 'Jean-Yves'}\n",
      "{'IdSportif': 108, 'Nom': 'LAURENCE', 'Prenom': 'Serge'}\n",
      "{'IdSportif': 109, 'Nom': 'SAUVAGE', 'Prenom': 'Patrick'}\n",
      "{'IdSportif': 110, 'Nom': 'ROULLAND', 'Prenom': 'Christian'}\n",
      "{'IdSportif': 111, 'Nom': 'LESIEUR', 'Prenom': 'Michel'}\n",
      "{'IdSportif': 112, 'Nom': 'LUYCKX', 'Prenom': 'Gérard'}\n",
      "{'IdSportif': 113, 'Nom': 'AVICE', 'Prenom': 'Benoît'}\n",
      "{'IdSportif': 114, 'Nom': 'MICHEL', 'Prenom': 'Danielle'}\n",
      "{'IdSportif': 115, 'Nom': 'LEMOUSSU', 'Prenom': 'Laurent'}\n",
      "{'IdSportif': 116, 'Nom': 'BELUAU', 'Prenom': 'Gilberte'}\n",
      "{'IdSportif': 117, 'Nom': 'FERREIRA', 'Prenom': 'Martine'}\n",
      "{'IdSportif': 118, 'Nom': 'FROMENT', 'Prenom': 'Philippe'}\n",
      "{'IdSportif': 119, 'Nom': 'GUITON', 'Prenom': 'Jean-paul'}\n",
      "{'IdSportif': 120, 'Nom': 'LECOMTE', 'Prenom': 'Christian'}\n",
      "{'IdSportif': 121, 'Nom': 'HUET', 'Prenom': 'Loïc'}\n",
      "{'IdSportif': 122, 'Nom': 'BECQUET', 'Prenom': 'Erika'}\n",
      "{'IdSportif': 123, 'Nom': 'LETHIMONNIER', 'Prenom': 'Victor'}\n",
      "{'IdSportif': 124, 'Nom': 'SWERTVAEGER', 'Prenom': 'Michelle'}\n",
      "{'IdSportif': 125, 'Nom': 'JALON', 'Prenom': 'Patrick'}\n",
      "{'IdSportif': 126, 'Nom': 'DEBOUT', 'Prenom': 'Eric'}\n",
      "{'IdSportif': 127, 'Nom': 'GASTELLIER', 'Prenom': 'Charles'}\n",
      "{'IdSportif': 128, 'Nom': 'GIRONIE', 'Prenom': 'André'}\n",
      "{'IdSportif': 129, 'Nom': 'DABON', 'Prenom': 'Richard'}\n",
      "{'IdSportif': 130, 'Nom': 'LECHAUVE', 'Prenom': 'Jean-Claude'}\n",
      "{'IdSportif': 131, 'Nom': 'GALLOIS', 'Prenom': 'Michelle'}\n",
      "{'IdSportif': 132, 'Nom': 'DORON', 'Prenom': 'Yannick'}\n",
      "{'IdSportif': 133, 'Nom': 'LENEVEU', 'Prenom': 'Julien'}\n",
      "{'IdSportif': 134, 'Nom': 'LERICHE', 'Prenom': 'Harry'}\n",
      "{'IdSportif': 135, 'Nom': 'MANCEL', 'Prenom': 'Jean-luc'}\n",
      "{'IdSportif': 136, 'Nom': 'LABOULAIS', 'Prenom': 'Chloé'}\n",
      "{'IdSportif': 137, 'Nom': 'DUDOUIT', 'Prenom': 'Chloé'}\n",
      "{'IdSportif': 138, 'Nom': 'MADELAINE', 'Prenom': 'Chloé'}\n",
      "{'IdSportif': 139, 'Nom': 'BESNARD', 'Prenom': 'Chloé'}\n",
      "{'IdSportif': 140, 'Nom': 'BELZ', 'Prenom': 'Chloé'}\n",
      "{'IdSportif': 141, 'Nom': 'BONNET', 'Prenom': 'Chloé'}\n",
      "{'IdSportif': 142, 'Nom': 'CORNET', 'Prenom': 'Chloé'}\n",
      "{'IdSportif': 143, 'Nom': 'BEUZELIN', 'Prenom': 'Chloé'}\n",
      "{'IdSportif': 144, 'Nom': 'GRANDIDIER', 'Prenom': 'Chloé'}\n",
      "{'IdSportif': 145, 'Nom': 'LENEVEU', 'Prenom': 'Marie'}\n",
      "{'IdSportif': 146, 'Nom': 'DABON', 'Prenom': 'Rick'}\n",
      "{'IdSportif': 147, 'Nom': 'CLERICE', 'Prenom': 'Alice'}\n",
      "{'IdSportif': 148, 'Nom': 'COMES', 'Prenom': 'Marie'}\n",
      "{'IdSportif': 149, 'Nom': 'BELZ', 'Prenom': 'Sylvianne'}\n",
      "{'IdSportif': 150, 'Nom': 'BELZ', 'Prenom': 'Paul'}\n",
      "{'IdSportif': 151, 'Nom': 'HENRY', 'Prenom': 'Maël'}\n"
     ]
    }
   ],
   "source": [
    "#7) Les identifiants, noms et prénoms des sports qui ont entre 20 et 30 ans\n",
    "sportifs = db.Sportifs.find({\"Age\": { \"$gte\": 20, \"$lte\": 30}},{\"_id\":0, \"Nom\":1, \"Prenom\":1, \"IdSportif\":1})\n",
    "for sportif in sportifs:\n",
    "    print(sportif)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "#8) Les identifiants et noms des sportifs qui jouent au handball\n",
    "sportifs = db.sportifs.find({\"Sports.Jouer\": {\"$in\" : [\"Hand ball\"]}}, {\"_id\": 0, \"Nom\": 1, \"IdSportif\":1})\n",
    "for sportif in sportifs:\n",
    "    print(sportif)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec69662b388eba46429c', 'IdGymnase': 4, 'NomGymnase': 'PAUL ELUARD', 'Adresse': 'Allée J.B. Lulli', 'Ville': 'SARCELLES', 'Surface': 500, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Vendredi', 'Horaire': 10.0, 'Duree': 30, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 6, 'Jour': 'mercredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba46429d', 'IdGymnase': 5, 'NomGymnase': 'BRASSENS', 'Adresse': '153 square Loliot', 'Ville': 'SARCELLES', 'Surface': 620, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 6, 'Jour': 'jeudi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a1', 'IdGymnase': 9, 'NomGymnase': 'CAMUS', 'Adresse': '3 esplanade des quatrans', 'Ville': 'SARCELLES', 'Surface': 620, 'Seances': [{'IdSportifEntraineur': 6, 'Jour': 'samedi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a8', 'IdGymnase': 16, 'NomGymnase': 'SAMOURAI', 'Adresse': '4 Allée des pendules', 'Ville': 'SARCELLES', 'Surface': 600, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'Lundi', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'Lundi', 'Horaire': 18.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'lundi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'Lundi', 'Horaire': 20.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 6, 'Jour': 'mercredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642ac', 'IdGymnase': 20, 'NomGymnase': 'LUMIERES', 'Adresse': '78 rue Vendôme', 'Ville': 'SARCELLES', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 6, 'Jour': 'mercredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642b1', 'IdGymnase': 25, 'NomGymnase': 'DOLTO', 'Adresse': '3 square Plaisir', 'Ville': 'VILLETANEUSE', 'Surface': 620, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Dimanche', 'Horaire': 18.0, 'Duree': 60, 'Libelle': 'Basket ball'}]}\n",
      "{'_id': '566eec69662b388eba4642b2', 'IdGymnase': 26, 'NomGymnase': 'MERMOZ', 'Adresse': '41 rue des ponts', 'Ville': 'VILLETANEUSE', 'Surface': 600}\n"
     ]
    }
   ],
   "source": [
    "#9) Gymnases de \"Villetaneuse\" ou de \"Sarcelles\" avec superficie > 400 m²\n",
    "gymnases = db.Gymnases.find({\"$and\": [{\"Surface\": { \"$gte\": 400}}, {\"$or\":[{\"Ville\": \"SARCELLES\"}, {\"Ville\": \"VILLETANEUSE\"}]}]})\n",
    "for gymnase in gymnases:\n",
    "    print(gymnase)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "#10) Gymnases ou il y a Hockey le mercredi après 15h00\n",
    "gymnases = db.Gymnases.find({\"$and\": [{\"Seances.Jour\":\"mercredi\"},{\"Seances.Horaire\":{\"$gte\":15.0}}, {\"Seance.Libelle\":\"Hockey\"}]})\n",
    "for gymnase in gymnases:\n",
    "    print(gymnase)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'IdSportif': 81, 'Nom': 'DROULLON'}\n",
      "{'IdSportif': 116, 'Nom': 'BELUAU'}\n",
      "{'IdSportif': 117, 'Nom': 'FERREIRA'}\n",
      "{'IdSportif': 131, 'Nom': 'GALLOIS'}\n",
      "{'IdSportif': 145, 'Nom': 'LENEVEU'}\n",
      "{'IdSportif': 146, 'Nom': 'DABON'}\n",
      "{'IdSportif': 147, 'Nom': 'CLERICE'}\n",
      "{'IdSportif': 148, 'Nom': 'COMES'}\n",
      "{'IdSportif': 150, 'Nom': 'BELZ'}\n"
     ]
    }
   ],
   "source": [
    "#11) identifiants et noms des sportifs sans sport\n",
    "sportifs = db.Sportifs.find({\"Sports.Jouer\": {\"$exists\" : False}}, {\"_id\":0, \"Nom\":1, \"IdSportif\":1})\n",
    "for sportif in sportifs:\n",
    "    print(sportif)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec69662b388eba46429a', 'IdGymnase': 2, 'NomGymnase': 'ARAGON', 'Adresse': 'Place du Chartres', 'Ville': 'MONTMORENCY', 'Surface': 450, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba46429b', 'IdGymnase': 3, 'NomGymnase': 'SAINT EXUPERY', 'Adresse': '47 bvd des brumes', 'Ville': 'PIERREFITTE', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Mercredi', 'Horaire': 11.0, 'Duree': 30, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'jeudi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba46429c', 'IdGymnase': 4, 'NomGymnase': 'PAUL ELUARD', 'Adresse': 'Allée J.B. Lulli', 'Ville': 'SARCELLES', 'Surface': 500, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Vendredi', 'Horaire': 10.0, 'Duree': 30, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 6, 'Jour': 'mercredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba46429d', 'IdGymnase': 5, 'NomGymnase': 'BRASSENS', 'Adresse': '153 square Loliot', 'Ville': 'SARCELLES', 'Surface': 620, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 6, 'Jour': 'jeudi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba46429e', 'IdGymnase': 6, 'NomGymnase': 'VERLAINE', 'Adresse': '14 bvd Serrault', 'Ville': 'STAINS', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 6, 'Jour': 'vendredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'jeudi', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba46429f', 'IdGymnase': 7, 'NomGymnase': 'JULES FERRY', 'Adresse': '45 rue de la gare', 'Ville': 'PIERREFITTE', 'Surface': 360}\n",
      "{'_id': '566eec69662b388eba4642a0', 'IdGymnase': 8, 'NomGymnase': 'PREVERT', 'Adresse': '12 rue des collines', 'Ville': 'MONTMORENCY', 'Surface': 420, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'vendredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 7, 'Jour': 'samedi', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'vendredi', 'Horaire': 14.0, 'Duree': 120, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a1', 'IdGymnase': 9, 'NomGymnase': 'CAMUS', 'Adresse': '3 esplanade des quatrans', 'Ville': 'SARCELLES', 'Surface': 620, 'Seances': [{'IdSportifEntraineur': 6, 'Jour': 'samedi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a2', 'IdGymnase': 10, 'NomGymnase': 'RIMBAUD', 'Adresse': '140 bvd Diderot', 'Ville': 'STAINS', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 60, 'Jour': 'samedi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 6, 'Jour': 'dimanche', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a3', 'IdGymnase': 11, 'NomGymnase': 'LAMARTINE', 'Adresse': '7 rue de la souris verte', 'Ville': 'PIERREFITTE', 'Surface': 300}\n",
      "{'_id': '566eec69662b388eba4642a4', 'IdGymnase': 12, 'NomGymnase': 'MOZART', 'Adresse': '6 Allée Rosana', 'Ville': 'MONTMORENCY', 'Surface': 480, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642a5', 'IdGymnase': 13, 'NomGymnase': 'RAVEL', 'Adresse': 'Place aux pommes', 'Ville': 'STAINS', 'Surface': 200, 'Seances': [{'IdSportifEntraineur': 60, 'Jour': 'dimanche', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 6, 'Jour': 'mercredi', 'Horaire': 20.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'lundi', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a6', 'IdGymnase': 14, 'NomGymnase': 'CHOPIN', 'Adresse': '23 rue Carafelli', 'Ville': 'MONTMORENCY', 'Surface': 500, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Mardi', 'Horaire': 10.0, 'Duree': 60, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642a7', 'IdGymnase': 15, 'NomGymnase': 'BREL', 'Adresse': '4 rue de la miséricorde', 'Ville': 'PIERREFITTE', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642a8', 'IdGymnase': 16, 'NomGymnase': 'SAMOURAI', 'Adresse': '4 Allée des pendules', 'Ville': 'SARCELLES', 'Surface': 600, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'Lundi', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'Lundi', 'Horaire': 18.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'lundi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'Lundi', 'Horaire': 20.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 6, 'Jour': 'mercredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a9', 'IdGymnase': 17, 'NomGymnase': 'GARCIA LORCA', 'Adresse': '45 bvd des Comes', 'Ville': 'STAINS', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 3, 'Jour': 'samedi', 'Horaire': 17.3, 'Duree': 120, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 3, 'Jour': 'vendredi', 'Horaire': 17.3, 'Duree': 120, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 3, 'Jour': 'dimanche', 'Horaire': 18.0, 'Duree': 30, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 3, 'Jour': 'mardi', 'Horaire': 20.0, 'Duree': 30, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 7, 'Jour': 'mardi', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642aa', 'IdGymnase': 18, 'NomGymnase': 'PABLO NERUDA', 'Adresse': '6 rue saint Jean', 'Ville': 'PIERREFITTE', 'Surface': 450, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'mardi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 14.0, 'Duree': 120, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 16.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642ab', 'IdGymnase': 19, 'NomGymnase': 'COCTEAU', 'Adresse': '45 bis rue du moulin rouge', 'Ville': 'MONTMORENCY', 'Surface': 500, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642ac', 'IdGymnase': 20, 'NomGymnase': 'LUMIERES', 'Adresse': '78 rue Vendôme', 'Ville': 'SARCELLES', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 6, 'Jour': 'mercredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642ad', 'IdGymnase': 21, 'NomGymnase': 'SIMON', 'Adresse': '8 bvd général de Gaulle', 'Ville': 'STAINS', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 30, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'mardi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 17.0, 'Duree': 30, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642ae', 'IdGymnase': 22, 'NomGymnase': 'BARBARA', 'Adresse': '45  rue du bossu', 'Ville': 'SAINT DENIS', 'Surface': 500, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'mardi', 'Horaire': 10.0, 'Duree': 30, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642af', 'IdGymnase': 23, 'NomGymnase': 'ARAGON', 'Adresse': '10 Bvd Lenoir', 'Ville': 'SAINT DENIS', 'Surface': 520}\n",
      "{'_id': '566eec69662b388eba4642b0', 'IdGymnase': 24, 'NomGymnase': 'BELFEGOR', 'Adresse': 'Place de Gaulle', 'Ville': 'SAINT DENIS', 'Surface': 450, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Jeudi', 'Horaire': 9.0, 'Duree': 90, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 57, 'Jour': 'mercredi', 'Horaire': 10.0, 'Duree': 90, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642b2', 'IdGymnase': 26, 'NomGymnase': 'MERMOZ', 'Adresse': '41 rue des ponts', 'Ville': 'VILLETANEUSE', 'Surface': 600}\n",
      "{'_id': '566eec69662b388eba4642b3', 'IdGymnase': 27, 'NomGymnase': 'PASCAL', 'Adresse': '20 rue de la pirogue', 'Ville': 'VILLETANEUSE', 'Surface': 350, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'jeudi', 'Horaire': 10.0, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 14.0, 'Duree': 120, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642b4', 'IdGymnase': 28, 'NomGymnase': 'BLAISE PASCAL', 'Adresse': '2bis rue de la moulerie', 'Ville': 'GARGES', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Lundi', 'Horaire': 9.0, 'Duree': 30, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 6, 'Jour': 'dimanche', 'Horaire': 14.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 6, 'Jour': 'dimanche', 'Horaire': 15.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 6, 'Jour': 'dimanche', 'Horaire': 16.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 6, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'mardi', 'Horaire': 18.0, 'Duree': 90, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'samedi', 'Horaire': 18.0, 'Duree': 90, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'vendredi', 'Horaire': 18.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n"
     ]
    }
   ],
   "source": [
    "#12) Gymnases fermés le dimanche\n",
    "gymnases = db.Gymnases.find({\"Seances.Jour\":{\"$nin\":[\"Dimanche\"]}})\n",
    "for gymnase in gymnases:\n",
    "    print(gymnase)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec69662b388eba464299', 'IdGymnase': 1, 'NomGymnase': 'PAUL ELUARD', 'Adresse': '2 rue des pépines', 'Ville': 'STAINS', 'Surface': 200, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Samedi', 'Horaire': 9.0, 'Duree': 60, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 1, 'Jour': 'Lundi', 'Horaire': 9.0, 'Duree': 60, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 1, 'Jour': 'Lundi', 'Horaire': 10.0, 'Duree': 60, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 1, 'Jour': 'Lundi', 'Horaire': 11.3, 'Duree': 60, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 1, 'Jour': 'Lundi', 'Horaire': 14.0, 'Duree': 90, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 1, 'Jour': 'lundi', 'Horaire': 17.3, 'Duree': 120, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 1, 'Jour': 'Lundi', 'Horaire': 19.3, 'Duree': 120, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 2, 'Jour': 'Dimanche', 'Horaire': 17.3, 'Duree': 120, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 2, 'Jour': 'Dimanche', 'Horaire': 19.3, 'Duree': 120, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 2, 'Jour': 'mardi', 'Horaire': 17.3, 'Duree': 120, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 2, 'Jour': 'mercredi', 'Horaire': 17.3, 'Duree': 120, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 2, 'Jour': 'Samedi', 'Horaire': 15.3, 'Duree': 60, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 2, 'Jour': 'Samedi', 'Horaire': 16.3, 'Duree': 60, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 2, 'Jour': 'Samedi', 'Horaire': 17.3, 'Duree': 120, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 3, 'Jour': 'jeudi', 'Horaire': 20.0, 'Duree': 30, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 3, 'Jour': 'lundi', 'Horaire': 14.0, 'Duree': 60, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 3, 'Jour': 'lundi', 'Horaire': 18.0, 'Duree': 30, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 3, 'Jour': 'lundi', 'Horaire': 19.0, 'Duree': 30, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 3, 'Jour': 'lundi', 'Horaire': 20.0, 'Duree': 30, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba46429a', 'IdGymnase': 2, 'NomGymnase': 'ARAGON', 'Adresse': 'Place du Chartres', 'Ville': 'MONTMORENCY', 'Surface': 450, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba46429b', 'IdGymnase': 3, 'NomGymnase': 'SAINT EXUPERY', 'Adresse': '47 bvd des brumes', 'Ville': 'PIERREFITTE', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Mercredi', 'Horaire': 11.0, 'Duree': 30, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'jeudi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba46429c', 'IdGymnase': 4, 'NomGymnase': 'PAUL ELUARD', 'Adresse': 'Allée J.B. Lulli', 'Ville': 'SARCELLES', 'Surface': 500, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Vendredi', 'Horaire': 10.0, 'Duree': 30, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 6, 'Jour': 'mercredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba46429d', 'IdGymnase': 5, 'NomGymnase': 'BRASSENS', 'Adresse': '153 square Loliot', 'Ville': 'SARCELLES', 'Surface': 620, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 6, 'Jour': 'jeudi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a0', 'IdGymnase': 8, 'NomGymnase': 'PREVERT', 'Adresse': '12 rue des collines', 'Ville': 'MONTMORENCY', 'Surface': 420, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'vendredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 7, 'Jour': 'samedi', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'vendredi', 'Horaire': 14.0, 'Duree': 120, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a2', 'IdGymnase': 10, 'NomGymnase': 'RIMBAUD', 'Adresse': '140 bvd Diderot', 'Ville': 'STAINS', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 60, 'Jour': 'samedi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 6, 'Jour': 'dimanche', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a4', 'IdGymnase': 12, 'NomGymnase': 'MOZART', 'Adresse': '6 Allée Rosana', 'Ville': 'MONTMORENCY', 'Surface': 480, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642a5', 'IdGymnase': 13, 'NomGymnase': 'RAVEL', 'Adresse': 'Place aux pommes', 'Ville': 'STAINS', 'Surface': 200, 'Seances': [{'IdSportifEntraineur': 60, 'Jour': 'dimanche', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 6, 'Jour': 'mercredi', 'Horaire': 20.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'lundi', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a6', 'IdGymnase': 14, 'NomGymnase': 'CHOPIN', 'Adresse': '23 rue Carafelli', 'Ville': 'MONTMORENCY', 'Surface': 500, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Mardi', 'Horaire': 10.0, 'Duree': 60, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642a7', 'IdGymnase': 15, 'NomGymnase': 'BREL', 'Adresse': '4 rue de la miséricorde', 'Ville': 'PIERREFITTE', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642a8', 'IdGymnase': 16, 'NomGymnase': 'SAMOURAI', 'Adresse': '4 Allée des pendules', 'Ville': 'SARCELLES', 'Surface': 600, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'Lundi', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'Lundi', 'Horaire': 18.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'lundi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'Lundi', 'Horaire': 20.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 6, 'Jour': 'mercredi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642a9', 'IdGymnase': 17, 'NomGymnase': 'GARCIA LORCA', 'Adresse': '45 bvd des Comes', 'Ville': 'STAINS', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 3, 'Jour': 'samedi', 'Horaire': 17.3, 'Duree': 120, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 3, 'Jour': 'vendredi', 'Horaire': 17.3, 'Duree': 120, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 3, 'Jour': 'dimanche', 'Horaire': 18.0, 'Duree': 30, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 3, 'Jour': 'mardi', 'Horaire': 20.0, 'Duree': 30, 'Libelle': 'Hand ball'}, {'IdSportifEntraineur': 7, 'Jour': 'mardi', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642aa', 'IdGymnase': 18, 'NomGymnase': 'PABLO NERUDA', 'Adresse': '6 rue saint Jean', 'Ville': 'PIERREFITTE', 'Surface': 450, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'mardi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 14.0, 'Duree': 120, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 16.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642ab', 'IdGymnase': 19, 'NomGymnase': 'COCTEAU', 'Adresse': '45 bis rue du moulin rouge', 'Ville': 'MONTMORENCY', 'Surface': 500, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642ad', 'IdGymnase': 21, 'NomGymnase': 'SIMON', 'Adresse': '8 bvd général de Gaulle', 'Ville': 'STAINS', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'lundi', 'Horaire': 16.3, 'Duree': 30, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 60, 'Jour': 'mardi', 'Horaire': 19.0, 'Duree': 60, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 17.0, 'Duree': 30, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642ae', 'IdGymnase': 22, 'NomGymnase': 'BARBARA', 'Adresse': '45  rue du bossu', 'Ville': 'SAINT DENIS', 'Surface': 500, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'mardi', 'Horaire': 10.0, 'Duree': 30, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642b0', 'IdGymnase': 24, 'NomGymnase': 'BELFEGOR', 'Adresse': 'Place de Gaulle', 'Ville': 'SAINT DENIS', 'Surface': 450, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Jeudi', 'Horaire': 9.0, 'Duree': 90, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 57, 'Jour': 'mercredi', 'Horaire': 10.0, 'Duree': 90, 'Libelle': 'Volley ball'}]}\n",
      "{'_id': '566eec69662b388eba4642b1', 'IdGymnase': 25, 'NomGymnase': 'DOLTO', 'Adresse': '3 square Plaisir', 'Ville': 'VILLETANEUSE', 'Surface': 620, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Dimanche', 'Horaire': 18.0, 'Duree': 60, 'Libelle': 'Basket ball'}]}\n",
      "{'_id': '566eec69662b388eba4642b3', 'IdGymnase': 27, 'NomGymnase': 'PASCAL', 'Adresse': '20 rue de la pirogue', 'Ville': 'VILLETANEUSE', 'Surface': 350, 'Seances': [{'IdSportifEntraineur': 57, 'Jour': 'jeudi', 'Horaire': 10.0, 'Duree': 90, 'Libelle': 'Volley ball'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 14.0, 'Duree': 120, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'mercredi', 'Horaire': 17.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n",
      "{'_id': '566eec69662b388eba4642b4', 'IdGymnase': 28, 'NomGymnase': 'BLAISE PASCAL', 'Adresse': '2bis rue de la moulerie', 'Ville': 'GARGES', 'Surface': 400, 'Seances': [{'IdSportifEntraineur': 149, 'Jour': 'Lundi', 'Horaire': 9.0, 'Duree': 30, 'Libelle': 'Basket ball'}, {'IdSportifEntraineur': 6, 'Jour': 'dimanche', 'Horaire': 14.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 6, 'Jour': 'dimanche', 'Horaire': 15.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 6, 'Jour': 'dimanche', 'Horaire': 16.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 6, 'Jour': 'dimanche', 'Horaire': 17.0, 'Duree': 60, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'mardi', 'Horaire': 18.0, 'Duree': 90, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'samedi', 'Horaire': 18.0, 'Duree': 90, 'Libelle': 'Hockey'}, {'IdSportifEntraineur': 7, 'Jour': 'vendredi', 'Horaire': 18.0, 'Duree': 90, 'Libelle': 'Hockey'}]}\n"
     ]
    }
   ],
   "source": [
    "#13) Gymnases avec que BasketBall ou VolleyBall\n",
    "gymnases = db.Gymnases.find({\"$or\": [{\"Seances.Libelle\":\"Basket ball\"},{\"Seances.Libelle\":\"Volley ball\"}]})\n",
    "for gymnase in gymnases:\n",
    "    print(gymnase)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec5f662b388eba464203', 'IdSportif': 1, 'Nom': 'BOUTAHAR', 'Prenom': 'Abderahim', 'Sexe': 'm', 'Age': 30, 'Sports': {'Jouer': ['Volley ball', 'Tennis', 'Football'], 'Arbitrer': ['Basket ball', 'Volley ball', 'Hockey'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Hockey', 'Badmington']}}\n",
      "{'_id': '566eec5f662b388eba464204', 'IdSportif': 2, 'Nom': 'KERVADEC', 'Prenom': 'Yann', 'Sexe': 'M', 'Age': 28, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Ping pong', 'Football'], 'Arbitrer': ['Hockey', 'Football'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Tennis', 'Hockey', 'Badmington', 'Ping pong', 'Boxe']}}\n",
      "{'_id': '566eec5f662b388eba464205', 'IdSportif': 3, 'Nom': 'HUE', 'Prenom': 'Pascale', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Volley ball', 'Ping pong'], 'Arbitrer': ['Volley ball', 'Badmington', 'Ping pong'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Badmington']}}\n",
      "{'_id': '566eec5f662b388eba464206', 'IdSportif': 4, 'Nom': 'DORLEANS', 'Prenom': 'Jean-michel', 'Sexe': 'M', 'Age': 32, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Volley ball', 'Football'], 'Arbitrer': ['Basket ball', 'Volley ball', 'Ping pong', 'Boxe'], 'Entrainer': ['Basket ball', 'Ping pong', 'Boxe']}}\n",
      "{'_id': '566eec5f662b388eba464208', 'IdSportif': 6, 'Nom': 'RETALDI', 'Prenom': 'Sophie', 'Sexe': 'F', 'Age': 30, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Ping pong'], 'Arbitrer': ['Basket ball', 'Hockey', 'Ping pong'], 'Entrainer': ['Hockey', 'Ping pong', 'Boxe']}}\n",
      "{'_id': '566eec5f662b388eba464209', 'IdSportif': 7, 'Nom': 'GOMEZ', 'Prenom': 'Diego', 'Sexe': 'M', 'Age': 25, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Volley ball', 'Tennis', 'Football'], 'Arbitrer': ['Volley ball', 'Hand ball', 'Hockey'], 'Entrainer': ['Volley ball', 'Hand ball', 'Hockey', 'Badmington']}}\n",
      "{'_id': '566eec5f662b388eba46421e', 'IdSportif': 29, 'Nom': 'ROUSSEL', 'Prenom': 'Nadège', 'Sexe': 'F', 'Age': 22, 'IdSportifConseiller': 5, 'Sports': {'Jouer': ['Volley ball', 'Hand ball', 'Badmington', 'Ping pong'], 'Arbitrer': 'Ping pong', 'Entrainer': 'Ping pong'}}\n",
      "{'_id': '566eec5f662b388eba46421f', 'IdSportif': 30, 'Nom': 'SCHINK', 'Prenom': 'Nicolas', 'Sexe': 'M', 'Age': 24, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Volley ball', 'Hand ball', 'Ping pong', 'Football'], 'Entrainer': 'Ping pong'}}\n",
      "{'_id': '566eec5f662b388eba464220', 'IdSportif': 31, 'Nom': 'STEMPUT', 'Prenom': 'Mathieu', 'Sexe': 'M', 'Age': 22, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Volley ball', 'Hand ball', 'Badmington', 'Football'], 'Entrainer': 'Ping pong'}}\n",
      "{'_id': '566eec5f662b388eba464221', 'IdSportif': 32, 'Nom': 'VAN CAUTER', 'Prenom': 'Vincent', 'Sexe': 'M', 'Age': 23, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Badmington', 'Ping pong', 'Football'], 'Arbitrer': 'Ping pong', 'Entrainer': 'Ping pong'}}\n",
      "{'_id': '566eec60662b388eba464224', 'IdSportif': 35, 'Nom': 'TANQUE', 'Prenom': 'Yann', 'Sexe': 'M', 'Age': 24, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Hand ball', 'Ping pong', 'Football'], 'Arbitrer': 'Badmington', 'Entrainer': ['Badmington', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba464225', 'IdSportif': 36, 'Nom': 'DJELOUDANE', 'Prenom': 'Zinedine', 'Sexe': 'M', 'Age': 28, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Ping pong', 'Football'], 'Entrainer': 'Badmington'}}\n",
      "{'_id': '566eec60662b388eba464227', 'IdSportif': 38, 'Nom': 'VASSEMON', 'Prenom': 'Laurent', 'Sexe': 'M', 'Age': 24, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Hand ball', 'Badmington', 'Football'], 'Entrainer': 'Ping pong'}}\n",
      "{'_id': '566eec60662b388eba464229', 'IdSportif': 40, 'Nom': 'VALIN', 'Prenom': 'Yann', 'Sexe': 'M', 'Age': 23, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Hand ball', 'Badmington', 'Ping pong', 'Football'], 'Entrainer': ['Badmington', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba464231', 'IdSportif': 48, 'Nom': 'HEDDI', 'Prenom': 'Zohra', 'Sexe': 'F', 'Age': 23, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong'], 'Entrainer': 'Badmington'}}\n",
      "{'_id': '566eec60662b388eba464233', 'IdSportif': 50, 'Nom': 'KALOMBO', 'Prenom': 'Yannick', 'Sexe': 'M', 'Age': 22, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong', 'Football'], 'Entrainer': 'Badmington'}}\n",
      "{'_id': '566eec60662b388eba464239', 'IdSportif': 56, 'Nom': 'GUERRAOUI', 'Prenom': 'Zohra', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Ping pong'], 'Entrainer': 'Badmington'}}\n",
      "{'_id': '566eec60662b388eba46423a', 'IdSportif': 57, 'Nom': 'BOISSEAU', 'Prenom': 'Eric', 'Sexe': 'M', 'Age': 25, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Tennis', 'Football'], 'Entrainer': ['Volley ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba46423b', 'IdSportif': 58, 'Nom': 'GUIGUI', 'Prenom': 'Vincent', 'Sexe': 'M', 'Age': 23, 'IdSportifConseiller': 4, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong', 'Football'], 'Entrainer': ['Volley ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba46423c', 'IdSportif': 59, 'Nom': 'CLERICE', 'Prenom': 'Stéphanie', 'Sexe': 'F', 'Age': 23, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong'], 'Arbitrer': 'Tennis', 'Entrainer': ['Volley ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba46423d', 'IdSportif': 60, 'Nom': 'TIZEGHAT', 'Prenom': 'Benamar', 'Sexe': 'M', 'Age': 32, 'IdSportifConseiller': 3, 'Sports': {'Jouer': ['Hand ball', 'Tennis', 'Football'], 'Arbitrer': 'Volley ball', 'Entrainer': ['Volley ball', 'Tennis', 'Ping pong']}}\n",
      "{'_id': '566eec60662b388eba46423e', 'IdSportif': 61, 'Nom': 'LAZARRE', 'Prenom': 'Jean', 'Sexe': 'M', 'Age': 27, 'IdSportifConseiller': 7, 'Sports': {'Jouer': 'Football', 'Entrainer': ['Volley ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba464296', 'IdSportif': 149, 'Nom': 'BELZ', 'Prenom': 'Sylvianne', 'Sexe': 'F', 'Age': 27, 'IdSportifConseiller': 7, 'Sports': {'Jouer': 'Basket ball', 'Arbitrer': 'Basket ball', 'Entrainer': 'Basket ball'}}\n",
      "{'_id': '566eec60662b388eba464298', 'IdSportif': 151, 'Nom': 'HENRY', 'Prenom': 'Maël', 'Sexe': 'M', 'Age': 25, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Hand ball'], 'Arbitrer': ['Basket ball', 'Hand ball'], 'Entrainer': ['Basket ball', 'Hand ball']}}\n"
     ]
    }
   ],
   "source": [
    "#14) Entraîneurs et Joueurs\n",
    "entraineurs_joueurs = db.Sportifs.find({\"$and\" : [{\"Sports.Jouer\" : {\"$exists\" : True}}, {\"Sports.Entrainer\" : {\"$exists\" : True}}]})\n",
    "for entraineur_joueur in entraineurs_joueurs:\n",
    "    print(entraineur_joueur)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec5f662b388eba464203', 'IdSportif': 1, 'Nom': 'BOUTAHAR', 'Prenom': 'Abderahim', 'Sexe': 'm', 'Age': 30, 'Sports': {'Jouer': ['Volley ball', 'Tennis', 'Football'], 'Arbitrer': ['Basket ball', 'Volley ball', 'Hockey'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Hockey', 'Badmington']}}\n",
      "{'_id': '566eec60662b388eba46422e', 'IdSportif': 45, 'Nom': 'CHAVANT', 'Prenom': 'Christophe', 'Sexe': 'M', 'Age': 25, 'Sports': {'Jouer': ['Tennis', 'Football']}}\n",
      "{'_id': '566eec60662b388eba46423c', 'IdSportif': 59, 'Nom': 'CLERICE', 'Prenom': 'Stéphanie', 'Sexe': 'F', 'Age': 23, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong'], 'Arbitrer': 'Tennis', 'Entrainer': ['Volley ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba464242', 'IdSportif': 65, 'Nom': 'CHESNIER', 'Prenom': 'Marc', 'Sexe': 'M', 'Age': 30, 'Sports': {'Jouer': 'Football'}}\n",
      "{'_id': '566eec60662b388eba46424f', 'IdSportif': 78, 'Nom': 'CHAUVIN', 'Prenom': 'Julien', 'Sexe': 'M', 'Age': 30, 'Sports': {'Jouer': 'Football'}}\n",
      "{'_id': '566eec60662b388eba46425a', 'IdSportif': 89, 'Nom': 'RIQUIER', 'Prenom': 'Jean-pierre', 'Sexe': 'M', 'Age': 30, 'Sports': {'Jouer': ['Hand ball', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464262', 'IdSportif': 97, 'Nom': 'BONHOMME', 'Prenom': 'Bruno', 'Sexe': 'M', 'Age': 30, 'Sports': {'Jouer': ['Tennis', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464264', 'IdSportif': 99, 'Nom': 'BONE', 'Prenom': 'Guy', 'Sexe': 'M', 'Age': 32, 'Sports': {'Jouer': 'Football'}}\n"
     ]
    }
   ],
   "source": [
    "#15) Sportifs et Conseillers\n",
    "entraineurs_joueurs = db.Sportifs.find({\"IdSportifConseiller\": {\"$exists\": False}})\n",
    "for entraineur_joueur in entraineurs_joueurs:\n",
    "    print(entraineur_joueur)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec5f662b388eba464203', 'Nom': 'BOUTAHAR'}\n"
     ]
    }
   ],
   "source": [
    "#16) Conseiller de KERVEDEC\n",
    "conseillerKervedec = db.Sportifs.find_one({\"IdSportif\": db.Sportifs.find_one({\"Nom\": \"KERVADEC\"}, {\"IdSportifConseiller\": 1, \"_id\": 0})['IdSportifConseiller']}, {\"Nom\": 1})\n",
    "print(conseillerKervedec)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec5f662b388eba464203', 'IdSportif': 1, 'Nom': 'BOUTAHAR', 'Prenom': 'Abderahim', 'Sexe': 'm', 'Age': 30, 'Sports': {'Jouer': ['Volley ball', 'Tennis', 'Football'], 'Arbitrer': ['Basket ball', 'Volley ball', 'Hockey'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Hockey', 'Badmington']}}\n",
      "{'_id': '566eec5f662b388eba464204', 'IdSportif': 2, 'Nom': 'KERVADEC', 'Prenom': 'Yann', 'Sexe': 'M', 'Age': 28, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Basket ball', 'Volley ball', 'Ping pong', 'Football'], 'Arbitrer': ['Hockey', 'Football'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Tennis', 'Hockey', 'Badmington', 'Ping pong', 'Boxe']}}\n",
      "{'_id': '566eec5f662b388eba464205', 'IdSportif': 3, 'Nom': 'HUE', 'Prenom': 'Pascale', 'Sexe': 'F', 'Age': 25, 'IdSportifConseiller': 1, 'Sports': {'Jouer': ['Volley ball', 'Ping pong'], 'Arbitrer': ['Volley ball', 'Badmington', 'Ping pong'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Badmington']}}\n",
      "{'_id': '566eec60662b388eba464298', 'IdSportif': 151, 'Nom': 'HENRY', 'Prenom': 'Maël', 'Sexe': 'M', 'Age': 25, 'IdSportifConseiller': 2, 'Sports': {'Jouer': ['Basket ball', 'Hand ball'], 'Arbitrer': ['Basket ball', 'Hand ball'], 'Entrainer': ['Basket ball', 'Hand ball']}}\n"
     ]
    }
   ],
   "source": [
    "#17) Entraineurs HandBall et BasketBall\n",
    "entraineurs_handb_basket = db.Sportifs.find({\"$and\" : [{\"Sports.Entrainer\" : \"Hand ball\"}, {\"Sports.Entrainer\":  \"Basket ball\"}]})\n",
    "for entraineur_handb_basket in entraineurs_handb_basket:\n",
    "    print(entraineur_handb_basket)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec5f662b388eba464203', 'IdSportif': 1, 'Nom': 'BOUTAHAR', 'Prenom': 'Abderahim', 'Sexe': 'm', 'Age': 30, 'Sports': {'Jouer': ['Volley ball', 'Tennis', 'Football'], 'Arbitrer': ['Basket ball', 'Volley ball', 'Hockey'], 'Entrainer': ['Basket ball', 'Volley ball', 'Hand ball', 'Hockey', 'Badmington']}}\n",
      "{'_id': '566eec60662b388eba46422e', 'IdSportif': 45, 'Nom': 'CHAVANT', 'Prenom': 'Christophe', 'Sexe': 'M', 'Age': 25, 'Sports': {'Jouer': ['Tennis', 'Football']}}\n",
      "{'_id': '566eec60662b388eba46423c', 'IdSportif': 59, 'Nom': 'CLERICE', 'Prenom': 'Stéphanie', 'Sexe': 'F', 'Age': 23, 'Sports': {'Jouer': ['Basket ball', 'Badmington', 'Ping pong'], 'Arbitrer': 'Tennis', 'Entrainer': ['Volley ball', 'Tennis']}}\n",
      "{'_id': '566eec60662b388eba464242', 'IdSportif': 65, 'Nom': 'CHESNIER', 'Prenom': 'Marc', 'Sexe': 'M', 'Age': 30, 'Sports': {'Jouer': 'Football'}}\n",
      "{'_id': '566eec60662b388eba46424f', 'IdSportif': 78, 'Nom': 'CHAUVIN', 'Prenom': 'Julien', 'Sexe': 'M', 'Age': 30, 'Sports': {'Jouer': 'Football'}}\n",
      "{'_id': '566eec60662b388eba46425a', 'IdSportif': 89, 'Nom': 'RIQUIER', 'Prenom': 'Jean-pierre', 'Sexe': 'M', 'Age': 30, 'Sports': {'Jouer': ['Hand ball', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464262', 'IdSportif': 97, 'Nom': 'BONHOMME', 'Prenom': 'Bruno', 'Sexe': 'M', 'Age': 30, 'Sports': {'Jouer': ['Tennis', 'Football']}}\n",
      "{'_id': '566eec60662b388eba464264', 'IdSportif': 99, 'Nom': 'BONE', 'Prenom': 'Guy', 'Sexe': 'M', 'Age': 32, 'Sports': {'Jouer': 'Football'}}\n"
     ]
    }
   ],
   "source": [
    "#18) Sportifs sans conseiller\n",
    "sportifs = db.Sportifs.find({\"IdSportifConseiller\": {\"$exists\": False}})\n",
    "for sportif in sportifs:\n",
    "    print(sportif)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '566eec69662b388eba464299'}\n"
     ]
    }
   ],
   "source": [
    "#19) Notre query\n",
    "entraineurParSeance = db.Gymnases.find({\"Seances.IdSportifEntraineur\": db.Sportifs.find_one({\"IdSportif\": 1}, {\"IdSportif\": 1, \"_id\": 0})['IdSportif']}, {\"Nom\": 1})\n",
    "for sportif in entraineurParSeance:\n",
    "    print(sportif)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}