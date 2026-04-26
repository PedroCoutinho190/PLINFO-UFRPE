import sqlite3



def creat_database():
    """
    Criando o Plinfo.db
    """
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
    


def insert_database(user_name, email, password):
    """
    Função para adicionar dados no banco!
    """
    conexao = sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()
    try:
        cursor.execute("""INSERT INTO users_informations
                    (user_name , email , password) VALUES
                    (? , ? , ?) 
                    """ , (user_name, email, password)) #O (?,?,?) = Para evitar ataques de sqlinjection , ai o sqlite vai substit. os "?" pelos valores fora da tripe" de forma segura!
        
        conexao.commit()
        conexao.close()
        return True , "Usuario Cadastrado com sucesso!✅"
    
    except sqlite3.IntegrityError:    #Aqui ele vai pegar a excessão (que seria quando o usuario ja tem o email cadastrado e ele quer cadastrar outro email igual...)
        conexao.close()               #Impedindo do codigo quebrar por errointegrity do sqlite3.
        return False , "E-mail já cadastrado!"


def search_user(email, password):
    """
    Função para validar o Login do usuario, vai buscar as informações a partir do E-mail do usuario e comparar com oq ele colocou!
    """
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
            return False , "Senha incorreta!"  #Retorna a senha incorrreta!
    else:
        return False , "E-mail não encontrado!"



def email_exists(email):
    """
    Função para verificar se o email ja esta cadastrado!
    """
    conexao = sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT email FROM users_informations WHERE email = ?", (email,)) #O , Transforma em uma tupla!
    result = cursor.fetchone()
    conexao.close

    return result is not None 



def get_user_data(email):
    """
    Função para pegar os dados do usuario
    """
    conexao =sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM users_informations WHERE email = ?", (email,))
    user = cursor.fetchone()
    conexao.close()
    return user



def delete_user(email):
    """
    Deletar Usuário
    """
    conexao = sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()

    cursor.execute("""DELETE FROM users_informations WHERE email = ?""", (email,))
    conexao.commit()
    conexao.close()


def update_name(email, new_name):
    """
    Alteração de nome
    """
    conexao = sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()

    cursor.execute("UPDATE users_informations SET user_name = ? WHERE email = ?", (new_name, email))
    conexao.commit()
    conexao.close()


def update_email(old_email, new_email):
    """
    Alteração de E-mail
    """
    conexao = sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()
    
    cursor.execute("UPDATE users_informations SET email = ? WHERE email = ?", (new_email, old_email))
    conexao.commit()
    conexao.close()




def update_password(email, new_password):
    """
    Alteração de Senha
    """
    conexao = sqlite3.connect("Plinfo.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE users_informations SET password = ? WHERE email = ?", (new_password, email))
    conexao.commit()
    conexao.close()
