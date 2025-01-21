print("Olá, mundo!")
nome = input("Como te chamas? ").strip().capitalize()
print(f"Olá, {nome}!")

idade = input("Qual a tua idade? ").strip()
while not idade.isdigit():
    print("Por favor, introduz um número válido para a idade.")
    idade = input("Qual a tua idade? ").strip()

apelido = input("Qual o teu apelido? ").strip().capitalize()
localidade = input("De onde és? ").strip().capitalize()

print(f"O teu nome completo é {nome} {apelido}.")
print(f"Tu tens {idade} anos de idade.")
print(f"És de {localidade}.")
