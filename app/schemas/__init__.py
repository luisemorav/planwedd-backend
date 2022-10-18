from pathlib import Path
from os import listdir
from importlib import import_module


path_parent = Path('./app/schemas')

for module in listdir(path_parent):
    if 'schema' in module:
        # print(module[inicio:fin:pasos])
        import_module(
            f'app.schemas.{module[:-3]}'
        )
