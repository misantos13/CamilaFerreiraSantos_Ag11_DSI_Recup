# Desenvolvimento de Sistemas I
# Agenda 11 - Monitoramento de Reservatório (Recuperação)
# Camila Ferreira Santos
# Turma: FMD

# Importa cor e inicialização da biblioteca colorama

from colorama import Fore, Style, init

# Inicializa o colorama
init()

# Lista com as mensagens de alerta do nível (1 a 5)
nivelAgua = [
    "Nível 1: Muito baixo (Crítico)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito alto (Alerta)",
]

def definirCorNivel(nivel):
  
# Define e retorna a cor conforme o nível informado.
  if nivel == 1:
    return Fore.RED
  elif nivel == 2:
    return Fore.YELLOW
  elif nivel == 3:
    return Fore.GREEN
  elif nivel == 4:
    return Fore.CYAN
  elif nivel == 5:
    return Fore.BLUE
  return Style.RESET_ALL

# Simulação de leituras
lerSimulacao = [1, 2, 3, 4, 5]

print("Simulação de Monitoramento do Reservatório de Água\n")

for nivelAtual in lerSimulacao:
  # Pega a mensagem correspondente
  mensagem = nivelAgua[nivelAtual - 1]

  # Obter a cor correspondente
  cor = definirCorNivel(nivelAtual)

  # Exibe a mensagem colorida
  print(cor + mensagem)

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL)