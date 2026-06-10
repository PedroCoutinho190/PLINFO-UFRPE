# 🌿 PLINFO

PLINFO é uma plataforma educacional interativa desenvolvida em Python com interface de terminal (TUI) que visa combater a "cegueira botânica" — a dificuldade das pessoas em reconhecer e valorizar as plantas ao redor. O sistema oferece um catálogo completo de espécies vegetais com informações detalhadas sobre cuidados, origem, curiosidades, reflorestamento e linha do tempo histórica, além de um módulo dedicado ao manejo de pragas agrícolas.

O projeto foi desenvolvido como trabalho acadêmico para o curso de **Sistemas de Informação** da **UFRPE**.

---

## 🚀 Release 2.0 (Atual)

### 🌱 Catálogo de Plantas
- Galeria geral com todas as espécies
- Filtro por plantas medicinais
- Filtro por plantas venenosas
- Filtro por plantas aquáticas
- Expansão para 50 espécies cadastradas
- Pesquisa avançada por nome e característica
- Novos filtros de navegação

### 📖 Informações por Planta
- Como Cuidar
- Reflorestamento
- Origem
- Curiosidades
- Linha do tempo histórica
- Informações botânicas (nome científico, família, classificação)

### 🐛 Módulo de Pragas
- Consulta de pragas por planta
- Sintomas de infestação
- Tratamentos recomendados
- Medidas de prevenção
- Vídeos sobre pragas via YouTube

### 🤖 Inteligência Artificial
- Sugestão de receitas com base na planta selecionada
- Simulador de ambiente inteligente
- Integração com modelos LLaMA via API da Groq

### 🎥 Integração com YouTube
- Busca automática de vídeos relacionados às plantas
- Vídeos educativos sobre pragas e cuidados

### 🔐 Autenticação e Segurança
- Cadastro de usuários
- Login e logout
- Verificação por código via e-mail
- Criptografia de senhas

### 👤 Configurações da Conta
- Edição de nome
- Alteração de senha
- Exclusão de conta

---

## 🏗️ Estrutura do Projeto

```text
plinfo/
├── ui/                  # Telas e componentes visuais (Textual)
│   ├── screens/         # Telas principais da aplicação
│   └── components/      # Componentes reutilizáveis da interface
├── services/            # Regras de negócio e lógica da aplicação
│   ├── plant_service.py
│   ├── pest_service.py
│   ├── ai_service.py
│   └── auth_service.py
├── database/            # Acesso ao banco de dados SQLite
│   ├── models/          # Modelos de dados
│   └── repositories/    # Consultas e operações no banco
├── api/                 # Integrações externas
│   ├── groq_client.py   # Integração com a API do Groq
│   └── youtube_client.py# Integração com YouTube Data API v3
├── .env                 # Variáveis de ambiente (não versionado)
├── requirements.txt     # Dependências do projeto
└── main.py              # Ponto de entrada da aplicação
```

---

## 🛠️ Tecnologias Utilizadas

- Python
- Textual (TUI)
- SQLite
- Groq API (LLaMA 3.1)
- YouTube Data API v3

---

## 📚 Bibliotecas Utilizadas

O PLINFO foi desenvolvido utilizando bibliotecas externas e módulos nativos do Python que juntos constroem a interface, a inteligência artificial, as integrações e a segurança da aplicação.

---

### Textual

Framework utilizado para construção da interface gráfica em terminal (TUI).

**Principais usos no projeto:**
- Criação de telas e layouts interativos no terminal
- Componentes visuais como botões, inputs, labels e tabelas
- Navegação entre páginas da aplicação
- Renderização assíncrona da interface

---

### Groq

SDK oficial da plataforma Groq para integração com modelos de Inteligência Artificial.

**Principais usos no projeto:**
- Sugestão de receitas culinárias e medicinais com base na planta selecionada
- Simulador de ambiente inteligente para cultivo de plantas
- Integração com os modelos `llama-3.1-8b-instant` e `llama-3.3-70b-versatile`

---

### google-api-python-client

Biblioteca oficial do Google para consumo de suas APIs.

**Principais usos no projeto:**
- Integração com a YouTube Data API v3
- Busca automática de vídeos educativos sobre plantas e pragas
- Exibição de conteúdo audiovisual diretamente na interface

---

### python-dotenv

Biblioteca responsável pelo carregamento de variáveis de ambiente armazenadas em arquivos `.env`.

**Principais usos no projeto:**
- Armazenamento seguro de chaves de API (Groq, YouTube)
- Configuração de credenciais de e-mail (Gmail SMTP)
- Separação de configurações sensíveis do código-fonte

---

### colorama

Biblioteca para aplicação de cores e estilos no terminal.

**Principais usos no projeto:**
- Destaque visual de informações importantes
- Melhoria da experiência do usuário na interface
- Diferenciação de categorias e alertas por cor

---

## 🐍 Bibliotecas Nativas do Python

Além das bibliotecas externas, o projeto utiliza diversos módulos nativos da linguagem Python.

