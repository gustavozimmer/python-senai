# pandas:
# pandas é uma biblioteca construida sobre a biblioteca numpy
# usada para manipulaçã, limpeza e analise de grandes volumes de dados

# Principais funções
# read_csv() / read_excel(): Abre arquivos de diferentes formatos.
# head(): Mostra as primeiras 5 linhas da tabela para você entender o que tem ali.
# info(): Exibe um resumo técnico (quantas colunas, nomes e se há valores vazios).

# fillna(): Preenche buracos (dados que estão faltando) com um valor padrão ou a média.
# drop(): Remove colunas ou linhas que não são úteis para a sua análise.
# rename(): Troca nomes de colunas (ex: mudar "col1" para "Preço").

# describe(): Gera estatísticas rápidas (média, valor máximo, mínimo, etc.).
# groupby(): Agrupa os dados por uma categoria (ex: ver o total de vendas por "Região").
# sort_values(): Ordena a tabela por uma coluna específica.

# exemplo
import pandas as pd

vendas = {
    'Vendedor': ['Ana', 'Bruno', 'Ana', 'Carlos'],
    'Valor': [100, 200, 150, 300]
}
df = pd.DataFrame(vendas)
print("--- Primeiras linhas ---")
print(df.head(2))
faturamento = df.groupby('Vendedor').sum()
print("-- Faturamento por Vendedor --")
print(faturamento)

# requests
# É uma biblioteca para fazer requisições http com python
# Simplifica o jeito de interagir com APIs

# Principais funções
# requests.get(url): É a mais comum. Você a usa para pedir dados (como baixar o conteúdo de uma página ou um JSON).
# requests.post(url, data=...): Usada para enviar dados para o servidor (como criar um novo cadastro).
# requests.put() / requests.delete(): Usadas para atualizar ou remover informações existentes.

import requests

resposta = requests.get('https://viacep.com.br/ws/01001000/json/')
if resposta.status_code == 200:
    dados = resposta.json()
    print(f"Cidade: {dados['localidade']}")


# beautifulsoup4

# É uma biblioteca usada para extrair dados de arquivos HTML e XML
# É util pois economiza tempo de leitura de código até encontrar a parte desejada

# Principais funções
# find(): Encontra o primeiro item que corresponde ao critério (ex: o primeiro título <h1>).
# find_all(): Pega todos os itens de um tipo (ex: todos os links <a> da página).

# Exemplo
from bs4 import BeautifulSoup
sopa = BeautifulSoup("""<html>
  <body>
    <h1 class="titulo-principal">Produtos em Destaque</h1>
    <p>Confira nossas ofertas do dia:</p>
    <ul>
      <li class="item">Notebook - R$ 3500</li>
      <li class="item">Smartphone - R$ 1500</li>
    </ul>
    <a href="https://loja.com/contato">Fale conosco</a>
  </body>
</html>""", 'html.parser')
titulo = sopa.find('h1', class_='titulo-principal').text
print(f"O título é: {titulo}")
link = sopa.find('a')['href']
print(f"O link de contato é: {link}")
