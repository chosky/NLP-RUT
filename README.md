**Python version**
3.8.5
**pip version**
pip 20.1.1

**Crear entorno virtual**
Creacion del entorno virtual al nivel de la carpeta nplrut
**Windows**
python -m venv env
env\Scripts\activate

**Mac Os**
sudo easy_install pip
pip install virtualenv
virtualenv nombre_de_tu_entorno -p python3

**Linux**
sudo apt-get install python-pip
pip install virtualenv
virtualenv nombre_de_tu_entorno -p python3

**Activar entorno virtual**
**windows**
env\Scripts\activate
**mac os**
source nombre_entorno_virtual/bin/activate
**Linux**
source nombre_entorno_virtual/bin/activate

**Desactivar entorno virtual**
deactivate

**Intalar requerimientos**
pip install -r config/requirements.txt

**Correr servidor**
python app.py