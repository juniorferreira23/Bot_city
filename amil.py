import re

def extrair_dados_amil(arquivo: str) -> list[object]:
  """
  Função para encontrar os contratos e parcelas no arquivo (extratos amil).

  Args:
    arquivo: Nome do arquivo .txt.

  Returns:
    Uma lista de objetos com todos os contratos de parcelas encontrados.
  """
  
  lista_de_contratos = []
  try:
    with open(arquivo, 'r') as file:
      for linha in file:
        # Padrão para números de 8 dígitos exatamente entre hashtags
        padrao_contrato = r"#\d{8}#"
        # Padrão para números com hashtags no início e fim, e dois dígitos aleatórios no meio
        padrao_parcela = r"#\d{1,2}#\d{1,3}#\d+/"

        # Busca por ambos os padrões na linha
        matches_contrato = re.findall(padrao_contrato, linha)
        matches_parcela = re.findall(padrao_parcela, linha)
        # print(matches_exatos
        # print(matches_parciais)
        
        # Formatando dados capturados
        if matches_contrato:
          matches_contrato = matches_contrato[0].replace('#', '')
          # print(matches_exatos)
        if matches_parcela:
          matches_parcela = matches_parcela[0].split('#')
          matches_parcela = matches_parcela[1]
          # print(matches_parciais)

        # Adiciona os dados encontrados à lista
        dados = {
          'contrato': matches_contrato,
          'parcela': matches_parcela
        }
        
        if dados['contrato'] and dados['parcela'] and dados not in lista_de_contratos:
          lista_de_contratos.append(dados)
        # numeros_encontrados.extend(matches_exatos)
        # numeros_encontrados.extend(matches_parciais)
      
  except Exception as err:
    print(f'ERROR: Não foi possível ler o arquvio {arquivo} - {err}')
    

  for contrato in lista_de_contratos:
    print(contrato)
  print('Contratos extraídos com sucesso')
  print('Quantidade de contratos encontrados: ', len(lista_de_contratos))
    
  return lista_de_contratos

if __name__ == '__main__':
    extrair_dados_amil()