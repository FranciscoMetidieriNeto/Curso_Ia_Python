# Utilizando input (coamndo para receber dados (entrada))
# Retorno de input será sempre string a não ser que defina o tipo de dado

# Input sendo usado para entrada de dados pelo usuário e \n para Top gunquebrar linha
nome = input("Digite o nome do filme: \n ")
release_year = int(input("Digite o ano de lançamento: \n "))
note_movie = float(input("Digite a nota do filme: \n "))

# Exibe as informações digitadas pelo usuário
print("Nome do filme:", nome)
print("Ano de lançamento:", release_year)
print("Nota do filme:", note_movie)

print(type(nome))          # str (string)
print(type(release_year)) # str (string) (Alterado para int no input)
print(type(note_movie))   # str (string) (Alterado para float no input)
