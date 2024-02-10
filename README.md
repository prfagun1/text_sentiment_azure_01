# Guia de Uso do Processo de reconhecimento de emoções em texto

Este é um guia para utilizar o script de detecção sentimentos em texto usando recursos da Azure.

## Descrição do Processo

O processo envolve as seguintes etapas:

1. **Preparação do Ambiente:**
   - Certifique-se de ter uma chave de assinatura válida e o URL da API do Azure.

2. **Configuração das Variáveis de Ambiente:**
   - Antes de executar o processo, você precisa configurar duas variáveis de ambiente:
     - `ENDPOINT`: O URL da API.
     - `KEY`: Sua chave de assinatura do Azure.

3. **Execução do Processo:**
   - Execute o script fornecido para realizar a detecção de sentimento em textos.

4. **Análise dos Resultados:**
   - Os resultados da detecção de faces serão salvos em arquivos JSON na pasta de saída especificada.

## Configuração das Variáveis de Ambiente

Para configurar as variáveis de ambiente no seu sistema:

### No Windows:

Abra o Prompt de Comando e execute os seguintes comandos, substituindo `sua_url_aqui` pelo URL da API do Azure e `sua_chave_aqui` pela chave de assinatura correspondente:

```cmd
set ENDPOINT=sua_url_aqui
set KEY=sua_chave_aqui
```

### No Linux:

Abra o terminal e execute os seguintes comandos, substituindo sua_url_aqui pelo URL da API do Azure e sua_chave_aqui pela chave de assinatura correspondente:
```
export ENDPOINT=sua_url_aqui
export KEY=sua_chave_aqui
```

5. **Instale os pré-requisitos**
```
pip install -r requirements.txt
```


