import pandas as pd
import mysql.connector
import re

banco = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '123123',
        database ='Livros'
)
cursor = banco.cursor()


cursor.execute("USE Livros")

def gravar_itens(lista_para_sql):
    for parte in lista_para_sql:
            titulo_ = parte.pop(0)
            autor_ = parte.pop(0)
            ano_ = parte.pop(0)
            pag_ = parte.pop(0)
            print("\n")
            ano__= ano_.item()
            pag__= pag_.item()
            ano__ = str(ano__)
            pag__ = str(pag__)
            
            try:
                sql = "INSERT INTO projeto (nome_livro, autor_livro, ano, paginas, entregar_dia) VALUES (%s, %s, %s, %s, %s)"
                valores = (titulo_, autor_, ano__, pag__, resposta_dia_entrega)
                print(f' è ESTEEEE {valores}')
                cursor.execute(sql, valores)
                banco.commit()
            except Exception as erro:
                print("confira abaixo o erro:")
                print(erro)

def visualizar_livros():
    leitura = []
    with open("./executavel/livros.csv", encoding="utf-8") as archive:
        for line in archive:
            result = line.split(sep=',')
            result = line.rstrip('\n')
            leitura.append(result)
    print(leitura)
    return(leitura)
    
def remover_item(resposta_rem):
    try:
        cursor.execute("DELETE FROM projeto WHERE id = ('"+resposta_rem+"')")
        banco.commit()
    except Exception as erro:
        print(f"Algo deu errado!{erro}")

    


# livros = pd.read_csv("./executavel/livros.csv")


# df = pd.DataFrame(livros)
# df.drop(columns = ['ISBN_13','ISBN_10','idioma','editora','rating','avaliacao','resenha','abandonos','relendo','querem_ler','lendo','leram','descricao','genero','male','female'], inplace = True)
# print(df)
# df.to_csv('livros_recorte.csv')

livros = pd.read_csv("./executavel/livros.csv")
df = pd.DataFrame(livros, columns= ["titulo", "autor", "ano", "paginas"])

while True:


    print("| -----------------------------------------------------|")
    print("| OQUE DSEJA FAZER?                                    |")
    print("| [1] --> EMPRESTAR UM LIVRO                           |")
    print("| [2] --> VISUALIZAR INFORMAÇÕES DE LIVROS EMPRESTADOS |")
    print("| [X] --> DEVOLVER OS LIVROS (NÃO CONFIGURADO)         |")
    print("| -----------------------------------------------------|")
    resposta1 = input("Digite um número... \n")

    if resposta1 == "#sair":
        print("Recomeçando o sistema...")
        continue       

    if resposta1 == "1":
        resposta2 = str(input("Escreva o nome do livro que deseja pegar emprestado...\n"))
        if resposta2 == "#sair":
            print("Recomeçando o sistema...")
            continue

        else:
            df1 = df[df['titulo'].str.contains(f'{resposta2}',case=False)]
            print(df1)
            resposta3 = int(input("Qual ídice do livro (primeiro número)?\n"))
            if resposta3 == "sair":
                print("Recomeçando o sistema...")
                continue  
 
            else:
                resposta_dia_entrega = (input("O livro deve ser entregue que dia? (aaaa-mm-dd)"))
                linha = df.iloc[resposta3].values.tolist()
                df = df.drop(resposta3)
                lista_para_sql = []
                lista_para_sql.append(linha)
                print(linha)
                gravar_itens(lista_para_sql)
                


    if resposta1 == "2":
        cursor.execute("SELECT * FROM projeto;")
        data = cursor.fetchall()
        print('\n')
        for lista_data in data:
            print(f'{lista_data}')
    print('\n')
