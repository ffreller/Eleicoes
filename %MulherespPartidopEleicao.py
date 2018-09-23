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
cols = ['UF', 'CARGO', 'SG_PARTIDO', 'propor10', 'propor14', 'propor18']
propor10 = 0
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
            for ano in ['2010', '2014', '2018']:
                SelAno = SelPart.loc[SelPart['ANO_ELEICAO'] == int(ano)]
                if len(SelAno) != 0:
                    SelMu = SelAno.loc[SelAno['DS_GENERO'] == 'FEMININO']
                    if ano == '2010':
                        propor10 = len(SelMu) / len(SelAno)
                    if ano == '2014':
                        propor14 = len(SelMu) / len(SelAno)
                    if ano == '2018':
                        propor18 = len(SelMu) / len(SelAno)
                        tabela.append([uf, cargo, sigla, propor10, propor14, propor18])


df = pd.DataFrame(tabela[1:], columns=cols)
df['Variaçao 14-18'] = (df['propor18'] - df['propor14']) / df['propor14']
df['Variaçao 10-14'] = (df['propor14'] - df['propor10']) / df['propor10']
df['Variaçao 10-18'] = (df['propor18'] - df['propor10']) / df['propor10']
df.to_csv('RESULTADOS/%MulherespPartidopEleicao.csv')

# def PegarSiglas(uf, ano, cargo):
#     df1 = pd.read_csv(f'DADOS/consulta_cand_{ano}_{uf}.csv', sep=',', header=0, encoding='latin-1')
#     if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
#         cargo = 'DEPUTADO DISTRITAL'
#     SelCargo = df1.loc[df1['DS_CARGO'] == cargo]
#     sgpartidos = SelCargo['SG_PARTIDO'].unique()
#     sgs = [[]]
#     for sg in sgpartidos:
#         sgs.append(sg)
#     return sgs
