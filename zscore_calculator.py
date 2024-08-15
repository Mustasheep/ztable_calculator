from scipy.stats import norm

def zscore_para_probabilidade(zscore):
  """
  Calcula a probabilidade acumulada para um determinado z-score usando scipy.stats.

  Args:
    zscore: O valor do z-score.

  Returns:
    A probabilidade acumulada correspondente ao z-score.
  """
  probabilidade = norm.cdf(zscore)
  return probabilidade

if __name__ == "__main__":
  while True:
    try:
      valor_str = input("Digite o Z Score, deve estar entre -4 e 4 (ou 'sair' para encerrar): ")
      if valor_str.lower() == 'sair':
        break

      # Substitui vírgula por ponto antes da conversão
      valor_str = valor_str.replace(",", ".")  
      valor_float = float(valor_str)

      if -4 <= valor_float <= 4:
        probabilidade = zscore_para_probabilidade(valor_float)
        print(f"Z Score: {valor_float:.5f}  |  Probabilidade: {probabilidade:.5f}") 
      else:
        print("O Z Score deve estar entre -4 e 4.")

    except ValueError as e:
      print(f"Erro: {e}")
