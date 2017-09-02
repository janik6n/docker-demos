README
======

A demo CLI App built on top of the official Python image python:3.6.2-stretch. Analysis of Finnish words passed as arguments, using Voikko's analyze-function.

Working Voikko installation containing:

- voikko-fi 2.1-1
- python-libvoikko 4.1-1

## Usage

Pull the image, and run the container with:
`docker run --rm -ti janikarh/python3-voikko:[Tag] [word_to_analyze]`

Example with the image version 1.0, and 2 words to analyze:
`docker run --rm -ti janikarh/python3-voikko:1.0 "rei'ittämättä" kansiossa`
