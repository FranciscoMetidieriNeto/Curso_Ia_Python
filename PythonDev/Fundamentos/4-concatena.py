# concatenação de valores em Python
name = input("Digite o nome do filme: \n ")
release_year = int(input("Digite o ano de lançamento: \n "))
note_movie = float(input("Digite a nota do filme: \n "))
print('Dados do filme:')
print("====================")

# Alternativa 1
print("nome do filme: ", name)
print("ano de lançamento: ", release_year)
print("nota do filme: ", note_movie)

# Alternativa 2 
print("nome do filme: ", name, "\nano de lançamento: ", release_year, "\nnota do filme: ", note_movie)

# Alternativa 3 - Usando f-string (forma mais moderna e recomendada)
print(f"nome do jogo: {name}\n" 
      f"ano de lançamento: {release_year}\n"
      f"nota do filme: {note_movie}\n"
      )