## 😇 This repository is for my practice of FastAPI 😇
## 🤣 Now you can see my project's site [here](https://fastapi-deployment-e0kg.onrender.com) 🤣

<br>

## 🪝 How to start for the first time
``` shell
# Create Docker image
$ docker-compose build

# Install dependencies packages (--no-root means that not installing myapp)
$ docker-compose run --entrypoint "poetry install --no-root" fastapi-practice

# Install all packages that in pyproject.toml
# (if you changed or installed package in pyproject.toml, you must execute this command for reflection)
$ docker-compose build --no-cache

# Launch container
$ docker-compose up
```
<br>

**<details><summary>🤷🏼‍♂️ What are in .env</summary>**

``` env
POSTGRES_USER=YOUR POSTGRES USER NAME
POSTGRES_DB=YOUR POSTGRES DB NAME
POSTGRES_PASSWORD=YOUR POSTGRES PASSWORD
PGADMIN_DEFAULT_EMAIL=YOUR EMAIL ADDRESS
PGADMIN_DEFAULT_PASSWORD=YOUR PASSWORD

# YOUR_SQLALCHEMY_DATABASE_NAME can be the database name that you made in PgAdmin
SQLALCHEMY_DATABASE_URL=postgresql://YOUR_POSTGRES_USER_NAME:YOUR_POSTGRES_PASSWORD@todo_db:5432/YOUR_SQLALCHEMY_DATABASE_NAME
TEST_SQLALCHEMY_DATABASE_URL=postgresql://YOUR_POSTGRES_USER_NAME:YOUR_POSTGRES_PASSWORD@todo_db:5432/YOUR_TEST_SQLALCHEMY_DATABASE_NAME
```
</details>

<br>

**<details><summary>👹 My pyproject.toml</summary>**

```toml
[tool.poetry]
name = "fastapi-practice"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.9"
fastapi = "^0.110.0"
uvicorn = {extras = ["standard"], version = "^0.29.0"}
sqlalchemy = "^2.0.29"
passlib = {extras = ["bcrypt"], version = "^1.7.4"}
bcrypt = "^4.1.2"
python-multipart = "^0.0.9"
python-jose = {extras = ["cryptography"], version = "^3.3.0"}
psycopg2-binary = "^2.9.9"
psycopg2 = "^2.9.9"
wheel = "^0.43.0"
alembic = "^1.13.1"
pytest = "^8.1.1"
httpx = "^0.27.0"
pytest-asyncio = "^0.23.6"
aiofiles = "^23.2.1"
jinja2 = "^3.1.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
</details>

<br>

## 🚦 NOT for the first time to use this
``` shell
# Launch container
$ docker-compose up
```
<br>

## 🦖 Info
- 😄 If you want to add a package, you can exec this command
```shell
# login to fastapi-practice
$ docker-compose exec fastapi-practice /bin/bash
# Then you can execute it
$ poetry add {the name of package}
```
<br>

- 🫀 If you want to connect PgAdmin to Postgres,
  - PgAdmin's connection section will be service_postgres
  - I think the name should be same as service_postgres
  - And the user name will be POSTGRES_USER and password is going to be POSTGRES_PASSWORD that are in env file

<br>

- 😵 **If you run alembic command**
```shell
# You have to add "poetry run" in front of "alembic" if you're using poetry
$ poetry run alembic [your_command]
```

- 🤡 About my deployment
  - I deployed the application (TodoAppFullStack) on [Render](https://fastapi-deployment-e0kg.onrender.com)
  - I deployed the database on [ElephantSQL](https://www.elephantsql.com)
  - So my database is provided by ElephantSQL for free but it might be removed on January 27, 2025

<br>


## 🚢 References

- FastAPI Rudimentary
  - [Similar article of Udemy course](https://qiita.com/yamarao/items/6889adfd4b484b7b5e11)
  - [Solve TemplateNotFound: home.html](https://www.reddit.com/r/FastAPI/comments/jd7h07/jinja2_templatenotfound_error/)
  - [error reading bcrypt version ](https://github.com/langflow-ai/langflow/issues/1173)
  - [What does Form(...) mean?](https://zenn.dev/chanyou0311/articles/fast-api-intro)

- Database
  - [SQLALCHEMY_DATABASE_URL_REFERENCE](https://stackoverflow.com/questions/71116549/sqlalchemy-exc-operationalerror-psycopg2-operationalerror-with-postgresql)
  - [Add Foreign key and delete Foreign key](https://postgresweb.com/post-6354#google_vignette)

- PgAdmin
  - [CSRF token is missing error in docker pgadmin](https://stackoverflow.com/questions/64394628/csrf-token-is-missing-error-in-docker-pgadmin)

- Docker
  - [FastAPI Introduction with Docker](https://zenn.dev/sh0nk/books/537bb028709ab9/)
  - [How to move to deferent directory like cd](https://qiita.com/rururu_kenken/items/8b5862e54fbe156a8cb8)
  - [For the psycopg2.OperationalError THE MOST IMPORTANT CODE!](https://zenn.dev/ryo_t/articles/3be7a5ca39d496)
  - [How to create docker-compose.yaml with Postgres and connecting with Pgadmin MAIN!](https://qiita.com/Akhr/items/8d5b5127ee971a640253)
  - [Remove volume](https://ysko909.github.io/posts/delete-volume-when-get-password-authentication-failed-error/)
  - [What's tty?](https://zenn.dev/hohner/articles/43a0da20181d34)
  - [.env file](https://qiita.com/SolKul/items/989727aeeafcae28ecf7)

- Python's Rudimentary
  - [How to import other file?](https://qiita.com/karadaharu/items/37403e6e82ae4417d1b3)

- Poetry
  - [What is poetry](https://qiita.com/nilwurtz/items/0e5b8382757ccad9a56c)
  - [How to run alembic command using poetry](https://zenn.dev/keita_f/articles/4493e3cfd76aec)
  - [How to add a package by using poetry](https://zenn.dev/rihito/articles/7b48821e4a3f74)
