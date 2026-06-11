import streamlit as st
import os
import base64

# ── Configuração da página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Download",
    page_icon="📱",
    layout="centered",
)

# ── CSS personalizado ───────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #f5faf6 !important;
    }

    /* Fundo da página */
    .stApp {
        background-color: #f5faf6;
    }

    .block-container {
        padding-top: 3rem;
        padding-bottom: 2rem;
        max-width: 520px;
    }

    /* Logo — fora do card, centralizada e maior */
    .logo-wrapper {
        text-align: center;
        margin-bottom: 1.75rem;
    }

    .logo-wrapper img {
        max-height: 100px;
        max-width: 280px;
        object-fit: contain;
    }

    /* Card */
    .download-card {
        background: #ffffff;
        border: 1px solid #d4eadb;
        border-radius: 18px;
        padding: 2.5rem 2.5rem 2rem;
        text-align: center;
        box-shadow: 0 6px 28px rgba(34, 139, 74, 0.08);
    }

    /* Título */
    .file-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1a3d27;
        margin-bottom: 0.4rem;
    }

    /* Metadados */
    .file-meta {
        font-size: 0.85rem;
        color: #6a9e7a;
        margin-bottom: 1.5rem;
        letter-spacing: 0.01em;
    }

    /* Descrição */
    .file-desc {
        color: #4a6655;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }

    /* Divider */
    .divider {
        border: none;
        border-top: 1px solid #e8f3ec;
        margin: 1.25rem 0;
    }

    /* Rodapé */
    .footer-note {
        font-size: 0.76rem;
        color: #a8c4b0;
        margin-top: 1.75rem;
        text-align: center;
    }

    /* Botão verde */
    .stDownloadButton > button {
        background: #228b4a !important;
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
        background: #1a6e3a !important;
    }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# ▸ CONFIGURAÇÃO — edite aqui
# ══════════════════════════════════════════════════════════════════════════════

ARQUIVO_PATH = "app_tellus.apk" 
ARQUIVO_NOME = "app_tellus.apk" 
TITULO       = "Baixar aplicativo Tellus" 
DESCRICAO    = "Clique no botão abaixo para baixar o aplicativo." 
ICONE        = "📱" 
MIME_TYPE    = "application/vnd.android.package-archive" 
LOGO_PATH    = "logo.png"

# ══════════════════════════════════════════════════════════════════════════════


def formatar_tamanho(bytes_: int) -> str:
    if bytes_ < 1024:
        return f"{bytes_} B"
    elif bytes_ < 1024 ** 2:
        return f"{bytes_ / 1024:.1f} KB"
    else:
        return f"{bytes_ / 1024 ** 2:.1f} MB"


def logo_base64(path: str) -> str | None:
    """Lê a logo e retorna como data URI base64."""
    if not path or not os.path.exists(path):
        return None
    ext = os.path.splitext(path)[1].lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "svg": "image/svg+xml"}.get(ext, "image/*")
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f"data:{mime};base64,{data}"


# ── Card + Logo (tudo em HTML puro para evitar elementos extras do Streamlit) ─
logo_uri = logo_base64(LOGO_PATH)
logo_html = f'<div class="logo-wrapper"><img src="{logo_uri}" alt="Logo"></div>' if logo_uri else ""

st.markdown(f"""
{logo_html}
<div class="download-card">
<div class="file-title">{TITULO}</div>
""", unsafe_allow_html=True)

if os.path.exists(ARQUIVO_PATH):
    tamanho  = os.path.getsize(ARQUIVO_PATH)
    extensao = os.path.splitext(ARQUIVO_NOME)[1].upper().lstrip(".")
    st.markdown(
        f'<div class="file-meta">{extensao} &nbsp;·&nbsp; {formatar_tamanho(tamanho)}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(f'<p class="file-desc">{DESCRICAO}</p>', unsafe_allow_html=True)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    with open(ARQUIVO_PATH, "rb") as f:
        st.download_button(
            label="⬇️  Baixar aplicativo",
            data=f,
            file_name=ARQUIVO_NOME,
            mime=MIME_TYPE,
        )
else:
    st.markdown(
        '<div class="file-meta" style="color:#c0392b;">Arquivo não encontrado.<br>'
        f'Coloque <code>{ARQUIVO_PATH}</code> na mesma pasta do app.</div>',
        unsafe_allow_html=True,
    )

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<p class="footer-note">O download é direto — nenhum dado é coletado.</p>',
    unsafe_allow_html=True,
)