| Biblioteca     | Finalidade                                                                 |
| -------------- | -------------------------------------------------------------------------- |
| `sqlite3`      | Criação e manipulação do banco de dados local                              |
| `smtplib`      | Envio de e-mails via Gmail SMTP para verificação de conta                  |
| `re`           | Validação de campos como nome, e-mail e senha com expressões regulares     |
| `asyncio`      | Gerenciamento de operações assíncronas da interface Textual e das APIs     |
| `dataclasses`  | Organização de modelos de dados de forma limpa e tipada entre as camadas   |
| `json`         | Serialização e desserialização de dados trocados entre módulos e APIs      |

---

## ⚙️ Funcionalidades elaboradas e seus objetivos

---

### ✅ Funcionalidades entregues na versão 1.0 — Primeira VA

As funcionalidades da Primeira VA foram organizadas para oferecer uma experiência inicial completa ao usuário, desde o cadastro até a navegação pelo catálogo de plantas com informações botânicas detalhadas e filtros por categoria.

---

#### 🔐 Autenticação e Segurança

| Funcionalidade                       | Descrição                                                                   | Objetivo                                                                               |
| ------------------------------------ | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Cadastro de usuário**              | Permite que novos usuários criem uma conta informando nome, e-mail e senha. | Registrar usuários no sistema de forma organizada e segura.                            |
| **Validação de dados**               | Valida nome, e-mail, senha e confirmação de senha durante o cadastro.       | Evitar dados inválidos, incompletos ou inconsistentes no banco de dados.               |
| **Verificação de e-mail por código** | Envia um código via Gmail SMTP antes de finalizar o cadastro.               | Confirmar que o e-mail realmente pertence ao usuário.                                  |
| **Login de usuário**                 | Permite o acesso ao sistema usando e-mail e senha cadastrados.              | Garantir que apenas usuários autenticados acessem as telas internas.                   |
| **Criptografia de senhas**           | Armazena as senhas usando hash seguro com salt aleatório.                   | Proteger as credenciais dos usuários e evitar o armazenamento de senhas em texto puro. |

---

#### 👤 Configurações da Conta

| Funcionalidade          | Descrição                                                                | Objetivo                                                               |
| ----------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Atualização de nome** | Permite que o usuário altere o nome exibido no perfil.                   | Manter os dados do usuário atualizados.                                |
| **Alteração de senha**  | Permite trocar a senha informando a senha atual e uma nova senha válida. | Oferecer uma forma segura de atualizar as credenciais da conta.        |
| **Exclusão de conta**   | Permite que o usuário remova sua conta do sistema.                       | Dar ao usuário controle sobre seus próprios dados dentro da aplicação. |

---

#### 🌿 Catálogo e Galeria de Plantas

| Funcionalidade            | Descrição                                                                      | Objetivo                                                                         |
| ------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| **Galeria geral**         | Exibe todas as plantas cadastradas no sistema em formato de catálogo visual.   | Oferecer uma visão completa do acervo disponível para exploração livre.          |
| **Filtro por medicinais** | Permite filtrar e listar apenas as plantas com propriedades medicinais.        | Facilitar a busca de plantas úteis para fins terapêuticos e de saúde.           |
| **Filtro por venenosas**  | Permite filtrar e listar apenas as plantas classificadas como venenosas.       | Alertar e informar o usuário sobre espécies que oferecem risco à saúde.         |
| **Filtro por aquáticas**  | Permite filtrar e listar apenas as plantas de ambiente aquático.               | Atender usuários interessados em espécies específicas de habitats aquáticos.    |
| **Como Cuidar**           | Exibe orientações sobre rega, luz, solo e manutenção de cada planta.           | Auxiliar o usuário a manter suas plantas saudáveis com informações confiáveis.  |
| **Reflorestamento**       | Apresenta o papel da planta em projetos de recuperação ambiental.              | Conscientizar o usuário sobre a importância ecológica das espécies cadastradas. |
| **Origem**                | Informa a origem geográfica e o histórico da espécie.                          | Enriquecer o conhecimento do usuário sobre a procedência das plantas.           |
| **Curiosidades**          | Apresenta fatos interessantes e pouco conhecidos sobre cada planta.            | Tornar a experiência mais envolvente e educativa.                                |
| **Linha do tempo**        | Exibe marcos históricos importantes relacionados à planta ao longo do tempo.   | Contextualizar historicamente cada espécie de forma visual e organizada.        |


---

### ✅ Funcionalidades entregues na versão 2.0 — Segunda VA (Atual)

A Segunda VA teve como foco transformar o PLINFO em uma plataforma mais robusta, interativa e útil, com interface completamente renovada via Textual, inteligência artificial com Groq, integração com YouTube e um módulo dedicado ao manejo de pragas.

---

#### 🏗️ Arquitetura e Interface

