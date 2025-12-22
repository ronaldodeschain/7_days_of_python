# Projeto Personagens de Avatar - 7 Days of Code (Alura)

Este projeto foi desenvolvido como parte do desafio "7 Days of Code" da Alura, com o objetivo de aprofundar meus conhecimentos em Django, requisições de API, internacionalização e paginação.

## Visão Geral

O projeto consiste em uma aplicação web que exibe uma lista de personagens do universo de Avatar: A Lenda de Aang, consumindo dados de uma API pública. Os principais recursos incluem:

-   **Listagem de Personagens:** Exibe os nomes, afiliações e imagens dos personagens.
-   **Tradução:** Utiliza a biblioteca `googletrans` para traduzir automaticamente os nomes e afiliações dos personagens para português.
-   **Paginação:** Implementa paginação para facilitar a navegação entre grandes quantidades de personagens, utilizando o `Paginator` do Django.

## Tecnologias Utilizadas

-   **Django:** Framework web Python de alto nível.
-   **httpx:** Cliente HTTP assíncrono para fazer requisições à API.
-   **googletrans:** Biblioteca para tradução automática de texto.
-   **Bootstrap:** Framework CSS para estilização e responsividade.

## Como Executar o Projeto

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/ronaldodeschain/7_days_of_python.git
    ```

2.  **Crie um ambiente virtual:**

    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**

    -   No Windows:

        ```bash
        venv\Scripts\activate
        ```

    -   No macOS e Linux:

        ```bash
        source venv/bin/activate
        ```

4.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Aplique as migrações:**

    ```bash
    python manage.py migrate
    ```

6.  **Execute o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

7.  **Acesse o projeto no seu navegador:**

    ```
    http://localhost:8000/personagens/
    ```

## Observações

Este projeto foi criado para fins de estudo e demonstração. Sinta-se à vontade para explorar o código, fazer modificações e utilizá-lo como base para seus próprios projetos.
