mkdir -p data
mkdir -p models

# Donwload and unzip the data
kaggle datasets download -d jonathansilva2020/orange-diseases-dataset -p data
unzip -u data/orange-diseases-dataset.zip -d data