arquivo = open('dados.txt','a+')
arquivo.write('Victor\t')
arquivo.write('12\n')
arquivo.seek(0)

conteudo = arquivo.read()
print(conteudo)

arquivo.close

