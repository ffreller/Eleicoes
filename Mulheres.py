import pandas as pd

# SEM PARITDO. MULHERES
tabela = [[]]
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
cols = ['ANO', 'UF', 'CARGO', 'HOMENS', 'MULHERES', 'TOTAL', 'DESPESAS', 'DESPESAS_MULHERES']

df1 = pd.read_pickle('DADOS/TODOS.pickle')
for uf in estados.keys():
    SelUf = df1.loc[df1['uf'] == uf]
    for ano in ['2010','2014', '2018']:
        SelAno = SelUf.loc[SelUf['ANO_ELEICAO'] == int(ano)]
        for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR']:
            if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
                cargo = 'DEPUTADO DISTRITAL'
            SelCargo = SelAno.loc[SelAno['DS_CARGO'] == cargo]
            mediadespesa = SelCargo['DESPESA_MAX_CAMPANHA'].mean() / 1000
            total = len(SelCargo)
            homens = len(SelCargo.loc[SelCargo['DS_GENERO'] == 'MASCULINO'])
            mulheres = len(SelCargo.loc[SelCargo['DS_GENERO'] == 'FEMININO'])
            mul = SelCargo.loc[SelCargo['DS_GENERO'] == 'FEMININO']
            mediadespesamul = mul['DESPESA_MAX_CAMPANHA'].mean()/1000
            tabela.append([ano, uf, cargo, homens, mulheres, total, mediadespesa, mediadespesamul])
            df = pd.DataFrame(tabela[1:], columns=cols)
            df['%MULHERES'] = df['MULHERES']/df['TOTAL']
            df['%HOMENS'] = df['HOMENS']/df['TOTAL']
            df['$DESPESA_MULHERES'] = df['DESPESA_MULHERES']/df['DESPESA']
            df.to_csv(f'RESULTADOS/EleicoespGenero_{cargo}.csv', encoding='latin-1')

# COM PARITDO. MULHERES
tabela = [[]]
cols = ['ANO', 'UF', 'CARGO', 'PARTIDO', 'HOMENS', 'MULHERES', 'TOTAL', 'DESPESAS', 'DESPESAS_MULHERES']
df1 = pd.read_pickle('DADOS/TODOS.pickle')
for uf in estados.keys():
    SelUf = df1.loc[df1['uf'] == uf]
    for ano in ['2010','2014', '2018']:
        SelAno = SelUf.loc[SelUf['ANO_ELEICAO'] == int(ano)]
        for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR']:
            if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
                cargo = 'DEPUTADO DISTRITAL'
            SelCargo = SelAno.loc[SelAno['DS_CARGO'] == cargo]
            sgpartidos = SelCargo['SG_PARTIDO'].unique()
            for sigla in sgpartidos:
                SelPart = SelCargo.loc[SelCargo['SG_PARTIDO'] == sigla]
                total = len(SelPart)
                mediadespesa = SelPart['DESPESA_MAX_CAMPANHA'].mean() / 1000
                homens = len(SelPart.loc[SelPart['DS_GENERO'] == 'MASCULINO'])
                mulheres = len(SelPart.loc[SelPart['DS_GENERO'] == 'FEMININO'])
                mul = SelPart.loc[SelPart['DS_GENERO'] == 'FEMININO']
                mediadespesamul = mul['DESPESA_MAX_CAMPANHA'].mean() / 1000
                tabela.append([ano, uf, cargo, sigla, homens, mulheres, total, mediadespesa, mediadespesamul])
            df = pd.DataFrame(tabela[1:], columns=cols)
            df['%MULHERES'] = df['MULHERES']/df['TOTAL']
            df['%HOMENS'] = df['HOMENS']/df['TOTAL']
            df.to_csv(f'RESULTADOS/EleicoespGeneropPartido_{cargo}.csv', encoding='latin-1')