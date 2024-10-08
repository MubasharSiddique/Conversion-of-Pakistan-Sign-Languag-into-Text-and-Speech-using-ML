# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 04:37:04 2018

"""
import sqlite3 
import cv2
import json
import math
#import move
#import scale
#import helperFunc as helper
import os

POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],[18,19],[19,20] ]

def plot_skeleton(fileName,background,isMove,isScale):
    js = json.loads(open(fileName).read())
    for items in js['people']:
        handRight = items["hand_right_keypoints_2d"]
    
    handCoord = helper.getCoordPoints(handRight)
    handPoints = helper.removePoints(handRight)
    
    p1 = [handPoints[0], handPoints[1]]
    p2 = [handPoints[18], handPoints[19]]
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    
    
    if isScale:
       handRightResult,handRightPoints = scale.scalePoints(handPoints,distance)
    else:
        handRightResult = handPoints
        handRightPoints = handCoord  
    
    if isMove:
        handRightResult,handRightPoints = move.centerPoints(handRightResult)
     
    
    p1 = [handRightResult[0], handRightResult[1]]
    p2 = [handRightResult[18], handRightResult[19]]
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    
    frame = cv2.imread('C:\\123Drive\\Python\\Sign_Language_Interpreter\\' + background)
    
    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]
    
        if handRightPoints[partA] and handRightPoints[partB]:
            cv2.line(frame, handRightPoints[partA], handRightPoints[partB], (0, 255, 255), 2)
            cv2.circle(frame, handRightPoints[partA], 5, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.circle(frame, handRightPoints[partB], 5, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
    
    return frame


def plot_points(points,background):
    
    handRight = points
    handRightPoints = []
    handRightX = []
    handRightY = []
    for x in range(0,len(handRight),2): 
        handRightX.append(handRight[x])
    for x in range(1,len(handRight),2): 
        handRightY.append(handRight[x])
    
    for x in range(len(handRightX)): 
        handRightPoints.append((int(handRightX[x]) , int(handRightY[x]))) 
    
    frame = cv2.imread('' + background)

    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]
    
        if handRightPoints[partA] and handRightPoints[partB]:
            cv2.line(frame, handRightPoints[partA], handRightPoints[partB], (0, 255, 255), 2)
            cv2.circle(frame, handRightPoints[partA], 5, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

    return frame



def plot_db():
    
    ret_frame = []
    POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],[18,19],[19,20] ]
    background = 'big_background.png'
    connection = sqlite3.connect("db\\main_dataset.db") 
    crsr = connection.cursor()
    
    sql = 'SELECT x1,y1'
    for x in range(2,22):
        sql = sql + ',x'+str(x)+',y'+str(x)
    sql = sql + ' FROM rightHandDataset WHERE 1'
    
    crsr.execute(sql)
    feature_res = crsr.fetchall()
    
    for x in range(len(feature_res)):
        points = feature_res[x]
        
        handRight = points
        handRightPoints = []
        handRightX = []
        handRightY = []
        for x in range(0,len(handRight),2): 
            handRightX.append(handRight[x])
        for x in range(1,len(handRight),2): 
            handRightY.append(handRight[x])
        
        for x in range(len(handRightX)): 
            handRightPoints.append((int(handRightX[x]) , int(handRightY[x]))) 
        
        frame = cv2.imread(background)
        
        # Draw Skeleton
        for pair in POSE_PAIRS:
            partA = pair[0]
            partB = pair[1]
        
            if handRightPoints[partA] and handRightPoints[partB]:
                cv2.line(frame, handRightPoints[partA], handRightPoints[partB], (0, 255, 255), 2)
                cv2.circle(frame, handRightPoints[partA], 5, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.circle(frame, handRightPoints[partB], 5, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
                
        # adjust cv2 colors        
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        ret_frame.append(frame)
        
        # reset background
        frame = cv2.imread(background)
        
        
    return ret_frame

def plot_db_label(label):
    
    ret_frame = []
    POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],[18,19],[19,20] ]
    background = 'big_background.png'
    connection = sqlite3.connect("db\\main_dataset.db") 
    crsr = connection.cursor()
    
    label = label.strip()
    label = "'"+label+"'"
    sql = 'SELECT x1,y1'
    for x in range(2,22):
        sql = sql + ',x'+str(x)+',y'+str(x)
    sql = sql + ' FROM rightHandDataset WHERE label = ' + label 
   
    crsr.execute(sql)
    feature_res = crsr.fetchall()
    
    for x in range(len(feature_res)):
        points = feature_res[x]
        
        handRight = points
        handRightPoints = []
        handRightX = []
        handRightY = []
        for x in range(0,len(handRight),2): 
            handRightX.append(handRight[x])
        for x in range(1,len(handRight),2): 
            handRightY.append(handRight[x])
        
        for x in range(len(handRightX)): 
            handRightPoints.append((int(handRightX[x]) , int(handRightY[x]))) 
        
        frame = cv2.imread(background)
        
        # Draw Skeleton
        for pair in POSE_PAIRS:
            partA = pair[0]
            partB = pair[1]
        
            if handRightPoints[partA] and handRightPoints[partB]:
                cv2.line(frame, handRightPoints[partA], handRightPoints[partB], (0, 255, 255), 2)
                cv2.circle(frame, handRightPoints[partA], 5, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.circle(frame, handRightPoints[partB], 5, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
                
        # adjust cv2 colors        
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        ret_frame.append(frame)
        
        # reset background
        frame = cv2.imread(background)
        
        
    return ret_frame



def plot_dataset(handRightPoints,color):
    
    ret_frame = []
    POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],
                   [10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],
                   [18,19],[19,20] ]
    
    colors = [ [0, 0, 130], [0, 0, 175],[0,0, 210],[0, 0, 250] , 
               [0,200,160], [0,180,150],[0,230,186],[0,255,255],
               [82,201,8], [82,204,0], [92,230,0], [102,252,6], 
               [197,88,17], [204,82,0],[179,71,0],[227,94,5],
               [204,0,163], [200,0,163], [196,0,163], [230,0,184]]
    
    
    
    color = color.capitalize()
    
    background = color+'_background.jpg'
        
    frame = cv2.imread("PSL\\" + background)
    
    count=0
    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]
    
        if handRightPoints[partA] and handRightPoints[partB]:
            
            if color == 'White':
                cv2.line(frame, handRightPoints[partA], handRightPoints[partB], colors[count], 10)
                cv2.circle(frame, handRightPoints[partA], 5, colors[count], thickness=10, lineType=cv2.FILLED)
                cv2.circle(frame, handRightPoints[partB], 15, (0,0,0), thickness=5, lineType=-1)
                
            else:
                cv2.line(frame, handRightPoints[partA], handRightPoints[partB], colors[count], 10)
                cv2.circle(frame, handRightPoints[partA], 5, (0, 0, 255), thickness=10, lineType=cv2.FILLED)
                cv2.circle(frame, handRightPoints[partB], 5, (255, 255, 255), thickness=15, lineType=cv2.FILLED)
            count+=1
            
    # adjust cv2 colors        
#    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    ret_frame.append(frame)
    
    # reset background
#    frame = cv2.imread(background)
        
        
    return frame


def save_old_dataset(handRightPoints,color,name):
    
    POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],
                  [10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],
                  [18,19],[19,20] ]
    colors = [ [0, 0, 130], [0, 0, 175],[0,0, 210],[0, 0, 250] , 
              [0,200,160], [0,180,150],[0,230,186],[0,255,255],
                 [82,201,8], [82,204,0], [92,230,0], [102,252,6], 
                 [197,88,17], [204,82,0],[179,71,0],[227,94,5],
                 [204,0,163], [200,0,163], [196,0,163], [230,0,184]]
    
    
    
    color = color.capitalize()
    
    background = color+'_background.jpg'
        
    frame = cv2.imread(background)
    
    count=0
    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]
    
        if handRightPoints[partA] and handRightPoints[partB]:
            
            if color == 'White':
                cv2.line(frame, handRightPoints[partA], handRightPoints[partB], colors[count], 10)
                cv2.circle(frame, handRightPoints[partA], 5, colors[count], thickness=10, lineType=cv2.FILLED)
                cv2.circle(frame, handRightPoints[partB], 15, (0,0,0), thickness=5, lineType=-1)
                
            else:
                cv2.line(frame, handRightPoints[partA], handRightPoints[partB], colors[count], 10)
                cv2.circle(frame, handRightPoints[partA], 5, (0, 0, 255), thickness=10, lineType=cv2.FILLED)
                cv2.circle(frame, handRightPoints[partB], 5, (255, 255, 255), thickness=15, lineType=cv2.FILLED)
            count+=1
            
    # adjust cv2 colors        
#    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    os.chdir('temp_old_dataset_processing')
    cv2.imwrite(name+'.png',frame)
    os.chdir('..')




























































