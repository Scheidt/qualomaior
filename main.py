from controlador_cadastros import Controlador_Cadastros

pontos = 0
jogo = Controlador_Cadastros()
while True:
    if jogo.menu():
        pontos += 1
    print(f"Você tem {pontos} pontos")
 