PLINFO Release 2.0 🌿

O *PLINFO* é uma aplicação de interface de terminal (TUI) desenvolvida como projeto prático para o curso de *Sistemas de Informação* da *UFRPE*. A plataforma visa conectar usuários ao mundo da botânica, oferecendo um catálogo interativo de plantas com informações detalhadas sobre cuidados, origem, curiosidades, reflorestamento e linha do tempo, além de um módulo completo para identificação e tratamento de pragas.

---

## Bibliotecas usadas

### Bibliotecas externas

| Biblioteca                  | Objetivo no projeto                                                                                       |
| --------------------------- | --------------------------------------------------------------------------------------------------------- |
| textual                   | Criar a interface gráfica em terminal, com telas, botões, inputs, labels e navegação entre páginas.       |
| groq                      | Integração com IA (llama-3.1-8b-instant e llama-3.3-70b-versatile) para sugestões e consultas inteligentes. |
| google-api-python-client  | Integração com a YouTube Data API v3 para busca e exibição de vídeos relacionados às plantas e pragas.   |
| python-dotenv             | Carregar variáveis de ambiente do arquivo .env, como chaves de API e credenciais de e-mail.            |
| colorama                  | Aplicar cores e estilos no terminal para melhorar a experiência visual da interface.                     |

### Bibliotecas nativas do Python

| Biblioteca     | Objetivo no projeto                                                              |
| -------------- | -------------------------------------------------------------------------------- |
| sqlite3      | Criar e manipular o banco de dados local SQLite.                                 |
| smtplib      | Enviar e-mails via Gmail SMTP para verificação de conta e recuperação de senha.  |
| re           | Validar campos como nome, e-mail e senha com expressões regulares.               |
| asyncio      | Gerenciar operações assíncronas da interface Textual e chamadas às APIs externas. |
| dataclasses  | Organizar modelos de dados de forma limpa e tipada entre as camadas da aplicação.|
| json         | Serializar e desserializar dados trocados entre módulos e APIs externas.         |

---

## 🏗️ Arquitetura

O projeto é organizado em *3 camadas* bem definidas:


UI (Textual Screens) → Services (lógica pura) → Database / APIs


- *UI* — Telas e componentes visuais construídos com Textual
- *Services* — Regras de negócio isoladas, sem dependência de interface
- *Database / APIs* — Acesso ao SQLite local e integrações com Groq, YouTube e Gmail SMTP

---

## ⚙️ Funcionalidades elaboradas e seus objetivos

### ✅ Funcionalidades entregues na versão 1.0 — Primeira VA

As funcionalidades da *Release 1.0* foram organizadas para oferecer uma experiência inicial completa ao usuário, desde o cadastro até a navegação pelo catálogo de plantas com informações botânicas detalhadas e filtros por categoria.

---

### 🔐 Autenticação e segurança

| Funcionalidade                       | Descrição                                                                   | Objetivo                                                                               |
| ------------------------------------ | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| *Cadastro de usuário*              | Permite que novos usuários criem uma conta informando nome, e-mail e senha. | Registrar usuários no sistema de forma organizada e segura.                            |
| *Validação de dados*               | Valida nome, e-mail, senha e confirmação de senha durante o cadastro.       | Evitar dados inválidos, incompletos ou inconsistentes no banco de dados.               |
| *Verificação de e-mail por código* | Envia um código via Gmail SMTP antes de finalizar o cadastro.               | Confirmar que o e-mail realmente pertence ao usuário.                                  |
| *Login de usuário*                 | Permite o acesso ao sistema usando e-mail e senha cadastrados.              | Garantir que apenas usuários autenticados acessem as telas internas.                   |
| *Criptografia de senhas*           | Armazena as senhas usando hash seguro com salt aleatório.                   | Proteger as credenciais dos usuários e evitar o armazenamento de senhas em texto puro. |

---

### 👤 Configurações da conta

| Funcionalidade          | Descrição                                                                | Objetivo                                                               |
| ----------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| *Atualização de nome* | Permite que o usuário altere o nome exibido no perfil.                   | Manter os dados do usuário atualizados.                                |
| *Alteração de senha*  | Permite trocar a senha informando a senha atual e uma nova senha válida. | Oferecer uma forma segura de atualizar as credenciais da conta.        |
| *Exclusão de conta*   | Permite que o usuário remova sua conta do sistema.                       | Dar ao usuário controle sobre seus próprios dados dentro da aplicação. |

---

### 🌿 Catálogo e galeria de plantas

