from __future__ import annotations

import itertools
import pkgutil

import pytest

import gh_workflows as pkg1

modules = (
    name
    for _, name, _ in itertools.chain(
        *(pkgutil.walk_packages(pkg.__path__, f"{pkg.__name__}.") for pkg in (pkg1,))
    )
)

ignore_modules: set[str] = set()


@pytest.mark.parametrize("import_name", modules)
def test_module_imports(import_name: str) -> None:
    if import_name in ignore_modules:
        return
    print(f"Importing {import_name}")
    __import__(import_name, fromlist=["_trash"])
