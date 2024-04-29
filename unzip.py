import zipfile
with zipfile.ZipFile("Archive.zip", 'r') as zip_ref:
    zip_ref.extractall("./unzipped_archive")

with zipfile.ZipFile("./unzipped_archive/resources/gdelt_persist_dir.zip", 'r') as zip_ref:
    zip_ref.extractall("./unzipped_archive/resources/")