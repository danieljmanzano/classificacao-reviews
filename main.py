'''
ideia de projeto de tratamento de dados e machine learning

classifica reviews de produtos em positivas e negativas
dataset tirado de: https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
'''

import pandas as pd

''' Função que carrega o arquivo CSV e retorna um DataFrame.'''
def carrega_arquivo(): # o arquivo é muito grande então to carregando só um pouco dele ainda rs
    df_amostra = pd.read_csv('Reviews.csv', nrows=50000)
    return df_amostra

def main():
    df_amostra = carrega_arquivo()
    
    # Exibe as primeiras linhas do DataFrame
    print(df_amostra.head())
    print("--------------------------------")
    # Exibe informações gerais do DataFrame
    print(df_amostra.info())
    print("--------------------------------")

    # Exibe estatísticas descritivas do DataFrame
    print(df_amostra.describe())
    print("--------------------------------")
    
    # Verifica se existem valores ausentes
    print(df_amostra.isnull().sum())
    print("--------------------------------")


if __name__ == "__main__":
    main()
