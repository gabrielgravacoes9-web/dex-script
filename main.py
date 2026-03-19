from executor import executar_codigo
from editor import mostrar_codigo
from comandos import limpar_codigo, salvar_codigo, carregar_codigo
from desenhos import desenhar
from arquivos import listar_arquivos

print("Mini Compilador Python v6")

print("Comandos:")
print("EXECUTAR")
print("VER")
print("SALVAR")
print("ABRIR")
print("LIMPAR")
print("DESENHAR nome")
print("DIR")
print("DIR ALL")
print("SAIR\n")

codigo = []

while True:
    linha = input(">>> ")
    comando = linha.upper()

    if comando == "EXECUTAR":
        executar_codigo(codigo)

    elif comando == "VER":
        mostrar_codigo(codigo)

    elif comando == "LIMPAR":
        codigo = limpar_codigo()

    elif comando == "SALVAR":
        salvar_codigo(codigo)

    elif comando == "ABRIR":
        codigo = carregar_codigo()

    elif comando == "DIR":
        listar_arquivos()

    elif comando == "DIR ALL":
        listar_arquivos("all")

    elif linha.lower().startswith("desenhar "):
        tag = linha.lower().replace("desenhar ", "").strip()
        desenhar(tag)
        continue

    elif comando == "SAIR":
        print("Encerrando compilador...")
        break

    else:
        codigo.append(linha)