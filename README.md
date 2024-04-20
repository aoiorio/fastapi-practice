## 😇 This repository is for my practice of FastAPI 😇
<br>

## 🪝 How to start for the first time
``` shell
# Create Docker image
$ docker-compose build

# Create pyproject.toml and install FastAPI by using "poetry"
$ docker-compose run \
  --entrypoint "poetry init \
    --name fastapi-practice \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  fastapi-practice

# Then you must answer n in the part of Author but just push enter key in the others

# Install dependencies packages (--no-root means that not installing myapp)
$ docker-compose run --entrypoint "poetry install --no-root" fastapi-practice

# Install all packages that in pyproject.toml
# (if you changed or installed package in pyproject.toml, you must execute this command for reflection)
$ docker-compose build --no-cache
```
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

- 😵 **If you run alembic command**
```shell
# You have to add "poetry run" in front of "alembic" if you're using poetry
$ poetry run alembic [your_command]
```

<br>

## 🚢 References
- [FastAPI Introduction](https://zenn.dev/sh0nk/books/537bb028709ab9/)
- [What is poetry](https://qiita.com/nilwurtz/items/0e5b8382757ccad9a56c)
- [How to add a package by using poetry](https://zenn.dev/rihito/articles/7b48821e4a3f74)
- [Similar article of Udemy course](https://qiita.com/yamarao/items/6889adfd4b484b7b5e11)
- [How to move to deferent directory like cd](https://qiita.com/rururu_kenken/items/8b5862e54fbe156a8cb8)
- [For the psycopg2.OperationalError THE MOST IMPORTANT CODE!](https://zenn.dev/ryo_t/articles/3be7a5ca39d496)
- [How to create docker-compose.yaml with Postgres and connecting with Pgadmin MAIN!](https://qiita.com/Akhr/items/8d5b5127ee971a640253)
- [.env file](https://qiita.com/SolKul/items/989727aeeafcae28ecf7)
- [Remove volume](https://ysko909.github.io/posts/delete-volume-when-get-password-authentication-failed-error/)
- [What's tty?](https://zenn.dev/hohner/articles/43a0da20181d34)
- [How to import other file?](https://qiita.com/karadaharu/items/37403e6e82ae4417d1b3)
- [How to run alembic command using poetry](https://zenn.dev/keita_f/articles/4493e3cfd76aec)
- [SQLALCHEMY_DATABASE_URL_REFERENCE](https://stackoverflow.com/questions/71116549/sqlalchemy-exc-operationalerror-psycopg2-operationalerror-with-postgresql)
- [error reading bcrypt version ](https://github.com/langflow-ai/langflow/issues/1173)
