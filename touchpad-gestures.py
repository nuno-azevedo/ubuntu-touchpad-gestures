#!/usr/bin/python

import os, re, sys, subprocess

def read_event():
    line = p.stdout.readline()
    while not line or re.search('[a-zA-Z]+', line): line = p.stdout.readline()
    tokens = [ c for c in re.split('([^0-9\.])+', line.strip()) if c.strip() ]
    return (int(tokens[1]), int(tokens[2]), int(tokens[4]))

def fingers_count(events):
    l = [ev[2] for ev in events]
    return max(set(l), key = l.count)

cmd = 'synclient -m 20'
p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = True)

try:
    x, y, n = read_event()
    while True:
        events = []
        x, y, n = read_event()
        while n != 0:
            x, y, n = read_event()
            events.append((x, y, n))
        if len(events) == 0: continue
        
        f = fingers_count(events)
        dx, dy = events[-1][0] - events[0][0], events[-1][1] - events[0][1]
        if f == 3:
            if   dx >  150: os.system("xdotool key ctrl+alt+Left")
            elif dx < -150: os.system("xdotool key ctrl+alt+Right")
        if f == 4:
            if   dy >  150: os.system("xdotool key super+D")
            elif dy < -150: os.system("xdotool key super+W")
        if f == 5:
            if abs(dy) > 100: os.system("xdotool key alt+F4")
except KeyboardInterrupt: pass
