def gerar_objeto_personalizado(cor, *, altura, formato):
    print("\n")
    print(f"{formato} de cor {cor} com {altura}m de altura!")
    print("\n")

# gerar_objeto_personalizado("Azul", 1.60, "Bola") Erro!
# gerar_objeto_personalizado(altura=1.60, formato="Bola", "Vermelho") Erro!

gerar_objeto_personalizado("Azul", altura=1.60, formato="Bola")