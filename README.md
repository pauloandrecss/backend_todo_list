## Back-End Todo List

Projeto de backend construído com FastAPI para gerenciar uma aplicação de lista de tarefas. 
Este projeto fornece uma API eficiente e fácil de usar para a criação, leitura, atualização e exclusão de tarefas,
juntamente com funcionalidades de autenticação para garantir que apenas usuários autenticados possam acessar e manipular seus próprios dados.
<br>

![screencapture-127-0-0-1-8000-docs-2024-08-05-23_16_35](https://github.com/user-attachments/assets/034d205b-61ce-47e1-b946-0813e069c4cc)

## Instalação

Para testar em sua máquina, siga os passos abaixo:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/pauloandrecss/backend_todo_list.git

2. **Navegue até o diretório do projeto**:

   ```bash
   cd backend_todo_list

3. **Crie um arquivo de variaveis .env como no exemplo**:

   ```.env
   POSTGRES_USER=app_user
   POSTGRES_DB=app_db
   POSTGRES_PASSWORD=app_password
   DATABASE_URL=postgresql+psycopg://app_user:app_password@todo_backend_database:5432/app_db
   SECRET_KEY = 'your-secret-key'
   ALGORITHM = 'HS256'
   ACCESS_TOKEN_EXPIRE_MINUTES = 30

4. **Utilize o docker para iniciar a aplicação**:

   ```bash
   docker compose up

5. **Acesse a documentação em seu navegador**:

   ```url
   http://127.0.0.1:8000/docs

obs: Caso ocorra um erro de permissão do arquivo entrypoint.sh execute o seguinte comando e reinicie o docker:

   ```
   chmod +x entrypoint.sh
   docker compose up --build
