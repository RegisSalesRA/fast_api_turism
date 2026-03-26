# Estágio 1: Builder
FROM python:3.12-alpine AS builder

WORKDIR /app

# Adicionamos dependências de compilação necessárias
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev python3-dev

COPY requirements.txt .

# Criamos o usuário aqui também para garantir o caminho correto do --user
RUN adduser -D -u 1000 appuser
USER appuser

RUN pip install --no-cache-dir --user -r requirements.txt

# Estágio 2: Final
FROM python:3.12-alpine

WORKDIR /app

# CORREÇÃO: libffi-libs -> libffi
RUN apk add --no-cache libffi openssl libstdc++

RUN adduser -D -u 1000 appuser

# Copia os pacotes instalados no estágio anterior
COPY --from=builder --chown=appuser:appuser /home/appuser/.local /home/appuser/.local
COPY --chown=appuser:appuser . .

USER appuser

# Garante que o Python encontre os pacotes e os binários (como o uvicorn)
ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONPATH=/home/appuser/.local/lib/python3.12/site-packages \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

# Ajustado para procurar o app dentro da pasta 'app' se o seu main.py estiver lá, 
# ou 'main:app' se estiver na raiz como mostra o seu 'ls'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]