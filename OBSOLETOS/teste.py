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
tm=False
propor = 0
tabela = [[]]
anos = ['2010', '2014', '2018']

# tabela.append[cols]

for cargo in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR', 'GOVERNADOR']:
    for uf in estados.keys():
        if uf == 'DF' and cargo == 'DEPUTADO ESTADUAL':
            cargo = 'DEPUTADO DISTRITAL'
        for ano in anos:
            df = pd.DataFrame()
            df = pd.read_csv(f'DADOS/consulta_cand_{ano}_{uf}.csv', sep=',', header=0, encoding='latin-1')
            if ano == '2018':
                b='GENERO'
            def ContarMulheres():
                global propor18
                global propor14
                global propor10
                SelCargo = df.loc[df[f'DS_CARGO'] == cargo]
                SelAno = SelCargo.loc[SelCargo['ANO_ELEICAO'] == int(ano)]
                SelMu = SelAno.loc[SelAno[f'DS_GENERO'] == 'FEMININO']
                mulheres = len(SelMu)
                homens = len(SelAno) - len(SelMu)
                if len(SelAno) != 0:
                    if ano == '2018':
                        propor18 = mulheres / len(SelAno)
                    if ano == '2014':
                        propor14 = mulheres / len(SelAno)
                    if ano == '2010':
                        propor10 = mulheres / len(SelAno)
                else:
                    if ano == '2010':
                        propor10 = 0
                    if ano == '2014':
                        propor14 = 0
                    if ano == '2018':
                        propor18 = 0
                if ano == '2018':
                    serie = [uf, cargo, propor10, propor14, propor18]
                    tabela.append(serie)
            ContarMulheres()


df = pd.DataFrame(tabela, columns=cols)

df['Variação 14-18'] = (df['propor18'] - df['propor14'])/df['propor14']
df['Variação 10-14'] = (df['propor14'] - df['propor10'])/df['propor10']
df['Variação 10-18'] = (df['propor18'] - df['propor10'])/df['propor10']

df.to_csv('RESULTADOS/MulheresPorAno.csv', encoding='latin-1')