# General Information
Source for ideas and code are described in the code file as comments. I've added also instructions on how to run the solutions.
For each problem I added images with solutions by my programs.
You might need to double check dependencies and compilations at your end in order to run my solutions.

# Problem 1
Since I was given a binary image with almost zero overlapping, I utilized a simple algortihm to count the rice.
I simply passed a line through the image and counted the changes in backgroung based on some heuristics for the grain of rice.
My program found 94 grains of rice.

# Problem 2
For this, I used the python version provided by YOLO: "darknet.py". I modified the "detect" class so it would give me only the classes it found. After that I counted the different names found, in this case only "person".
Lastly, I plotted the number of people the program found, in this case: 7 people.

# Problem 3
In order to have samples for "Undefined" category I download random car images that were no mercedes.
For this, I used the provided code by Adrian Rosebrock and modified it to train the proposed problem.
In order to asses the performance I set apart 5 images of each category. Results are in the folder "examples". The names on the images refer to the class each car is. Ex.: type0-3.* is the undefined category, and the thrid image selected.

The "plot" image shows loss/accuracy for each epoch.

I used 500 epochs and converted the images to grey-scale.

I argue that better results would be possible if more images were given.
