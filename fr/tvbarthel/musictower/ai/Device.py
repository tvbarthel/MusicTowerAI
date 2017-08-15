from com.android.monkeyrunner import MonkeyRunner


class Device:
    """
    Encapsulate every logic linked to the current phone devices
    Currently based on MonkeyRunner#Device
    """

    TEMP_SCREEN_SHOT_FILE = "temp/screenshot.png"

    def __init__(self):
        self.wrappedDevice = MonkeyRunner.waitForConnection()
        pass

    def take_screenshot(self, rect=None):
        """
        Take a screen shot
        :param rect: optional portion of the screen to consider.
        :return: file name where the screen shot is stored temporary.
        """
        self.lastScreenShot = self.wrappedDevice.takeSnapshot()

        if rect != None:
            self.lastScreenShot = self.lastScreenShot.getSubImage(rect)

        self.lastScreenShot.writeToFile(self.TEMP_SCREEN_SHOT_FILE, "png")

        return self.TEMP_SCREEN_SHOT_FILE

    def get_pixel(self, x, y):
        """
        Returns the single pixel at last screen shot location (x,y ), as an a tuple of integer, in the form (a,r,g,b)
        See also: take_screen_shot
        :param x: horizontal coordinate of the pixel on the screen
        :param y: vertical coordinate of the pixel on the screen
        :return: tuple in the form (a,r,g,b) or empty tuple if no screen shot has been taken previously
        """
        if self.lastScreenShot:
            return self.wrappedDevice.image.getRawPixel(x, y)
        else:
            return ()
