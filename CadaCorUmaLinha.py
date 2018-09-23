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

cols = ['UF', 'ANO', 'CARGO', 'DS', 'COR', 'CANDIDATOS_COR', 'TOTAL']

#CADA COR TEM UMA LINHA EM CADA ELEICAO

for uf in estados.keys():
    for ano in ['2014','2018']:
        df = pd.read_pickle(f'DADOS/consulta_cand_{ano}_{uf}.pickle')
        for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR']:
            if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
                cargo = 'DEPUTADO DISTRITAL'
            SelCargo = df.loc[df['DS_CARGO'] == cargo]
            sgpartidos = SelCargo['SG_PARTIDO'].unique()
            for sigla in sgpartidos:
                SelPart = SelCargo.loc[SelCargo['SG_PARTIDO'] == sigla]
                if len(SelPart) != 0:
                    for cor in ['BRANCA', 'PRETA', 'PARDA', 'AMARELA', 'INDÍGENA']:
                        SelCor = SelPart.loc[SelCargo['DS_COR_RACA'] == cor]
                        candidatoscor = len(SelCor)
                        if candidatoscor != 0:
                            tabela.append([uf, ano, cargo, sigla, cor, candidatoscor, len(SelPart)])

df = pd.DataFrame(tabela[1:], columns=cols)
df['% do Total'] = df['CANDIDATOS_COR']/df['TOTAL']
df.to_csv('RESULTADOS/CadaCorUmaLinha.csv', encoding='latin-1')




