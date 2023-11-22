# visualize-irrationals

Code plots the graph of exp(theta * i) + exp(theta * num * i) using matplotlib python library. Here num is the irrational number to be visualized. Theta changes with each frame to get a new point on the graph. The animation is written to an mp4 file.

# Install guide
1. Install python3
2. Install matplotlib using python -m pip install matplotlib
3. Install ffmpeg. On Mac this can be done using homebrew by brew install ffmpeg

# Run
python visualize.py