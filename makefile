
.PHONY: help venv install sync run prod clean

# Variáveis com valores padrão e compatibilidade
PYTHON ?= python3
UV ?= uv
HOST ?= 0.0.0.0
ifneq (,$(wildcard .env))
PORT_FROM_ENV := $(shell grep -E '^PORT=' .env | head -n1 | cut -d'=' -f2 | tr -d '"')
endif
PORT ?= $(or $(PORT_FROM_ENV),8000)

ifeq ($(OS),Windows_NT)
IS_WINDOWS := 1
else
IS_WINDOWS :=
endif

# Comando padrão
help:
	@echo "Comandos disponíveis:"
	@echo "  make venv     - Mostra instruções para ativar o ambiente virtual (PowerShell/Unix)"
	@echo "  make install  - Instala as dependências com uv"
	@echo "  make sync     - Sincroniza as dependências com uv sync"
	@echo "  make run      - Executa o projeto em modo dev (uv run fastapi dev)"
	@echo "  make prod     - Executa o projeto em modo prod (uv run fastapi run)"
	@echo "  make clean    - Remove cache e arquivos temporários"
	@echo "  make help     - Mostra esta ajuda"

# Ativar ambiente virtual (apenas instruções)
venv:
	@echo "Para ativar o ambiente virtual, execute:" \
		&& if [ "$(IS_WINDOWS)" = "1" ]; then \
			echo ".venv\\Scripts\\Activate.ps1 (PowerShell)"; \
		else \
			echo "source .venv/bin/activate (Unix)"; \
		fi

# Instalar dependências
install:
	$(UV) install

# Sincronizar dependências
sync:
	$(UV) sync

# Executar o projeto dev e prod
run:
	$(UV) run fastapi dev app/startup.py --host $(HOST) --port $(PORT)

prod:
	$(UV) run fastapi run app/startup.py --host $(HOST) --port $(PORT)

# Limpar cache e arquivos temporários
clean:
	@if [ "$(IS_WINDOWS)" = "1" ]; then \
		powershell -NoProfile -Command "Get-ChildItem -Recurse -Force -Include '__pycache__' | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue; Get-ChildItem -Recurse -Force -Include '*.pyc','*.pyo','*.pyd','.coverage' | Remove-Item -Force -ErrorAction SilentlyContinue"; \
		rmdir /s /q build 2>nul || true; \
	else \
		find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true; \
		find . -type f -name '*.pyc' -delete || true; \
		find . -type f -name '*.pyo' -delete || true; \
		find . -type f -name '*.pyd' -delete || true; \
		find . -type f -name '.coverage' -delete || true; \
		find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true; \
	fi
