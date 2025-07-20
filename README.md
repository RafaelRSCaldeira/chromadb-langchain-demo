# PDF Semantic Search with LangChain, OpenAI & ChromaDB

Este projeto realiza **ingestão e busca semântica em documentos PDF** utilizando LangChain, OpenAI Embeddings e o banco vetorial **ChromaDB**.

## 🧠 Tecnologias Utilizadas

* [LangChain](https://www.langchain.com/)
* [OpenAI API](https://platform.openai.com/)
* [ChromaDB](https://www.trychroma.com/)
* [dotenv](https://pypi.org/project/python-dotenv/) para gerenciamento de variáveis de ambiente

## ⚙️ Requisitos

* Python 3.8+
* Uma conta e chave de API da OpenAI

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual e ative:

```bash
python -m venv venv
source venv/bin/activate  # ou `venv\Scripts\activate` no Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` com sua chave da OpenAI:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

5. Coloque seu arquivo PDF na pasta `./assets` com o nome `document.pdf`.

## ▶️ Como executar

Execute o script principal:

```bash
python app.py
```

## 🔍 O que o código faz

1. **Carregamento do PDF**
   Usa o `PyPDFLoader` para carregar e dividir o PDF em partes (chunks).

2. **Inicialização do modelo**

   * Cria o modelo de linguagem com `ChatOpenAI` (usando `gpt-3.5-turbo`).
   * Cria embeddings com `OpenAIEmbeddings`.

3. **Criação da coleção no ChromaDB**
   Instancia um cliente local ChromaDB e cria uma coleção chamada `demo_collection`.

4. **Adição de documentos**
   Os chunks do PDF são adicionados à coleção como vetores.

5. **Consulta semântica**
   Uma consulta textual é feita, e o ChromaDB retorna os chunks mais semelhantes semanticamente com base nos embeddings.

## 📤 Exemplo de saída

```
{'ids': [['id1']], 'documents': [[...]]}
```

## 📝 Notas

* O projeto atualmente armazena apenas um documento (`id1`) por vez. Para adicionar múltiplos documentos, adapte a lógica do `collection.add()` com IDs únicos.
* ChromaDB nesta implementação está rodando localmente (in-memory). Para persistência ou uso em produção, consulte a [documentação oficial](https://docs.trychroma.com/).

## 📚 Fontes recomendadas

* [LangChain Docs](https://docs.langchain.com/)
* [ChromaDB GitHub](https://github.com/chroma-core/chroma)
* [ChromaDB Docs](https://docs.trychroma.com/docs/overview/getting-started)
* [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
