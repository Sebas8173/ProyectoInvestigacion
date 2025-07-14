from flask import Flask, render_template, request, redirect, url_for, session
import database

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Vulnerabilidad: Clave hardcodeada

# Ruta para login
@app.route('/', methods=['GET', 'POST'])
def login():
    """Maneja el inicio de sesión de bibliotecarios."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Vulnerabilidad: Verificación insegura con inyección SQL posible
        bibliotecario = database.check_bibliotecario(username, password)
        if bibliotecario:
            session['logged_in'] = True
            session['username'] = bibliotecario[1]  # Almacena el username
            session['name'] = bibliotecario[3]  # Almacena el nombre
            return redirect(url_for('books'))
        else:
            return render_template('login.html', error='Credenciales inválidas')
    return render_template('login.html')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    """Cierra la sesión del usuario."""
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('name', None)
    return redirect(url_for('login'))

# Ruta para listar y gestionar libros
@app.route('/books', methods=['GET', 'POST'])
def books():
    """Gestiona la lista de libros y operaciones CRUD."""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'add' in request.form:
            title = request.form['title']
            author_id = request.form['author_id']
            publication_year = request.form['publication_year']
            summary = request.form['summary']
            publisher = request.form['publisher']
            database.add_book(title, author_id, publication_year, summary, publisher)
        elif 'update' in request.form:
            id = request.form['id']
            title = request.form['title']
            author_id = request.form['author_id']
            publication_year = request.form['publication_year']
            summary = request.form['summary']
            publisher = request.form['publisher']
            database.update_book(id, title, author_id, publication_year, summary, publisher)
        elif 'delete' in request.form:
            id = request.form['id']
            database.delete_book(id)
    
    books = database.get_books()
    authors = database.get_authors()
    return render_template('books.html', books=books, authors=authors)

# Ruta para listar y gestionar autores
@app.route('/authors', methods=['GET', 'POST'])
def authors():
    """Gestiona la lista de autores y operaciones CRUD."""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'add' in request.form:
            name = request.form['name']
            nationality = request.form['nationality']
            database.add_author(name, nationality)
        elif 'update' in request.form:
            id = request.form['id']
            name = request.form['name']
            nationality = request.form['nationality']
            database.update_author(id, name, nationality)
        elif 'delete' in request.form:
            id = request.form['id']
            database.delete_author(id)
    
    authors = database.get_authors()
    return render_template('authors.html', authors=authors)

# Ruta para listar y gestionar préstamos
@app.route('/loans', methods=['GET', 'POST'])
def loans():
    """Gestiona la lista de préstamos y operaciones CRUD."""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'add' in request.form:
            book_id = request.form['book_id']
            user_name = request.form['user_name']
            loan_date = request.form['loan_date']
            return_date = request.form['return_date']
            database.add_loan(book_id, user_name, loan_date, return_date)
        elif 'update' in request.form:
            id = request.form['id']
            book_id = request.form['book_id']
            user_name = request.form['user_name']
            loan_date = request.form['loan_date']
            return_date = request.form['return_date']
            database.update_loan(id, book_id, user_name, loan_date, return_date)
        elif 'delete' in request.form:
            id = request.form['id']
            database.delete_loan(id)
    
    loans = database.get_loans()
    books = database.get_books()
    return render_template('loans.html', loans=loans, books=books)

# Ruta para listar y gestionar bibliotecarios
@app.route('/bibliotecarios', methods=['GET', 'POST'])
def bibliotecarios():
    """Gestiona la lista de bibliotecarios y operaciones CRUD."""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'add' in request.form:
            username = request.form['username']
            password = request.form['password']
            name = request.form['name']
            database.add_bibliotecario(username, password, name)
        elif 'update' in request.form:
            id = request.form['id']
            username = request.form['username']
            password = request.form['password']
            name = request.form['name']
            database.update_bibliotecario(id, username, password, name)
        elif 'delete' in request.form:
            id = request.form['id']
            database.delete_bibliotecario(id)
    
    bibliotecarios = database.get_bibliotecarios()
    return render_template('bibliotecarios.html', bibliotecarios=bibliotecarios)

if __name__ == '__main__':
    database.init_db()
    app.run(debug=True)  # Modo debug (vulnerabilidad en producción)