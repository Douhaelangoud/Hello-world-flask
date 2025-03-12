from flask import Flask

# Crée une instance de l'application Flask
app = Flask(__name__)

# Définit une route pour la racine ("/")
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Point d'entrée pour exécuter l'application
if __name__ == '__main__':
    app.run(debug=True)
