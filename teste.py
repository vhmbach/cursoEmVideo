texto = """Vitor Vitor Hugo Hugo Martins Martins Bach Bach Lima Lima"""
palavras = texto.split()
palavras_unicas = list(set(palavras))
texto_sem_repeticao = " ".join(palavras_unicas)
print(texto_sem_repeticao)
print(palavras_unicas)