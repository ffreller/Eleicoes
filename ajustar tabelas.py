import pandas as pd

def AjustarTabelas():

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
    for uf in estados.keys():
        for ano in ['2006','2010', '2014','2018']:
            # colunas = [[]]
            if ano == '2018':
                df = pd.read_csv(f'DADOS_CRUS/consulta_cand_2018_{uf}.csv', sep=';', header=0, encoding='latin-1')
                df.to_pickle(f'DADOS/consulta_cand_2018_{uf}.pickle')
            if ano == '2014':
                df = pd.read_csv(f'DADOS_CRUS/consulta_cand_2014_{uf}.txt', sep=';', header=0, encoding='latin-1')
                df.columns = ['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'NR_TURNO', 'DS_ELEICAO',
                              'SG_UF', 'SG_UE ', 'DS_UE', 'CD_CARGO', 'DS_CARGO', 'NM_CANDIDATO',
                              'SQ_CANDIDATO', 'NR_CANDIDATO', 'CPF_CANDIDATO','NM_URNA_CANDIDATO',
                              'COD_SITUACAO_CAND', 'DS_DETALHE_SITUACAO_CAND','NR_PARTIDO',
                              'SG_PARTIDO', 'NM_PARTIDO', 'CD_LEGENDA', 'SG_LEGENDA', 'COMPOSICAO_LEGENDA',
                              'NM_LEGENDA', 'CD_OCUPACAO', 'DS_OCUPACAO', 'DT_NASCIMENTO',
                              'NUM_TITULO_ELEITORAL_CANDIDATO', 'IDADE_DT_ELEICAO', 'CD_GENERO', 'DS_GENERO',
                              'COD_GRAU_INSTRUCAO', 'DS_GRAU_INSTRUCAO', 'CD_ESTADO_CIVIL',
                              'DS_ESTADO_CIVIL', 'CD_COR_RACA', 'DS_COR_RACA', 'CD_NACIONALIDADE',
                              'DS_NACIONALIDADE', 'SG_UF_NASCIMENTO', 'CD_MUNICIPIO_NASCIMENTO',
                              'NM_MUNICIPIO_NASCIMENTO', 'DESPESA_MAX_CAMPANHA', 'COD_SIT_TOT_TURNO',
                              'DS_SIT_TOT_TURNO',
                              'NM_EMAIL']
                df.to_pickle(f'DADOS/consulta_cand_2014_{uf}.pickle')
            if ano == '2010':
                df = pd.read_csv(f'DADOS_CRUS/consulta_cand_2010_{uf}.txt', sep=';', header=0, encoding='latin-1')
                df.columns = ['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'NR_TURNO',
                              'DS_ELEICAO','SG_UF', 'SG_UE', 'DS_UE', 'CD_CARGO', 'DS_CARGO',
                              'NM_CANDIDATO', 'SQ_CANDIDATO', 'NR_CANDIDATO', 'CPF_CANDIDATO',
                              'NM_URNA_CANDIDATO', 'COD_SITUACAO_CAND', 'DS_DETALHE_SITUACAO_CAND','NR_PARTIDO',
                              'SG_PARTIDO', 'NM_PARTIDO', 'CD_LEGENDA', 'SG_LEGENDA','COMPOSICAO_LEGENDA',
                              'NM_LEGENDA', 'CD_OCUPACAO', 'DS_OCUPACAO', 'DT_NASCIMENTO',
                              'NUM_TITULO_ELEITORAL_', 'IDADE_DT_ELEICAO', 'CD_GENERO', 'DS_GENERO',
                              'COD_GRAU_INSTRUCAO', 'DS_GRAU_INSTRUCAO', 'CD_ESTADO_CIVIL','DS_ESTADO_',
                              'CD_NACIONALIDADE', 'DS_NACIONALIDADE', 'SG_UF_NASCIMENTO','CD_MUNICIPIO_',
                              'NM_MUNICIPIO_NASCIMENTO', 'DESPESA_MAX_CAMPANHA', 'COD_SIT_TOT_TURNO','DS_SIT_TOT_TURNO']
                df.to_pickle(f'DADOS/consulta_cand_2010_{uf}.pickle')
            if ano == '2006':
                df = pd.read_csv(f'DADOS_CRUS/consulta_cand_2006_{uf}.txt', sep=';', header=0, encoding='latin-1')
                df.columns = ['DT_GERACAO', 'HORA_GERACAO','ANO_ELEICAO','NR_TURNO', 'DS_ELEICAO ','SG_UF','SG_UE',
                              'DS_UE','CD_CARGO','DS_CARGO', 'NM_CANDIDATO', 'SEQUENCIAL_CANDIDATO',
                              'NR_CANDIDATO', 'CPF_CANDIDATO', 'NM_URNA_CANDIDATO','COD_SITUACAO_CAND','DS_DETALHE_SITUACAO_CAND',
                              'NR_PARTIDO','SG_PARTIDO','NM_PARTIDO','CD_LEGENDA','SG_LEGENDA','COMPOSICAO_LEGEN',
                              'NM_LEGENDA','CD_OCUPACAO', 'DS_OCUPACAO','DT_NASCIMENTO','NUM_TITULO_ELEITOR',
                              'IDADE_DT_ELEICAO','CD_GENERO','DS_GENERO','COD_GRAU_INSTRUCAO','DS_GRAU_INSTRUCAO',
                              'CD_ESTADO_CIVIL','DS_ESTADO_CIVIL','CD_NACIONALIDE','DS_NACIONALIDADE','SG_UF_NASCIMENTO',
                              'CD_MUNICIPIO_NASCIMENTO','NM_MUNICIPIO_NASCIMENTO','DESPESA_MAX_CAMPANHA','COD_SIT_TOT_TURNO','DS_SIT_TOT_TURNO']
                df.to_pickle(f'DADOS/consulta_cand_2006_{uf}.pickle')

