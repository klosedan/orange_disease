# Organge disease detection

The project can be run inside a devcontainer which is baded on Python 3.11 and is allowed to run with GPU acceleration.

## Environment

The recommended way is to start this workspace in a vscode devcontainer. The intial build of the container takes a few minutes. 

## Procedure

I created a few notebooks to analyze, train and validate the orange disease classification task:

1. data_analysis: Here I analyzed the data, checked sample sizes and plotted a few examples within the dataset.
2. mobile_net_v2: In this notebook, I trained the mobile net v2 Model on the classification task. I workd with a fixed train/validation split before training a final model.
3. cross_val_mobile_net_v2: At some point, I realized that cross validation might be a useful tool for the rather small dataset. Therefore, I started another notebook based on mobile_net_v2. 
4. model_validation: In this part, I validated the resulting models.
5. model_compression: In this part, I compressed the model using weights pruninig. 
5. captum: Finally, I got some insights into the decision making using captum. 

## Folder structure

The folders are structured as follows:

- data: Here the data images for the oranges can be found.
- notebooks: Here you can find the notebooks to analyse the data and train the models
- models: In this folder, the trained models are stored
- src: Some helper functions to read the data can be found here


## Needed times

1. Setup environment (90min): set up vscode devcontainer with hardware acceleration, download data files in postCreateCommand script
2. Data preprocessing (90min): Read in data, plot image resolution and number of images for each category.  
3. Initial training tries (180min): Build a model with a fixed train/validation split and try combinations of hyperparameters 
4. Cross validation (180min): I struggled some time to efficiently store training results in order to not run it again for every code change. 
5. Model compression (30min): I applied pruning to the model.  
6. Captum (60min): I used the libary to get some insights into the decision making.

## Open questions

- How to optimally save training results. I needed to retrain a lot and especcially with cross validation, it is very time consuming.
- 