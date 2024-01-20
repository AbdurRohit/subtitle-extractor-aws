# Subtitle Extractor with AWS

Subtitle Extractor with AWS is a tool that extracts subtitles from videos, stores them locally, uploads the video and subtitles to an AWS S3 bucket, sends the subtitles to DynamoDB in JSON format, generates pre-signed URLs for video and subtitles, and redirects to the `view_video` page.

## Overview

The repository includes the following components:

1. **Subtitle Extraction and Storage:**
   - Takes a video file, extracts subtitles, and stores the video locally.
   
2. **AWS Integration:**
   - Uploads the video and subtitles to an AWS S3 bucket.
   
3. **DynamoDB Integration:**
   - Sends subtitles to DynamoDB in JSON format.
   
4. **Pre-signed URL Generation:**
   - Generates pre-signed URLs for the video and subtitles.

5. **View Video Page:**
   - Displays the output video with subtitles.
   - Includes a search box to search for words and retrieve timestamps from DynamoDB.

## Project Structure

The project is structured as follows:

```plaintext
subtitle-extractor-aws/
│
├── assets/
│   └── 96853180/
│       └── c045b3c7-0602-4ae5-99e7-6115fadb4d32
│           └── sub-ext-main-drawio.png
│
├── src/
│   ├── extraction_script.py
│   └── view_video.py
│
├── templates/
│   └── view_video.html
│
├── README.md
├── requirements.txt
└── .gitignore
```
## Clone the repository:
``git clone https://github.com/AbdurRohit/subtitle-extractor-aws.git
cd subtitle-extractor-aws``

## Install dependencies:
``pip install -r requirements.txt``
## Visit the view_video page:

## Run the extraction script:
``python src/extraction_script.py``

``python src/view_video.py``

