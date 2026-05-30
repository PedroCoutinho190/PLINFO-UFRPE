import sqlite3

class DataManager:

    def __init__(self):
        self.connection = sqlite3.connect("Plinfo.db")
        self.cursor = self.connection.cursor()
    
    def _commit(self):
        self.connection.commit()

    def creat_database(self):
        """
        Método para Criar o Plinfo.db
        """
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users_informations(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                    )""")
        self._commit()
    
    def insert_database(self, user_name, email, password):
        """
        Método para adicionar dados no banco!
        """
        try:
            self.cursor.execute("""INSERT INTO users_informations
                        (user_name , email , password) VALUES
                        (? , ? , ?) 
                        """ , (user_name, email, password)) #O (?,?,?) = Para evitar ataques de sqlinjection , ai o sqlite vai substit. os "?" pelos valores fora da tripe" de forma segura!
            
            self._commit()
            return True , "Usuario Cadastrado com sucesso!✅"
        
        except sqlite3.IntegrityError:    #Aqui ele vai pegar a excessão (que seria quando o usuario ja tem o email cadastrado e ele quer cadastrar outro email igual...)
            return False , "E-mail já cadastrado!"

    def search_user(self, email, password):
        """
        Método para validar o Login do usuario, vai buscar as informações a partir do E-mail do usuario e comparar com oq ele colocou!
        """
        self.cursor.execute("""SELECT * FROM users_informations
                    WHERE email = ?""" , (email,)) # A "," é necessária pq o cursor.execute() espera um tupla com 02 argumentos, como so tem 01 usa a , !
        user = self.cursor.fetchone() # Puxa uma coluna do banco

        if user:
            if user[3] == password:
                return True , user[1]  #Vai retornar o nome do usuario!(Operação de login deu certo!)
            else:
                return False , "Senha incorreta!"  #Retorna a senha incorrreta!
        else:
            return False , "E-mail não encontrado!"

    def email_exists(self, email):
        """
        Método para verificar se o email ja esta cadastrado!
        """
        self.cursor.execute("SELECT email FROM users_informations WHERE email = ?", (email,)) #O , Transforma em uma tupla!
        result = self.cursor.fetchone()

        return result is not None 

    def get_user_data(self, email):
        """
        Método para pegar os dados do usuario
        """
        self.cursor.execute("SELECT * FROM users_informations WHERE email = ?", (email,))
        user = self.cursor.fetchone()
        return user

    def delete_user(self, email):
        """
        Método para Deletar o Usuário
        """
        self.cursor.execute("""DELETE FROM users_informations WHERE email = ?""", (email,))
        self._commit()

    def update_name(self, email, new_name):
        """
        Método pra Alteração de nome
        """
        self.cursor.execute("UPDATE users_informations SET user_name = ? WHERE email = ?", (new_name, email))
        self._commit()

    def update_email(self, old_email, new_email):
        """
        Método para Alteração de E-mail
        """
        self.cursor.execute("UPDATE users_informations SET email = ? WHERE email = ?", (new_email, old_email))
        self._commit()

    def update_password(self, email, new_password):
        """
        Método para Alteração de Senha
        """
        self.cursor.execute("UPDATE users_informations SET password = ? WHERE email = ?", (new_password, email))
        self._commit()

db = DataManager() #Criando o Objeto inicializador do DataManager()