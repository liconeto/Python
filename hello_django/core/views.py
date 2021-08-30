from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos</h1>')


def soma(request, n1, n2):
    s = n1 + n2
    return HttpResponse(f'A soma de {n1} + {n2} = {s}')

def subtracao(request, n1, n2):
    sub = n1 - n2
    return HttpResponse(f'A subtração de {n1} - {n2} = {sub}')

def multiplicacao(request, n1, n2):
    multicacao = n1 * n2
    return HttpResponse(f'A Multiplicação de {n1} * {n2} = {multicacao}')

def divisao(request, n1, n2):
    divisao = n1 / n2
    return HttpResponse(f'A Divisão de {n1} / {n2} = {divisao}')