import sys, os
import sqlite3 as sq
import time
import getpass

#vars
os.system('clear')
dia = time.strftime("%d/%m/%Y")
dia2 = time.strftime("%d_%m")
vitrine = ()
area = ()
confinado = ()
total = ()

#Diretorio android
dir = "/storage/emulated/0/Download/AFT"

#Conexão database
conn = sq.connect("AFT.db")
c = conn.cursor()

#login INIT
af = input('Abre[A] ou Fecha[F]?: ').upper()
nome = input ("Nome: ").lower()
senha = getpass.getpass("A senha esta oculta, mas pode digitar...\nSenha: ")

#Login Cond
if nome == "guilherme" or nome != "elias" or nome != "kadu":
    if senha != '8458':
        sys.exit()
    else:
        os.system('clear')
        print("Contagem[c]\nConsultar[cons]")

#Funções 
def criar():
    c.execute (f"CREATE TABLE IF NOT EXISTS Contagem{dia2}(af TEXT,vitrine INTEGER, area INTEGER, confinado INTEGER, defeito INTEGER, total INTEGER, operador TEXT, criado_em TEXT)")
    print(f"Tudo Ok {nome}♡ database criada com sucesso")
    
def inserir(v1, v2, v3, defeito, operador, af):
    criar()
    op = operador
    c.execute(f"INSERT INTO Contagem{dia2}(af,vitrine,area,confinado,defeito,total,operador,criado_em) VALUES ('{af}','{v1}','{v2}','{v3}','{defeito}','{total}','{op}','{dia2}')")
    print (f"Realizado com sucesso {op} - TOTAL:{total}")
def cons():
    #afc = input('Abre(a) ou Fecha(f): ')
    dia3 = input("Data a consultar[??_??]: ")
    c.execute(f"SELECT * FROM Contagem{dia3}")
    const = c.fetchone()
    os.system('clear')
    print('A/F: %s \nVitrine: %i \nArea: %i \nConfinado: %i \nDefeito: %i \nTOTAL: %i \nOperador: %s \nCriado_em: %s'%const)
def cs():
    dia3 = input("Data a consultar: ")
    print ("""
Setores:
Vitrine
Area 
Confinado
Defeito
Operador
Total
""")
    setor = input("Qual o setor? ")
    c.execute (f"SELECT {setor} FROM Contagem{dia3}")
    csa = c.fetchone()
    os.system('clear')
    print(f"|  SETOR   | VALOR |\n| {setor} |  %s   |"%csa)
def adddef(x):
  global defeito 
  defeito = 4
  defeito += x
  print(defeito)
while True:
    #Entrada
    ent = input (f"Pois não {nome}: ").lower()
    if ent == "cont" or ent == "contagem" or ent == "c":
        criar()
        vitrine = int(input ("Vitrine: "))
        area = int(input("Área: "))
        confinado = int(input("Confinado: "))
        defeito = int(4)
        total = vitrine + area + confinado + defeito
        inserir(vitrine,area,confinado,defeito,nome,af)
        conn.commit()
    if ent == 'cons':
        cons()
    if ent == '':
        os.system('clear')
    if ent == 'defeito' or ent == 'df':
      adddef(int(input('Quantos: ')))
    if ent == "consultar_setor" or ent == "cs":
        cs()
    if ent == 'sair':
        sys.exit()