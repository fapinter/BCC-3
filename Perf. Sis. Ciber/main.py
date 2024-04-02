import time
import LFU
import LRU
import FIFO
import Simulacao

#Grupo RA1 1
#   Fabricio Goes Pinterich
#   Gabriel Marques Simini
#   Guilherme Luiz da Câmara Falcão
#   Crystofer Samuel Demetino dos Santos

menu = True
simulacaoRodada = False
opcao_menu = -1

cacheHit = 0
cacheMiss = 0

while menu:

  print("""\n
    ***************************************
    **              M E N U              **
    **                                   **
    ** Escolher Texto: (1 - 100)         **
    ** Modo de Simulação: (-1)           **
    ** Sair: (0)                         **
    ***************************************\n
    """)
  opcao_menu = int(input("Digite o número que deseja: "))
  while opcao_menu < -1 or opcao_menu > 100:
    opcao_menu = int(input("Opção inválida, digite um número de -1 a 100: "))

  if opcao_menu == 0:
    print("\nSaindo do aplicativo...")
    time.sleep(1.5)
    menu = False

  elif opcao_menu == -1:
    print("\nModo simulação selecionado! Segue a simulação:")
    time.sleep(3)

    melhor_algoritmo = Simulacao.modoSimulacao()
    simulacaoRodada = True

  else:
    time.sleep(3)
    arquivo = f'textos/{opcao_menu}.txt'  # Caminho para a pasta "textos" + nome do arquivo com base na opção do menu

    if simulacaoRodada:
      #Caso a simulação tenha sido rodada previamente, faremos a impressão dos textos imediatamente
      try:
        #Aparece como nao atribuido no Replit, mas como é obrigatorio rodar a simulação antes, ele possui uma atribuição
        InCache = melhor_algoritmo.checkCache(arquivo)
        if InCache:
          print("\nImprimindo o texto...")
          time.sleep(3)
          with open(arquivo, 'r') as f:
            print(f.read())  # Imprime o conteúdo do arquivo
        else:
          melhor_algoritmo.addCache(arquivo, cacheHit, cacheMiss)
          print("\nImprimindo o texto...")
          time.sleep(3)
          with open(arquivo, 'r') as f:
            print(f.read())

      except FileNotFoundError:
        print("Arquivo não encontrado.")
    else:
      #Caso a simulação não tenha sido rodada, forçaremos a simulação antes de fazer a busca pelo texto
      print("\nModo Simulação ainda não rodado\nExecutando Modo Simulação...")
      time.sleep(3)
      melhor_algoritmo = Simulacao.modoSimulacao()
      simulacaoRodada = True

      InCache = melhor_algoritmo.checkCache(arquivo)
      if InCache:
        # Se o arquivo está no cache, basta imprimí-lo diretamente
        try:
          with open(arquivo, 'r') as f:
            print(f.read())  # Imprime o conteúdo do arquivo
        except FileNotFoundError:
          print("Arquivo não encontrado.")
      else:
        # Se o arquivo não está no cache, adicionamos ao cache e depois imprimimos
        melhor_algoritmo.addCache(arquivo, cacheHit, cacheMiss)
        try:
          with open(arquivo, 'r') as f:
            conteudo_arquivo = f.read()  # Lê todo o conteúdo do arquivo
            print(conteudo_arquivo)  # Imprime o conteúdo do arquivo
        except FileNotFoundError:
          print("Arquivo não encontrado.")
