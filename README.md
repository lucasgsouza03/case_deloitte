# Case Deloitte
## Installation / Usage

#### Dependências
* Para execução do projeto é necessário a instalação dos seguintes programas:
    * Docker
    * Docker-Compose

#### Executando o sistema em seu localhost
* Efetue o clone da aplicação na sua maquina:
    ```
    $ git clone git@github.com:lucasgsouza03/case_deloitte.git
    ```
* Inicie o container da aplicação com docker-compose:

    ```
    $ cd $path-to-project
    ```
* Faça uma copia do arquivo '.env.example' renomeando para '.env'

* Execute o build do container com o comando abaixo:

    ```
    $ docker-compose up --build -d
    ```

* Execute o script de inicialização da base de dados no container

    ```
    $ docker exec -t -i web bash
    $ ./migration.sh
    $ exit
    ```

#### Executando tests
    ```
    $ python manage.py test
    ```
#### Endpoints

* Base url:
    
        http://localhost:8000/
        http://127.0.0.1:8000/
    
* Endpoints disploniveis nas paginas de swagger da API:
    * $url-to-api/swagger/ - GET
    * $url-to-api/ - GET

* O sistema já vem com dados pré-cadastrados
    * Para utilização do sistema tera caradastro o usuário abaixo:
    ```
    email = admin@email.com
    password = admin
    ```