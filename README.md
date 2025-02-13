# Connect4

Since we're acquiring a lot of files, I'm writing descriptions here so you know where to look for something.

## Data
- Put the files ready for analysis on [Box](https://utexas.box.com/s/05xac31resiaf6a1kww32ba2htftff4i) because the files were too large.

## Data Cleaning
- UpdatedConnect4_FixShape.ipynb: Dataset generation code with 6x7x2 board shape. Includes the processing within the file, so dataprocessing.ipynb is no longer necessary.
- UpdatedConnect4.ipynb: original version of dataset generation using MCTS 1500 and 2x6x7 board shape.
- data_processing.ipynb: used to combine and process all of the datasets from UpdatedConnect4.ipynb into one dataset ready for analysis.

## Modeling
- cnn.ipynb: Femke's CNN
- transformer.ipynb: Femke's transformer
- kennedy_tuning: moved my notebooks and tuning files here so that it's all contained in one spot
- environment_setup_instructions.txt: If you do any modeling, you need to make sure you are using the same environment so that it works on AWS.
- setup_environment.sh: The isntructions above explain how to use this.

## For AWS:
- requirements.txt: records package versions used when training the best models
- best_connect4_cnn.h5: best CNN model so far 
- game_play.ipynb: Loads the best models and uses them to play a game. Can be hosted on the back end and displayed on website.

