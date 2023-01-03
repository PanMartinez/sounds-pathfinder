# --------------------- #
# ---- core image ----- #
# --------------------- #

# ------ python ------- #
FROM python:3.11 as builder

WORKDIR /spf-backend

COPY . .

RUN pip3 install poetry
RUN poetry config --local virtualenvs.in-project true  && poetry install


FROM python:3.11-alpine3.17

WORKDIR /spf-backend

COPY --from=builder /spf-backend /spf-backend
ENV PATH=/spf-backend/.venv/bin:$PATH

CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
