displayWidth = 960
displayHeight = 540

fps = 30

defaultFontSize = 18
defaultFontColor = (40, 40, 40)

backgroundFilePath = './images/background.png'
birdFilePath = './images/bird.png'
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