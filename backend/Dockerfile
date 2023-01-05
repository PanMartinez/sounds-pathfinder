# --------------------- #
# ---- core image ----- #
# --------------------- #

FROM python:3.11 as builder

WORKDIR /spf-core

COPY . .

RUN pip3 install poetry
RUN poetry config --local virtualenvs.in-project true  && poetry install


FROM python:3.11-alpine3.17

WORKDIR /spf-core

COPY --from=builder /spf-core /spf-core
ENV PATH=/spf-core/.venv/bin:$PATH
