def desenhar(tag):
    desenhos = {
        "macaco": r"""
   @@@@@
  ( o o )
 /  ---  \
 |  ---  |
  \_____/
  /| | |\
   |_|_|
""",

        "escola": r"""
      /\ 
     /  \ 
    /____\ 
   | _  _ |
   || || ||
   ||_||_||
   |  __  |
   | |  | |
   |_|__|_|
""",

        "emoji_feliz": r"""
   _____
  /     \
 |  ^ ^  |
 |   -   |
 | \___/ |
  \_____/
""",

        "coracao": r"""
   **   **
  ****** *
 *********
 *********
  *******
   *****
    ***
     *
""",

        "navio": r"""
        |\
       /| \
      /_|__\
        |
    ____|____
   \        /
~~~~\______/~~~~
""",

        "aviao": r"""
        ^
       / \
      /___\
--====| |====--
       | |
       | |
      /   \
"""
    }

    if tag in desenhos:
        print(desenhos[tag])
    else:
        print("Desenho não encontrado.")