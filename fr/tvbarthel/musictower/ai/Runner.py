from Device import Device
from OCRManager import OCRManager

print "MusicTower AI"
device = Device()
ocrManager = OCRManager()

print ocrManager.get_score(device)
