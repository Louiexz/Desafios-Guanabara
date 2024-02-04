# desafio 8
medida = int(input('Distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dcm = medida * 10000
km = medida * 0.001
hec = medida * 0.01
dec = medida * 0.1
print(f'Distancias: \n \033[0;31mEm cm é {cm}\033[m \n \033[0;32mEm mm é {mm}\033[m \n \033[0;33mEm dcm é {dcm}\n \033[0;34mEm km é {km}\033[m \n \033[0;35mEm hec é {hec}\033[m \n \033[0;36mEm dec é {dec}\033[m')