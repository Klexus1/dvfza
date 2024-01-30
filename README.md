## Welcome to the DVFZA - Damn Vulnerable File Zipper App

### This is a CTF (Capture the flag) like exercise.

### This app is for learning purposes only and should never be used in any real production environment.

# This app is damn vulnerable.

Not even this any of this should be trusted so please perform the due diligence between running this app in your environment.

## You need to hack this app.

The app is intended to be run as a docker container, but could be run on a testing debian-based linux server too.

# Prerequisites

You need to have docker installed. 
It is a containerized app, so it needs to be run as such.
DO NOT exec into the container using docker commands and work with it as if it was a server. Cheating won't be punnished but the fun will be gone.
Check <a href="#how-to-run">how to run the app container</a>

# Game scenario:

There are two flags on the server (container) that need to be found and captured. <br>
Hint - you have the source code available :)

If you were really stuck, there is the solution directory. <br>
It holds two base64 encoded files with suggested solutions. Decode only the part1 first. 

# App description:

Welcome to the finest Zipper App out there! You have files that you need to upload and download them as a zip files?
We have you covered, try it out!

<i> Hint: try checking your localhost:5000 upon running the container. </i>

# How to run the app container {#how-to-run}
1) Perform your due diligence on the app, I mean it
2) clone this repository
4) in the root of the project, run ```docker build -t dvfza .```
5) run the app by ```docker run -p 0.0.0.0:5000:5000 -p 0.0.0.0:2222:2222 dvfza```

Have fun.

Feel free to open pull requests.
