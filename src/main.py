from canvasapi import Canvas, assignment
import urllib.request
import subprocess
import tkinter as tk
import os
from os import path
import sys
import yaml
import shutil

# clean up past submissions
if path.exists("submissions"):
    if path.isdir("submissions"):
        shutil.rmtree("submissions")
    else:
        os.remove("submissions")

os.mkdir("submissions")

with open("associations.yaml") as f:
    assocs = yaml.load(f, Loader=yaml.FullLoader)
    PDF_READER = assocs["pdf"]
    IMG_READER = assocs["img"]
    TAR_READER = assocs["tar"]
    ZIP_READER = assocs["zip"]

if len(sys.argv) != 3:
    print("Needs at least two arguments: course code and assignment code")
    quit()

COURSE_ID = sys.argv[1]
ASSG_ID = sys.argv[2]

update = False

# hack to create the file if it doesn't exist
open("credentials.yaml", "a+").close()

# we need readwrite in case we need to update the credentials
with open("credentials.yaml", "r+") as f:
    creds = yaml.load(f, Loader=yaml.FullLoader)
    if creds and "url" in creds and creds["url"] != "":
        API_URL = creds["url"]
    else:
        API_URL = input("Canvas URL: ")
        update = True
    if creds and "token" in creds and creds["token"] != "":
        API_KEY = creds["token"]
    else:
        API_KEY = input("Access token: ")
        update = True

    if update:
        f.write("url: " + API_URL)
        f.write("\n")
        f.write("token: " + API_KEY)

# Try to connect to Canvas
try:
    canvas = Canvas(API_URL, API_KEY)
except Exception as e:
    print("Could not connect to Canvas, exiting...")
    quit()

print("Current user: " + str(canvas.get_current_user()))
course = canvas.get_course(COURSE_ID)
print("Course name: " + course.name)
assg = course.get_assignment(ASSG_ID)
print("Assignment name: " + course.name)

# We want all the submissions
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
            elif ctype == "application/x-tar":
                extension = "tar.gz"
                app = TAR_READER
            elif ctype == "application/zip":
                extension = "zip"
                app = TAR_READER
            else:
                print("Unhandled file type " + ctype + " , skipping...")
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
