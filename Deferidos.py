import pandas as pd
import matplotlib as plt


df = pd.read_pickle('DADOS/TODOS.pickle')
tabela=[[]]


for ano in ['2006','2010','2014', '2018']:
    SelAno = df.loc[df['ANO_ELEICAO'] == int(ano)]
    for uf in df['uf'].unique():
        SelUf = SelAno.loc[SelAno['uf'] == uf]
        for cargo in ['DEPUTADO ESTADUAL','DEPUTADO FEDERAL']:
            if cargo == 'DEPUTADO ESTADUAL' and uf == 'DF':
                cargo = 'DEPUTADO DISTRITAL'
            SelCargo = SelUf.loc[SelUf['DS_CARGO'] == cargo]
            sgpartidos = SelCargo['SG_PARTIDO'].unique()
            SelHo = SelCargo.loc[SelCargo['DS_GENERO'] == 'MASCULINO']
            SelMu = SelCargo.loc[SelCargo['DS_GENERO'] == 'FEMININO']
            pmu = len(SelMu)/len(SelCargo)
            deferidoh = SelHo.loc[SelHo['DS_DETALHE_SITUACAO_CAND'] == 'DEFERIDO']
            if ano == '2018':
                print(len(SelHo))
                print(len(deferidoh))
            deferidom = SelMu.loc[SelMu['DS_DETALHE_SITUACAO_CAND'] == 'DEFERIDO']
            pdeferidoh = len(deferidoh) / len(SelHo)
            if len(SelMu) != 0:
                pdeferidom = len(deferidom) / len(SelMu)
            else:
                pdeferidom = 0
            tabela.append([ano, uf, cargo, len(SelHo), len(SelMu), pmu, len(deferidoh), len(deferidom), pdeferidoh, pdeferidom])


df = pd.DataFrame(tabela[1:], columns=['ANO', 'UF', 'CARGO', 'QTD_HOMENS', 'QTD_MULHERES','p_MULHERES', 'DEFERIDOS_HOMENS', 'DEFERIDO_MULHERES',
                                       'p_DEFERIDOS_ENTRE_HOMENS', 'p_DEFERIDOS_ENTRE_MULHERES'])

df.to_csv('RESULTADOS/deferidos.csv', encoding='latin-1')
print(df['p_MULHERES'].groupby(df['ANO']).mean())
print(df['p_DEFERIDOS_ENTRE_MULHERES'].groupby(df['ANO']).mean())
col = df.ANO.map({'2018':'g','2014':'b', '2010':'r', '2006':'y'})
a = df.plot.scatter(x='p_MULHERES', y='p_DEFERIDOS_ENTRE_MULHERES', c=col)
plt.pyplot.show(a)


