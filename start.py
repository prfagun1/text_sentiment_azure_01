import os
import json
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def analyze_sentiment(input_folder, output_folder, endpoint, key):
    # Inicialize o cliente para a análise de texto
    credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
    
    # Lista os arquivos na pasta de entrada
    files = os.listdir(input_folder)
    
    # Analisa cada arquivo de texto na pasta de entrada
    for file in files:
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file.split('.')[0] + '.json')
        
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Realiza a análise de sentimento
        result = text_analytics_client.analyze_sentiment(documents=[{"id": "1", "language": "pt", "text": text}])[0]
        
        # Salva o resultado em JSON na pasta de saída
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                "id": result.id,
                "sentiment": result.sentiment,
                "confidence_scores": {
                    "positive": result.confidence_scores.positive,
                    "neutral": result.confidence_scores.neutral,
                    "negative": result.confidence_scores.negative
                },
                "sentences": [{
                    "text": sentence.text,
                    "sentiment": sentence.sentiment,
                    "confidence_scores": {
                        "positive": sentence.confidence_scores.positive,
                        "neutral": sentence.confidence_scores.neutral,
                        "negative": sentence.confidence_scores.negative
                    }
                } for sentence in result.sentences]
            }, f, ensure_ascii=False, indent=4)

# Parâmetros de configuração
input_folder = 'input'
output_folder = 'output'

key = os.environ.get('SUBSCRIPTION_KEY')
endpoint = os.environ.get('ENDPOINT')


# Chama a função para análise de sentimento
analyze_sentiment(input_folder, output_folder, endpoint, key)
