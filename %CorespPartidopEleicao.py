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
cargo = ''
tabela = [[]]
sgl = [[]]
cols = ['UF', 'CARGO', 'SG_PARTIDO', 'COR', 'propor14', 'propor18']
propor14 = 0
propor18 = 0


df = pd.read_pickle(f'DADOS/TODOS.pickle')
for uf in estados.keys():
    SelUf = df.loc[df['uf'] == uf]
    for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR']:
        SelCargo = SelUf.loc[SelUf['DS_CARGO'] == cargo]
        if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
            cargo = 'DEPUTADO DISTRITAL'
        siglas = SelCargo['SG_PARTIDO'].unique()
        for sigla in siglas:
            SelPart = SelCargo.loc[SelCargo['SG_PARTIDO'] == sigla]
            for cor in ['PARDA', 'BRANCA', 'PRETA', 'AMARELA', 'INDÍGENA']:
                for ano in ['2014', '2018']:
                    SelAno = SelPart.loc[SelPart['ANO_ELEICAO'] == int(ano)]
                    SelCor = SelAno.loc[SelAno['DS_COR_RACA'] == cor]
                    if len(SelAno) != 0:
                        if ano == '2014':
                            propor14 = len(SelCor) / len(SelAno)
                        if ano == '2018':
                            propor18 = len(SelCor) / len(SelAno)
                            tabela.append([uf, cargo, sigla, cor, propor14, propor18])
                    else:
                        if ano == '2014':
                            propor14 = 0
                        if ano == '2018':
                            propor18 = 0
                            tabela.append([uf, cargo, sigla, cor, propor14, propor18])


df = pd.DataFrame(tabela[1:], columns=cols)
df['Variaçao 14-18'] = (df['propor18'] - df['propor14']) / df['propor14']
df.to_csv('RESULTADOS/%CorespPartidopEleicao.csv')
