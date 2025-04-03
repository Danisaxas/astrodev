from flask import Flask, render_template

# Crea una instancia de la aplicación Flask.
app = Flask(__name__)

# Define la ruta para la página principal.
# Ahora, la ruta principal ("/") renderiza el contenido de "desarrollador.html".
@app.route('/')
def index():
    """
    Esta función se llama cuando un usuario visita la página principal (/).
    Ahora renderiza la plantilla 'desarrollador.html'.
    """
    return render_template('index.html')

# Define una ruta para la página "/home".
@app.route('/home')
def home():
    """
    Esta función se llama cuando un usuario visita la ruta /home.
    Renderiza la plantilla 'saludo.html'.
    """
    return render_template('saludo.html')

# Este bloque principal asegura que el servidor de desarrollo de Flask se ejecute
# solo cuando el script se ejecuta directamente (no cuando se importa como módulo).
if __name__ == '__main__':
    # Inicia el servidor de desarrollo de Flask.
    # debug=True permite la recarga automática del servidor al guardar los cambios,
    # lo cual es útil durante el desarrollo.  NO USAR EN PRODUCCION.
    app.run(debug=True, host="0.0.0.0", port=5000)
    # Para acceder desde fuera de la máquina local, usa host="0.0.0.0"
    # y asegúrate de que el puerto 5000 esté abierto en tu firewall.
