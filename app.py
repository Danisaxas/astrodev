from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal con identificador numérico
@app.route('/page/1')
def index():
    return render_template('index.html')

# Ruta "home" con identificador numérico
@app.route('/page/2')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)