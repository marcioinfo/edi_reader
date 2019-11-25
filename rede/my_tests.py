from rede import file_info
import csv
# Todo listar os arquivos do diretório(pode ser local, mas depois será do s3)
result = file_info('20191031-REDE-CFR13-1-1-VC-72932.txt')
tipo_02 = []
for each in result:
    codigo = each.get('tipo_registro')
# Todo criar lógica de mapeamento para tratar dos os tipos de registros
    if codigo == '012':
        tipo_02.append(each)
# Todo Gerar CSV para cada tipo de registros e enviar para o s3
keys = tipo_02[0].keys()
with open('test12.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(tipo_02)
print(tipo_02)