| Funcionalidade            | Descrição                                                                      | Objetivo                                                                         |
| ------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| *Galeria geral*         | Exibe todas as plantas cadastradas no sistema em formato de catálogo visual.   | Oferecer uma visão completa do acervo disponível para exploração livre.          |
| *Filtro por medicinais* | Permite filtrar e listar apenas as plantas com propriedades medicinais.        | Facilitar a busca de plantas úteis para fins terapêuticos e de saúde.           |
| *Filtro por venenosas*  | Permite filtrar e listar apenas as plantas classificadas como venenosas.       | Alertar e informar o usuário sobre espécies que oferecem risco à saúde.         |
| *Filtro por aquáticas*  | Permite filtrar e listar apenas as plantas de ambiente aquático.               | Atender usuários interessados em espécies específicas de habitats aquáticos.    |
| *Como Cuidar*           | Exibe orientações sobre rega, luz, solo e manutenção de cada planta.           | Auxiliar o usuário a manter suas plantas saudáveis com informações confiáveis.  |
| *Reflorestamento*       | Apresenta o papel da planta em projetos de recuperação ambiental.              | Conscientizar o usuário sobre a importância ecológica das espécies cadastradas. |
| *Origem*                | Informa a origem geográfica e o histórico da espécie.                          | Enriquecer o conhecimento do usuário sobre a procedência das plantas.           |
| *Curiosidades*          | Apresenta fatos interessantes e pouco conhecidos sobre cada planta.            | Tornar a experiência mais envolvente e educativa.                                |
| *Linha do tempo*        | Exibe marcos históricos importantes relacionados à planta ao longo do tempo.   | Contextualizar historicamente cada espécie de forma visual e organizada.        |
---

### ✅ Funcionalidades entregues na versão 2.0 — Segunda VA (Atual)

As funcionalidades da *Release 2.0* ampliaram o PLINFO com uma interface completamente renovada via Textual, inteligência artificial com Groq, integração com YouTube e um módulo dedicado ao manejo de pragas.

Essa versão teve como foco transformar o sistema em uma plataforma mais robusta, interativa e útil tanto para entusiastas quanto para usuários com necessidades práticas no trato com plantas.

---

### 🏗️ Arquitetura e interface

| Funcionalidade                          | Descrição                                                                                                                          | Objetivo                                                                            |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| *Migração para POO*                   | Refatora o código para aplicar Programação Orientada a Objetos, organizando telas, serviços, modelos e repositórios separadamente. | Melhorar a manutenção, a organização, a reutilização e a escalabilidade do projeto. |
| *Migração para interface com Textual* | Substitui a interface anterior por uma TUI completa desenvolvida com a biblioteca textual.                                       | Oferecer uma experiência visual mais rica, navegável e profissional no terminal.    |
| *Melhorias gerais de arquitetura*     | Revisão e reestruturação dos módulos internos, consolidando as 3 camadas UI → Services → Database/APIs.                           | Garantir um código mais limpo, coeso e preparado para novas expansões.              |

---

### 🌱 Expansão do catálogo

| Funcionalidade               | Descrição                                                              | Objetivo                                                                           |
| ---------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| *Expansão para 50 plantas* | Amplia o catálogo com novas espécies cadastradas e documentadas.       | Oferecer uma base de dados mais completa e diversificada para os usuários.         |
| *Novos filtros*            | Adiciona critérios adicionais de filtragem no catálogo.                | Melhorar a experiência de busca e navegação pelo acervo de plantas.                |
| *Pesquisa avançada*        | Permite buscas mais detalhadas por nome, característica ou categoria.  | Facilitar a localização de plantas específicas em um catálogo maior.               |

---

### 🤖 Inteligência artificial e receitas

| Funcionalidade            | Descrição                                                                                | Objetivo                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| *Integração com Groq*   | Conecta a aplicação aos modelos llama-3.1-8b-instant e llama-3.3-70b-versatile via API. | Oferecer respostas e sugestões dinâmicas geradas por inteligência artificial.    |
| *Sugestão de receitas com IA* | Sugere receitas culinárias, medicinais ou de uso prático com base na planta selecionada. | Agregar valor prático ao catálogo, explorando o uso das plantas no cotidiano. |
| *Simulador de ambiente com IA* | Simula diferentes condições de ambiente e seu impacto no desenvolvimento das plantas. | Auxiliar o usuário a escolher o ambiente mais adequado para cada espécie.    |

---

### 🎥 Integração com YouTube

| Funcionalidade             | Descrição                                                                       | Objetivo                                                                         |
| -------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| *Integração com YouTube* | Busca e exibe vídeos via YouTube Data API v3 relacionados à planta selecionada. | Enriquecer o conteúdo com material audiovisual prático e acessível ao usuário.  |
| *Vídeos sobre pragas*    | Apresenta vídeos específicos sobre identificação e tratamento de pragas.        | Facilitar a compreensão visual do problema e das soluções disponíveis.           |

---

### 🐛 Módulo de pragas

| Funcionalidade         | Descrição                                                                         | Objetivo                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| *Consulta de pragas* | Permite ao usuário pesquisar pragas que afetam as plantas cadastradas no sistema. | Centralizar informações sobre agentes nocivos e facilitar o diagnóstico pelo usuário.    |
| *Sintomas*           | Exibe os principais sintomas causados por cada praga nas plantas afetadas.        | Ajudar o usuário a identificar rapidamente se sua planta está sendo atacada.             |
| *Tratamentos*        | Lista os tratamentos recomendados para combater cada praga identificada.          | Orientar o usuário sobre as melhores práticas para eliminar ou controlar a praga.        |
| *Prevenção*          | Apresenta medidas preventivas para evitar o surgimento de pragas nas plantas.     | Incentivar boas práticas de cultivo e reduzir a incidência de problemas fitossanitários. |
