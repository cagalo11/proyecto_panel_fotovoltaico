from flask import Flask, render_template, request, send_file, jsonify
import matplotlib.pyplot as plt
import io
import base64
import os
import pandas as pd

from PVModel import PVModel

app = Flask(__name__)

# Load CSV data from the static directory
def load_data():
    csv_url = os.path.join(app.static_folder, "data.csv")  # Assuming the file is named data.csv
    return pd.read_csv(csv_url)

data2 = load_data()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        A=location_lookup()
        print('aqui ok')
        latitud = request.form.get('parameters')
        longitud = float(request.form.get('irradiancia'))
        temperatura = float(request.form.get('temperatura'))
        
        # Sample calculation for Potencia (customize this based on your actual equation)
        parameters = [float(i) for i in user_parameters.split(',')]
        potencia = sum(parameters) * irradiancia * temperatura
        
        # Generate a plot
        fig, ax = plt.subplots()
        ax.plot(parameters, label='Sample Data')
        ax.set(title='Potencia Plot', xlabel='X-Axis', ylabel='Potencia')
        ax.legend()
        
        # Convert plot to PNG image
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        
        return render_template('result.html', potencia=potencia, plot_url=plot_url)
    return render_template('index.html')

@app.route('/location_lookup', methods=['POST'])
def location_lookup():
    data = request.get_json()
    lat = data['lat']
    lon = data['lng']
    result = data2[(data2['left'] <= lon) & (data2['right'] >= lon) & 
                  (data2['bottom'] <= lat) & (data2['top'] >= lat)]

    if not result.empty:
        record = result.iloc[0]
        if record['left'] <= lon <= record['right'] and record['bottom'] <= lat <= record['top']:
            Modelo = PVModel(4,3)
            resultados, Vmpp, Impp, P_max = Modelo.modelo_pv(G=record['ghi'], T=273.15+record['temperature'])
            
            fig, axs = plt.subplots(2, 1, figsize=(10, 10))

            # Subplot para la curva V-I
            axs[0].plot(resultados['Voltaje (V)'], resultados['Corriente (A)'], label='Curva V-I')
            axs[0].scatter(Vmpp, Impp, color='red', label='Punto de Máxima Potencia (MPP)')
            axs[0].set_title('Curva Característica V-I del Panel Fotovoltaico')
            axs[0].set_xlabel('Voltaje (V)')
            axs[0].set_ylabel('Corriente (A)')
            axs[0].legend()
            axs[0].grid(True)

            # Subplot para la curva de potencia
            axs[1].plot(resultados['Voltaje (V)'], resultados['Potencia (W)'], label='Curva de Potencia')
            axs[1].scatter(Vmpp, P_max, color='red', label='Punto de Máxima Potencia (MPP)')
            axs[1].set_title('Curva de Potencia del Panel Fotovoltaico')
            axs[1].set_xlabel('Voltaje (V)')
            axs[1].set_ylabel('Potencia (W)')
            axs[1].legend()
            axs[1].grid(True)
        
            # Ajustar el layout para que no haya superposición de títulos
            plt.tight_layout()

            # Guardar la figura completa como imagen
            buf = io.BytesIO()  # Usar un buffer si quieres guardar en memoria
            plt.savefig(buf, format='png')  # Corrección en 'format', estaba 'fomat'

            plt.close(fig)  # Cerrar la figura para liberar memoria
            plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')
            buf.close()

            return jsonify({'url_plot': plot_url})
    else:
        return jsonify({'error': 'No data found for the selected location'}), 404

if __name__ == '__main__':
    app.run(debug=True)
