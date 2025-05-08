# 🩺 Analisador de Editais para Equipamentos de Radiologia

Este aplicativo permite comparar editais de equipamentos médicos com as especificações do seu equipamento, identificando se os requisitos são atendidos, neutros ou não atendidos, além de sugerir justificativas técnicas.

## 🚀 Como usar

1. Acesse o aplicativo online hospedado via [Streamlit Cloud](https://share.streamlit.io).
2. Faça upload dos três arquivos:
   - **Edital**: Lista de requisitos do edital (.xlsx)
   - **Equipamento**: Especificações do seu equipamento (.xlsx)
   - **Justificativas**: Sugestões técnicas para itens não conformes (.xlsx)
3. Clique em **"Comparar"**.
4. Visualize a análise e baixe o resultado em Excel.

## 📂 Arquivos de exemplo

- `edital_exemplo.xlsx`
- `equipamento_exemplo.xlsx`
- `justificativas_exemplo.xlsx`

## 🧠 Lógica de comparação

- **Atende**: Requisito exatamente igual.
- **Neutro**: Requisito ausente no edital ou especificação superior.
- **Não Atende**: Requisito exigido maior do que o disponível ou diferente (com justificativa técnica).

## 📸 Imagem de demonstração

![Demo](demo.png) <!-- Adicione uma captura de tela se desejar -->

---

## 🤖 Tecnologias

- Python
- Streamlit
- Pandas
- OpenPyXL

## 🧪 Desenvolvido por

Willian
