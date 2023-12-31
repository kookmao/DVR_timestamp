# logic.py
import re
import ffmpeg
import pytesseract
from PIL import Image, ImageOps, ImageChops, ImageEnhance


def text_to_time(input_str):
    date_match = None
    time_match = None
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
        return [date_str, time_str]
    else:
        return None


def export_frame_from_video(input_path, start_time):
    try:
        ffmpeg.input(input_path, ss=start_time).output(
            "exported_frame.jpg", vframes=1, v=0
        ).run(overwrite_output=True)
        # ffmpeg.input(input, ss=0).output(export, vframes=1).run(overwrite_output=True)

        return ".\\exported_frame.jpg"
    except ffmpeg.Error as e:
        print("Error:", e.stderr)
        return None


def extract_timestamp(input, selection, gui_width, gui_height):
    """
    convert selection displayed into actual image size
    extract a date from an image
    return: extracted text | None
    """
    img = Image.open(input)
    # FIXME ???? change the damn +10 -10 thing, i think the misplacment
    # comes from the fact that the UI display is in weird resolution
    #w_scale_factor = (img.size[0] - 10) / gui_width
    #h_scale_factor = (img.size[1] + 10) / gui_height
    w_scale_factor = (img.size[0]) / gui_width
    h_scale_factor = (img.size[1]) / gui_height
 
    scaled_tuple = tuple(
        int((value * scale_factor))
        for value, scale_factor in zip(
            selection, (w_scale_factor, h_scale_factor, w_scale_factor, h_scale_factor)
        )
    )
    # print(selection)
    # print(scaled_tuple)

    # grayscaled cropped img and apply hard light blending mode for better readability
    # TODO consider using a different technique
    cropped_image = img.crop(box=(scaled_tuple))
    cropped_image = cropped_image.convert("L")
    copied_image = cropped_image.copy()
    copied_image = ImageOps.invert(copied_image)
    
    enhancer = ImageEnhance.Sharpness(cropped_image)
    sharpness_factor = 4
    sharpened_image = enhancer.enhance(sharpness_factor)

    
    result_image = ImageChops.hard_light(sharpened_image, copied_image)
    result_image = ImageOps.invert(result_image)
    

    # save the now (hopefully) OCR friendly image; send to OCR
    result_image.save("output_image.png")

    # TODO find a different way to use the OCR
    # specify the path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    # perform OCR on the image
    extracted_text = pytesseract.image_to_string("output_image.png")
    # a different config: check if there's a lang= 'numbers' or something
    # extracted_text = pytesseract.image_to_string('output_image.png', lang='eng', config='--psm 6')

    print("extract_timestamp: Extracted Text: \n", extracted_text)
    if extracted_text == "":
        return None

    return text_to_time(extracted_text)


# FIXME use this functions idea to get a formatted text out of the img


def scan_video_for_timestamp(input_video_path):
    """
    seek date from an image
    return formatted string of a date (together)

    """
    formatted_text = None
    i = 0
    seek_interval = 5
    cap_ss = 50
    # iterate with 5 second intervals until there's a date
    while formatted_text is None and i < cap_ss:
        exported_frame_path = export_frame_from_video(input_video_path, i)
        i = +seek_interval
        formatted_text = extract_timestamp(exported_frame_path, 0.1)

    if i < 50:
        print(f"formatted text: {formatted_text}")
        return str(formatted_text)

    return None
