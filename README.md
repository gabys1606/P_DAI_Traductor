# App Traductora - Lenguajes y Autómatas

Este proyecto es una aplicación web de traducción de texto (Español, Inglés, Francés), desarrollada como entrega práctica para la clase de **Lenguajes y Autómatas**.

## Arquitectura y Stack Tecnológico

*   **Backend:** Desarrollado en **Python** utilizando el framework **Flask**. El backend expone un endpoint de API para procesar las traducciones de forma asíncrona.
*   **Motor de traducción:** Se emplea la librería `deep-translator` la cual funciona de manera rápida y sin necesidad de configurar API keys externas.
*   **Frontend:** Construido con **HTML5** y estilizado usando **Tailwind CSS** vía CDN para asegurar un diseño responsivo, limpio y moderno.
*   **Lógica de Interfaz:** Implementada en **Vanilla JavaScript**. La comunicación con el backend se realiza de forma asíncrona utilizando la **API Fetch**, gestionando estados visuales (como "Traduciendo...") y validaciones simples de lado del cliente.

## Requisitos Previos

*   Python 3.8+ instalado en el sistema.

## Instrucciones de Instalación y Ejecución

1. **Clonar o descargar el repositorio.**

2. **Crear y activar un entorno virtual:**

   En Windows:
   ```bash
   py -m venv venv
   venv\Scripts\activate
   ```
   En macOS / Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar las dependencias del proyecto:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

5. **Probar:** 
   Abre tu navegador web y navega a [http://localhost:5000](http://localhost:5000).

## Características Implementadas
- Diseño responsivo adaptado a múltiples dispositivos.
- Traducción entre idiomas sin recargar la página.
- Manejo de estado visual (boton deshabilitado, indicador de "Traduciendo...").
- Validación de campos vacíos (alerta de navegador).
