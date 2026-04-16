import sqlite3

"""
Criando o Plinfo.db
"""

def creat_database():
    conexao = sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users_informations(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
                )""")

    conexao.commit()
    conexao.close()
    
"""
Função para adicionar dados no banco!
"""

def insert_database(user_name , email , password):
    conexao = sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()
    try:
        cursor.execute("""INSERT INTO users_informations
                    (user_name , email , password) VALUES
                    (? , ? , ?) 
                    """ , (user_name , email , password)) #O (?,?,?) = Para evitar ataques de sqlinjection , ai o sqlite vai substit. os "?" pelos valores fora da tripe" de forma segura!
        
        conexao.commit()
        conexao.close()
        return True , "Usuario Cadastrado com sucesso!✅"
    
    except sqlite3.IntegrityError:    #Aqui ele vai pegar a excessão (que seria quando o usuario ja tem o email cadastrado e ele quer cadastrar outro email igual...)
        conexao.close()               #Impedindo do codigo quebrar por errointegrity do sqlite3.
        return False , "E-mail já cadastrado!"
"""
Função para validar o Login
"""

def search_user(email , password):
    conexao = sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()

    cursor.execute("""SELECT * FROM users_informations
                   WHERE email = ?""" , (email,)) # A "," é necessária pq o cursor.execute() espera um tupla com 02 argumentos, como so tem 01 usa a , !
    user = cursor.fetchone() # Puxa uma coluna do banco
    conexao.close()

    if user:
        if user[3] == password:
            return True , user[1]  #Vai retornar o nome do usuario!(Operação de login deu certo!)
        else:
            return False , "Senha incorreta!"  #Retorna a senha incorrreta ou email n encontrado!
    else:
        return False , "E-mail não encontrado!"


"""
Função para verificar se o email ja esta cadastrado!
"""

def email_exists(email):
    conexao = sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT email FROM users_informations WHERE email = ?", (email,)) #O , Transforma em uma tupla!
    result = cursor.fetchone()
    conexao.close

    return result is not None 
