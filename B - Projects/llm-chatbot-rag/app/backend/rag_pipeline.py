"""
# Charge les variables d'environnement depuis le fichier .env
from dotenv import load_dotenv

# Modèle OpenAI utilisé pour générer la réponse finale
from langchain_openai import ChatOpenAI

# Fonctions internes du projet
from app.backend.vector_store import load_vector_store, similarity_search
from app.backend.prompt import build_prompt


# Charge les variables d'environnement
load_dotenv()


def format_context(documents) -> str:
    
    Transforme une liste de documents en un bloc de texte.

    Chaque chunk retrouvé est concaténé pour former
    le contexte qui sera envoyé au LLM.
    
    context_parts = []

    for i, doc in enumerate(documents, start=1):
        context_parts.append(f"[Extrait {i}]\n{doc.page_content}")

    return "\n\n".join(context_parts)


def generate_answer(question: str, k: int = 3) -> dict:
    
    Exécute le pipeline RAG complet.

    Étapes :
    1. recharge le vector store
    2. retrouve les chunks les plus pertinents
    3. construit le contexte
    4. construit le prompt
    5. interroge le LLM
    6. retourne la réponse + les sources
    

    # Recharge le vector store FAISS sauvegardé
    vector_store = load_vector_store()

    # Recherche des chunks les plus proches de la question
    retrieved_docs = similarity_search(question, vector_store, k=k)

    # Construit le contexte textuel à partir des chunks
    context = format_context(retrieved_docs)

    # Construit le prompt final
    prompt = build_prompt(context=context, question=question)

    # Initialise le modèle de génération
    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    # Génère la réponse
    response = llm.invoke(prompt)

    # On retourne un dictionnaire, pas une simple string
    return {
        "question": question,
        "answer": response.content,
        "sources": retrieved_docs
    }


if __name__ == "__main__":
    question = "De quoi parlent ces documents ?"

    result = generate_answer(question)

    print("\nQuestion :")
    print(result["question"])

    print("\nRéponse du chatbot :")
    print(result["answer"])

    print("\nNombre de sources retrouvées :")
    print(len(result["sources"]))


    """

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from app.backend.vector_store import load_vector_store, similarity_search
from app.backend.prompt import build_prompt

load_dotenv()


def format_context(documents) -> str:
    """
    Transforme les documents retrouvés en un bloc de texte exploitable par le LLM.
    """
    context_parts = []

    for i, doc in enumerate(documents, start=1):
        metadata = doc.metadata
        title_line = metadata.get("title_line", f"Extrait {i}")
        perfume_number = metadata.get("perfume_number", "inconnu")

        context_parts.append(
            f"[Extrait {i} | Parfum #{perfume_number} | {title_line}]\n{doc.page_content}"
        )

    return "\n\n".join(context_parts)


def format_history(chat_history: list[dict]) -> str:
    """
    Transforme l'historique de conversation en texte.
    """
    if not chat_history:
        return ""

    lines = []
    for message in chat_history:
        role = message.get("role", "")
        content = message.get("content", "")

        if role == "user":
            lines.append(f"Client : {content}")
        elif role == "assistant":
            lines.append(f"Conseiller Dubai Vie : {content}")

    return "\n".join(lines)


def generate_answer(question: str, chat_history: list[dict] | None = None, k: int = 4) -> dict:
    """
    Pipeline RAG complet avec historique conversationnel.
    """
    if chat_history is None:
        chat_history = []

    vector_store = load_vector_store()
    retrieved_docs = similarity_search(question, vector_store, k=k)

    context = format_context(retrieved_docs)
    history = format_history(chat_history)

    prompt = build_prompt(
        context=context,
        question=question,
        history=history
    )

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0.3
    )

    response = llm.invoke(prompt)

    return {
        "question": question,
        "answer": response.content,
        "sources": retrieved_docs
    }


if __name__ == "__main__":
    result = generate_answer("Je cherche un parfum élégant pour une soirée.")

    print(result["answer"])