AjustarTabelas()

def UmaTabelaSo():
    # CRIAR UMA TABELAS SÓ COM OS SEGUINTES DADOS: 'ANO_ELEICAO', 'uf', 'DESPESA_MAX_CAMPANHA', 'DS_COR_RACA', 'DS_GENERO', 'DS_CARGO', 'SG_PARTIDO', 'NM_PARTIDO'
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
    for uf in estados.keys():
        for ano in ['2006','2010', '2014', '2018']:
            if uf == 'AC' and ano == '2006':
                df = pd.read_pickle(f'DADOS/consulta_cand_{ano}_{uf}.pickle')
                df['uf'] = uf
            else:
                df1 = pd.read_pickle(f'DADOS/consulta_cand_{ano}_{uf}.pickle')
                df1['uf'] = uf
                df = df.append(df1, sort=True)
    nv = df[['ANO_ELEICAO', 'uf', 'DESPESA_MAX_CAMPANHA', 'DS_COR_RACA', 'DS_GENERO',
             'DS_CARGO', 'SG_PARTIDO', 'NM_PARTIDO', 'DS_DETALHE_SITUACAO_CAND', 'DS_SIT_TOT_TURNO']]
    nv.to_pickle('DADOS/TODOS.pickle')

UmaTabelaSo()



#soluçao antiga, depois de if ano == 2018
# df = pd.read_csv(f'DADOS1/consulta_cand_2018_{uf}.csv', sep=';', header=0, encoding='latin-1')
# colunaso = df.columns
# for cont in range(1, 58):
#     coluna = colunaso[cont]
#     # print(coluna)
#     if 'GENERO' in coluna:
#         co = f'{coluna[:3]}SEXO'
#         coluna = co
#     if 'DS' in coluna:
#         co = f'DESCRICAO{coluna[2:]}'
#     if 'SG' in coluna:
#         co = f'SIGLA{coluna[2:]}'
#     if 'NM' in coluna:
#         co = f'NOME{coluna[2:]}'
#     colunas.append(co)
# df.columns = colunas
# # df.to_pickle(f'DADOS1/consulta_cand_2018_{uf}.pickle', encoding='latin-1')
# df.to_pickle(f'DADOS1/consulta_cand_2018_{uf}.csv', encoding='latin-1')