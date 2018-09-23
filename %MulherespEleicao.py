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
cargo = 'abcddeee'
df = pd.DataFrame()
cols = ['uf', 'cargo', 'propor10', 'propor14', 'propor18']
propor10 = 0
propor14 = 0
propor18 = 0
tabela = [[]]
anos = ['2010', '2014', '2018']

df = pd.read_pickle('DADOS/TODOS.pickle')
for uf in estados.keys():
    SelUf = df.loc[df['uf'] == uf]
    for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR']:
        if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
            cargo = 'DEPUTADO DISTRITAL'
        SelCargo = SelUf.loc[SelUf[f'DS_CARGO'] == cargo]
        for ano in anos:
            SelAno = SelCargo.loc[SelCargo['ANO_ELEICAO'] == int(ano)]
            SelMu = SelAno.loc[SelAno['DS_GENERO'] == 'FEMININO']
            mulheres = len(SelMu)
            if ano == '2010':
                propor10 = mulheres / len(SelAno)
            if ano == '2014':
                propor14 = mulheres / len(SelAno)
            if ano == '2018':
                propor18 = mulheres / len(SelAno)
                tabela.append([uf, cargo, propor10, propor14, propor18])

df = pd.DataFrame(tabela[1:], columns=cols)

df['Variação 14-18'] = (df['propor18'] - df['propor14'])/df['propor14']
df['Variação 10-14'] = (df['propor14'] - df['propor10'])/df['propor10']
df['Variação 10-18'] = (df['propor18'] - df['propor10'])/df['propor10']

df.to_csv('RESULTADOS/%MulherespEleicao.csv',encoding='latin-1')