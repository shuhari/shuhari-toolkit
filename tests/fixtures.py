import os

from shuhari_toolkit.fileutils import relative_of


def ensure_var_folder():
    var_path = relative_of(__file__, '../var')
    os.makedirs(var_path, exist_ok=True)
    return var_path


def get_var_path(relative_path: str) -> str:
    return os.path.join(ensure_var_folder(), relative_path)
