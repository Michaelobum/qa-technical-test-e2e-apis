=============================================================================
PROYECTO: AUTOMATIZACIÓN E2E UI - SAUCEDEMO (OPCIÓN 2)
=============================================================================

DESCRIPCIÓN:
Prueba automatizada del flujo de compra "Happy Path" en la tienda online
SauceDemo (https://www.saucedemo.com/).

Implementado con:
- Lenguaje: Python
- Framework Web: Selenium WebDriver
- Runner & Assertions: Pytest
- Patrón de Diseño: Page Object Model (POM)

El flujo automatizado cubre:
1. Login exitoso (standard_user).
2. Adición de 2 productos al carrito.
3. Navegación y validación del carrito.
4. Completado del formulario de checkout.
5. Finalización de compra y validación del mensaje de éxito.

REQUISITOS PREVIOS:
- Python 3.8 o superior.
- Google Chrome instalado (el driver se gestiona automáticamente).

INSTALACIÓN DE DEPENDENCIAS:
Se recomienda utilizar un entorno virtual.

1. Crear entorno virtual (opcional pero recomendado):
   python -m venv venv

2. Activar entorno:
   - Windows: .\venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate

3. Instalar librerías requeridas:
   pip install -r requirements.txt

INSTRUCCIONES DE EJECUCIÓN:
Para correr la prueba y ver los logs en consola:

   pytest tests/checkout_test.py

EVIDENCIA (CAPTURAS DE PANTALLA):
El script cuenta con un mecanismo automático de captura de evidencia.
Al finalizar la ejecución, revise la carpeta generada automáticamente:

   /evidencias

Encontrará 5 capturas de pantalla correspondientes a los hitos clave del flujo
(Login, Carrito, Productos Agregados, Checkout y Confirmación).

AUTOR:
Michael Eduardo Morán Naranjo