# Imagen base: usamos Apache Airflow como punto de partida
FROM apache/airflow:latest              

# Cambiamos al usuario root para poder instalar paquetes del sistema
USER root

# Actualizamos el sistema e instalamos git
RUN apt-get update && apt-get install -y git && apt-get clean

# Instalamos paquetes de Python adicionales necesarios
# RUN pip install --no-cache-dir \
#    pandas \
#    numpy \
#    requests

# Volvemos al usuario airflow (por seguridad)
USER airflow

# Fin del Dockerfile

# comandos para construir y ejecutar la imagen
# docker build -t sleek-airflow:latest .
#                 #nombre de la imagen:etiqueta

# comando para ver las imágenes creadas (docker image ls)
# comando para eliminar imagen (docker rmi "nombre" o id)
