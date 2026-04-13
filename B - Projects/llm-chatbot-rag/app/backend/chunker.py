"""
# Permet de typer les listes
from typing import List

# Outil LangChain pour découper du texte intelligemment
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Type Document LangChain
from langchain_core.documents import Document


def split_documents(
    documents: List[Document],
    chunk_size: int = 1500,
    chunk_overlap: int = 80
) -> List[Document]:
    
    Cette fonction découpe des documents en chunks (morceaux de texte).

    Paramètres :
    - documents : liste de documents LangChain (pages PDF par exemple)
    - chunk_size : taille max d’un chunk
    - chunk_overlap : chevauchement entre chunks

    Retour :
    - liste de chunks (toujours des objets Document)
    

    # Si la liste est vide, on retourne directement une liste vide
    if not documents:
        return []

    # On crée un splitter intelligent
    text_splitter = RecursiveCharacterTextSplitter(

        # Taille max d’un chunk
        chunk_size=chunk_size,

        # Chevauchement entre chunks (important pour le contexte)
        chunk_overlap=chunk_overlap,

        # Ordre de découpage (du plus logique au plus brut)
        separators=["\n\n", "\n", ".", " ", ""]
    )

    # Découpe les documents en chunks
    chunks = text_splitter.split_documents(documents)

    return chunks
    """
import re
from typing import List
from langchain_core.documents import Document


def _merge_documents_text(documents: List[Document]) -> str:
    return "\n".join(doc.page_content for doc in documents if doc.page_content)


def _clean_perfume_chunk(text: str) -> str:
    """
    Nettoie un chunk parfum en supprimant certains artefacts du PDF.
    """

    # Supprime les numéros de page du type : — 10 —
    text = re.sub(r"^\s*—\s*\d+\s*—\s*$", "", text, flags=re.MULTILINE)

    # Supprime les titres de section du type : — CHANEL —
    text = re.sub(r"^\s*—\s*[A-ZÀ-ÖØ-Ý'&\.\-\s]+\s*—\s*$", "", text, flags=re.MULTILINE)

    # Supprime les espaces en fin de ligne
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)

    # Réduit les sauts de ligne multiples
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def split_documents(documents: List[Document]) -> List[Document]:
    if not documents:
        return []

    full_text = _merge_documents_text(documents)

    pattern = r"^#\d+\s*—\s*.*$"
    matches = list(re.finditer(pattern, full_text, flags=re.MULTILINE))

    if not matches:
        return [
            Document(
                page_content=_clean_perfume_chunk(full_text),
                metadata={
                    "source_type": "parfum_guide",
                    "chunk_type": "full_document_fallback"
                }
            )
        ]

    perfume_chunks: List[Document] = []

    for i, match in enumerate(matches):
        start_index = match.start()

        if i + 1 < len(matches):
            end_index = matches[i + 1].start()
        else:
            end_index = len(full_text)

        chunk_text = full_text[start_index:end_index].strip()

        if not chunk_text:
            continue

        chunk_text = _clean_perfume_chunk(chunk_text)

        number_match = re.search(r"#(\d+)", chunk_text)
        perfume_number = number_match.group(1) if number_match else None

        first_line = chunk_text.splitlines()[0].strip() if chunk_text.splitlines() else ""

        perfume_chunks.append(
            Document(
                page_content=chunk_text,
                metadata={
                    "source_type": "parfum_guide",
                    "chunk_type": "single_perfume",
                    "perfume_number": perfume_number,
                    "title_line": first_line
                }
            )
        )

    return perfume_chunks