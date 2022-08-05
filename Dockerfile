FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# set path to our python api file
ENV MODULE_NAME="ipchecker.app"
# copy contents of project into docker
COPY ./ /app
# install poetry
RUN pip install poetry
# disable virtualenv for peotry
RUN poetry config virtualenvs.create false
# install dependencies
RUN poetry install

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]