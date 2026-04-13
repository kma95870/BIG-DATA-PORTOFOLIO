# Permet de manipuler les chemins de fichiers et dossiers
from pathlib import Path

# Permet d'indiquer qu'une fonction retourne une liste
from typing import List

# Chargeur PDF LangChain
from langchain_community.document_loaders import PyPDFLoader

# Type Document de LangChain
from langchain_core.documents import Document


def load_pdf(file_path: str) -> List[Document]:
    """
    Charge un seul fichier PDF.

    Paramètre :
    - file_path : chemin vers le fichier PDF

    Retour :
    - une liste de documents LangChain
      (souvent un document par page)
    """
    # On transforme le chemin reçu en objet Path
    path = Path(file_path)

    # Vérifie que le fichier existe
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")

    # Vérifie qu'il s'agit bien d'un PDF
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Le fichier doit être un PDF : {file_path}")

    # Crée le loader PDF
    loader = PyPDFLoader(str(path))

    # Charge le contenu du PDF
    documents = loader.load()

    return documents


def load_pdfs_from_folder(folder_path: str) -> List[Document]:
    """
    Charge tous les PDF présents dans un dossier.

    Paramètre :
    - folder_path : chemin vers le dossier contenant les PDF

    Retour :
    - une liste de tous les documents/pages chargés
    """
    # On transforme le chemin reçu en objet Path
    folder = Path(folder_path)

    # Vérifie que le dossier existe
    if not folder.exists():
        raise FileNotFoundError(f"Dossier introuvable : {folder_path}")

    # On récupère tous les fichiers .pdf du dossier
    pdf_files = list(folder.glob("*.pdf"))

    # Si aucun PDF n'est trouvé, on lève une erreur
    if not pdf_files:
        raise ValueError(f"Aucun PDF trouvé dans : {folder_path}")

    # Liste qui contiendra toutes les pages de tous les PDF
    all_documents: List[Document] = []

    # On charge chaque PDF un par un
    for pdf_file in pdf_files:
        docs = load_pdf(str(pdf_file))
        all_documents.extend(docs)

    return all_documents