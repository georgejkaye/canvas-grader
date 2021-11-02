from canvasapi import Canvas, assignment
import urllib.request
import subprocess
import tkinter as tk
import os
import sys
import yaml

with open("preferences.yaml") as f:
    prefs = yaml.load(f, Loader=yaml.FullLoader)
    PDF_READER = prefs["viewers"]["pdf"]
    IMG_READER = prefs["viewers"]["img"]
    ODF_READER = prefs["viewers"]["odf"]

if len(sys.argv) != 3:
    print("Needs at least two arguments: course code and assignment code")
    quit()

COURSE_ID = sys.argv[1]
ASSG_ID = sys.argv[2]

with open("token") as f:
    token = f.readline()

API_URL = "https://canvas.bham.ac.uk/"
API_KEY = token

canvas = Canvas(API_URL, API_KEY)
print("You are: " + canvas.get_current_user())


course = canvas.get_course(COURSE_ID)
print("Course name: " + course.name)

assg = course.get_assignment(ASSG_ID)
print("Assignment name: " + course.name)

subs = assg.get_submissions()

for sub in subs:

    print("Marking submission " + str(sub.id))
    processes = []

    try:
        for file in sub.attachments:
            url = file["url"]
            ctype = file["content-type"]

            if ctype == "application/pdf":
                extension = "pdf"
                app = PDF_READER
            else:
                print("Unhandled file type, skipping...")
                continue

            # download the attachment
            path = os.path.join("submissions",  str(sub.id) + "." + extension)
            urllib.request.urlretrieve(url, path)

            # open the submission
            p = subprocess.Popen(app + " " + path, shell=True)
            # add process to list so we can kill it later
            processes.append(p)

        x = input("Enter when done")

        # kill all the processes
        for p in processes:
            p.kill()

    except AttributeError:
        print("No submission, skipping...")
