from flask import Flask, render_template, request
import requests

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
            ('ch', 'Suisse'), ('de', 'Allemagne'), ('us', 'États-Unis'),
            ('tg', 'Togo')
        ]

def generate_dorks(country_code, domain_name):
    if domain_name:
        site_filter = f"site:{domain_name}"
    else:
        site_filter = f"site:{country_code}"

    dork_categories = {
        "Répertoires ouverts": [
            f'{site_filter} intitle:"index of"',
            f'{site_filter} "index of" inurl:ftp',
            f'{site_filter} intitle:"index of" inurl:backup'
        ],
        "Fichiers exposés": [
            f'{site_filter} filetype:pdf',
            f'{site_filter} filetype:sql',
            f'{site_filter} filetype:env',
            f'{site_filter} filetype:log',
            f'{site_filter} ext:php intitle:phpinfo "published by the PHP Group"'
        ],
        "Injection SQL": [
            f'{site_filter} inurl:item_id=',
            f'{site_filter} inurl:id= inurl:page=',
            f'{site_filter} inurl:product=',
            f'{site_filter} inurl:category='
        ],
        "Panels d'administration": [
            f'{site_filter} intitle:"admin"',
            f'{site_filter} inurl:admin',
            f'{site_filter} inurl:login',
            f'{site_filter} intitle:"login"'
        ],
        "Configurations sensibles": [
            f'{site_filter} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini',
            f'{site_filter} "db_password" ext:env',
            f'{site_filter} "API_KEY" ext:env'
        ],
        "Technologies vulnérables": [
            f'{site_filter} "powered by wordpress"',
            f'{site_filter} "powered by joomla" inurl:administrator',
            f'{site_filter} "wp-content" ext:php'
        ]
    }
    
    return dork_categories

@app.route('/', methods=['GET', 'POST'])
def index():
    countries = get_countries()
    
    if request.method == 'POST':
        country_code = request.form.get('country')
        domain_name = request.form.get('search', '').strip()
        
        dork_categories = generate_dorks(country_code, domain_name)
        
        return render_template(
            'index.html',
            countries=countries,
            dork_categories=dork_categories,
            search_term=domain_name,
            country_code=country_code
        )
    
    return render_template('index.html', countries=countries)

if __name__ == '__main__':
    app.run(debug=True)

