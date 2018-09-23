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
# SEM PARTIDO. MULHERES E COR
cols = ['ANO', 'UF', 'CARGO', 'TOTAL', 'MULHERES', 'PARDOS', 'BRANCOS', 'PRETOS', 'AMARELOS', 'INDÍGENAS',
        'MULHERES_PARDAS', 'MULHERES_BRANCAS', 'MULHERES_PRETAS', 'MULHERES_AMARELAS', 'MULHERES_INDÍGENAS']
df1 = pd.read_pickle('DADOS/TODOS.pickle')
for ano in [ '2014', '2018']:
    SelAno = df1.loc[df1['ANO_ELEICAO'] == int(ano)]
    for uf in estados.keys():
        SelUf = SelAno.loc[SelAno['uf'] == uf]
        for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR']:
            if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
                cargo = 'DEPUTADO DISTRITAL'
            SelCargo = SelUf.loc[SelUf['DS_CARGO'] == cargo]
            mulheres = SelCargo.loc[SelCargo['DS_GENERO'] == 'FEMININO']
            parda = SelCargo.loc[SelCargo['DS_COR_RACA'] == 'PARDA']
            pardamu = parda.loc[parda['DS_GENERO'] == 'FEMININO']
            branca = SelCargo.loc[SelCargo['DS_COR_RACA'] == 'BRANCA']
            brancamu = branca.loc[branca['DS_GENERO'] == 'FEMININO']
            preta = SelCargo.loc[SelCargo['DS_COR_RACA'] == 'PRETA']
            pretamu = preta.loc[preta['DS_GENERO'] == 'FEMININO']
            amarela = SelCargo.loc[SelCargo['DS_COR_RACA'] == 'AMARELA']
            amarelamu = amarela.loc[amarela['DS_GENERO'] == 'FEMININO']
            indigena = SelCargo.loc[SelCargo['DS_COR_RACA'] == 'INDÍGENA']
            indigenamu = indigena.loc[indigena['DS_GENERO'] == 'FEMININO']
            tabela.append([ano, uf, cargo, len(SelCargo), len(mulheres), len(parda), len(branca),
                           len(preta), len(amarela), len(indigena), len(pardamu), len(brancamu),
                           len(pretamu), len(amarelamu), len(indigenamu)])
            df = pd.DataFrame(tabela[1:], columns=cols)
            df['%MULHERES'] = df['MULHERES'] / df['TOTAL']
            df['%PARDOS'] = df['PARDOS'] / df['TOTAL']
            df['%MULHERES ENTRE PARDOS'] = df['MULHERES PARDAS'] / df['PARDOS']
            df['%BRANCOS'] = df['BRANCOS'] / df['TOTAL']
            df['%MULHERES ENTRE BRANCOS'] = df['MULHERES BRANCAS'] / df['BRANCOS']
            df['%PRETOS'] = df['PRETOS'] / df['TOTAL']
            df['%MULHERES ENTRE PRETOS'] = df['MULHERES PRETAS'] / df['PRETOS']
            df['%AMARELOS'] = df['AMARELOS'] / df['TOTAL']
            df['%MULHERES ENTRE AMARELOS'] = df['MULHERES AMARELAS'] / df['AMARELOS']
            df['%INDÍGENAS'] = df['INDÍGENAS'] / df['TOTAL']
            df['%MULHERES ENTRE INDÍGENAS'] = df['MULHERES INDÍGENAS'] / df['INDÍGENAS']
            df.to_csv(f'RESULTADOS/EleicoespGeneropCor_{cargo}.csv', encoding='latin-1')


#PARTIDO, MULHERES E COR
tabela = [[]]
cols = ['ANO', 'UF', 'CARGO', 'SIGLA', 'TOTAL', 'MULHERES', 'PARDOS', 'BRANCOS', 'PRETOS', 'AMARELOS', 'INDÍGENAS',
        'MULHERES PARDAS', 'MULHERES BRANCAS', 'MULHERES PRETAS', 'MULHERES AMARELAS', 'MULHERES INDÍGENAS']
df1 = pd.read_pickle('DADOS/TODOS.pickle')
for ano in ['2014', '2018']:
    SelAno = df1.loc[df1['ANO_ELEICAO'] == int(ano)]
    for uf in estados.keys():
        SelUf = SelAno.loc[SelAno['uf'] == uf]
        for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR']:
            if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
                cargo = 'DEPUTADO DISTRITAL'
            SelCargo = SelUf.loc[SelUf['DS_CARGO'] == cargo]
            for sigla in SelCargo['SG_PARTIDO'].unique():
                SelPart = SelCargo.loc[SelCargo['SG_PARTIDO'] == sigla]
                mulheres = SelPart.loc[SelPart['DS_GENERO'] == 'FEMININO']
                parda = SelPart.loc[SelPart['DS_COR_RACA'] == 'PARDA']
                pardamu = parda.loc[parda['DS_GENERO'] == 'FEMININO']
                branca = SelPart.loc[SelPart['DS_COR_RACA'] == 'BRANCA']
                brancamu = branca.loc[branca['DS_GENERO'] == 'FEMININO']
                preta = SelPart.loc[SelPart['DS_COR_RACA'] == 'PRETA']
                pretamu = preta.loc[preta['DS_GENERO'] == 'FEMININO']
                amarela = SelPart.loc[SelPart['DS_COR_RACA'] == 'AMARELA']
                amarelamu = amarela.loc[amarela['DS_GENERO'] == 'FEMININO']
                indigena = SelPart.loc[SelPart['DS_COR_RACA'] == 'INDÍGENA']
                indigenamu = indigena.loc[indigena['DS_GENERO'] == 'FEMININO']
                tabela.append([ano, uf, cargo, sigla, len(SelPart), len(mulheres), len(parda), len(branca),
                           len(preta), len(amarela), len(indigena), len(pardamu), len(brancamu),
                           len(pretamu), len(amarelamu), len(indigenamu)])
            df = pd.DataFrame(tabela[1:], columns=cols)
            df['%MULHERES'] = df['MULHERES'] / df['TOTAL']
            df['%PARDOS'] = df['PARDOS'] / df['TOTAL']
            df['%MULHERES ENTRE PARDOS'] = df['MULHERES PARDAS'] / df['PARDOS']
            df['%BRANCOS'] = df['BRANCOS'] / df['TOTAL']
            df['%MULHERES ENTRE BRANCOS'] = df['MULHERES BRANCAS'] / df['BRANCOS']
            df['%PRETOS'] = df['PRETOS'] / df['TOTAL']
            df['%MULHERES ENTRE PRETOS'] = df['MULHERES PRETAS'] / df['PRETOS']
            df['%AMARELOS'] = df['AMARELOS'] / df['TOTAL']
            df['%MULHERES ENTRE AMARELOS'] = df['MULHERES AMARELAS'] / df['AMARELOS']
            df['%INDÍGENAS'] = df['INDÍGENAS'] / df['TOTAL']
            df['%MULHERES ENTRE INDÍGENAS'] = df['MULHERES INDÍGENAS'] / df['INDÍGENAS']
            df.to_csv(f'RESULTADOS/EleicoespGeneropCorpPartido_{cargo}.csv', encoding='latin-1')







