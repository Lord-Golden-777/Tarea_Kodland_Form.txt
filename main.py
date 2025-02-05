# Importar Flask
from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# Primera página
@app.route('/')
def index():
    return render_template('index.html')

# Segunda página
@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

# Tercera página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                           result=result_calculate(int(size), int(lights), int(device)))

# Formulario
@app.route('/form')
def form():
    return render_template('form.html')

# Resultados del formulario
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Recoger datos del formulario
        name = request.form['name']

        # Guardar datos en form.txt
        with open('form.txt', 'a') as f:
            f.write(f'Nombre: {name}\n---\n')

        # Mostrar los datos en form_result.html
        return render_template('form_result.html', name=name)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
