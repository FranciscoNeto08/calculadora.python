import math

print('Escreva um numero')
numero1 = int(input())

print('=-'*15)

print('Escreva um operador')
operador = input()

print('=-'*15)

print('Escreva outro numero')
numero2 = int(input())

print('=-'*15)

if operador == '+':
  resultado = numero1 + numero2
  print('Resultado é', resultado)

elif operador == '-':
  resultado = numero1 - numero2
  print('Resultado é', resultado)

elif operador == '*':
  resultado = numero1 * numero2
  print('Resultado é', resultado)

elif operador == '/':
  resultado = numero1 / numero2
  print('Resultado é', resultado)



