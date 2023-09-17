# Image Flashcard Generator

## Introduction

The Image Flashcard Generator is a Python script designed to create flashcards for studying purposes from a collection of images. It pairs up images in sequence, using one as the question (front) and the next as the answer (back) to create flashcards. This tool utilizes the [genanki](https://github.com/kerrickstaley/genanki) library to generate Anki-compatible flashcard decks.

## Getting Started

### Prerequisites

Before using this script, ensure you have the following prerequisites installed:

- Python 3.x
- [genanki](https://github.com/kerrickstaley/genanki)

### Installation

1. Clone or download this repository to your local machine.

```bash
git clone https://github.com/KringeKrimson/ImageFlashcards2Anki.git
```
2. Install the genanki library if you haven't already.

```bash
pip3 install genanki
```
### Usage
1. Place your image files (in .png or .jpg format) in the same directory as this script.

2. Ensure there is an even number of images in the directory. The script pairs them up serially, using one as the question and the next as the answer.

3. Run the script by executing it with Python:
```bash
python3 main.py
```
4. Follow the on-screen instructions. The script will prompt you to enter a name for your flashcards.
The script will automatically pair the images and generate flashcards. Each flashcard will have an image on the front (question) and the following image on the back (answer).

5. Find your deck saved as '[Your Deck Name].apkg' in the same directory.
  
7. Import this deck into Anki for studying.
### Notes:
1. This is for imageflashcards not for images that have not been made into flashcards.
2. Make sure there are even number of images. It pairs odd and even as question and answers serially. 
