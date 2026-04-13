import base64
from pathlib import Path

import streamlit as st

from app.backend.rag_pipeline import generate_answer


def get_base64_image(image_path: str) -> str:
    """
    Convertit une image locale en base64 pour l'afficher dans l'interface.
    """
    path = Path(image_path)

    if not path.exists():
        return ""

    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# ==========================================================
# CONFIG PAGE
# ==========================================================
st.set_page_config(
    page_title="Dubai Vie - Guide de Parfum",
    page_icon="✨",
    layout="wide"
)

logo_base64 = get_base64_image("app/frontend/assets/dubai_vie.png")


# ==========================================================
# CSS GLOBAL
# ==========================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

    :root {
        --gold: #b88a2a;
        --gold-soft: #d6b15a;
        --gold-dark: #8f6a22;
        --text: #6d5320;
        --text-soft: #8f7748;
        --border: rgba(184, 138, 42, 0.24);
        --card: rgba(255,255,255,0.82);
        --shadow: rgba(120, 90, 30, 0.10);
        --bg1: #faf8f3;
        --bg2: #f3efe7;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(255,255,255,0.95), rgba(248,245,239,0.96)),
            linear-gradient(135deg, var(--bg1), var(--bg2));
    }

    /* Effet marbre discret */
    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        opacity: 0.16;
        background-image:
            linear-gradient(
                115deg,
                rgba(180,180,180,0.10) 0%,
                rgba(255,255,255,0) 18%,
                rgba(180,180,180,0.08) 36%,
                rgba(255,255,255,0) 54%,
                rgba(180,180,180,0.07) 72%,
                rgba(255,255,255,0) 100%
            ),
            linear-gradient(
                70deg,
                rgba(170,170,170,0.05) 0%,
                rgba(255,255,255,0) 28%,
                rgba(170,170,170,0.06) 58%,
                rgba(255,255,255,0) 100%
            );
        z-index: 0;
    }

    .block-container {
        max-width: 920px;
        padding-top: 2rem;
        padding-bottom: 9rem;
        position: relative;
        z-index: 1;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ===== FIX COULEURS TEXTE ===== */
    body, p, span, div, label, li {
        color: var(--text) !important;
    }

    h1, h2, h3 {
        font-family: 'Cormorant Garamond', serif !important;
        color: var(--gold) !important;
        letter-spacing: 0.3px;
    }

    .hero-card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 28px;
        padding: 2.2rem 2rem 1.8rem 2rem;
        box-shadow: 0 14px 40px var(--shadow);
        backdrop-filter: blur(8px);
        margin-bottom: 1.5rem;
        text-align: center;
    }

    .logo-wrap {
        display: flex;
        justify-content: center;
        margin-bottom: 0.7rem;
    }

    .logo-wrap img {
        width: 120px;
        height: auto;
        object-fit: contain;
        display: block;
        filter: drop-shadow(0 6px 16px rgba(184, 138, 42, 0.14));
    }

    .brand-title {
        text-align: center;
        font-family: 'Cormorant Garamond', serif;
        color: var(--gold) !important;
        font-size: 4rem;
        font-weight: 700;
        line-height: 1;
        margin-bottom: 0.45rem;
    }

    .brand-subtitle {
        text-align: center;
        color: var(--gold-dark) !important;
        font-size: 1.08rem;
        margin-bottom: 0.8rem;
    }

    .brand-divider {
        width: 120px;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--gold-soft), transparent);
        margin: 0.8rem auto 1rem auto;
    }

    .intro-text {
        text-align: center;
        color: var(--text-soft) !important;
        font-style: italic;
        font-size: 1rem;
    }

    /* Messages chat */
    [data-testid="stChatMessage"] {
        background: rgba(255,255,255,0.78);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 1rem 1.1rem;
        box-shadow: 0 6px 20px rgba(120, 90, 30, 0.04);
    }

    [data-testid="stChatMessage"] * {
        color: var(--text) !important;
    }

    /* Bouton */
    .stButton button {
        background: linear-gradient(135deg, var(--gold-soft), var(--gold)) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.65rem 1.2rem !important;
        font-weight: 600 !important;
        box-shadow: 0 8px 18px rgba(184,138,42,0.18);
    }

    .stButton button:hover {
        filter: brightness(1.03);
    }

    /* Zone chat fixe et uniforme */
    section[data-testid="stChatInput"] {
        position: fixed;
        bottom: 18px;
        left: 50%;
        transform: translateX(-50%);
        width: min(860px, 82%);
        z-index: 999;
        background: transparent !important;
        border-top: none !important;
    }

    section[data-testid="stChatInput"] > div {
        background: rgba(255,255,255,0.97) !important;
        border: 1px solid var(--border) !important;
        border-radius: 22px !important;
        padding: 10px 12px !important;
        box-shadow: 0 12px 32px rgba(120, 90, 30, 0.13) !important;
    }

    section[data-testid="stChatInput"] textarea,
    section[data-testid="stChatInput"] input {
        background: transparent !important;
        border: none !important;
        color: var(--text) !important;
        font-size: 15px !important;
    }

    section[data-testid="stChatInput"] textarea::placeholder,
    section[data-testid="stChatInput"] input::placeholder,
    textarea::placeholder {
        color: #a88a55 !important;
        opacity: 1 !important;
    }

    section[data-testid="stChatInput"] button {
        background: linear-gradient(135deg, var(--gold-soft), var(--gold)) !important;
        color: white !important;
        border-radius: 50% !important;
        width: 42px !important;
        height: 42px !important;
        border: none !important;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# SESSION STATE
# ==========================================================
if "messages" not in st.session_state:
    st.session_state.messages = []


def submit_user_prompt(prompt_text: str):
    """
    Ajoute la question utilisateur, appelle le pipeline RAG,
    puis stocke la réponse dans l'historique.
    """
    if not prompt_text.strip():
        return

    st.session_state.messages.append({
        "role": "user",
        "content": prompt_text
    })

    try:
        result = generate_answer(
            question=prompt_text,
            chat_history=st.session_state.messages[:-1]
        )

        answer = result["answer"]

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        error_msg = f"Une erreur est survenue : {e}"
        st.session_state.messages.append({
            "role": "assistant",
            "content": error_msg
        })


# ==========================================================
# HEADER
# ==========================================================
st.markdown('<div class="hero-card">', unsafe_allow_html=True)

if logo_base64:
    st.markdown(
        f"""
        <div class="logo-wrap">
            <img src="data:image/png;base64,{logo_base64}" alt="Dubai Vie logo">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("Logo introuvable : place `dubai_vie.png` dans `app/frontend/assets/`.")

st.markdown('<div class="brand-title">Dubai Vie</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="brand-subtitle">Guide de parfum intelligent — luxe, élégance et recommandation sur mesure</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="brand-divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="intro-text">Trouvez votre signature olfactive parmi une sélection d’exception.</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)


# ==========================================================
# HISTORIQUE CONVERSATION
# ==========================================================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ==========================================================
# RESET
# ==========================================================
if st.button("Réinitialiser la conversation"):
    st.session_state.messages = []
    st.rerun()


# ==========================================================
# CHAT INPUT
# ==========================================================
user_prompt = st.chat_input("Décrivez le parfum que vous recherchez...")

if user_prompt:
    submit_user_prompt(user_prompt)
    st.rerun()