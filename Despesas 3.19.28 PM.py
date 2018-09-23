import pandas as pd

df = pd.read_pickle('DADOS/TODOS.pickle')
print(df['DES_SITUACAO_CANDIDATURA'].unique())
print(df['DESC_SIT_TOT_TURNO'].unique())
tabela=[[]]

for ano in ['2010', '2014', '2018']:
    SelAno = df.loc[df['ANO_ELEICAO'] == int(ano)]
    for uf in df['uf'].unique():
        SelUf = SelAno.loc[SelAno['uf'] == uf]
        for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL','SENADOR']:
            if cargo == 'DEPUTADO ESTADUAL' and uf=='DF':
                cargo = 'DEPUTADO DISTRITAL'
            SelCargo = SelUf.loc[SelUf['DS_CARGO'] == cargo]
            sgpartidos = SelCargo['SG_PARTIDO'].unique()
            for sigla in sgpartidos:
                SelPart = SelCargo.loc[SelCargo['SG_PARTIDO'] == sigla]
                SelMu = SelPart.loc[SelPart['DS_GENERO'] == 'FEMININO']
                media = SelPart['DESPESA_MAX_CAMPANHA'].mean()/1000
                mediam = SelMu['DESPESA_MAX_CAMPANHA'].mean()/1000
                tabela.append([ano, uf, cargo, sigla, len(SelPart), media, len(SelMu), mediam])

df = pd.DataFrame(tabela[1:], columns=['ANO', 'UF', 'CARGO', 'SIGLA', 'QTD_TOTAL', 'MÉDIA_DE_DESPESAS', 'QTD_MULHERES', 'MEDIA_DE_DESPESAS_MULHERES'])
# a = df.sort_values(by=['MÉDIA DE DESPESAS'])
df.to_csv('RESULTADOS/teste.csv', encoding='latin-1')

