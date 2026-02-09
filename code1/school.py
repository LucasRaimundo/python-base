#!/usr/bin/env python3

"""Codigo para mostrar quais os alunos de determinadas salas estão fazendo determinadas atividades
-> Exercicio
"""

__version__="0.1.0"
__author__="Lucas"

alunos_sala1 = ["Lucas", "Bianca", "Maria", "Ana", "Rafael"]
alunos_sala2 = ["Marcia", "Lana", "Benicio", "Rogério", "Keila"]

aula_ingles = ["Lucas", "Lana", "Benicio", "Maria", "Keila"]
aula_musica = ["Bianca", "Ana", "Rafael", "Rogério"]
    
atividades = [("Ingles", aula_ingles),("Musica",aula_musica)]

for nome_atividade, atividade in atividades:
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in alunos_sala1:
            atividade_sala1.append(aluno)
        elif aluno in alunos_sala2:
            atividade_sala2.append(aluno)
    
    print(f"Alunos da atividade {nome_atividade} para a sala 1: {atividade_sala1}")
    print(f"Alunos da atividade {nome_atividade} para a sala 2: {alunos_sala2}")
    print("*" * 80)

