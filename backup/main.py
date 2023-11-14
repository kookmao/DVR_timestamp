###
# file handler
# ffmpeg
# time stamp extractor from image
# calculate time difference
# select corner - later via UI
# burn in time (using ffmpeg?)
# UI
# make runnable



import datetime
import os
import ffmpeg
from PIL import Image, ImageOps, ImageChops
import pytesseract
import re
import dateutil.parser as dparser
from datetime import datetime
import cv2
import datefinder


input_video_path = r"C:\Users\noahs\DVR_timestamp\input.mp4"

##TODO 23:23:23

def text_to_time(input_str):
        #   Step 1: Extract the date and time
    date_time_pattern = r'\d{1,4}[-/]\d{1,2}[-/]\d{2,4}\s?\d{1,2}:\d{1,2}(:\d{1,2})?\s?[APap][Mm]?|\d{1,2}:\d{1,2}(:\d{1,2})?\s?[APap][Mm]?'

    date_time_match = re.search(date_time_pattern, input_str)
    if date_time_match:
        date_time_str = date_time_match.group()
        print("Extracted Date and Time:", date_time_str)
        # extract the date (in MM-DD-YYYY format)
        date_match = re.search(r'\d{2}-\d{2}-\d{4}', date_time_str)
        if date_match:
            date_str = date_match.group()
            print("Extracted Date:", date_str)

        # extract the time (in any time format)
        time_match = re.search(r'\d{2}:\d{2}:\d{2} [APap][Mm]', date_time_str)
        if time_match:
            time_str = time_match.group()
            print("Extracted Time:", time_str)
    
    if date_match == None and time_match == None:
        return None
    else: 
        return None
        
    
    
def export_frame_from_video(input,start_time):
    ffmpeg.input(input, ss=start_time).output("exported_frame.jpg", vframes=1,v=0).run(overwrite_output=True)
   # ffmpeg.input(input, ss=0).output(export, vframes=1).run(overwrite_output=True)
    return r"C:\Users\noahs\DVR_timestamp\exported_frame.jpg"
     
# TODO send co-ordinates from the ui
def extract_timestamp(input,percent):
    img = Image.open(input)
    
    # TODO use UI coordinates to crop the image
    width, height = img.size
    print(img.size)
    
    top_height  = int(height * percent)  # % of the height from the top
    cropped_top = img.crop(box=(width/1.8, 0, width, top_height))
    
    # copy grayscaled cropped img and
    # apply hard light blending mode
    # for better readability
    cropped_top = cropped_top.convert("L")
    copied_image = cropped_top.copy()
    copied_image = ImageOps.invert(copied_image)
        
    result_image = ImageChops.hard_light(cropped_top, copied_image)
  
    # save the now (hopefully) OCR friendly image; send to OCR
    result_image.save("output_image.png")

    ## FIXME wtf is this path error smh my head
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    extracted_text = pytesseract.image_to_string('output_image.png',lang='eng', config='--psm 6')

    print("Extracted Text: \n",extracted_text)
    
    return extracted_text

if __name__ == "__main__":

    # TODO use file chooser
    input_video_path = r"C:\Users\noahs\DVR_timestamp\input.mp4"
    formatted_text = None
    i=0
    while formatted_text == None and i<50:
        exported_frame_path = export_frame_from_video(input_video_path,i)
        i= i+5
        text = extract_timestamp(exported_frame_path,0.1)
        formatted_text = text_to_time(text)
    if i==50: print("couldn't find a date, please enter manually")
    if i<50: print("got the date:")
    print(formatted_text)
        
        
    # export an image, replace 0.1 by ui slider of some sort (maybe use something else entirely)
    
    # crop the image, use OCR get number
    
    # convert text into time ( if possible )
        
    
    
    
#def timestamp_from_image():   