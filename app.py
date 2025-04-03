from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    """
    Esta función maneja la página principal y cualquier solicitud con el parámetro 'page'.
    """
    # Obtiene el valor del parámetro 'page' de la URL.
    page = request.args.get('page')

    # Lógica para determinar qué plantilla renderizar basado en el valor de 'page'.
    if page == 'home':
        return render_template('home.html')
    elif page == 'index': #agregado para evitar error si se llama index.html
        return render_template('index.html')
    else:
        # Si no se proporciona 'page' o no coincide con ninguna opción conocida,
        # renderiza la página de índice por defecto.
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
