#=====MasterSynth=====#

from pyo import *
import mido

# NOTAS (em Hertz)
notes = {
    60: 262,  # C4
    62: 294,  # D4
    64: 330,  # E4
    65: 349,  # F4
    67: 392,  # G4
    69: 440,  # A4
    71: 494,  # B4
}

# Inicializar o servidor de áudio
s = Server().boot()

# Envelopes e oscilador
env = Adsr(attack=0.01, decay=0.1, sustain=0.5, release=0.5)
osc = SuperSaw(freq=440, mul=env)

# Saída de som
osc.out()

# Iniciar o servidor
s.start()

# Função para tocar a nota
def play_note(note):
    if note in notes:
        osc.freq = notes[note]
        env.play()

# Função para parar a nota
def stop_note():
    env.stop()

# Listar dispositivos MIDI disponíveis
input_names = mido.get_input_names()
print("Dispositivos de entrada MIDI disponíveis:")
for i, name in enumerate(input_names):
    print(f"{i}: {name}")

# Escolher o índice do controlador MIDI
device_index = int(input("Selecione o índice do seu controlador MIDI: "))

# Tentar abrir o dispositivo MIDI
try:
    with mido.open_input(input_names[device_index]) as inport:
        print(f"Aguardando mensagens do dispositivo: {input_names[device_index]}")
        while True:
            for msg in inport.iter_pending():
                if msg.type == 'note_on':
                    play_note(msg.note)
                elif msg.type == 'note_off':
                    stop_note()
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Manter o GUI
s.gui(locals())



































"""







from pyo import *

# NOTAS (em Hertz) // Dividir ou Multiplicar para 8as acima ou abaixo
print("C4: 262 Hz\nD4: 294 Hz\nE4: 330 Hz\nF4: 349 Hz\nG4: 392 Hz\nA4: 440 Hz\nB4: 494 Hz")

# START
s = Server().boot()

# ENVELOPE
attack = 0.5
decay = 0.8
sustain = 1
release = 0.8
# ADSR
env = Adsr(attack=attack, decay=decay, sustain=sustain, release=release)

# OSC

freqs = [110, 262, 330, 494] #Amadd9
#freqs = [294, 349, 440, 660] #Dmadd9
#osc = [Sine(freq=freq, mul=env) for freq in freqs]
osc = [SuperSaw(freq=freq, mul=env) for freq in freqs]
combined_signal = sum(osc)

# FILTER
filt = ButLP(osc, freq=800)

# VOLUME
volume = Sig(0.8)
output = filt * volume

# OUT
out = out = output.out()

# SERVER
s.start()
#s.stop()

# ENVELOPE PLAY
env.play()

# KEEP
s.gui(locals())
"""



"""

from pyo import *
import pygame
import sys

# Frequências das notas na oitava central (C4 a B4)
NOTES = [
    261.63,  # C4
    277.18,  # C#4
    293.66,  # D4
    311.13,  # D#4
    329.63,  # E4
    349.23,  # F4
    369.99,  # F#4
    392.00,  # G4
    415.30,  # G#4
    440.00,  # A4
    466.16,  # A#4
    493.88   # B4
]

# Inicializa o servidor de áudio
s = Server().boot()

# Define o envelope ADSR
env = Adsr(attack=0.01, decay=0.1, sustain=0.7, release=0.5, dur=1, mul=0.5)

# Define os osciladores para cada nota da escala cromática
oscillators = [Sine(freq=freq, mul=env) for freq in NOTES]

# Combina os sinais dos osciladores
combined_signal = sum(oscillators)

# Define um filtro passa-baixa
filt = ButLP(combined_signal, freq=800)

# Define um controle de volume ajustável
volume = Sig(0.5)

# Aplica o controle de volume ao sinal filtrado
output = filt * volume

# Define a saída do áudio
out = output.out()

# Inicia o servidor de áudio
s.start()

# Inicializa o Pygame
pygame.init()

# Define as teclas associadas a cada nota da escala cromática
key_mapping = {
    pygame.K_a: 0,   # C4
    pygame.K_w: 1,   # C#4
    pygame.K_s: 2,   # D4
    pygame.K_e: 3,   # D#4
    pygame.K_d: 4,   # E4
    pygame.K_f: 5,   # F4
    pygame.K_t: 6,   # F#4
    pygame.K_g: 7,   # G4
    pygame.K_y: 8,   # G#4
    pygame.K_h: 9,   # A4
    pygame.K_u: 10,  # A#4
    pygame.K_j: 11   # B4
}

# Laço principal do programa
while True:
    # Processa eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Verifica se a tecla pressionada está associada a uma nota
            if event.key in key_mapping:
                # Obtém o índice da nota correspondente à tecla pressionada
                idx = key_mapping[event.key]
                # Define a frequência dos osciladores para tocar a nota
                for i, osc in enumerate(oscillators):
                    osc.setFreq(NOTES[idx] * pow(2, i / 12.0))
        # Verifica se a tecla ESC foi pressionada para encerrar o programa
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
"""




