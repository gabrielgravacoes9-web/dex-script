def limpar_codigo():
    print("Código apagado.\n")
    return []

def salvar_codigo(codigo):
    nome = input("Nome do arquivo: ") + ".py"
    with open(nome, "w", encoding="utf-8") as f:
        f.write("\n".join(codigo))
    print("Arquivo salvo.\n")

def carregar_codigo():
    nome = input("Arquivo para abrir: ")
    try:
        with open(nome, "r", encoding="utf-8") as f:
            linhas = f.read().split("\n")
        print("Arquivo carregado.\n")
        return linhas
    except:
        print("Erro ao abrir arquivo.\n")
        return []