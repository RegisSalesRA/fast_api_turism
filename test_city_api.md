# Testes da API de Cidades

## Endpoints Disponíveis

### 1. Listar todas as cidades
```bash
GET http://localhost:8000/cities/
```

**Exemplo com curl:**
```bash
curl -X GET "http://localhost:8000/cities/"
```

---

### 2. Buscar cidades por nome
```bash
GET http://localhost:8000/cities/search/?name={nome}
```

**Exemplo com curl:**
```bash
curl -X GET "http://localhost:8000/cities/search/?name=São"
```

---

### 3. Buscar cidade por ID
```bash
GET http://localhost:8000/cities/{city_id}
```

**Exemplo com curl:**
```bash
curl -X GET "http://localhost:8000/cities/1"
```

---

### 4. Criar nova cidade
```bash
POST http://localhost:8000/cities/
Content-Type: application/json

{
  "name": "São Paulo",
  "state": "SP",
  "country": "Brasil",
  "description": "Maior cidade do Brasil"
}
```

**Exemplo com curl:**
```bash
curl -X POST "http://localhost:8000/cities/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "São Paulo",
    "state": "SP",
    "country": "Brasil",
    "description": "Maior cidade do Brasil"
  }'
```

---

### 5. Atualizar cidade
```bash
PUT http://localhost:8000/cities/{city_id}
Content-Type: application/json

{
  "name": "São Paulo",
  "state": "SP",
  "country": "Brasil",
  "description": "Capital financeira do Brasil"
}
```

**Exemplo com curl:**
```bash
curl -X PUT "http://localhost:8000/cities/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "São Paulo",
    "state": "SP",
    "country": "Brasil",
    "description": "Capital financeira do Brasil"
  }'
```

---

### 6. Deletar cidade
```bash
DELETE http://localhost:8000/cities/{city_id}
```

**Exemplo com curl:**
```bash
curl -X DELETE "http://localhost:8000/cities/1"
```

---

## Exemplos de Teste Completo

### Criar várias cidades:

```bash
# Rio de Janeiro
curl -X POST "http://localhost:8000/cities/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Rio de Janeiro",
    "state": "RJ",
    "country": "Brasil",
    "description": "Cidade maravilhosa"
  }'

# Belo Horizonte
curl -X POST "http://localhost:8000/cities/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Belo Horizonte",
    "state": "MG",
    "country": "Brasil",
    "description": "Capital mineira"
  }'

# Salvador
curl -X POST "http://localhost:8000/cities/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Salvador",
    "state": "BA",
    "country": "Brasil",
    "description": "Primeira capital do Brasil"
  }'
```

### Buscar por nome:

```bash
# Buscar cidades com "Rio" no nome
curl -X GET "http://localhost:8000/cities/search/?name=Rio"

# Buscar cidades com "Belo" no nome
curl -X GET "http://localhost:8000/cities/search/?name=Belo"
```

---

## Documentação Interativa

Acesse a documentação Swagger em:
```
http://localhost:8000/docs
```

Ou a documentação ReDoc em:
```
http://localhost:8000/redoc
```

