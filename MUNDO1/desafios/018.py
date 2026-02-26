#Programa que leia um ângulo qualquer e mostre o valor seno, cosseno e tangente
import math

ang = float(input('Digite um ângulo: '))
con = math.radians(ang)

sen = math.sin(con)
cos = math.cos(con)
tang = math.tan(con)

print(f'seno: {sen:.2f}\ncossêno: {cos:.2f}\ntangente: {tang:.2f}')