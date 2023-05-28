# N-Gram Viewer - bancos de dados em .txt

O projeto é parte de uma tese de doutorado em História, Pólítica e Bens Culturais, pela FGV-RJ. Inspirado no N-Gram Viewer do Google, construímos um visualizador de N-Gram que permite utilizar-se de um banco de dados em formato .txt, para construir gráficos de frequência ao longo de uma linha do tempo. O bando de dados que usamos como treinamento é composto por 211 teses e dissertações defendidas na Pós-Graduação em História, no Brasil, entre 1994-2022 e que versam sobre as dissidências sexuais e desobedidesobediências de gênero.

[Documentação de construção do dataset](./build_db/README.md)

## Estrutura do projeto
  ```bash
    ├── ./ # base do projeto contendo os arquivos de implementação do python
        └── build_db # possui o script de processamento de construção do dataset
        └── data # devemos colocar o dataeset gerado nessa pasta com o seguinte nome DataSet_.gzip
        └── static # são os arquivos estáticos para uso no front
        └── templates # possui o html onde mostramos os gráficos
  ```
## Requisitos

- Python 3.10 (versão específica usada no projeto)
- Flask (incluído no arquivo requirements.txt)

## Instalação

Aqui estão os passos para configurar o ambiente e executar o projeto em sua máquina:

1. **Python**: Verifique se você possui o Python 3.10 instalado. Caso contrário, siga as instruções de instalação adequadas para o seu sistema operacional:

- **Windows**: 

  - Acesse [python.org](https://www.python.org/downloads/windows/) e baixe o instalador do Python 3.10.
  - Execute o arquivo baixado e siga as instruções do instalador. Lembre-se de marcar a opção "Adicionar Python ao PATH" durante o processo de instalação.

- **Linux** (Debian/Ubuntu):

  - Abra o terminal e execute os seguintes comandos:

  ```bash
  sudo apt update
  sudo apt install python3.10
  ```

- **macOS** (Homebrew):

  - Abra o terminal e execute o seguinte comando:

  ```bash
  brew install python@3.10
  ```

2. **pip**: O pip3 é o gerenciador de pacotes padrão para o Python. Verifique se você tem o pip3 instalado seguindo as instruções abaixo:

- **Windows**: O Python 3.10 já deve ter o pip3 instalado por padrão. Verifique digitando o seguinte comando no Prompt de Comando:

  ```bash
  pip3 --version
  ```

- **Linux** (Debian/Ubuntu):

  - Abra o terminal e execute o seguinte comando:

  ```bash
  sudo apt update
  sudo apt install python3-pip
  ```

- **macOS** (Homebrew):

  - Abra o terminal e execute o seguinte comando:

  ```bash
  brew install pipenv
  ```

2. **Clonar o repositório**: Faça o clone deste repositório em seu ambiente local usando o seguinte comando:

```bash
git clone https://github.com/LucianoPedroso/N-gram_Viewer.git
```

3. **Ambiente virtual (opcional)**: É recomendável criar um ambiente virtual para isolar as dependências do projeto. Entre na pasta do projeto e execute os seguintes comandos:

```bash
cd N-gram_Viewer
python3 -m venv venv
```

4. **Ativar o ambiente virtual**: Agora, ative o ambiente virtual recém-criado. Dependendo do seu sistema operacional, o comando pode variar:

- No Windows:

```bash
venv\Scripts\activate.bat
```

- No Linux/macOS:

```bash
source venv/bin/activate
```

5. **Instalar as dependências**: Agora, instale as dependências do projeto utilizando o pip e o arquivo requirements.txt:

```bash
pip3 install -r requirements.txt
```

## Executando o Projeto

1. **Executar**: Agora você pode iniciar o projeto. Navegue para o diretório raiz do projeto e execute o seguinte comando:

Use a production WSGI server instead

```bash
python index.py
```

2. **Acessar o projeto**: Após executar o comando acima, você poderá acessar o projeto em seu navegador, digitando `http://localhost:5000` na barra de endereços.

## Contribuição

Se você quiser contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork deste repositório e clone-o em seu ambiente local.

2. Crie uma nova branch para suas alterações:

```bash
git checkout -b minha-nova-feature
```

3. Faça suas alterações e faça commit delas:

```bash
git commit -am "Adicionei uma nova feature"
```

4. Envie suas alterações para o repositório remoto:

```bash
git push origin minha-nova-feature
```

5. Envie uma Pull Request para que possamos revisar suas alterações e mesclá-las ao projeto principal.

## Licença

Licença MIT (ATUALIZAR)
