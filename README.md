# Organge disease detection

The project can be run inside a devcontainer which is baded on Python 3.11 and is allowed to run with GPU acceleration.

## Environment

The recommended way is to start this workspace in a vscode devcontainer. The intial build of the container takes up a few minutes. 

## Procedure

I created a few notebooks to analyze, train and validate the orange disease classification task:

1. data_analysis: Here I analyzed the data, checked sample sizes and plotted a few examples within the dataset.
2. mobile_net_v2: In this notebook, I trained the mobile net v2 Model on the classification task. 
3. cross_val_mobile_net_v2: At some point, I realized that I cross validation might be a useful tool for the rather small dataset. Therefore, I started another notebook based on mobile_net_v2. 
4. model_validation: In this part I validated the resulting models.

## Folder structure

The folders are structured as follows:

- data: Here the data images for the oranges can be found. The folders structure the images into fresh, ??
- notebooks: Here you can find the notebooks to analyse the data and train the models
- models: In this folder, the trained models are stored


## Needed times

1. Setup environment (90min): set up vscode devcontainer with hardware acceleration, download data files in postCreateCommand script
2. Data preprocessing (90min): Read in data, plot image resolution and number of images for each category.  
3. Initial training tries (180min): Build a model with a fixed train/validation split and try combinations of hyperparameters 