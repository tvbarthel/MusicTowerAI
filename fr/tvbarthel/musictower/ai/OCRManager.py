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
        command = ['tesseract', 'stdin', 'stdout', '--psm', '7', '--oem', '0', 'tesseract/digits']
        proc = subprocess.Popen(command, stdin=input_file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = proc.communicate()
        return int(output.splitlines()[0])
