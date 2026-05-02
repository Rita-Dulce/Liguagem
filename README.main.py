# Liguagem
estudantes = [
    {"nome": "Ana", "idade": 21, "curso": "Eng. Informática"},
    {"nome": "Bruno", "idade": 19, "curso": "Gestão"},
    {"nome": "Carla", "idade": 22, "curso": "Eng. Civil"},
    {"nome": "Daniel", "idade": 20, "curso": "Eng. Informática"}
]
idade_filtro = int(input("Digite a idade mínima: "))
nomes_maiores = [
    estudante["nome"].upper() 
    for estudante in estudantes 
    if estudante["idade"] > idade_filtro
]

# Imprime o resultado
print(f"Estudantes com mais de {idade_filtro} anos: {nomes_maiores}")

# O QUE ESTÁ A ACONTECER:
# 1. O código recebe um número do utilizador (a idade mínima).
# 2. Percorre a lista 'estudantes' e filtra apenas aqueles cuja idade é superior ao valor inserido.
# 3. Transforma os nomes filtrados para letras maiúsculas e guarda-os na lista 'nomes_maiores'.
# 4. Imprime o resultado final no ecrã.
