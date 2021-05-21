#!/bin/bash

# Check if brew is installed, you are hosed if ruby isn't on your machine
which -s brew
if [[ $? != 0 ]] ; then
    # Install Homebrew
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
else
    brew update
fi

# Install rubberband (this is a required dependency)
brew install rubberband

# Install python dependencies
pip install -r requirements.txt
