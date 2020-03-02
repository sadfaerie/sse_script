FROM python:3.6-slim

RUN pip3 install pipenv

WORKDIR /sse_script

COPY Pipfile ./
COPY Pipfile.lock ./

COPY README.md ./
COPY setup.py ./

ENV MONGO_HOST="mongo"

COPY src ./src

RUN set -ex && pipenv install --deploy --system
RUN pip install -e .

COPY . .

COPY start.sh ./start.sh
RUN chmod +x ./start.sh


CMD [ "./start.sh" ]