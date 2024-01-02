# Download from youtube and cut the audio segment

## Installation
To install the necessary dependencies, run the following command:
```
pip install -r requirements.txt
```
You need to install and add FFmpeg to PATH
## Usage
To use downloader, execute the following Python script:
```
python startdl.py
```
## Notes

The line skipping mechanism needs to be improved. To start from the desired line is temporarily used startdlskip.py

XLSX file contains columns 'yotubelink', 'correct', 'starttime' and 'endtime'.