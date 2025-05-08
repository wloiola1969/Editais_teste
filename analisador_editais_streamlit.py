
import pandas as pd
import streamlit as st
import io

st.title("Analisador de Edital para Equipamentos de Radiologia")

# Upload dos arquivos
edital_file = st.file_uploader("Selecionar arquivo do Edital (.xlsx)", type="xlsx")
equip_file = st.file_uploader("Selecionar arquivo do Equipamento (.xlsx)", type="xlsx")
just_file = st.file_uploader("Selecionar arquivo de Justificativas (.xlsx)", type="xlsx")

def buscar_justificativa(justs, campo):
    match = justs[justs['Campo'] == campo]
    if not match.empty:
        return match.iloc[0]['Justificativa']
    return "Sem justificativa técnica cadastrada."

if st.button("Comparar"):
    if edital_file and equip_file and just_file:
        edital = pd.read_excel(edital_file)
        equipamento = pd.read_excel(equip_file)
        justs = pd.read_excel(just_file)

        resultado = []

        for i, row in edital.iterrows():
            item = row['Item']
            campo = row['Campo']
            req = str(row['Requisito'])
            esp = str(equipamento.loc[i, 'Especificação'])

            if pd.isna(req) or req.strip() == "":
                status = "Neutro"
                sugestao = "Item não informado."
            elif req == esp:
                status = "Atende"
                sugestao = "-"
            elif esp.replace(".", "").replace(",", "").isdigit() and req.replace(".", "").replace(",", "").isdigit():
                if float(esp.replace(",", ".")) > float(req.replace(",", ".")):
                    status = "Neutro"
                    sugestao = "Superior ao solicitado."
                else:
                    status = "Não Atende"
                    sugestao = buscar_justificativa(justs, campo)
            else:
                status = "Não Atende"
                sugestao = buscar_justificativa(justs, campo)

            resultado.append([item, campo, req, esp, status, sugestao])

        df_result = pd.DataFrame(resultado, columns=['Item', 'Campo', 'Edital', 'Equipamento', 'Status', 'Justificativa'])

        st.success("Comparação concluída!")
        st.dataframe(df_result)

        # Criar arquivo Excel em memória para download
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_result.to_excel(writer, index=False)
        output.seek(0)

        st.download_button(
            label="📥 Baixar resultado em Excel",
            data=output,
            file_name="resultado_comparativo.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.warning("Por favor, selecione todos os arquivos antes de comparar.")
