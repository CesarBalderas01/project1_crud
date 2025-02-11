# Usa una imagen base de Python
FROM python:3.9-slim

# Instala las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    python3-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en el contenedor
WORKDIR /opt/projects/django/project1_crud

# Copia los archivos del proyecto al contenedor
COPY . /opt/projects/django/project1_crud

# Copia los archivos necesarios para instalar las dependencias
COPY requirements.txt .

# Instala las dependencias de Python desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando por defecto para correr el servidor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project1_crud.wsgi:application"]
