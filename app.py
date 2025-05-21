from flask import Flask, render_template, request
import requests
from urllib.parse import quote

app = Flask(__name__)

COUNTRIES_API = "https://restcountries.com/v3.1/all"

def get_countries():
    try:
        response = requests.get(COUNTRIES_API, timeout=5)
        response.raise_for_status()
        countries = sorted([(country['cca2'].lower(), country['name']['common']) 
                          for country in response.json()])
        return countries
    except:
        return [
            ('fr', 'France'), ('be', 'Belgique'), ('ca', 'Canada'),
            ('ch', 'Suisse'), ('de', 'Allemagne'), ('us', 'États-Unis')
        ]

def generate_dorks(country_code, search_term):
    dork_categories = {
        "Répertoires ouverts": [
            f'site:{country_code} intitle:"index of" {search_term}',
            f'site:{country_code} "index of" inurl:ftp {search_term}',
            f'site:{country_code} intitle:"index of" inurl:backup {search_term}'
        ],
        "Fichiers exposés": [
            f'site:{country_code} filetype:pdf {search_term}',
            f'site:{country_code} filetype:sql {search_term}',
            f'site:{country_code} filetype:env {search_term}',
            f'site:{country_code} filetype:log {search_term}',
            f'site:{country_code} ext:php intitle:phpinfo "published by the PHP Group"'
        ],
        "Injection SQL": [
            f'site:{country_code} inurl:item_id= {search_term}',
            f'site:{country_code} inurl:id= inurl:page= {search_term}',
            f'site:{country_code} inurl:product= {search_term}',
            f'site:{country_code} inurl:category= {search_term}'
        ],
        "Panels d'administration": [
            f'site:{country_code} intitle:"admin" {search_term}',
            f'site:{country_code} inurl:admin {search_term}',
            f'site:{country_code} inurl:login {search_term}',
            f'site:{country_code} intitle:"login" {search_term}'
        ],
        "Configurations sensibles": [
            f'site:{country_code} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini {search_term}',
            f'site:{country_code} "db_password" ext:env {search_term}',
            f'site:{country_code} "API_KEY" ext:env {search_term}'
        ],
        "Technologies vulnérables": [
            f'site:{country_code} "powered by wordpress" {search_term}',
            f'site:{country_code} "powered by joomla" inurl:administrator {search_term}',
            f'site:{country_code} "wp-content" ext:php {search_term}'
        ]
    }
    
    return dork_categories

@app.route('/', methods=['GET', 'POST'])
def index():
    countries = get_countries()
    
    if request.method == 'POST':
        country_code = request.form.get('country')
        search_term = request.form.get('search', '').strip()
        
        if not search_term:
            return render_template('index.html', countries=countries, error="Veuillez entrer un terme de recherche")
        
        dork_categories = generate_dorks(country_code, search_term)
        
        return render_template(
            'index.html',
            countries=countries,
            dork_categories=dork_categories,
            search_term=search_term,
            country_code=country_code
        )
    
    return render_template('index.html', countries=countries)

if __name__ == '__main__':
    app.run(debug=True)
