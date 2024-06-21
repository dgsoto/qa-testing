# Trello API Testing Framework

Este proyecto es un framework de pruebas automatizadas para la API de Trello, construido con Python, `pytest` y herramientas de reporte. El framework está organizado de manera modular para facilitar la escalabilidad y el mantenimiento.

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Configuración](#configuración)
- [Ejecución de Pruebas](#ejecución-de-pruebas)
- [Análisis de Código con `pylint`](#análisis-de-código-con-pylint)
- [Buenas Prácticas](#buenas-prácticas)
- [Contribuciones](#contribuciones)

## Estructura del Proyecto

```plaintext
trello_api/
│
├── entities/
│   ├── board.py
│   ├── card.py
│   └── __init__.py
├── modules/
│   ├── boards.py
│   ├── cards.py
│   └── __init__.py
├── tests/
│   ├── test_boards.py
│   ├── test_cards.py
│   └── __init__.py
├── utils/
│   ├── api_client.py
│   ├── config.py
│   └── __init__.py
├── reports/
│   └── __init__.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── .env
```

## Descripción de Directorios y Archivos
- entities/: Define las entidades del dominio (por ejemplo, Board, Card).
- modules/: Contiene la lógica para interactuar con la API de Trello.
- tests/: Contiene los archivos de pruebas con pytest.
- utils/: Utilidades como el cliente de API y configuración.
- reports/: Carpeta para almacenar los reportes de las pruebas.
- .gitignore: Archivos y carpetas a ignorar por git.
- pytest.ini: Configuración de pytest.
- requirements.txt: Dependencias del proyecto.
- .env: Archivo para configurar las variables de entorno.

## Requisitos
- Python 3.x
- pip (Administrador de paquetes de Python)

## Configuración
1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/trello_api_tests.git
    cd trello_api_tests
    ```

2. Crear un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate   # En Windows usa `venv\Scripts\activate`
    ```
3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Configurar variables de entorno:

    Crea un archivo .env en el directorio raíz del proyecto con el siguiente contenido:
    ```plaintext
    TRELLO_API_KEY=tu_trello_api_key
    TRELLO_TOKEN=tu_trello_token
    ```

5. Actualizar utils/config.py si es necesario:
    ```python
    from dotenv import load_dotenv
    import os

    # Cargar variables de entorno desde .env
    load_dotenv()

    API_KEY = os.getenv('TRELLO_API_KEY')
    TOKEN = os.getenv('TRELLO_TOKEN')
    BASE_URL = 'https://api.trello.com/1'

    # Verificar que las variables estén configuradas correctamente
    assert API_KEY, "TRELLO_API_KEY no está configurado"
    assert TOKEN, "TRELLO_TOKEN no está configurado"
    ```

## Ejecución de Pruebas
Para ejecutar todas las pruebas, usa el siguiente comando:

```bash
pytest
```

Para ejecutar un archivo de prueba específico:
```bash
pytest tests/test_boards.py
```

Para ejecutar un método de prueba específico dentro de un archivo:
```bash
pytest tests/test_boards.py::TestBoards::test_get_boards
```

## Análisis de Código con pylint
Para analizar tu código con pylint, usa el siguiente comando:
```bash
pylint <nombre_del_módulo>.py
```

Por ejemplo, para analizar el módulo cards:
```bash
pylint modules/cards.py
```

## Buenas Prácticas
- Modularidad: Mantén tu código modular separando la lógica de la API y las pruebas en diferentes módulos.
- Manejo de Errores: Usa response.raise_for_status() para manejar errores HTTP de forma explícita.
- Configuración: Utiliza un archivo de configuración para manejar parámetros como URLs y credenciales.
- Seguridad: No incluyas tus credenciales en el repositorio. Usa .gitignore para excluir archivos sensibles.
- Documentación: Documenta tu código y pruebas para mejorar la mantenibilidad.

## Contribuciones
¡Las contribuciones son bienvenidas! Por favor, sigue los siguientes pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza los cambios necesarios y realiza commit (git commit -m 'Añadir nueva funcionalidad').
4. Sube tus cambios a la rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.