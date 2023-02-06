# Descrição do Projeto 🧑🏻‍💻🖱️

Projeto desenvolvido no módulo de ciência da computação na instituição 🖱️[Trybe](https://www.betrybe.com/), com o objetivo de raspar dados (_scraper_) de uma [página](https://blog.betrybe.com/) usando python e inserir no banco de dados (_mongodb_).


# Estrutura do projeto

Estrutura do projeto e descrição dos arquivos que foram desenvolvidos por mim e pela Trybe.

```
Legenda:
🔸Arquivos desenvolvidos pela Trybe (não foram alterados).
🔹Arquivos desenvolvidos por mim.
.
├── tech_news
│   ├── analyzer
│   │   ├── 🔹ratings.py
│   │   └── 🔹search_engine.py
│   ├── 🔸database.py
│   └── 🔹menu.py
│   └── 🔹scraper.py
├── tests
│   ├── 🔸assets/*
│   ├── 🔸__init__.py
│   ├── 🔸generate_fixture.py
│   ├── 🔸news.py
│   ├── 🔸test_menu.py
│   ├── 🔸test_ratings.py
│   ├── 🔸test_scraper.py
│   ├── 🔸test_search_engine.py
│   └── 🔸utils.py
├── 🔸dev-requirements.txt
├── 🔸docker-compose.yml
├── 🔸Dockerfile
├── 🔸pyproject.toml
├── 🔹README.md
├── 🔸requirements.txt
├── 🔸setup.cfg
├── 🔸setup.py
└── 🔸trybe.yml
```

# Tecnologias utilizado 🖱️
 
 > Desenvolvindo usando: [Python](https://www.python.org/), [Docker](https://www.docker.com/), [MongoDB](https://www.mongodb.com/pt-br), [Pymongo](https://pymongo.readthedocs.io/en/stable/)
 
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
 ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
 
  # Como rodar o projeto
 
1 - Clone o repositório
    
    git clone git@github.com:Ytellon/tech-news-python.git

2 - Crie ambiente virtual e instale as dependências

    cd tech-news/
    python3 -m venv .venv && source .venv/bin/activate
    python3 -m pip install -r dev-requirements.txt
    
3 - Rode o banco de dados via docker

    docker-compose up -d mongodb
    
# Como usar

1. Para inserir e listar uma quantidade de notícias.

-   Use o comando:
    ```
    python3 -i tech_news/scraper.py
    ```
-   Depois:
    ```
    get_tech_news(quantidade_de_news)
    ```
-   Retorno:
    ```python
    >>> get_tech_news(1)
    [
        {
            "url":"https://blog.betrybe.com/tecnologia/informatica-basica/",
            "title":"Informática básica: o que é e quais os 16 conceitos principais",
            "timestamp":"09/11/2022",
            "writer":"Lucas Custódio",
            "comments_count":0,
            "summary":"Os computadores dominaram o mundo. Por isso, é uma grande vantagem ter algum conhecimento em Informática básica, especialmente se você for da área de tecnologia.",
            "tags":[
                ],
                "category":"Tecnologia"
        }
    ]
    ```

2. Pesquisar notícias por título.

-   Use o comando:
    ```
    python3 -i tech_news/analyzer/search_engine.py
    ```
-   Depois:
    ```
    search_by_title("Informática")
    ```
-   Retorno - Uma lista com o título e o link para a notícia:
    ```python
    >>> search_by_title("Informática")
    [('Informática básica: o que é e quais os 16 conceitos principais', 'https://blog.betrybe.com/tecnologia/informatica-basica/')]
    ```

3. Pesquisar notícias por data.

-   Use o comando:
    ```
    python3 -i tech_news/analyzer/search_engine.py
    ```
-   Depois:
    ```
    search_by_date("2022-11-09")
    ```
-   Retorno - Uma lista com o título e o link para a notícia:
    ```python
    >>> search_by_date("2022-11-09")
    [('Informática básica: o que é e quais os 16 conceitos principais', 'https://blog.betrybe.com/tecnologia/informatica-basica/')]
    ```