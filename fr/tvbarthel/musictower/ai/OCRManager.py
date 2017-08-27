import os
import subprocess


class OCRManager:
    """
    Used to encapsulate OCR performed to retrieve the current score.
    Currently based on tesseract.
    """

    # Sub part of the screen containing the score, format (x, y, w, h).
    SCORE_RECT = (282, 217, 520, 160)

    def __init__(self):
        pass

    def get_score(self, device):
        """
        Return the current score display on the device
        :param device: device from which the score must be extracted.
        :return: current score displayed on the device as an int.
        """
        file = device.take_screenshot(self.SCORE_RECT)

        input_file = open(file)

        # convert the screenshot into black and white for better OCR
        current_dir = os.path.dirname(os.path.realpath(__file__))
        script_path = os.path.join(current_dir, "image_convertor.py")
        command = ['python', script_path, file, file]
        subprocess.Popen(command)

        # run tesseract on the black and white image
        command = ['tesseract', 'stdin', 'stdout', '--psm', '7', '--oem', '0', 'tesseract/digits']
        proc = subprocess.Popen(command, stdin=input_file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = proc.communicate()

        return int(output.splitlines()[0].replace(' ', ''))
