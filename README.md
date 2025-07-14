# Sistema CRUD de Biblioteca

## Descripción
Sistema CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar una biblioteca, desarrollado con Python 3.9+, Flask 2.0.1 y SQLite. Permite administrar libros, autores y préstamos a través de una interfaz web minimalista y moderna con formularios modales. Incluye un login básico y vulnerabilidades intencionales (inyección SQL, XSS, falta de CSRF, etc.) para fines educativos. **Advertencia**: No usar en producción debido a estas vulnerabilidades.

## Requisitos
- Python 3.9+
- Entorno virtual (`virtualenv`)
- Navegador web moderno

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Sebas8173/ProyectoInvestigacion.git
   cd ProyectoInvestigacion
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
5. Accede a `http://localhost:5000` en un navegador.

## Estructura del Proyecto
- `app.py`: Lógica principal de Flask, rutas CRUD y login.
- `database.py`: Configuración y consultas a SQLite (con vulnerabilidades intencionales).
- `templates/`:
  - `base.html`: Plantilla base con navegación y estilos.
  - `books.html`: Interfaz para gestionar libros.
  - `authors.html`: Interfaz para gestionar autores.
  - `loans.html`: Interfaz para gestionar préstamos.
  - `login.html`: Formulario de login.
- `static/style.css`: Estilos CSS minimalistas y modernos.
- `requirements.txt`: Dependencias del proyecto.
- `library.db`: Base de datos SQLite (generada automáticamente).

## Vulnerabilidades Intencionales
- **Inyección SQL**: Consultas no parametrizadas en `database.py`.
- **XSS**: Entradas de usuario no sanitizadas en plantillas HTML.
- **Falta de CSRF**: Formularios sin tokens de protección.
- **Autenticación débil**: Login básico con credenciales hardcodeadas.
- **Exposición de errores**: Mensajes de error detallados.

## Notas
- Usa Visual Studio Code para editar y ejecutar el proyecto.
- La interfaz utiliza formularios modales para una experiencia moderna.
- Corrige las vulnerabilidades antes de usar en producción (consultas parametrizadas, sanitización, CSRF, etc.).