# BiblioDesk - Sistema CRUD de Biblioteca

## Descripción

BiblioDesk es un sistema CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar una biblioteca, desarrollado con Python 3.9+, Flask 2.0.1 y SQLite. Permite a bibliotecarios iniciar sesión y administrar libros, autores, préstamos y cuentas de bibliotecarios a través de una interfaz web moderna con formularios modales y un diseño elegante en tonos azules. Incluye vulnerabilidades intencionales (inyección SQL, XSS, contraseñas en texto plano, falta de CSRF) para fines educativos. **Advertencia**: No usar en producción debido a estas vulnerabilidades.

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
5. Accede a `http://localhost:5000` en un navegador. Usa las credenciales `admin`/`password` para iniciar sesión (bibliotecario por defecto).

## Características del Diseño

- **Interfaz Moderna**: Diseño elegante con paleta de azules y celestes pasteles
- **Logo Corporativo**: Logo integrado en el header con el nombre BiblioDesk
- **Iconos Profesionales**: Utiliza Font Awesome 6.7.1 para iconos consistentes
- **Responsive Design**: Adaptable a dispositivos móviles y tablets
- **Efectos Visuales**: Animaciones suaves y transiciones elegantes

## Estructura del Proyecto

- `app.py`: Lógica principal de Flask, rutas CRUD y login.
- `database.py`: Configuración y consultas a SQLite (con vulnerabilidades intencionales).
- `templates/`:
  - `base.html`: Plantilla base con navegación y estilos.
  - `books.html`: Interfaz para gestionar libros.
  - `authors.html`: Interfaz para gestionar autores.
  - `loans.html`: Interfaz para gestionar préstamos.
  - `bibliotecarios.html`: Interfaz para gestionar bibliotecarios.
  - `login.html`: Formulario de login.
- `static/style.css`: Estilos CSS minimalistas y modernos.
- `static/script.js`: Funciones JavaScript para modales.
- `requirements.txt`: Dependencias del proyecto.
- `library.db`: Base de datos SQLite (generada automáticamente).

## Vulnerabilidades Intencionales

- **Inyección SQL**: Consultas no parametrizadas en `database.py`.
- **XSS**: Entradas de usuario no sanitizadas en plantillas HTML.
- **Contraseñas en texto plano**: Almacenadas en la tabla `bibliotecarios`.
- **Falta de CSRF**: Formularios sin tokens de protección.
- **Exposición de errores**: Mensajes de error detallados.

## Notas

- Usa Visual Studio Code para editar y ejecutar el proyecto.
- BiblioDesk utiliza una interfaz moderna con formularios modales y diseño responsive.
- El logo corporativo está integrado en el header y página de login.
- Utiliza Font Awesome 6.7.1 para iconos profesionales y consistentes.
- La paleta de colores en azules y celestes pasteles proporciona una experiencia visual elegante.
- Corrige las vulnerabilidades antes de usar en producción (consultas parametrizadas, sanitización, CSRF, etc.).
- Las secciones de autores y préstamos son funcionalidades adicionales para demostrar más vulnerabilidades.