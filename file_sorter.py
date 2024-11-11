import json, shutil
from pathlib import Path

folder_to_sort = Path("c:/xampp/htdocs/DEV/PYTHON/formation_python_trieur_de_fichiers/data/")
ref = Path(__file__).parent / "ref.json"

with open(ref, "r") as f:
    suffix_dict = json.load(f)

for file in folder_to_sort.iterdir():
    if file.suffix in suffix_dict:
        folder_to_create = folder_to_sort / suffix_dict[file.suffix]
    else:
        folder_to_create = folder_to_sort / "Autre"
        
    folder_to_create.mkdir(exist_ok=True)
    shutil.move(file, folder_to_create)