AMBIENTES VIRTUALES EN PYTHON
Navegar con bash hasta la carpeta del proyecto
Ejecutar en terminal: python3 -m venv nombre_del_entorno para crear el entorno virtual #nombre_del_entorno: por defecto aparecerá \venv si lo creas por la barra izquierda pero puede ser cualquiera
Ejecutar en terminal: source nombre_del_entorno/bin/activate (MAC/LINUX) o nombre_del_entorno\Scripts\activate (WINDOWS) para activar el entorno virtual
Usar el entorno virtual: F1 —> Python: Select Interpreter —> nombre_del_entorno
Se instalan todas las dependencias
Una vez acabado el desarrollo se ejecuta el siguiente comando: pip freeze > requirements.txt
Instalar todas las dependencias del archivo requirements: pip install -r requirements.txt

GITIGNORE

#En gitignore, cada línea representa un archivo o directorio que se debe ignorar. Puedo utilizar el símbolo * para hacer coincidir archivos con un solo patrón, o las barras / para especificar las rutas desde el directorio raíz de un directorio o conjunto de archivos

#Ignora archivos que no quiera que interprete
documentacion.py
#Ignora archivos de configuración global
*.exe
#Ignora directorios
info_extra/

"""
AMBIENTE VIRTUAL: Entorno de desarrollo aislado, que me va a permitir gestionar de forma independiente las dependencias de un proyecto. 
    · Garantiza la coherencia de las bibliotecas instaladas.
    · Garantiza la independencia de las bibliotecas instaladas.
    · Evitar conflictos de versiones entre las dependencias de mi proyecto y las dependencias de otros proyectos o incluso de mi SO.
    · Asegura la portabilidad del código entre diferentes sistemas.
    · Reproducible en cualquier entorno de desarrollo. Independientemente del SO o la versión del SO en la que se ejecute mi proyecto, los resultados siempre van a ser los mismos.
    · Ahorrar espacio y recursos: es muy eficiente en cuestión de espacio y recursos ya que no interfiere con otras instalaciones de Python o bibliotecas del sistema y además, los ambientes virtuales ocupan muy poco espacio.
    · Requirements.txt: lista de todas las bibliotecas y sus versiones utilizadas en mi proyecto
    
    --> Métodos para crear un ambiente virtual 
        · VENV: python3 -m venv nobre_del_entorno
        · VIRTUALENV: 
            1. Instalar virtualenv en mi proyecto: pip install virtualenv
            2. Crear un entorno virtual en mi proyecro: virtualenv nombre_del_entorno_virtual
        
    --> Activar el ambiente virtual
        · VENV Y VIRTUALENV: 
            - Windows:              nombre_del_entorno\Scripts\activate
            - Mac/Linux:            source nombre_del_entorno/bin/activate
            
            
SOLUCIÓN DE PROBLEMAS
· Ejecución de scripts deshabilitada en Windows. En PowerShell como administrador:
    - Set-ExecutionPolicy 
    - RemoteSigned
    - s
· "Command pip not found": 
    - Descargar el script de instalación de pip: https://bootstrap.pypa.io/get-pip.py
    - Instalar pip desde el script: 
        · Windows: python get-pip.py
        · Linux / Mac: python3 get-pip.py
"""



""" 
Proyecto:
    README.md
    requirements.txt
    directorio app/
        __init__.py
        modules/
        templates/
        static/
        routes.py
    test/
    
"""

