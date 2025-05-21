# 🔍 Outil de Google Dorking

Un outil web intuitif pour générer des **requêtes Google Dorks** ciblées, permettant d’identifier des **fichiers exposés**, **répertoires ouverts**, **panneaux d'administration**, **failles potentielles** et bien plus, de manière **catégorisée** et **structurée**.

> ⚠️ **Usage légal uniquement.** Cet outil est conçu à des fins éducatives et de tests de sécurité autorisés. Veuillez toujours obtenir une autorisation avant toute analyse.

---

## 🚀 Fonctionnalités

* 🎯 **Recherche ciblée par pays** (via extensions `.fr`, `.be`, `.ca`, etc.)
* 📂 Catégorisation des dorks par type :

  * Répertoires ouverts
  * Fichiers exposés (`.pdf`, `.sql`, `.env`, etc.)
  * Injections SQL
  * Panneaux d'administration
  * Fichiers de configuration sensibles
  * Technologies vulnérables (WordPress, Joomla)
* 💡 Interface claire avec résultats cliquables
* 🔐 Message d’avertissement légal intégré
* 🌍 Chargement dynamique de la liste des pays via API

---

## 🛠️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/hackusman/google_dork_tool.git
cd google_dork_tool
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

> Assure-toi d’avoir Python 3.7+ installé.

### 3. Lancer l'application

```bash
python app.py
```

Ouvre ton navigateur sur :

```
http://localhost:5000
```

---

## 📁 Structure du projet

```
.
├── app.py                   # Application Flask
├── templates/
│   └── index.html           # Interface utilisateur
├── requirements.txt         # Dépendances Python
└── README.md                # Ce fichier
```

---

## 📘 Exemple d’usage

Choisissez un pays comme **France (.fr)**, entrez un nom de domaine comme `exemple.com` puis cliquez sur **Générer les Dorks** pour obtenir des recherches préformatées, prêtes à être exécutées dans Google.

---

## ⚠️ Avertissement légal

Cet outil est exclusivement destiné à :

* Des **recherches légitimes**
* Des **tests de sécurité autorisés**
* Un **usage éducatif** et personnel

**N’utilisez jamais cet outil pour accéder ou tenter d’accéder à des systèmes sans autorisation explicite.**

---

## 🧠 Auteur

Développé avec ❤️ par **hackus\_man**
