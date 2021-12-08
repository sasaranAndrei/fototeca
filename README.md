# fototeca
Python Script used for downloading the whole gallery from https://fototeca.iiccmer.ro/fototeca/.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)

## General info
After running the script, you can see the downloaded photos sorted by year in the `output` folder.

At this moment, the `output` folder will contain ~1.8 GB of photos.

Each photo has this format: `"year | description | id | place".jpg`.

Example: `1954 | O parte a delegaţiilor de peste hotare participante la funeraliile lui Gheorghe Gheorghiu-Dej. | #A001 | Bucureşti.jpg`



## Technologies
Project is created with:
* Ubuntu: 20.04
* Python: 3.8.10
* PyInstaller: 4.7

## Setup
If you are using Git, you can clone / fork this repository.
If you are not using Git:
  1) Click on `Code` green button from the main page
  2) Download ZIP
  3) Unzip the downloaded file

## Usage
Open a Command Line / Terminal in the `fototeca` folder, which contains all the `.py` files.

Based on your OS, you can run this script with:

Linux: `./fototeca`

macOS: 

Windows: 
