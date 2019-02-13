import sys
import os
import  Scene as s

def touchCheck(scenee):
    if (len(scenee.bodies)<2):
        print ("the total number of bodies in this frame is less than 2 so there are no touches ")
    else:
        counter=0;
        for i in range (0,len(scenee.bodies)):
            for j in range(i+1,len(scenee.bodies)):
                for k in range(0,24):
                    for h in range(k,24):

                        dist=((((scenee.bodies[i]).joints[k]).x - ((scenee.bodies[j]).joints[h]).x)**2 +(((scenee.bodies[i]).joints[k]).y - ((scenee.bodies[j]).joints[h]).y)**2 + (((scenee.bodies[i]).joints[k]).z - ((scenee.bodies[j]).joints[h]).z)**2 )
                        if(dist<0.173049):
                            #0.17309
                            print("there is touches!")
                            counter=counter+1
                            print("the body's  :",scenee.bodies[i].id,(scenee.bodies[i]).joints[k].name,"seems to touch the body's",scenee.bodies[j].id,(scenee.bodies[j]).joints[h].name)
                            confidence = (scenee.bodies[i]).joints[k].conf * (scenee.bodies[j]).joints[h].conf
                            print("we are ",confidence,"confident of this touch")

    print("total number of touches is: ",counter)
    return


def lookcheck(scenee):

    if (len(scenee.bodies)<2):
        print ("the total number of bodies in this frame is less than 2 so there are no lookings ")


    else:
        for i in range (0,len(scenee.bodies)):
            for j in range(i+1,len(scenee.bodies)):

                head1x = scenee.bodies[i].joints[3].x # consider switching to 4
                head1y = scenee.bodies[i].joints[3].y
                head1z = scenee.bodies[i].joints[3].z

                head2x = scenee.bodies[j].joints[3].x
                head2y = scenee.bodies[j].joints[3].y
                head2z = scenee.bodies[j].joints[3].z





    return




file = open(
            'C:\\Users\\Bayan\\Desktop\\university materials\\final project\\recordings\\mom\\Body\\-8586515569246497929%718160465426.txt',
            'r')
#lines = file.readlines()
#print(lines[0])
ob = s.Scene(file)
touchCheck(ob)
#lookcheck(ob)
