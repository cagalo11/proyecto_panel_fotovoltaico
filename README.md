# python_web
## Proyecto módulo desarrollo web con Python
### Autores:
* Camilo García López
* Yamid Andrés Melgarejo
* Juan Esteban de la Calle
* Esperanza Cortés
* Victor Manuel Hincapié


### Descripción:


La aplicación desarrollada toma como insumo los niveles de irradiancia (Watts / m2) y temperatura (Kelvin) para obtener las curvas características de Voltaje - Corriente y de Potencia - Voltaje. Adionalmente, ubica el MPP (Punto de máxima Potencia). Los valores de entrada temperatura e irradiance si ingresan a la aplicación de forma interactiva al cambiar la ubicación en el mapa.

### Instrucciones de uso: 

Para ejecutar la aplicación, se debe correr *python app.py* y posteriormente hacer click en la dirección URL suministrada por la consola. Al hacer click, se desplegará un mapa interactivo en el cual podrá seleccionar cualquier lugar del mundo. Al hacer click en la ubicación deseada, en la parte inferior de la página web se mostrarán las curvas características de Voltaje - Corriente y de Potencia - Voltaje para un panel Sunset con las condiciones de irradiance y temperatura promedio del lugar seleccionado.

## Nota técnica:

La estimación de la potencia máxima se hace con el *Modelo de los Cinco Parámetros*, para  cual se tomó como base la tésis de maestría *Control por modos deslizantes
aplicado a un inversor de fuente de corriente monofásico conectado a la red*, la cual se puede leer  [en este documento](https://repositorio.unal.edu.co/bitstream/handle/unal/79905/1086362120.2021.pdf?sequence=4&isAllowed=y). El desarrollo de la aplicación se hizo usando el módulo de *flask* en Python, donde utilizamos *html* para el diseño de la interfaz y datos geospaciales de la NASA tratados en *Arcgis* para la asociación de niveles de temperatura e irradiancia para cada lugar del mapa.
