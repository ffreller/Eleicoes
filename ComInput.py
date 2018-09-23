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
ano = '0'
uf = '0'
cargo = '0'
# while (cargo.upper() in df['DS_CARGO']) == False:
# sprj18 = pd.concat([sp18, sp14, sp10], ignore_index=True, sort=True)

def Inputs():
    while cargo not in ['DEPUTADO ESTADUAL', 'DEPUTADO FEDERAL', 'SENADOR', 'GOVERNADOR']:
        cargo = str(input('Cargo desdejado: ')).upper()

    while uf not in estados.keys():
        uf = input('Deseja saber os dados de qual Estado? Digite a sigla: ').upper()


    while ano != '2014' and ano != '2010' and ano != '2018':
        ano = input('Ano desejado (2010, 2014, 2018): ')

Inputs()
df = pd.read_csv(f'DADOS/consulta_cand_{ano}_{uf}.csv', sep=',', header=0, encoding='latin-1')
SelTurno = df.loc[df['NR_TURNO'] == 1]
SelCargo = SelTurno.loc[SelTurno['DS_CARGO'] == cargo]
SelMulheres = SelCargo.loc[SelCargo['DS_GENERO'] == 'FEMININO']
estado = estados[f'{uf}']

if len(SelMulheres) != 0:
    ntotal = len(SelCargo)
    nhomens = ntotal-len(SelMulheres)
    nmulheres = len(SelMulheres)
    print(f'{nmulheres} mulher(es) e {nhomens} concorreu(ram) a {cargo} no {estado}. Ela(s) representa(m) {nmulheres/ntotal*100:.2f}% dos candidatos nessa eleição')
else:
    print(f'Nenhuma mulher concorreu ao cargo de {cargo.lower().capitalize()} no estado do {estado} em {ano}')


