import os

def listar_arquivos(modo="normal"):
    try:
        itens = os.listdir()

        print("\nArquivos na pasta:\n")

        for item in itens:
            if modo == "all":
                print(item)
            else:
                if os.path.isfile(item):
                    print(item)

        print()

    except Exception as erro:
        print("Erro ao listar arquivos:", erro)