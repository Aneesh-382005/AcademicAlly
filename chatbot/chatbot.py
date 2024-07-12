import json
from datetime import datetime
import os
import re

llm = os

with open('data.json') as f:
    data = json.load(f)

def getCurrentTime():
    now = datetime.now()
    return now.strftime("%I:%M %p")

def ParseTime(timeString):
    return datetime.strptime(timeString, "%I:%M %p")

def findCurrentSession(daySchedule, currentTime):
    currentTime = ParseTime(currentTime)
    for i in range(len(daySchedule) - 1):
        startTime = ParseTime(daySchedule[i]["Time"])
        endTime = ParseTime(daySchedule[i+1]["Time"])
        if startTime <= currentTime < endTime:
            return daySchedule[i]["Session"]
    return "No session currently"

def getSchedule():
    now = datetime.now()
    currentDay = now.strftime("%A")

    response = {}
    for yearGroup, classes in data.items():
        response[yearGroup] = {}
        for className, schedule in classes.items():
            if currentDay in schedule:
                session = findCurrentSession(schedule[currentDay], getCurrentTime())
                response[yearGroup][className] = session
            else:
                response[yearGroup][className] = "No classes for today :)"
    return response

print(json.dumps(getSchedule(), indent = 4))
