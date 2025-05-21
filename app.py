from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

# Filtre Jinja pour encoder une chaîne en URL safe
@app.template_filter('url_encode')
def url_encode_filter(s):
    return urllib.parse.quote_plus(s)

def generate_dorks(domain_name):
    site_filter = f"site:{domain_name}"

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
    dork_categories = None
    search_term = ""

    if request.method == 'POST':
        search_term = request.form.get('search', '').strip()
        if search_term:
            dork_categories = generate_dorks(search_term)

    return render_template(
        'index.html',
        dork_categories=dork_categories,
        search_term=search_term
    )

if __name__ == '__main__':
    app.run(debug=True)

