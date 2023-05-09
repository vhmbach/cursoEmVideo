import pandas as pd
uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula2.1/movies.csv'
uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.2/ratings.csv'
filmes = pd.read_csv(uri)
filmes.columns = ["filmeId", "titulo", "generos"]
print(filmes.head())
