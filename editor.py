def mostrar_codigo(codigo):
    if not codigo:
        print("Código vazio.\n")
        return

    print("\nSeu código:\n")

    for i, linha in enumerate(codigo, start=1):
        print(f"{i:03} | {linha}")

    print()