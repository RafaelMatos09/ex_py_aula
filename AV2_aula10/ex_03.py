"""
Aluno: Rafael Moreira Matos  
Matrícula: 202209201907 
Unidade: Maracanã

3 -  Qual biblioteca você utilizaria e quais funções você
 deveria utilizar para a implementação da calculadora?
"""
import operator
from math import *


def adicao(*args):
    a = sum(args)
    return a


def subtracao(x, y):
    a = operator.sub(x, y)
    return a


def divisao(x, y):
    a = operator.floordiv(x, y)
    return a


def multiplicacao(x, y):
    a = operator.mul(x, y)
    return a


def seno(x):
    a = sin(x)
    return a


def cosseno(x):
    a = cos(x)
    return a


def tangente(x):
    a = tan(x)
    return a


c1 = adicao(2, 2)
print(c1)
c2 = subtracao(22, 2)
print(c2)
c3 = divisao(22, 2)
print(c3)
c4 = multiplicacao(2, 2)
print(c4)
c5 = seno(33)
print(c5)
c6 = cosseno(22)
print(c6)
c7 = tangente(22)
print(c7)
