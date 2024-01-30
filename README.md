# file-backup

## Version française

Il s'agit d'un utilitaire python qui permet de sauvegarder des fichiers d'un dossier vers un autre dossier. 
Il est possible de spécifier le dossier source, le dossier de destination, le temps d'attente entre chaque sauvegarde.

Le fichier config/params.json

{
    "folder_to_backup": "",
    "folder_of_backup": "",
    "time_interval": 5
}

folder_to_backup : dossier source
folder_of_backup : dossier de destination
time_interval : temps d'attente entre chaque sauvegarde

Le fichier fb.py permet de lancer le script.
Le fichier restore.py permet de restaurer les fichiers sauvegardés.

## Installation

```bash
git clone git@github.com:carion21/file-backup.git
cd file-backup
pip install -r requirements.txt
```

## Lancement

```bash
python fb.py
```

## Lancement avec nohup
    
```bash
nohup python fb.py &
```

## Configuration

```bash
vim config/params.json
```

## Restauration

```bash
python restore.py
```

## Licence
[MIT](https://choosealicense.com/licenses/mit/)

## Version anglaise

This is a python utility that allows you to back up files from one folder to another folder.
It is possible to specify the source folder, the destination folder, the waiting time between each backup.

The config / params.json file

{
    "folder_to_backup": "",
    "folder_of_backup": "",
    "time_interval": 5
}

folder_to_backup: source folder
folder_of_backup: destination folder
time_interval: waiting time between each backup

The fb.py file allows you to launch the script.
The restore.py file allows you to restore the backed up files.

## Installation

```bash
git clone 
cd file-backup
pip install -r requirements.txt
```

## Launch

```bash
python fb.py
```

## Launch with nohup

```bash
nohup python fb.py &
```

## Configuration

```bash
vim config/params.json
```

## Restoration

```bash
python restore.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

