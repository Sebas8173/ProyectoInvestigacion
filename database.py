import sqlite3

def init_db():
    """Inicializa la base de datos y crea las tablas si no existen."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER,
        publication_year INTEGER,
        summary TEXT,
        publisher TEXT,
        FOREIGN KEY (author_id) REFERENCES authors(id)
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        nationality TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS loans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        user_name TEXT NOT NULL,
        loan_date TEXT NOT NULL,
        return_date TEXT,
        FOREIGN KEY (book_id) REFERENCES books(id)
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS bibliotecarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,  -- Vulnerabilidad: Contraseña en texto plano
        name TEXT NOT NULL
    )''')
    # Insertar un bibliotecario por defecto
    c.execute("INSERT OR IGNORE INTO bibliotecarios (username, password, name) VALUES ('admin', 'password', 'Administrador')")
    conn.commit()
    conn.close()

def get_books():
    """Obtiene todos los libros con sus autores."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('SELECT books.id, books.title, authors.name, books.publication_year, books.summary, books.publisher FROM books JOIN authors ON books.author_id = authors.id')
    books = c.fetchall()
    conn.close()
    return books

def get_authors():
    """Obtiene todos los autores."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('SELECT * FROM authors')
    authors = c.fetchall()
    conn.close()
    return authors

def get_loans():
    """Obtiene todos los préstamos con los títulos de los libros."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('SELECT loans.id, books.title, loans.user_name, loans.loan_date, loans.return_date FROM loans JOIN books ON loans.book_id = books.id')
    loans = c.fetchall()
    conn.close()
    return loans

def get_bibliotecarios():
    """Obtiene todos los bibliotecarios."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('SELECT * FROM bibliotecarios')
    bibliotecarios = c.fetchall()
    conn.close()
    return bibliotecarios

def add_book(title, author_id, publication_year, summary, publisher):
    """Agrega un nuevo libro."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"INSERT INTO books (title, author_id, publication_year, summary, publisher) VALUES ('{title}', {author_id}, {publication_year}, '{summary}', '{publisher}')")
    conn.commit()
    conn.close()

def update_book(id, title, author_id, publication_year, summary, publisher):
    """Actualiza un libro existente."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"UPDATE books SET title='{title}', author_id={author_id}, publication_year={publication_year}, summary='{summary}', publisher='{publisher}' WHERE id={id}")
    conn.commit()
    conn.close()

def delete_book(id):
    """Elimina un libro."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"DELETE FROM books WHERE id={id}")
    conn.commit()
    conn.close()

def add_author(name, nationality):
    """Agrega un nuevo autor."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"INSERT INTO authors (name, nationality) VALUES ('{name}', '{nationality}')")
    conn.commit()
    conn.close()

def update_author(id, name, nationality):
    """Actualiza un autor existente."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"UPDATE authors SET name='{name}', nationality='{nationality}' WHERE id={id}")
    conn.commit()
    conn.close()

def delete_author(id):
    """Elimina un autor."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"DELETE FROM authors WHERE id={id}")
    conn.commit()
    conn.close()

def add_loan(book_id, user_name, loan_date, return_date):
    """Agrega un nuevo préstamo."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"INSERT INTO loans (book_id, user_name, loan_date, return_date) VALUES ({book_id}, '{user_name}', '{loan_date}', '{return_date}')")
    conn.commit()
    conn.close()

def update_loan(id, book_id, user_name, loan_date, return_date):
    """Actualiza un préstamo existente."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"UPDATE loans SET book_id={book_id}, user_name='{user_name}', loan_date='{loan_date}', return_date='{return_date}' WHERE id={id}")
    conn.commit()
    conn.close()

def delete_loan(id):
    """Elimina un préstamo."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"DELETE FROM loans WHERE id={id}")
    conn.commit()
    conn.close()

def add_bibliotecario(username, password, name):
    """Agrega un nuevo bibliotecario."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL y contraseña en texto plano
    c.execute(f"INSERT INTO bibliotecarios (username, password, name) VALUES ('{username}', '{password}', '{name}')")
    conn.commit()
    conn.close()

def update_bibliotecario(id, username, password, name):
    """Actualiza un bibliotecario existente."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"UPDATE bibliotecarios SET username='{username}', password='{password}', name='{name}' WHERE id={id}")
    conn.commit()
    conn.close()

def delete_bibliotecario(id):
    """Elimina un bibliotecario."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"DELETE FROM bibliotecarios WHERE id={id}")
    conn.commit()
    conn.close()

def check_bibliotecario(username, password):
    """Verifica las credenciales de un bibliotecario."""
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Vulnerabilidad: Inyección SQL
    c.execute(f"SELECT * FROM bibliotecarios WHERE username='{username}' AND password='{password}'")
    bibliotecario = c.fetchone()
    conn.close()
    return bibliotecario