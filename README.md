# Prueba técnica para puesto de QA Jr

Este proyecto contiene un script automatizado en Python para realizar una prueba de inicio de 
sesión en la página web [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login). 
El script realiza el proceso de autenticación y toma capturas de pantalla en cada paso.

## Estructura:
- ```functions.py:```Contiene funciones auxiliares como la captura de pantalla y la configuración del navegador.
- ```locators.py:``` Define los localizadores de los elementos de la página de inicio de sesión.
- ```requirements.txt:``` Lista de dependencias necesarias para ejecutar los tests.
- ```test_login.py:``` Script principal que realiza la prueba de login y toma capturas de pantalla.

## Pre-requisitos
- Python 3.8+: Asegúrate de tener instalado Python.
- Edge Browser: Navegador utilizado para las pruebas.

## Instalación
### 1. Crea un entorno virtual (opcional pero recomendado):
- ```python -m venv venv```
### 2. Activar Entorno Virtual 
- ```source venv/bin/activate  # Linux/Mac```
- ```venv\Scripts\activate     # Windows```
## Clonar repositorio:
- ```git clone https://github.com/jdfloresf/Prueba-Tecnica-QA.git```

## Instalar dependencias:
- ```pip install -r requirements.txt```

## Ejecución del Test
Para ejecutar el test, asegúrate de estar en el directorio raíz del proyecto y usa el siguiente comando:
```pytest test_login.py -v -s``
- La opción -v permite ver más detalles sobre qué pruebas pasaron o fallaron:
- La opción -s permite ver la salida de las funciones de prueba, como los print() y otros mensajes de depuración que normalmente son capturados por pytest.
