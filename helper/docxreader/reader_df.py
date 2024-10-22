import pandas as pd
from pandas import DataFrame
from pathlib import Path
import docx

from ._utils import list_dir
from .reader import read_docx

def read_docx_dir_df(directory: Path, recursive=True) -> pd.DataFrame:
    """Reads all .docx files in a directory and returns a pandas DataFrame."""
    paths_ls = list_dir(directory, pattern="*.docx", recursive=recursive)
    stem_ls = [path.stem for path in paths_ls]
    doc_ls = [read_docx(path) for path in paths_ls]
    return pd.DataFrame({"filename": stem_ls, "path": paths_ls, "content": doc_ls})