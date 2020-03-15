import pyautogui
import time

class AutoSecretShop:

    cov_count = 0
    mm_count = 0

    def __init__(self, skystones, cov_bm_line, cov_bm_buy, mystic_bm_line, mystic_bm_buy, refresh_button, refresh_confirm):
        self.skystones = skystones
        self.cov_bm_line = cov_bm_line
        self.cov_bm_buy = cov_bm_buy
        self.mystic_bm_line = mystic_bm_line
        self.mystic_bm_buy = mystic_bm_buy
        self.refresh_button = refresh_button
        self.refresh_confirm = refresh_confirm

    def startASS(self):
        num_skystones = self.skystones

        while num_skystones >= 3:
            num_skystones -= 3

            time.sleep(1)
            self.findAndBuyCovenantBookmark()
            time.sleep(1)
            self.findAndBuyMysticMedal()

            time.sleep(1)
            self.scrollDown()
            time.sleep(1)

            self.findAndBuyCovenantBookmark()
            time.sleep(1)
            self.findAndBuyMysticMedal()
            time.sleep(1)
            self.refreshShop()
            time.sleep(1)

        time.sleep(1)
        self.findAndBuyCovenantBookmark()
        time.sleep(1)
        self.findAndBuyMysticMedal()

        time.sleep(1)
        self.scrollDown()
        time.sleep(1)

        self.findAndBuyCovenantBookmark()
        time.sleep(1)
        self.findAndBuyMysticMedal()
        time.sleep(1)

        with open("DATA.txt", 'a') as f:
            f.write("Skystones: " + str(self.skystones) + " | Covenant Bookmarks: " + str(
                self.cov_count) + " | Mystic Medals: " + str(self.mm_count) + "\n")

        print("Finished. Skystones: " + str(self.skystones) + " | Covenant Bookmarks: " + str(
            self.cov_count) + " | Mystic Medals: " + str(self.mm_count))



    def refreshShop(self):
        print("Refreshing shop")
        refresh_button = pyautogui.locateOnScreen(self.refresh_button, confidence = 0.9)

        if refresh_button == None:
            print("No refresh button found")
            return

        pyautogui.moveTo(refresh_button)
        pyautogui.click(button='left', clicks=2, interval=0.1)
        time.sleep(0.125)

        refresh_confirm = pyautogui.locateOnScreen(self.refresh_confirm, confidence = 0.9)

        if refresh_confirm == None:
            print("No refresh confirm button found")
            return

        pyautogui.moveTo(refresh_confirm)
        pyautogui.click(button='left', clicks=2, interval=0.1)
        time.sleep(0.125)

    def scrollDown(self):
        print("Scrolling down")
        size = pyautogui.size()
        x1 = (size[0] / 2) + size[0]*0.1
        y2 = size[1] / 2
        pyautogui.moveTo(x1, y2)
        pyautogui.drag(0, -y2*0.75, 0.5, button='left')
        time.sleep(1)

    def findAndBuyCovenantBookmark(self):
        print("Finding covenant bookmark image")
        cov_bm_box = pyautogui.locateOnScreen(self.cov_bm_line, confidence = 0.9)

        if cov_bm_box == None:
            print("No covenant bookmarks found")
            return

        # width, height
        # left of image + 5/6 width of image
        pyautogui.moveTo(cov_bm_box[0] + cov_bm_box[2]*6,
        # top of image + 3/4 height of image
                         cov_bm_box[1] + (3/4) * cov_bm_box[3])

        pyautogui.click(button='left', clicks=2, interval=0.1)
        time.sleep(0.125)
        # move to buy button
        cov_buy_button = pyautogui.locateOnScreen(self.cov_bm_buy, confidence = 0.9)

        if cov_buy_button == None:
            print("No covenant buy button found")
            return

        pyautogui.moveTo(cov_buy_button)
        pyautogui.click(button='left', clicks=2, interval=0.1)
        self.cov_count += 1
        time.sleep(0.125)

    def findAndBuyMysticMedal(self):
        print("Finding mystic medal image")
        mm_box = pyautogui.locateOnScreen(self.mystic_bm_line, confidence = 0.9)

        if mm_box== None:
            print("No mystic medal found")
            return

        # width, height
        # left of image + 5/6 width of image
        pyautogui.moveTo(mm_box[0] + + mm_box[2]*6,
        # top of image + 3/4 height of image
                         mm_box[1] + (3/4) * mm_box[3])

        pyautogui.click(button='left', clicks=2, interval=0.1)
        time.sleep(0.125)

        # move to buy button
        mm_buy_button = pyautogui.locateOnScreen(self.mystic_bm_buy, confidence = 0.9)

        if mm_buy_button == None:
            print("No mystic medal buy button found")
            return

        pyautogui.moveTo(mm_buy_button)
        pyautogui.click(button='left', clicks=2, interval=0.1)
        self.mm_count += 1
        time.sleep(0.125)