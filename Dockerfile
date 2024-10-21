FROM python:3 AS app

RUN --mount=type=cache,target=/var/cache/apt \
	apt update && apt install --yes postgresql-client && apt autoclean

COPY pyproject.toml .

RUN --mount=type=cache,target=/root/.cache/pip \
	python3 -m pip install --upgrade pip poetry wheel
RUN --mount=type=cache,target=/root/.cache/pypoetry \
	poetry --version && \
	poetry config virtualenvs.create false && \
	poetry install -vv --no-interaction --no-root --no-ansi \
		--without=test

FROM app AS test

RUN --mount=type=cache,target=/root/.cache/pypoetry \
	poetry --version && \
	poetry config virtualenvs.create false && \
	poetry install -vv --no-interaction --no-root --no-ansi \
		--with=test

COPY entrypoint.sh /

WORKDIR /test

ENTRYPOINT ["/entrypoint.sh"]
