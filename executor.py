def executar_codigo(codigo):
    if not codigo:
        print("Nenhum código para executar.\n")
        return

    codigo_final = "\n".join(codigo)

    try:
        bytecode = compile(codigo_final, "usuario", "exec")
        print("\nExecutando...\n")
        exec(bytecode)
    except Exception as erro:
        print("Erro encontrado:")
        print(erro)

    print()