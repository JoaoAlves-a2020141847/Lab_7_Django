# 🌐 Funcionamento da Aplicação

## 🛠 Estrutura do Projeto

Antes de mais, abaixo encontra-se uma descrição dos ficheiros e pastas principais do projeto/aplicação, podendo-se assim ter uma visão geral da operação do Django como um todo:

- **admin.py**: Contém a lógica da interface de administrador.
- **manage.py**: Ficheiro principal para executar comandos do Django.
- **models.py**: Contém os modelos de dados (o esquema da base de dados) da aplicação.
- **settings.py**: Configurações da aplicação, incluindo base de dados, templates, e middleware.
- **tests.py**: Contém os testes unitários definidos para garantir o bom funcionamento da aplicação.
- **urls.py**: Define as rotas (URLs) para as diferentes páginas da aplicação.
- **views.py**: Contém a lógica para manipular pedidos HTTP e devolver respostas.
- **templates/**: Pasta onde estão localizados os ficheiros HTML.



## 🌐 Componentes da Aplicação

A aplicação Django funciona seguindo o padrão MTV (Model-Template-View), no qual cada componente desempenha um papel específico no fluxo de dados e na renderização das páginas. Existem três grandes componentes nesta aplicação, e em aplicações Django como um todo.

### Rotas e URLs

As rotas e URLs da aplicação são definidas no ficheiro urls.py. Este ficheiro conecta URLs a funções chamadas views, que processam os pedidos HTTP e devolvem respostas ao utilizador. Cada URL pode estar associada a uma função ou classe definida no views.py do projeto ou da app. O mapeamento é feito com o método path().

Por exemplo:

    / -> Página inicial (index): Mostra uma lista de tópicos ou conteúdo dinâmico.
    /admin/ -> Painel de administração: Uma interface fornecida pelo Django para gerir dados na base de dados.

### Views

As views são responsáveis por processar os pedidos recebidos pelo servidor e decidir qual a resposta a enviar ao cliente (navegador). Existem funções, que são simples de implementar e amplamente utilizadas em projetos pequenos ou médios, e classes, também conhecidas como Class-Based Views (CBVs), onde oferecem uma estrutura mais robusta e reutilizável para projetos maiores.


### Templates

Os templates são ficheiros HTML que utilizam a linguagem de templates do Django para exibir variáveis, criar loops, ou renderizar dados dinâmicos. Os ficheiros de template devem estar na pasta **templates/** (ou noutra especificada nas configurações). Utilizam tags e filtros do Django, como ```{% for %}, {% if %}, e {{ variable_name }}``` para exibir ou processar conteúdo.
