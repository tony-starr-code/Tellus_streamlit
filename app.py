import streamlit as st
import os

# ── Configuração da página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Download",
    page_icon="⬇️",
    layout="centered",
)

# ── CSS personalizado ───────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Importa fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Remove padding padrão do Streamlit */
    .block-container {
        padding-top: 4rem;
        padding-bottom: 2rem;
        max-width: 560px;
    }

    /* Card central */
    .download-card {
        background: #ffffff;
        border: 1px solid #e8e8e8;
        border-radius: 16px;
        padding: 3rem 2.5rem;
        text-align: center;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
    }

    /* Ícone grande */
    .file-icon {
        font-size: 4rem;
        line-height: 1;
        margin-bottom: 1.25rem;
    }

    /* Título */
    .file-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #111111;
        margin-bottom: 0.5rem;
    }

    /* Metadados (tamanho, tipo) */
    .file-meta {
        font-size: 0.875rem;
        color: #888888;
        margin-bottom: 2rem;
        letter-spacing: 0.01em;
    }

    /* Divider */
    .divider {
        border: none;
        border-top: 1px solid #f0f0f0;
        margin: 1.5rem 0;
    }

    /* Rodapé */
    .footer-note {
        font-size: 0.78rem;
        color: #bbbbbb;
        margin-top: 2rem;
        text-align: center;
    }

    /* Botão de download do Streamlit — sobrescreve estilo padrão */
    .stDownloadButton > button {
        background: #111111 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.75rem 2rem !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.02em !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: background 0.2s ease !important;
    }

    .stDownloadButton > button:hover {
        background: #333333 !important;
    }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# ▸ CONFIGURAÇÃO — edite aqui
# ══════════════════════════════════════════════════════════════════════════════

ARQUIVO_PATH   = "meu_arquivo.pdf"   # caminho do arquivo (relativo ao app.py)
ARQUIVO_NOME   = "meu_arquivo.pdf"   # nome que o usuário verá ao baixar
TITULO         = "Relatório Mensal"  # título exibido na página
DESCRICAO      = "Clique no botão abaixo para baixar o arquivo."
ICONE          = "📄"               # emoji usado como ícone do arquivo
MIME_TYPE      = "application/pdf"   # tipo MIME (ex: "text/csv", "application/zip")

# ══════════════════════════════════════════════════════════════════════════════


def formatar_tamanho(bytes_: int) -> str:
    """Converte bytes em string legível (KB / MB)."""
    if bytes_ < 1024:
        return f"{bytes_} B"
    elif bytes_ < 1024 ** 2:
        return f"{bytes_ / 1024:.1f} KB"
    else:
        return f"{bytes_ / 1024 ** 2:.1f} MB"


# ── Layout ──────────────────────────────────────────────────────────────────
st.markdown('<div class="download-card">', unsafe_allow_html=True)

st.markdown(f'<div class="file-icon">{ICONE}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="file-title">{TITULO}</div>', unsafe_allow_html=True)

# Verifica se o arquivo existe e exibe metadados
if os.path.exists(ARQUIVO_PATH):
    tamanho = os.path.getsize(ARQUIVO_PATH)
    extensao = os.path.splitext(ARQUIVO_NOME)[1].upper().lstrip(".")
    st.markdown(
        f'<div class="file-meta">{extensao} &nbsp;·&nbsp; {formatar_tamanho(tamanho)}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(f'<p style="color:#555;font-size:0.9rem;margin-bottom:1.5rem;">{DESCRICAO}</p>', unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    with open(ARQUIVO_PATH, "rb") as f:
        st.download_button(
            label="⬇️  Baixar arquivo",
            data=f,
            file_name=ARQUIVO_NOME,
            mime=MIME_TYPE,
        )

else:
    # Arquivo não encontrado — exibe aviso claro
    st.markdown(
        '<div class="file-meta" style="color:#e05555;">Arquivo não encontrado.<br>'
        f'Verifique se <code>{ARQUIVO_PATH}</code> existe na mesma pasta do app.</div>',
        unsafe_allow_html=True,
    )

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<p class="footer-note">O download é direto — nenhum dado é coletado.</p>',
    unsafe_allow_html=True,
)