| Funcionalidade                          | Descrição                                                                                                                          | Objetivo                                                                            |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Migração para POO**                   | Refatora o código para aplicar Programação Orientada a Objetos, organizando telas, serviços, modelos e repositórios separadamente. | Melhorar a manutenção, a organização, a reutilização e a escalabilidade do projeto. |
| **Migração para interface com Textual** | Substitui a interface anterior por uma TUI completa desenvolvida com a biblioteca `textual`.                                       | Oferecer uma experiência visual mais rica, navegável e profissional no terminal.    |
| **Melhorias gerais de arquitetura**     | Revisão e reestruturação dos módulos internos, consolidando as 3 camadas UI → Services → Database/APIs.                           | Garantir um código mais limpo, coeso e preparado para novas expansões.              |

---

#### 🌱 Expansão do Catálogo

| Funcionalidade               | Descrição                                                             | Objetivo                                                                           |
| ---------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Expansão para 50 plantas** | Amplia o catálogo com novas espécies cadastradas e documentadas.      | Oferecer uma base de dados mais completa e diversificada para os usuários.         |
| **Novos filtros**            | Adiciona critérios adicionais de filtragem no catálogo.               | Melhorar a experiência de busca e navegação pelo acervo de plantas.                |
| **Pesquisa avançada**        | Permite buscas mais detalhadas por nome, característica ou categoria. | Facilitar a localização de plantas específicas em um catálogo maior.               |

---

#### 🤖 Inteligência Artificial e Receitas

| Funcionalidade                   | Descrição                                                                                | Objetivo                                                                         |
| -------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Integração com Groq**          | Conecta a aplicação aos modelos `llama-3.1-8b-instant` e `llama-3.3-70b-versatile`.     | Oferecer respostas e sugestões dinâmicas geradas por inteligência artificial.    |
| **Sugestão de receitas com IA**  | Sugere receitas culinárias, medicinais ou de uso prático com base na planta selecionada. | Agregar valor prático ao catálogo, explorando o uso das plantas no cotidiano.    |
| **Simulador de ambiente com IA** | Simula diferentes condições de ambiente e seu impacto no desenvolvimento das plantas.    | Auxiliar o usuário a escolher o ambiente mais adequado para cada espécie.        |

---

#### 🎥 Integração com YouTube

| Funcionalidade             | Descrição                                                                       | Objetivo                                                                         |
| -------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Integração com YouTube** | Busca e exibe vídeos via YouTube Data API v3 relacionados à planta selecionada. | Enriquecer o conteúdo com material audiovisual prático e acessível ao usuário.  |
| **Vídeos sobre pragas**    | Apresenta vídeos específicos sobre identificação e tratamento de pragas.        | Facilitar a compreensão visual do problema e das soluções disponíveis.           |

---

#### 🐛 Módulo de Pragas

| Funcionalidade         | Descrição                                                                         | Objetivo                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Consulta de pragas** | Permite ao usuário pesquisar pragas que afetam as plantas cadastradas no sistema. | Centralizar informações sobre agentes nocivos e facilitar o diagnóstico pelo usuário.    |
| **Sintomas**           | Exibe os principais sintomas causados por cada praga nas plantas afetadas.        | Ajudar o usuário a identificar rapidamente se sua planta está sendo atacada.             |
| **Tratamentos**        | Lista os tratamentos recomendados para combater cada praga identificada.          | Orientar o usuário sobre as melhores práticas para eliminar ou controlar a praga.        |
| **Prevenção**          | Apresenta medidas preventivas para evitar o surgimento de pragas nas plantas.     | Incentivar boas práticas de cultivo e reduzir a incidência de problemas fitossanitários. |

---

## 📊 Modelos Principais

### Autenticação
- Usuario
- CodigoVerificacao

### Plantas
- Planta
- Cuidado
- LinhaDoTempo

### Pragas
- Praga
- Sintoma
- Tratamento

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/plinfo.git
cd plinfo
```

### 2. Crie e ative um ambiente virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
GROQ_API_KEY=sua_chave_groq
YOUTUBE_API_KEY=sua_chave_youtube
EMAIL_ADDRESS=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app
```

### 5. Inicie a aplicação

```bash
python main.py
```

---

## 🎯 Objetivos

- Combater a cegueira botânica por meio de uma plataforma interativa e educativa.
- Facilitar o acesso a informações botânicas de forma organizada e visual.
- Promover o uso consciente das plantas e boas práticas de cultivo.
- Auxiliar no diagnóstico e tratamento de pragas agrícolas.

---

## 👨‍💻 Autores

Renato Rodrigues Barbosa Filho
Pedro Henrique Albuquerque Coutinho

---

## 🎯 Drive contendo a Planilha de Funcionalidades + Artigo em PDF

https://drive.google.com/drive/folders/1b35CsPMOBCuEuYnAT25FKOF2Z7jiajzE?usp=drive_link

---

## 🎯 Link do Artigo do OverLeaf

https://www.overleaf.com/read/cxgndpxmgptg#abe0d5

---

## 🎯 Link da DemoDay

- https://youtu.be/rmaiuhSFgos
