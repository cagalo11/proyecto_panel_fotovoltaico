from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_parameters = request.form.get('parameters')
        irradiancia = float(request.form.get('irradiancia'))
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

if __name__ == '__main__':
    app.run(debug=True)
