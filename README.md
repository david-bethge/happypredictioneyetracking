# Happy Emotion Detection with Eye Tracking Features 

This is an implementation of the paper: "Analyzing Transferability of Happiness Detection via Gaze Tracking in Multimedia Applications" 
accepted at ACM ETRA 2020

## Getting Started
Due to copyright, the eye tracking data is not stored here but can be downloaded from: http://bcmi.sjtu.edu.cn/~seed/seed-iv.html. The downloaded data should be stored in the empty data/ folder.

As a next step preprocess the data with the Notebook: "Preprocess Eye Gaze.inpynb". 

Then you should be ready for reproducing the papers result by running the "Happy_Classification.inpynb" Notebook.

The emotional labels are originally decoded as follows:
(Label) 0: neutral, 1: sad, 2: fear, 3: happy
In this analysis, we decode happy emotions as 1 (all other observations as 0).


## Installing
Clone the existing repository:
```git clone https://github.com/davebeght/happypredictioneyetracking```
