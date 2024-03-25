# download python 3.9 for executing
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
# --reload means that when we changed code, uvicorn server will reload immediately
ENTRYPOINT ["poetry", "run", "uvicorn", "books:app", "--host", "0.0.0.0", "--reload"]