displayWidth = 960
displayHeight = 540

fps = 30

defaultFontSize = 18
defaultFontColor = (40, 40, 40)

backgroundFilePath = './images/background.png'
birdFilePath = ['./images/bird0.png', './images/bird1.png', './images/bird2.png']
pipeFilePath = './images/pipe.png'

sceneSpeed = 70/1000 #70px per second

pipeDone = 1
pipeMoving = 0
pipeUpper = 1
pipeLower = 0

pipeHeight = 500
pipePairGap = 160
pipeMinSize = 80
pipeMaxSize = displayHeight - pipeMinSize - pipePairGap # 300

pipeSequenceGap = 160
pipeStartX = displayWidth
pipeFirstX = 400

birdStartX = 200
birdStartY = 200
birdAlive = 1
birdDead = 0
birdFlyUpSpeed = -0.32

gravity = 0.001

generationSize = 60

neuralNetInputs = 2
neuralNetHidden = 5
neuralNetOutput = 1

flyUpChance = 0.5

#normalizing

maxYDiff = displayHeight - pipeMinSize - pipePairGap/2 # 380
minYDiff = -(pipeMaxSize + pipePairGap/2 ) # -380
yShift = abs(minYDiff)

normalizer = abs(minYDiff) + maxYDiff

mutationWeightModifyChance = 0.2
mutationArrayMixPerc = 0.5
mutationCutOff = 0.4
mutationBadToKeep = 0.2
mutationModifyChanceLimit = 0.4