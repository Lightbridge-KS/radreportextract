from pathlib import Path
import docx

from ._utils import list_dir


def read_docx_dir(directory: Path, recursive=True) -> dict:
    """Reads all .docx files in a directory and returns a dictionary."""
    paths_ls = list_dir(directory, pattern="*.docx", recursive=recursive)
    stem_ls = [path.stem for path in paths_ls]
    doc_ls = [read_docx(path) for path in paths_ls]
    return dict(zip(stem_ls, doc_ls))
    

def read_docx(path: Path) -> str:
    """Reads the content of a .docx file and returns it as a string."""
    doc = docx.Document(path)
    doc_gen = (para.text for para in doc.paragraphs)
    return "".join(doc_gen)




