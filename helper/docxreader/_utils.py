from pathlib import Path

def list_dir(directory, pattern: str = "", recursive = True) -> list[Path]:
    path = Path(directory)
    if recursive:
        return list(path.rglob(pattern))
    else:
        return list(path.glob(pattern))
    