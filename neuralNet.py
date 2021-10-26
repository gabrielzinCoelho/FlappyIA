import numpy as np
import scipy.special
import random

from constants import *

class NeuralNetwork():

    def __init__(self, numInput, numHidden, numOutput): 
        self.numInput = numInput
        self.numHidden = numHidden
        self.numOutput = numOutput
        self.weightInputHidden = np.random.uniform(-0.5, 0.5, size = (numHidden, numInput))
        self.weightHiddenOutput = np.random.uniform(-0.5, 0.5, size = (numOutput, numHidden))
        self.activateFunction = lambda x: scipy.special.expit(x)

    def getOutputs(self, inputList):
        inputs = np.array(inputList, ndmin = 2).T
        hiddenInputs = np.dot(self.weightInputHidden, inputs)
        hiddenOutputs = self.activateFunction(hiddenInputs)

        finalInputs = np.dot(self.weightHiddenOutput, hiddenOutputs)
        finalOutputs = self.activateFunction(finalInputs)

        return finalOutputs

    def getMaxValue(self, inputList):
        outputs = self.getOutputs(inputList)
        return np.max(outputs)

    def modifyWeights(self):
        NeuralNetwork.modifyArray(self.weightInputHidden)
        NeuralNetwork.modifyArray(self.weightHiddenOutput)

    def createMixedWeights(self, nnet1, nnet2):
        self.weightInputHidden = NeuralNetwork.getMixFromArrays(nnet1.weightInputHidden, nnet2.weightInputHidden)
        self.weightHiddenOutput = NeuralNetwork.getMixFromArrays(nnet1.weightHiddenOutput, nnet2.weightHiddenOutput)

    def modifyArray(array):
        for x in np.nditer(array, op_flags = ["readwrite"]):
            if random.random() < mutationWeightModifyChance:
                x[...] = np.random.random_sample() - 0.5
    
    def getMixFromArrays(array1, array2):
        totalEntries = array1.size
        numRows = array1.shape[0]
        numCollumns = array1.shape[1]

        numToTake = totalEntries - int(totalEntries * mutationArrayMixPerc)
        idx = np.random.choice(np.arange(totalEntries), numToTake, replace=False)

        res = np.random.rand(numRows, numCollumns)

        for row in range(0, numRows):
            for col in range(0, numCollumns):
                index = row * numCollumns + col
                if index in idx:
                    res[row][col] = array1[row][col]
                else:
                    res[row][col] = array2[row][col]
        
        return res
