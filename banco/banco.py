import sqlite3
import os
class Banco():

    def __init__(self):
        
        dirbanco = os.path.normpath('banco/coletanea.sqlite')
        self.banco = sqlite3.connect(dirbanco)
        self.cursor = self.banco.cursor()
        #self.criarTabela()
    
    def criarTabela(self):

        self.cursor.execute("""
        CREATE TABLE coletaneas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        musica TEXT NOT NULL,
        endereco_musica TEXT NOT NULL,
        numero INTEGER,
        album TEXT NOT NULL,
        trecho TEXT
        );
        """)
        print('tabela criada com sucesso')

    def selecionarDados(self,tipo,pesquisa):

        sql = ("""
                SELECT * FROM coletaneas
                WHERE {} LIKE'%{}%' order by id
                """.format(tipo,pesquisa))

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def pesquisa_album(self):

        sql = (""" SELECT DISTINCT album FROM coletaneas order by id """)
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def selecionarColetanea(self,pesquisa):
        sql = ("""
                SELECT * FROM coletaneas
                WHERE album == '{}'  order by musica
                """.format(pesquisa))

        self.cursor.execute(sql)
        return self.cursor.fetchall()
                
    

'''
banco = banco()
banco.inserirDados('testeGrave','video.mp4',1,'teste','teste de grave')
'''