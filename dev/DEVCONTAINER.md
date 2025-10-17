# 🐳 DevContainer - Guia de Configuração

## 🏗️ Montando o Ambiente

Este repositório está organizado com um DevContainer para facilitar o desenvolvimento.
Para instanciá-lo no VS Code, são recomendadas as seguintes configurações:

## 🔧 Pré-requisitos

### 📦 Extensões Recomendadas

**Remote Development**
- **Nome:** Remote Development
- **ID:** `ms-vscode-remote.vscode-remote-extensionpack`
- **Descrição:** Pack de extensões que permite abrir qualquer pasta em um container, máquina remota ou WSL, aproveitando todos os recursos do VS Code
- **Publisher:** Microsoft
- **Link:** [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

### 🐳 Docker Engine

É **obrigatório** ter o Docker Engine instalado e configurado. Para mais informações sobre como instalar o Docker Engine em seu sistema operacional:

📖 **[Instruções de instalação do Docker Engine](https://docs.docker.com/engine/install/)**

## 🚀 Procedimento de Configuração

### ⚡ Passos para instanciar o projeto no VS Code:

1. **📥 Instale o pack de extensões** Remote Development
2. **📋 Clone/Fork** este repositório
3. **📂 Abra o diretório** deste repositório no VS Code como um projeto
4. **🔄 Execute o comando** `Dev Containers: Reopen in Container` 
   - Use a paleta de comandos: `F1` ou `Ctrl+Shift+P`

### ✅ Resultado

Após a compilação do container, o VS Code abrirá o repositório em um ambiente completamente encapsulado, executando diretamente de dentro do container conforme configurado nas definições do `/.devcontainer`.