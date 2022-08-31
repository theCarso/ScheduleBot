from pypresence import Presence
import time
import course

courseList = []
 
options = open("options.txt", "r")
for x in options:
    if x.startswith("#"): continue
    settingsplit = x.replace("\n", "").split("=", 1)
    if settingsplit[0] == "clientid":
        clientid = settingsplit[1]
        continue
    if(settingsplit[0].startswith("class")):
        coursesplit=settingsplit[1].split(",")

        courseName=coursesplit[0]
        startTime=coursesplit[1].split(":")
        endTime=coursesplit[2].split(":")
        days=coursesplit[3]

        courseList.append(course.Course(courseName, startTime[0], startTime[1], endTime[0], endTime[1], days))
        continue


RPC = Presence(clientid)
RPC.connect()

lastTime = time.time()

defaultStatus = "Not In Class"
defaultState ="Designed by theCarso#9732"

currentStatus = defaultStatus
currentState = defaultState

while True:
    print("startloop")
    inClass=False
    for course in courseList:
        if course.isInClass():
            inClass=True
            newStatus = "Currently in class: " + course.name
            newState = "Class will end at: " + course.getEndTimeString()
            if currentStatus != newStatus:
                currentState=newState
                currentStatus=newStatus
                lastTime=time.time()
            break
    if (currentStatus != defaultStatus) & (not inClass):
        currentStatus = defaultStatus
        currentState = defaultState
        lastTime = time.time()
        
    RPC.update(
        details=currentStatus,
        state=currentState,
        large_image='icon',
        large_text='Class?',
        start=int(lastTime)
    )
    time.sleep(3)