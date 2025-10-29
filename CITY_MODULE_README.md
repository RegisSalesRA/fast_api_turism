# Módulo CRUD de Cidades - Documentação

## 📋 Resumo

Foi implementado um módulo CRUD completo para **Cidades** seguindo a Clean Architecture do projeto, com todas as funcionalidades solicitadas incluindo filtro por nome.

---

## 🏗️ Arquitetura Implementada

### 1. **Domain Layer** (Camada de Domínio)

#### Entity
- **Arquivo**: `app/domain/entities/city_entity.py`
- **Descrição**: Define a entidade de negócio City
- **Campos**:
  - `id`: Identificador único (opcional para criação)
  - `name`: Nome da cidade
  - `state`: Estado
  - `country`: País (padrão: "Brasil")
  - `description`: Descrição opcional

#### Repository Interface
- **Arquivo**: `app/domain/repositories/city_repository.py`
- **Descrição**: Interface abstrata que define os contratos do repositório
- **Métodos**:
  - `create()`: Criar cidade
  - `list_all()`: Listar todas
  - `get_by_id()`: Buscar por ID
  - `update()`: Atualizar cidade
  - `delete()`: Deletar cidade
  - `search_by_name()`: **Buscar por nome (filtro)**

#### Use Case
- **Arquivo**: `app/domain/usecases/city_usecase.py`
- **Descrição**: Regras de negócio e validações
- **Funcionalidades**:
  - Validação de campos obrigatórios
  - Tratamento de erros (NotFoundError)
  - Orquestração das operações do repositório

---

### 2. **Data Layer** (Camada de Dados)

#### Model
- **Arquivo**: `app/data/models/city_model.py`
- **Descrição**: Modelo SQLAlchemy para persistência
- **Tabela**: `cities`
- **Campos**:
  - `id`: Primary Key
  - `name`: String(255)
  - `state`: String(100)
  - `country`: String(100) - default "Brasil"
  - `description`: Text (nullable)
  - `created_at`: Timestamp automático
  - `updated_at`: Timestamp automático

#### Repository Implementation
- **Arquivo**: `app/data/repository/city_repository_impl.py`
- **Descrição**: Implementação concreta do repositório usando SQLAlchemy
- **Funcionalidades**:
  - CRUD completo
  - **Filtro por nome usando ILIKE** (case-insensitive)
  - Paginação (limit/offset)

---

### 3. **Infrastructure Layer** (Camada de Infraestrutura)

#### Schemas (Request)
- **Arquivo**: `app/infrastructure/api/schemas/city/request/create_city.py`
  - Schema para criação de cidade
  - Validações com Pydantic

- **Arquivo**: `app/infrastructure/api/schemas/city/request/update_city.py`
  - Schema para atualização de cidade

#### Schemas (Response)
- **Arquivo**: `app/infrastructure/api/schemas/city/response/city_detail.py`
  - Schema de resposta com todos os dados da cidade

#### Router
- **Arquivo**: `app/infrastructure/api/routes/city_router.py`
- **Endpoints**:
  - `GET /cities/` - Listar todas as cidades
  - `GET /cities/search/?name={nome}` - **Buscar por nome**
  - `GET /cities/{city_id}` - Buscar por ID
  - `POST /cities/` - Criar cidade
  - `PUT /cities/{city_id}` - Atualizar cidade
  - `DELETE /cities/{city_id}` - Deletar cidade

---

### 4. **Core Layer** (Configuração)

#### Dependency Injection
- **Arquivo**: `app/core/injection_dependencies.py`
- **Função adicionada**: `get_city_usecase()`
- **Descrição**: Injeta dependências (repository → usecase)

---

### 5. **Database Migration**

#### Migration
- **Arquivo**: `migrations/versions/20251029_1843_create_cities_table.py`
- **Descrição**: Cria a tabela `cities` no banco de dados
- **Status**: ✅ Aplicada com sucesso

---

## 🚀 Como Usar

### 1. Iniciar o servidor
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Acessar documentação interativa
```
http://localhost:8000/docs
```

### 3. Exemplos de uso

#### Criar cidade
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

#### Buscar por nome (FILTRO)
```bash
curl -X GET "http://localhost:8000/cities/search/?name=São"
```

#### Listar todas
```bash
curl -X GET "http://localhost:8000/cities/"
```

#### Buscar por ID
```bash
curl -X GET "http://localhost:8000/cities/1"
```

#### Atualizar
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

#### Deletar
```bash
curl -X DELETE "http://localhost:8000/cities/1"
```

---

## 📁 Arquivos Criados/Modificados

### Arquivos Criados (9 novos arquivos):
1. `app/data/models/city_model.py`
2. `app/domain/entities/city_entity.py`
3. `app/domain/repositories/city_repository.py`
4. `app/data/repository/city_repository_impl.py`
5. `app/domain/usecases/city_usecase.py`
6. `app/infrastructure/api/schemas/city/request/create_city.py`
7. `app/infrastructure/api/schemas/city/request/update_city.py`
8. `app/infrastructure/api/schemas/city/response/city_detail.py`
9. `app/infrastructure/api/routes/city_router.py`

### Arquivos Modificados (4 arquivos):
1. `app/core/injection_dependencies.py` - Adicionada função `get_city_usecase()`
2. `main.py` - Registrado router de cities
3. `app/data/models/__init__.py` - Importado CityModel
4. `migrations/env.py` - Importado CityModel para migrations

### Migration Criada:
1. `migrations/versions/20251029_1843_create_cities_table.py`

---

## ✅ Funcionalidades Implementadas

- ✅ **CREATE** - Criar nova cidade
- ✅ **READ** - Listar todas as cidades
- ✅ **READ** - Buscar cidade por ID
- ✅ **UPDATE** - Atualizar cidade existente
- ✅ **DELETE** - Deletar cidade
- ✅ **SEARCH** - **Filtrar cidades por nome** (case-insensitive)

---

## 🎯 Padrões Seguidos

1. **Clean Architecture** - Separação clara de responsabilidades
2. **Dependency Injection** - Inversão de dependências
3. **Repository Pattern** - Abstração da camada de dados
4. **Use Case Pattern** - Lógica de negócio isolada
5. **DTO Pattern** - Schemas Pydantic para request/response
6. **Consistência** - Seguiu exatamente o padrão dos módulos existentes (Point Turism e Category)

---

## 🔍 Detalhes do Filtro por Nome

O filtro por nome foi implementado usando:
- **Endpoint**: `GET /cities/search/?name={nome}`
- **Método**: `search_by_name()` no repository
- **SQL**: Usa `ILIKE` para busca case-insensitive
- **Comportamento**: Busca parcial (ex: "São" encontra "São Paulo")

**Exemplo de código:**
```python
def search_by_name(self, name: str) -> List[CityEntity]:
    cities = self.db.query(CityModel)\
                    .filter(CityModel.name.ilike(f"%{name}%"))\
                    .all()
    return [CityEntity(...) for c in cities]
```

---

## 📊 Estrutura do Banco de Dados

```sql
CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL DEFAULT 'Brasil',
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL
);

CREATE INDEX ix_cities_id ON cities(id);
```

---

## 🎉 Conclusão

O módulo CRUD de Cidades foi implementado com sucesso, seguindo todos os padrões e arquitetura do projeto. Todas as funcionalidades solicitadas estão funcionando, incluindo o **filtro por nome**.

