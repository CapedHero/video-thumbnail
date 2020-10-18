# Video Thumbnail

+ This project implements a simplified function that:
  1. Extracts the last non-blank frame from a video under a given path.
  2. Saves such frame in a temporary location.
  3. Returns the location of the saved frame.

+ The logic is heavily reliant on the identification of a non-blank frame, which
  is defined as a "frame that after 'grayification' has an average color above
  an arbitrary threshold".
  
+ As for fading to black at the end, given the logic described above,
  the threshold would have to be experimented with to deliver satisfying results.

+ To run the function:
  1. Install dependencies from requirements.txt.
  2. Call `python main.py --input-file-path *YOUR-VIDEO-FILE-PATH` from 
     the project's root directory.

+ To run the test suite:
  1. Install dependencies from requirements.txt and requirements.test.txt.
  2. Call `python -m pytest tests/` from the project's root directory.
