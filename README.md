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
- If you want to add a package, you can exec this command
```shell
# login to fastapi-practice
$ docker-compose exec fastapi-practice /bin/bash
# Then you can execute it
$ poetry add {the name of package}
```
<br>

## 🚢 references
- [FastAPI Introduction](https://zenn.dev/sh0nk/books/537bb028709ab9/)
- [What is poetry](https://qiita.com/nilwurtz/items/0e5b8382757ccad9a56c)
- [How to add a package by using poetry](https://zenn.dev/rihito/articles/7b48821e4a3f74)
- [Similar article of Udemy course](https://qiita.com/yamarao/items/6889adfd4b484b7b5e11)
- [How to move to deferent directory like cd](https://qiita.com/rururu_kenken/items/8b5862e54fbe156a8cb8)