# Documentação Script Construção Data Set

O Script do arquivo jupyter notebook Script_construcao foi elaborado, para poder extrair os documentos .txt e restrutura-los para que no final se tenha um data set informando o texto/teses , o ano de publicação e o autor responsável. Para que isso o script se divide em xxxx Etapas, onde

### 1º Etapa - Import Bibliotecas

Nessa etapa foi importado todas bibliotecas necessarias para realização da tarefe. Entre as principais, estão numpy, pandas, nltk e spacy

### 2º Etapa - Extração dos arquivos

Para ocorrer essa etapa é importante que um inicialmente seja realizado o download de todos os arquivos .txt e salva-los com formato .zip. Na sequencia renome o arquivo como Arquivos_DataSet.zip

### 3º Etapa - Estruturando Conjunto de dados

Após a leitura dos arquivos foi utilizado a biblioteca pandas para poder estrutura um data set, contendo as seguintes colunas: texto , autor e ano .

### 4º Etapa -  Identificando Entidades de Localização nos textos

Nessa etapa foi utilizado tecnicas de localização de entidades para podemos identificar palavras compostas que representam localização, como por exemplo: São Paulo e Rio de Janeiro. Essa forma essas palavras foram identificadas e não foram aplicadas técnicas de tokenização e lematização.

### 5º Lematização das palavras

Apos a identificação de entidades, foi aplicado processo de lematização nas palavras, com exceção palavras que foram identificadas na etapa anterior 

### 6º Remoção de stop word

Essa etapa foi realizada a remoção de stop word.

### 7º Salvar Conjunto de dados

No final desse processo inteiro é salvo o arquivo no nome: DataSet_.gzip , onde esse arquivo vai ser utilizado no front end para criar a visualização.
