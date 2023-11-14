# logic.py
import re
import ffmpeg
import pytesseract
from PIL import Image, ImageOps, ImageChops


def text_to_time(input_str):
    # Step 1: Extract the date and time
    date_time_pattern = r"\d{1,4}[-/]\d{1,2}[-/]\d{2,4}\s?\d{1,2}:\d{1,2}(:\d{1,2})?\s?[APap][Mm]?|\d{1,2}:\d{1,2}(:\d{1,2})?\s?[APap][Mm]?"

    date_time_match = re.search(date_time_pattern, input_str)
    if date_time_match:
        date_time_str = date_time_match.group()
        print("text_to_time: Extracted Date and Time:", date_time_str)
        # extract the date (in MM-DD-YYYY format)
        date_match = re.search(r"\d{2}-\d{2}-\d{4}", date_time_str)
        if date_match:
            date_str = date_match.group()
            print("text_to_time: Extracted Date:", date_str)

        # extract the time (in any time format)
        time_match = re.search(r"\d{2}:\d{2}:\d{2} [APap][Mm]", date_time_str)
        if time_match:
            time_str = time_match.group()
            print("text_to_time: Extracted Time:", time_str)

    if date_match is not None and time_match is not None:
        return date_time_str
    else:
        return None


def export_frame_from_video(input, start_time):
    ffmpeg.input(input, ss=start_time).output("exported_frame.jpg", vframes=1, v=0).run(
        overwrite_output=True
    )
    # ffmpeg.input(input, ss=0).output(export, vframes=1).run(overwrite_output=True)
    return r"C:\Users\noahs\DVR_timestamp\exported_frame.jpg"


def extract_timestamp(input, percent):
    img = Image.open(input)

    # Use UI coordinates to crop the image
    width, height = img.size
    print(img.size)

    top_height = int(height * percent)  # % of the height from the top
    cropped_top = img.crop(box=(width / 1.8, 0, width, top_height))

    # Copy grayscaled cropped img and apply hard light blending mode for better readability
    cropped_top = cropped_top.convert("L")
    copied_image = cropped_top.copy()
    copied_image = ImageOps.invert(copied_image)
    result_image = ImageChops.hard_light(cropped_top, copied_image)

    # Save the now (hopefully) OCR friendly image; send to OCR
    result_image.save("output_image.png")

    # Specify the path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    # perform OCR on the image
    extracted_text = pytesseract.image_to_string(
        "output_image.png", lang="eng", config="--psm 6"
    )
    # extracted_text = pytesseract.image_to_string('output_image.png', lang='eng', config='--psm 6')

    print("extract_timestamp: Extracted Text: \n", extracted_text)

    return extracted_text


# seek date from an image
def scan_video_for_timestamp(input_video_path):
    formatted_text = None
    i = 0
    seek_interval = 5
    cap_ss = 50
    # iterate with 5 second intervals until
    while formatted_text is None and i < cap_ss:
        exported_frame_path = export_frame_from_video(input_video_path, i)
        i = +seek_interval
        extracted_text = extract_timestamp(exported_frame_path, 0.1)
        formatted_text = text_to_time(extracted_text)

    if i < 50:
        return str(formatted_text)

    return None
