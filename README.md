# Trabalhos da disciplina Projeto e Análise de Algoritmos DIM0605

## Configurando o ambiente
Para a execução do algoritmo, é necessário instalar o pandas presente no arquivo requirement.txt. A heurística desenvolvida
não utiliza pacotes de terceiros para sua execução e suas estruturas de dados utilizadas na heurística foram criadas pelos próprios
alunos ou pelo próprio python. Utilizamos a biblioteca pandas com o intuito de facilitar o tratamento de dados
e a leitura do arquivo de instância do problema. Para fazer a instalação do pandas para a execução do projeto
rode o seguinte comando

```bash
$ pip install -r requirement.txt
```

## Arquitetura do projeto
data/data/ -> Contém os valores das instancias dos problemas. Elas estão separadas entre as pastas j30, j60, j90 e j120 onde a pasta indica quantas tarefas as instâncias da pasta vão possuir.

requirement.txt -> Requisitos do python

main.py -> Ponto de inicio do algoritmo, recebe parâmetros

run_and_write.sh -> Script para rodar instancias do algoritmo e armazenar os resultados ex. entrada: "3_6"

src/ -> Codigo fonte onde:
- noh.py -> Classe que define um No
- read_data_convert_dataframe.py -> Lê arquivos do sistema para receber os parametros do problema
- greedy_randomized_procedure.py -> onde o algoritmo esta definido

## Rodando o algoritmo
O algoritmo deve ser iniciado pelo arquivo main.py onde recebe dois possiveis parametros: 
- --file -> Caminho para o arquivo contendo os parametros do problema. Caso não seja informado, o valor default é o "data/data/j30/j301_1.sm"
-  --alfa -> Parâmetro do algoritmo que ajusta os possíveis candidatos selecionados na etapa de busca por possíveis candidatos a serem processados. Se alfa=0, todas as atividades se tornam possíveis de serem selecionadas. Se alfa=1, só a atividade com maior valor de recursos será selecionada sempre e seria equivalente a deixar o algoritmo a uma construção gulosa sem a parte da aleatoriedade. Caso não seja informado, o valor default é 0.5.

Exemplo de execução sem a passagem de parâmetros:
```bash
$ python main.py
([3, 2, 4, 7, 13, 8, 9, 11, 17, 18, 14, 6, 12, 27, 20, 22, 26, 5, 15, 30, 10, 28, 25, 31, 23, 19, 24, 16, 29, 21], 40)
```

Exemplo de execução com a passagem de parâmetros:
```bash
$ python main.py --file "data/data/j60/j603_2.sm" --alfa 0.8
([3, 2, 4, 17, 5, 40, 7, 24, 34, 8, 36, 6, 38, 10, 41, 35, 43, 9, 42, 46, 61, 52, 16, 50, 18, 27, 26, 44, 29, 57, 55, 31, 58, 20, 28, 60, 59, 47, 54, 33, 49, 25, 11, 56, 8, 13, 21, 51, 12, 15, 22, 14, 30, 37, 23, 19, 53, 39, 32, 45], 72)
```

O resultado é uma lista contendo a ordenação escolhida para a alocação das tarefas e a quantidade de unidades de tempo necessárias para completar todo o projeto.
