import json, pathlib
p = pathlib.Path("RetinaLiteClassifier.ipynb")
nb = json.loads(p.read_text())
nb.get("metadata", {}).pop("widgets", None)   # drop the bad block
p.write_text(json.dumps(nb, indent=2))
