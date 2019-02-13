import Joint as jo
class Body:
    def __init__(self, file,startIndex):
        file = open(
            'C:\\Users\\Bayan\\Desktop\\university materials\\final project\\recordings\\mom\\Body\\-8586515569246497929%718160465426.txt',
            'r')

        startIndex=startIndex*31

        lines = file.readlines()
        if(startIndex > 0):
            startIndex=startIndex-1
        line = lines[startIndex]
        words = line.split("#")
        self.iCount=words[0];
        self.id = words[1];
        self.joints = list()

        line = lines[startIndex+1]
        words = line.split("#")
        self.isTracked = words[0];
        self.isStable = words[1];
        self.isRestricted = words[2];

        line = lines[startIndex + 2]
        words = line.split("#")
        self.clippedEdges = words[0]
        self.leanVectorX = words[1]
        self.leanVectorY = words[2]
        self.leanTrackingState = words[3]
        self.height = words[4];


        line = lines[startIndex + 3]
        words = line.split("#")
        self.handLeftState = words[0]
        self.handLeftConf = words[1]
        self.handRightState = words[2]
        self.handRightConf = words[3]

        for i in range(0,24):
            line = lines[startIndex + 4+i]
            words = line.split("#")
            j = jo.Joint(words[0],words[1],words[2],words[3],words[4],words[5],words[6],words[7],words[8])
            self.joints.append(j)

        line = lines[startIndex + 29]
        words = line.split("#")
        self.FloorPlaneX= words[0]
        self.FloorPlaneY = words[1]
        self.FloarPlaneZ = words[2]
        self.FloarPlaneW = words[3]
        self.CameraHeight = words[4]
        self.CameraTilt = words[5]



