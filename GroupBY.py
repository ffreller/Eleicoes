import pandas as pd
import matplotlib as plt


df = pd.read_pickle('DADOS/TODOS.pickle')
print(df['uf'])
print(df.uf)
print(len(df))

df = df.loc[df['DS_CARGO'] == 'DEPUTADO ESTADUAL']
a = df['DESPESA_MAX_CAMPANHA'].groupby(df['uf']).mean()
b = pd.DataFrame(a, columns= ['uf','DESPESA'])
b = a.sort_values(na_position='first')
# print(df['DES_SITUACAO_CANDIDATURA'].unique())
# print(a/1000)
print(b)
# print(df['DS_GENERO'].unique())

plt.interactive(False)

a = df['DESPESA_MAX_CAMPANHA'].groupby(df['uf']).mean().plot(kind='bar')
plt.pyplot.show(a)