# System requirements
1. Python 3
2. pygame (`python3 -m pip install -U pygame --user`)
3. (optional) pythonhead (`pip3 install opencv-contrib-python numpy python-osc scikit-image scipy ocrd-fork-pylsd --user`)

# Files present
This repo comes with sample files. 
1. make_animation.py - this file animates either line **or** circle visualizations from pythonhead
2. light_circles.json - this file contains the output from pythonhead's do_circle for the `changing_lights` video
3. dog_doline.json - this file contains the output from pythonhead's do_line for the `dog` video
4. changing_lights.mp4 - a video with changing circular lights
5. dog.mp4 - a video with a dog eating from a bowl

# How to run
1. Make sure all system requirements are met
2. In this repo, run `python3 make_animation.py line` to activate the line animation
3. To run the circle animation, simply omit or misspell 'line'

# Creating your own JSON files 
1. to make the circle file, run
`python3 <path to process.py for pythonhead> --video <path to video> --do_flow --do_circles > <name of output file>`
2. to make the line file, run
`python3 <path to process.py for pythonhead> --video <path to video> --do_flow --do_lines > <name of output file>`

# Next steps
Potential next steps include 
1. Experimenting with videos that dramatically change in color
2. Experimenting with videos of varying speeds to change the FPS of the animation
3. Experimenting with more than one type of shape (ie draw both circles and lines)
