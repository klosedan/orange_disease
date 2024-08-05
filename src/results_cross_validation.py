
import numpy as np 
from typing import List

class ResultsCrossValidation:
    def __init__(self, num_folds: int, num_epochs: int):
        self._n_splits = num_folds
        self._num_epochs = num_epochs

        self.predictions = [[[] for _ in range(num_folds)] for _ in range(num_epochs)]
        self.labels = [[[] for _ in range(num_folds)] for _ in range(num_epochs)]
        self.losses = np.empty((num_epochs, num_folds))

    def getAccuracyEpoch(self,epoch: int)-> float:
        labels = self.getPredictionsEpoch(epoch)
        preds = self.getLabelsEpoch(epoch) 
        accuracy = sum(1 for elem1, elem2 in zip(labels, preds) if elem1 == elem2)/len(labels)
        return accuracy
    
    def getValidationLossEpoch(self, epoch: int) -> float:
        return np.mean(self.losses[epoch,:])

    def addLoss(self, fold: int, epoch: int, loss: float) -> None:
        self.losses[epoch, fold] = loss
    
    def getLossesEpoch(self, epoch: int):
        return self.losses[epoch,:]

    def addPredictions(self, fold: int, epoch: int, predictions: List):
        self.predictions[epoch][fold] = predictions

    def addLabels(self, fold: int, epoch: int, labels: List):
        self.labels[epoch][fold] = labels

    def getLabelsEpoch(self, epoch: int) -> List:
        ret = []
        for fold in range(self._n_splits):
            ret.extend(self.labels[epoch][fold])
        return ret
    
    def getLabelsFold(self, fold: int) -> List:
        ret = []
        for epoch in range(self._num_epochs):
            ret.extend(self.labels[epoch][fold])
        return ret
    
    def getPredictionsEpoch(self, epoch):
        ret = []
        for fold in range(self._n_splits):
            ret.extend(self.predictions[epoch][fold])
        return ret
    
    def getPredictionsFold(self, fold):
        ret = []
        for epoch in range(self._num_epochs):
            ret.extend(self.predictions[epoch][fold])
        return ret