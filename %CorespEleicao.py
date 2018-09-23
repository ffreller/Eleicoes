import pandas as pd

estados = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}
tabela = [[]]
cols = ['UF', 'CARGO', 'COR', 'propor14', 'propor18']

df = pd.read_pickle('DADOS/TODOS.pickle')
for uf in estados.keys():
    SelUf = df.loc[df['uf'] == uf]
    for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR']:
        if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
            cargo = 'DEPUTADO DISTRITAL'
        SelCargo = SelUf.loc[SelUf[f'DS_CARGO'] == cargo]
        for cor in ['BRANCA', 'PRETA', 'PARDA', 'AMARELA', 'INDÍGENA']:
            for ano in ['2014', '2018']:
                SelAno = SelCargo.loc[SelCargo['ANO_ELEICAO'] == int(ano)]
                SelCor = SelAno.loc[SelAno['DS_COR_RACA'] == cor]
                if ano == '2014':
                    propor14 = len(SelCor)/len(SelAno)
                if ano == '2018':
                    propor18 = len(SelCor)/len(SelAno)
                    tabela.append([uf, cargo, cor, propor14, propor18])

df = pd.DataFrame(tabela[1:], columns=cols)
df['Variaçao 14-18'] = (df['propor18'] - df['propor14'])/df['propor14']
df.to_csv('RESULTADOS/%CorespEleicao.csv', encoding='latin-1')
