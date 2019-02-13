import Body as b
class Scene:
    def __init__(self,file):
        i=0
        self.bodies =list()
        for line in file:
           i=i+1

        i = i/30
        for j in range(0,int(i)):
            b1 = b.Body(file,j)
            self.bodies.append(b1)


