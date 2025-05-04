# Como rodar o projeto (PRIMEIRA VEZ)

* Passo 1:
    * Rodar o comando no seu terminal:
    ```
        python -m venv venv

    ```
    PS: apos rodar, espere alguns segundos para criar a pasta.

    <br>
    Isso cria um ambiente virtual no seu projeto onde você possa instalar as biblotecas python necesárias.

    <br>
    <br>
* Passo 2:
    * Rodar o comando no seu terminal:
    ```
    #Se for Windows (CMD = Command Prompt)
        .\venv\Scripts\activate
    ```
    ```
    #Se for Linux (Bash)
        source venv/Scripts/activate
    ```

    Após rodar esse comando, você tera algo assim escrito no seu terminal
    <br>
    No Windows:
    (venv) C:\pasta\pasta\pasta\past>
    <br>
    No Linux:
    (venv) 
    usarior@Computador-FAJSH MINGW64 /pasta/pasta/pasta/past
    <br>

    Isso quer dizer que você acesso a venv
    <br>

* Passo 3:
    * Rodar o comando no seu terminal:
    ```
    pip install -r requirements.txt
    ```

    Vai instalar todas as biblotecas necessárias para o projeto, essa biblotecas estão listadas dentro do arquivo requirements.txt

    <br>

* Passo 4:
    * Rodar o comando no seu terminal:
    ```
    python manage.py makemigrations
    ```

    Cria as tabelas usando o ORM do django

    <br>

* Passo 5:
    * Rodar o comando no seu terminal:
    ```
    python manage.py migrate
    ```

    Aplica as tabelas usando o ORM do django, no banco de dados sqlite (Banco padrao do django, da para ser alterado)

    <br>

* Passo 6:
    * Rodar o comando no seu terminal:
    ```
    python manage.py runserver
    ```

    Inicia seu servidor, e você tem o acesso no link:

    http://localhost:8000

    <br>

    Apos essa primeira configuração, quando quiser ligar o teu projeto é só utilizar o:

    ```
    python manage.py runserver
    ```

    para inicia-lo novamente.