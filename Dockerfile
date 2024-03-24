# download python 3.9
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

# specify the directory that I'll execute the below commands
WORKDIR /src

# install poetry using pip
RUN pip install poetry

# if it exists, copy the poetry's definition file
COPY pyproject.toml* poetry.lock* ./

# install libraries using poetry
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# start server of uvicorn
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]