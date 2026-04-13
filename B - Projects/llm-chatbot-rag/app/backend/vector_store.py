"""""
# On importe une fonction qui permet de charger les variables du fichier .env
from dotenv import load_dotenv

# On importe le modèle d'embeddings OpenAI via LangChain
from langchain_openai import OpenAIEmbeddings

# FAISS = base vectorielle (stocke les vecteurs + permet recherche)
from langchain_community.vectorstores import FAISS

# Fonction qui charge tous les PDF du dossier data/raw
from app.backend.loader import load_pdfs_from_folder

# Fonction qui découpe les documents en chunks
from app.backend.chunker import split_documents

# Cette ligne charge les variables du fichier .env dans l'environnement Python
# Exemple : OPENAI_API_KEY devient accessible dans le code
load_dotenv()


def get_embedding_model():
    
    Cette fonction crée et retourne un modèle d'embeddings.

    Un modèle d'embeddings sert à transformer du texte en vecteur (liste de nombres),
    ce qui permet ensuite de faire de la recherche sémantique.
   

    # On choisit ici un modèle OpenAI pour créer les embeddings
    # "text-embedding-3-small" = bon compromis coût / performance
    return OpenAIEmbeddings(model="text-embedding-3-small")


def create_vector_store(chunks):
    
    Cette fonction crée une base vectorielle FAISS à partir des chunks.

    Étapes :
    1. Prendre les chunks (morceaux de texte)
    2. Les transformer en embeddings
    3. Les stocker dans FAISS
    

    # On récupère le modèle d’embeddings
    embeddings = get_embedding_model()

    # FAISS va :
    # - transformer chaque chunk en vecteur
    # - stocker ces vecteurs
    # - construire un index pour la recherche
    vector_store = FAISS.from_documents(chunks, embeddings)

    return vector_store


# Ce bloc s’exécute seulement si on lance ce fichier directement
if __name__ == "__main__":

    # Étape 1 — Charger les PDF
    docs = load_pdfs_from_folder("data/raw")

    # Étape 2 — Découper en chunks
    chunks = split_documents(docs)

    # On affiche des infos pour vérifier
    print(f"Nombre de pages chargées : {len(docs)}")
    print(f"Nombre de chunks générés : {len(chunks)}")

    # Étape 3 — Créer la base vectorielle
    vector_store = create_vector_store(chunks)

    # Message de validation
    print("Vector store FAISS créé avec succès.")
"""

# Permet de charger les variables d’environnement depuis le fichier .env
from dotenv import load_dotenv

# Permet de manipuler proprement les chemins de fichiers/dossiers
from pathlib import Path

# Modèle d’embeddings OpenAI : texte -> vecteur
from langchain_openai import OpenAIEmbeddings

# FAISS : base vectorielle pour stocker les embeddings et rechercher par similarité
from langchain_community.vectorstores import FAISS

# Type Document de LangChain
from langchain_core.documents import Document

# Fonction qui charge les PDF du dossier data/raw
from app.backend.loader import load_pdfs_from_folder

# Fonction qui découpe les documents en chunks
from app.backend.chunker import split_documents


# Charge les variables du fichier .env
load_dotenv()


def get_embedding_model():
    """
    Crée et retourne le modèle d'embeddings OpenAI.

    Ce modèle sert à transformer :
    - les chunks de texte
    - la question utilisateur
    en vecteurs numériques comparables mathématiquement.
    """
    return OpenAIEmbeddings(model="text-embedding-3-small")


def create_vector_store(chunks: list[Document]) -> FAISS:
    """
    Crée une base vectorielle FAISS à partir d’une liste de chunks.

    Étapes internes :
    1. calcul des embeddings pour chaque chunk
    2. stockage des vecteurs dans FAISS
    3. création d’un index de recherche
    """
    # On récupère le modèle d'embeddings
    embeddings = get_embedding_model()

    # FAISS calcule les embeddings et construit l'index
    vector_store = FAISS.from_documents(chunks, embeddings)

    return vector_store


def save_vector_store(vector_store: FAISS, folder_path: str = "data/vectorstore"):
    """
    Sauvegarde le vector store sur disque.

    Pourquoi ?
    Pour éviter de recalculer tous les embeddings à chaque lancement.
    """
    # On transforme le chemin en objet Path
    path = Path(folder_path)

    # On crée le dossier s’il n’existe pas
    path.mkdir(parents=True, exist_ok=True)

    # Sauvegarde locale du vector store
    vector_store.save_local(str(path))


def load_vector_store(folder_path: str = "data/vectorstore") -> FAISS:
    """
    Recharge un vector store sauvegardé sur disque.

    Cela permet de réutiliser la base vectorielle sans tout reconstruire.
    """
    # On prépare le chemin
    path = Path(folder_path)

    # Vérifie que le dossier existe
    if not path.exists():
        raise FileNotFoundError(f"Le dossier du vector store est introuvable : {folder_path}")

    # On recharge le modèle d'embeddings
    # IMPORTANT : il faut le même type d'embeddings qu’à la création
    embeddings = get_embedding_model()

    # Recharge FAISS depuis le disque
    vector_store = FAISS.load_local(
        str(path),
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


def similarity_search(query: str, vector_store: FAISS, k: int = 3) -> list[Document]:
    """
    Recherche les k chunks les plus proches de la question utilisateur.

    Paramètres :
    - query : question posée par l'utilisateur
    - vector_store : base vectorielle FAISS déjà créée
    - k : nombre de chunks à retourner

    Retour :
    - une liste de Documents pertinents
    """
    # Vérifie que la question n’est pas vide
    if not query.strip():
        raise ValueError("La requête utilisateur est vide.")

    # FAISS :
    # 1. transforme la question en embedding
    # 2. compare cet embedding aux embeddings stockés
    # 3. renvoie les chunks les plus proches
    results = vector_store.similarity_search(query, k=k)

    return results


if __name__ == "__main__":
    # ----------------------------
    # ÉTAPE 1 — Charger les PDF
    # ----------------------------
    docs = load_pdfs_from_folder("data/raw")

    # ----------------------------
    # ÉTAPE 2 — Découper en chunks
    # ----------------------------
    chunks = split_documents(docs)

    print(f"Nombre de pages chargées : {len(docs)}")
    print(f"Nombre de chunks générés : {len(chunks)}")

    # -----------------------------------------
    # ÉTAPE 3 — Créer le vector store en mémoire
    # -----------------------------------------
    vector_store = create_vector_store(chunks)
    print("Vector store FAISS créé avec succès.")

    # -----------------------------------------
    # ÉTAPE 4 — Sauvegarder le vector store
    # -----------------------------------------
    save_vector_store(vector_store)
    print("Vector store sauvegardé dans data/vectorstore.")

    # -----------------------------------------
    # ÉTAPE 5 — Recharger le vector store
    # -----------------------------------------
    loaded_vector_store = load_vector_store()
    print("Vector store rechargé avec succès.")

    # -----------------------------------------
    # ÉTAPE 6 — Tester une recherche sémantique
    # -----------------------------------------
    query = "De quoi parle ce document ?"

    results = similarity_search(query, loaded_vector_store, k=3)

    print(f"\nQuestion : {query}")
    print(f"Nombre de résultats trouvés : {len(results)}")

    # On affiche les résultats
    for i, doc in enumerate(results, start=1):
        print(f"\n--- Résultat {i} ---")
        print(doc.page_content[:700])  # extrait du texte
        print("\nMétadonnées :")
        print(doc.metadata)