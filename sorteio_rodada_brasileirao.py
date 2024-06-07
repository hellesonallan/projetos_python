import random

def definir_times():
  times = [
  "Botafogo",
  "Athletico Paranaense",
  "Bahia",
  "Red Bull Bragantino",
  "Flamengo",
  "São Paulo",
  "Internacional",
  "Cruzeiro",
  "Atlético Mineiro",
  "Palmeiras",
  "Fortaleza",
  "Grêmio",
  "Vasco da Gama",
  "Juventude",
  "Fluminense",
  "Criciúma",
  "Corinthians",
  "Atlético Goianiense",
  "Vitória",
  "Cuiabá"
  ]
  return times

times = definir_times()

rodadas = list()

for i in range(0, 10):
  time_casa = times[random.randint(0, len(times) - 1)]
  times.remove(time_casa)

  time_visitante = times[random.randint(0, len(times) - 1)]
  times.remove(time_visitante)
    
  rodadas.append([time_casa, time_visitante])
  
times = definir_times()

for rodada in rodadas:
  print(rodada[0] + " X " + rodada[1])