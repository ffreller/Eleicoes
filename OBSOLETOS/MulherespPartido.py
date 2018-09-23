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

cols = ['UF', 'ANO', 'CARGO', 'SIGLA', 'MULHERES', 'TOTAL']

for uf in estados.keys():
    for ano in ['2010','2014','2018']:
        for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR']:
            if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
                cargo = 'DEPUTADO DISTRITAL'
            df = pd.read_csv(f'DADOS/consulta_cand_{ano}_{uf}.csv', sep=',', header=0, encoding='latin-1')
            sgpartidos = df['SG_PARTIDO'].unique()
            # print(df.head())
            # print(ano, cargo, uf)
            for sigla in sgpartidos:
                SelCargo = df.loc[df['DS_CARGO'] == cargo]
                SelPart = SelCargo.loc[SelCargo['SG_PARTIDO'] == sigla]
                ntotal = len(SelPart)
                if len(SelPart) != 0:
                    SelMul = SelPart.loc[SelPart['DS_GENERO'] == 'FEMININO']
                    nmulheres = len(SelMul)
                    tabela.append([uf, ano, cargo, sigla, nmulheres, ntotal])

df = pd.DataFrame(tabela[1:], columns=cols)
df['Proporcao de Mulheres'] = df['MULHERES']/df['TOTAL']
df.to_csv('RESULTADOS/%deMulherespPartido.csv')