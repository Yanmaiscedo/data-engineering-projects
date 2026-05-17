import os
import json
import requests
import boto3
from datetime import datetime

# --- Função de Ingestão de Dados da API ---
# Esta função é responsável por se comunicar com a API do TMDB.
def get_movies_by_genre_and_year(api_key, year, genre_ids):
    """
    Busca todos os filmes de um ano e gênero específicos, paginando a API.
    A paginação é crucial para APIs que limitam o número de resultados por requisição.
    """
    all_movies = []
    page = 1
    total_pages = 1  # Inicia com 1, o valor real será atualizado após a primeira requisição.

    # O loop 'while' garante que todas as páginas de resultados sejam coletadas.
    while page <= total_pages:
        # Constrói a URL completa para a requisição, incluindo a chave da API e os parâmetros de busca.
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&primary_release_year={year}&with_genres={','.join(map(str, genre_ids))}&page={page}"
        
        try:
            # Faz a requisição HTTP GET para a API.
            response = requests.get(url)
            # Levanta um erro se a requisição não for bem-sucedida (ex: 404, 500).
            response.raise_for_status()
            # Converte a resposta JSON em um dicionário Python.
            data = response.json()
            
            # Adiciona os filmes da página atual à lista principal.
            all_movies.extend(data['results'])
            
            # Atualiza o número total de páginas a serem processadas.
            if 'total_pages' in data:
                total_pages = data['total_pages']
            
            print(f"Página {page}/{total_pages} do ano {year} processada.")
            
            # Avança para a próxima página no loop.
            page += 1
            
        except requests.exceptions.RequestException as e:
            # Captura erros de requisição, como problemas de conexão ou HTTP.
            print(f"Erro na requisição à API do TMDB na página {page} para o ano {year}: {e}")
            break # Interrompe o loop em caso de erro para evitar falhas repetidas.
            
    return all_movies

# --- Função Principal da AWS Lambda ---
# Esta é a função de entrada que a AWS Lambda irá executar.
def lambda_handler(event, context):
    """
    Função principal que será executada pela AWS Lambda.
    'event' e 'context' são parâmetros padrão passados pela AWS.
    """
    # 1. Configura a API e o S3
    # Obtém a chave da API de uma variável de ambiente, uma prática de segurança recomendada.
    tmdb_api_key = os.environ.get('TMDB_API_KEY')
    
    # Define o nome do bucket S3 de destino.
    bucket_name = "bucket-name"  
    
    # Cria um cliente S3 para interagir com o serviço. O Boto3 usa as credenciais do IAM Role da Lambda.
    s3_client = boto3.client('s3')

    # Verifica se a chave da API foi configurada corretamente.
    if not tmdb_api_key:
        print("Erro: A variável de ambiente 'TMDB_API_KEY' não está configurada.")
        # Retorna uma resposta de erro para a Lambda.
        return {
            'statusCode': 500,
            'body': json.dumps('Configuração de ambiente ausente.')
        }

    # 2. Define os parâmetros de busca
    genre_ids_to_search = [18, 10749]  # ID do gênero Drama (18) e Romance (10749).
    years_to_search = [2023, 2024] # Anos de interesse para a busca.
    all_movie_data = []

    # 3. Coleta os dados de todos os anos
    # Itera sobre a lista de anos para buscar os filmes.
    for year in years_to_search:
        print(f"\nColetando filmes de drama/romance do ano: {year}...")
        movies_for_year = get_movies_by_genre_and_year(tmdb_api_key, year, genre_ids_to_search)
        all_movie_data.extend(movies_for_year)

    # Verifica se a lista de dados está vazia antes de tentar salvar.
    if not all_movie_data:
        print("Nenhum dado encontrado para salvar.")
        return {
            'statusCode': 204, # Código HTTP 204 significa "No Content".
            'body': json.dumps('Nenhum dado encontrado.')
        }

    # 4. Salva os dados no S3 com o caminho padronizado
    # Obtém a data e hora atuais para criar a estrutura de pastas no S3 (formato Data Lake).
    data_atual = datetime.now()
    ano, mes, dia = data_atual.strftime("%Y"), data_atual.strftime("%m"), data_atual.strftime("%d")
    
    # Constrói o caminho completo do arquivo no S3.
    # O caminho é: Raw/TMDB/JSON/Ano/Mês/Dia/NomeDoArquivo.json
    file_path = f"Raw/TMDB/JSON/{ano}/{mes}/{dia}/movies_drama_romance_{years_to_search[0]}_{years_to_search[-1]}_{data_atual.strftime('%Y-%m-%d_%H-%M-%S')}.json"
    
    try:
        # Usa o cliente S3 para fazer o upload do objeto (o arquivo JSON).
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_path,
            # Converte a lista de filmes em uma string JSON formatada.
            Body=json.dumps(all_movie_data, indent=2, ensure_ascii=False),
            ContentType='application/json' # Define o tipo de conteúdo do arquivo.
        )
        print(f"Busca concluída. Total de filmes encontrados: {len(all_movie_data)}")
        print(f"Dados salvos com sucesso em s3://{bucket_name}/{file_path}")
        
        # Retorna uma resposta de sucesso para a Lambda, indicando que a função terminou bem.
        return {
            'statusCode': 200,
            'body': json.dumps('Dados da API do TMDB salvos com sucesso!')
        }
    except Exception as e:
        # Captura qualquer outro erro que possa ocorrer durante a operação do S3.
        print(f"Erro ao salvar dados no S3: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Erro na ingestão: {str(e)}")
        }