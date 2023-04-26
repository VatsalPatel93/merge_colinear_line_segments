#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:00:03 2023

@author: vatsal
"""

import math
def slope(x1, y1, x2, y2): # Slope of a line, given two coordinates:
    return (y2-y1)/(x2-x1)

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))

def mergeLineSegments(segments, tolerance):
    while True:
        l = len(segments)
        i = 0
        while i < len(segments)-1:
            #align points in correct order to get correct distance
            if segments[i][0] > segments[i+1][0]:
                [segments[i], segments[i+1]] = [segments[i+1], segments[i]]
            
            #slope of two lines and third potential joint segment
            slope1 = slope(segments[i][0], segments[i][1], segments[i][2], segments[i][3])
            slope2 = slope(segments[i+1][0], segments[i+1][1], segments[i+1][2], segments[i+1][3])
            slope3 = slope(segments[i][0], segments[i][1], segments[i+1][2], segments[i+1][3])
        
            #distance between two closest points of the line
            dist = distance(segments[i][2], segments[i][3], segments[i+1][0], segments[i+1][1])
            
            #If three slopes are equal, lines are colinear, hence ok to merge if distance is less than tolerance
            if slope1 == slope2 == slope3 and dist <= tolerance:
                sl = list(segments[i])
                sl[2] = segments[i+1][2]
                sl[3] = segments[i+1][3]
                segments[i] = tuple(sl)
                segments.pop(i+1)
            else:
                i += 1
        
        #to ensure we run the merging as many times as needed
        if l == len(segments):
            break
    return segments

print(mergeLineSegments([(5, 5, 7, 7), (7, 7, 9, 9), (0, 0, 2, 2), (2, 2, 4, 4), (5, 4, 7, 2), (7, 2, 9, 0), (0, 9, 2, 7), (2, 7, 4, 5)]
, 2))

"""
Time complexity:
    
    - We make multiple passes to ensure all possible line segments are combined.
    - Let's assume we need k passes
    - For each pass, we go through the segments list one time so that is O(n), n being length of segments list.
    - If we merge two segments, that involves removing one from the list, in worst case that is O(n)
    - So, overall time complexity for this solution is O(kn)

Space Complexity:
    O(n), n being length of segments list
    - We change the segments list in place so no extra space is needed. 
"""