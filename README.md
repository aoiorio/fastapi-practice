## This repository is for my practice of FastAPI
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

## 🚢 reference
- [FastAPI Introduction](https://zenn.dev/sh0nk/books/537bb028709ab9/)