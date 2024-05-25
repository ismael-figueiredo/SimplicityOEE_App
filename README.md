# SimplicityOEE App 

## Sobre o Projeto

Este projeto visa fornecer uma solução simples e gratuita para pequenas empresas monitorarem sua produção. A aplicação OEE (Overall Equipment Effectiveness) é voltada para empresas que não têm condições de adquirir softwares MES (Manufacturing Execution System) caros e querem iniciar a gestão e o monitoramento de suas operações de forma eficaz. O projeto é open-source, sob a licença MIT, construído com Python, SQLite, Dash, Dash Bootstrap Components, entre outras tecnologias.

## Configuração

### Pré-requisitos

Antes de iniciar, certifique-se de ter Python instalado em sua máquina. Este projeto foi desenvolvido utilizando Python 3.8. Recomenda-se usar um ambiente virtual para gerenciar as dependências.

### Instalação das Dependências

Para instalar as dependências necessárias para o projeto, execute o seguinte comando em seu terminal:

```bash
pip install -r requirements.txt
```
### Criação do Banco de Dados e Configuração Inicial
Depois de instalar as dependências, é necessário configurar o banco de dados e adicionar um setor e usuário padrões. Execute o comando abaixo para criar o banco de dados e realizar as configurações iniciais:
```bash
python src/database/create_database.py
```
Este comando irá configurar o banco de dados necessário para a aplicação e adicionará um setor padrão "Adm" e um usuário "Admin" com uma senha padrão.

## Executando a Aplicação
Para iniciar a aplicação, navegue até o diretório do projeto e execute o seguinte comando:

```bash
python src/app.py
```
Este comando iniciará o servidor local, e você poderá acessar a interface da aplicação através de um navegador web no endereço indicado no terminal, geralmente http://localhost:8050.

## Contribuições
Contribuições são sempre bem-vindas! Se você tem sugestões para melhorar esta aplicação, sinta-se à vontade para criar um fork do projeto e enviar um pull request, ou abrir uma issue no GitHub.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.