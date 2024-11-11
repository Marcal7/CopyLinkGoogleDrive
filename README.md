# 📸 CopyLinkGoogleDrive 🗂️

## 🚀 Descrição
O projeto **CopyLinkGoogleDrive** tem como objetivo automatizar o processo de copiar os links das fotos armazenadas no Google Drive. Utilizando a biblioteca Python `pyautogui`, este projeto permite a interação com a interface do Google Drive para selecionar, copiar e organizar os links de várias imagens de forma eficiente e prática. Ideal para quem precisa coletar múltiplos links de fotos de forma rápida e automatizada.

## 🛠️ Funcionalidades

- **Automação de Clique**: Clica automaticamente no botão de **compartilhar** e **copiar link** para cada imagem.
- **Navegação Rápida**: Permite navegar para a próxima foto usando a tecla **seta para a direita**.
- **Armazenamento de Links**: Coleta os links e armazena em um arquivo de texto, pronto para ser utilizado posteriormente.

## 💡 Como Funciona

1. **Clique Duplo**: O script clica automaticamente na foto para abrir o menu de compartilhamento.
2. **Copiar Link**: Clica em "Compartilhar" e seleciona "Copiar link" da foto.
3. **Armazenamento**: O link copiado é salvo em um arquivo de texto (`ListLink.txt`).
4. **Navegação**: O script avança para a próxima foto automaticamente.

## 🛠️ Requisitos

Para rodar este projeto, você precisará de:

- Python 3.6 ou superior
- Bibliotecas Python:
  - `pyautogui` 🎮
  - `pyperclip` 📋
  - `numpy` ➗ (para manipulação de dados)
  - `pandas` 📊

Para instalar as dependências, basta executar:

```bash
pip install pyautogui pyperclip numpy pandas

