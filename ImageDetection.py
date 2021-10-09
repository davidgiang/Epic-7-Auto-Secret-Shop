import pyautogui
import time
import tkinter as tk
from tkinter import *
import threading
from threading import *
import os

class AutoSecretShop():

    cov_count = 0
    mm_count = 0
    stop_bool = False
    skystones_spent = 0

    def __init__(self, skystones, gold, cov_bm_line, cov_bm_buy, mystic_bm_line, mystic_bm_buy, refresh_button, refresh_confirm, try_again):
        self.skystones = skystones
        self.gold = gold
        self.cov_bm_line = cov_bm_line
        self.cov_bm_buy = cov_bm_buy
        self.mystic_bm_line = mystic_bm_line
        self.mystic_bm_buy = mystic_bm_buy
        self.refresh_button = refresh_button
        self.refresh_confirm = refresh_confirm
        self.try_again = try_again

    def startASS(self):
        num_skystones = self.skystones
        num_gold = self.gold
        self.stop_bool = False
        self.last_flag = False

        print(num_skystones)
        print(num_gold)

        if self.stop_bool == True:
            print("Stopping")

        while True:

            if self.last_flag == True:
                print("Last flag break")
                break
            else:
                if num_skystones < 2 or num_gold < 184000 or self.stop_bool == True:
                    print("Stopping")
                    self.stop_bool = True
                    break

            self.checkDispatchMission()
            time.sleep(0.5)
            self.findAndBuyCovenantBookmark()
            time.sleep(0.5)
            self.findAndBuyMysticMedal()

            time.sleep(0.5)
            self.scrollDown()
            time.sleep(0.5)

            self.findAndBuyCovenantBookmark()
            time.sleep(0.5)
            self.findAndBuyMysticMedal()
            time.sleep(0.5)
            if self.stop_bool == True:
                print("Stopping midway")
                break
            else:
                num_skystones -= 3
                if num_skystones == 0:
                    print("Setting last flag")
                    self.last_flag = True
                self.skystones_spent += 3
                skystone_amt.set(num_skystones)
                self.refreshShop()

        if self.stop_bool != True and self.last_flag == True:
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
        else:
            print("No last check needed")

        with open("DATA.txt", 'a') as f:
            f.write("Skystones: " + str(self.skystones_spent) + " | Covenant Bookmarks: " + str(
                self.cov_count) + " | Mystic Medals: " + str(self.mm_count) + "\n")

        print("Finished. Skystones: " + str(self.skystones) + " | Covenant Bookmarks: " + str(
            self.cov_count) + " | Mystic Medals: " + str(self.mm_count))

    def stopASS(self):
        self.stop_bool = True

    def refreshShop(self):
        print("Refreshing shop")
        refresh_button = pyautogui.locateOnScreen(self.refresh_button, confidence = 0.9, grayscale=True)

        if refresh_button == None:
            print("No refresh button found")
            return

        pyautogui.moveTo(refresh_button)
        pyautogui.click(button='left', clicks=2, interval=0.1)
        time.sleep(0.125)

        refresh_confirm = pyautogui.locateOnScreen(self.refresh_confirm, confidence = 0.9, grayscale=True)

        if refresh_confirm == None:
            print("No refresh confirm button found")
            return

        pyautogui.moveTo(refresh_confirm)
        pyautogui.click(button='left', clicks=2, interval=0.1)
        time.sleep(0.125)

    def scrollDown(self):
        print("Scrolling down")
        # refresh_button = pyautogui.locateOnScreen(self.refresh_button, confidence = 0.9)
        size = pyautogui.size()
        x1 = (size[0] / 2) + size[0]*0.05
        y2 = size[1] / 1.75
        pyautogui.moveTo(x1, y2)
        # pyautogui.moveTo(refresh_button[0] + refresh_button[0],
        #                  refresh_button[1] - 2*refresh_button[1])
        pyautogui.drag(0, -y2*0.75, 0.5, button='left')
        time.sleep(1)

    def findAndBuyCovenantBookmark(self):
        print("Finding covenant bookmark image")
        cov_bm_box = pyautogui.locateOnScreen(self.cov_bm_line, confidence = 0.9, grayscale=True)

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
        cov_buy_button = pyautogui.locateOnScreen(self.cov_bm_buy, confidence = 0.9, grayscale=True)

        if cov_buy_button == None:
            print("No covenant buy button found")
            return

        pyautogui.moveTo(cov_buy_button)
        pyautogui.click(button='left', clicks=2, interval=0.1)
        self.cov_count += 1
        self.gold -= 184000
        gold_amt.set(self.gold)
        time.sleep(0.125)

    def findAndBuyMysticMedal(self):
        print("Finding mystic medal image")
        mm_box = pyautogui.locateOnScreen(self.mystic_bm_line, confidence = 0.9, grayscale=True)

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
        mm_buy_button = pyautogui.locateOnScreen(self.mystic_bm_buy, confidence = 0.9, grayscale=True)

        if mm_buy_button == None:
            print("No mystic medal buy button found")
            return

        pyautogui.moveTo(mm_buy_button)
        pyautogui.click(button='left', clicks=2, interval=0.1)
        self.mm_count += 1
        self.gold -= 280000
        gold_amt.set(self.gold)
        time.sleep(0.125)

    def checkDispatchMission(self):
        try_again = pyautogui.locateOnScreen(self.try_again, confidence = 0.9, grayscale=True)

        if try_again == None:
            print("no dispatch mission pop-up")
        else:
            pyautogui.moveTo(try_again)
            pyautogui.click(button='left')


####################################################


root = tk.Tk()

skystone_amt = StringVar()
skystone_amt.set('Not entered')
gold_amt = StringVar()
gold_amt.set('Not entered')

def bootUp():
    try:
        global ASS
        ASS = AutoSecretShop(int(skystone_amt.get()), int(gold_amt.get()), 'cov_bm.png', 'covbuybutton.png', 'mm_bm.png', 'mmbuybutton.png', 'refreshbutton.png', 'refreshconfirm.png', 'dispatch_tryagain.png')
        print("ASS initiated")
        print(ASS)
    except:
        print("Failed to initiate ASS")

def enterSkystone():
    print("Submitting Skystone Amount")
    get_call = skystoneEntry.get()
    try:
        if isinstance(int(get_call), int):
            skystone_amt.set(get_call)
        else:
            skystone_amt.set("Invalid")
    except:
        skystone_amt.set("Invalid")

    bootUp()

def enterGold():
    print("Submitting Gold Amount")
    get_call = goldEntry.get()
    try:
        if isinstance(int(get_call), int):
            gold_amt.set(get_call)
        else:
            gold_amt.set("Invalid")
    except:
        gold_amt.set("Invalid")

    bootUp()

def startButton():
    print("Starting Auto Secret Shop")
    startButton['state'] = 'disabled'
    skystoneSubmit['state'] = 'disabled'
    goldSubmit['state'] = 'disabled'
    skystoneEntry['state'] = 'disabled'
    goldEntry['state'] = 'disabled'

    print(ASS)

    if skystone_amt.get() == "Invalid" or skystone_amt.get() == "Not entered" or gold_amt.get == "Invalid" or gold_amt.get == "Not entered":
        print("Error")
    else:
        try:
            threading.Thread(target=ASS.startASS).start()
        except:
            print("No ASS initiated yet")

def stopButton():
    print("Stopping Auto Secret Shop")
    startButton['state'] = 'normal'
    skystoneSubmit['state'] = 'normal'
    goldSubmit['state'] = 'normal'
    skystoneEntry['state'] = 'normal'
    goldEntry['state'] = 'normal'

    try:
        threading.Thread(target=ASS.stopASS).start()
    except:
        print("No ASS initiated yet")

########################################

startButtonFrame = tk.Frame(
    master = root,
    height = 500,
    width = 500
)

stopButtonFrame = tk.Frame(
    master = root,
    height = 500,
    width = 500
)

startButton = tk.Button(
    master = startButtonFrame,
    text = "Start",
    width = 5,
    height = 1,
    bg = "gray",
    fg = "black",
    command = startButton
)

stopButton = tk.Button(
    master = stopButtonFrame,
    text = "Stop",
    width = 5,
    height = 1,
    bg = "gray",
    fg = "black",
    command = stopButton
)

skystoneFrame = tk.Frame(
    master = root,
    height = 500,
    width = 500
)

skystoneLabel = tk.Label(
    master = skystoneFrame,
    text = "Enter Skystone Amount: ",
)

skystoneEntry = tk.Entry(
    master = skystoneFrame,
    width = 17
)

goldFrame = tk.Frame(
    master = root,
    height = 500,
    width = 500
)

goldLabel = tk.Label(
    master = goldFrame,
    text = "Enter Gold Amount:        "
)

goldEntry = tk.Entry(
    master = goldFrame,
    width = 17
)

skystoneToBeUsed = tk.Label(
    master = root,
    text = "Skystone Left to Use: "
)

goldToBeUsed = tk.Label(
    master = root,
    text = "Gold Left to Use:     "
)

skystoneAmt = tk.Label(
    master = root,
    textvariable = skystone_amt
)

goldAmt = tk.Label(
    master = root,
    textvariable = gold_amt
)

skystoneSubmit = tk.Button(
    master=root,
    text="Enter",
    width=5,
    height=1,
    bg="gray",
    fg="black",
    command=enterSkystone
)

goldSubmit = tk.Button(
    master=root,
    text="Enter",
    width=5,
    height=1,
    bg="gray",
    fg="black",
    command=enterGold
)

startButtonFrame.pack()
startButtonFrame.place(relx=0.04, rely=0.85)

stopButtonFrame.pack()
stopButtonFrame.place(relx=0.22, rely=0.85)

startButton.pack()
stopButton.pack()

skystoneFrame.pack()
skystoneFrame.place(relx=0.04, rely=0.1)
skystoneLabel.pack(side="left")
skystoneEntry.pack()

goldFrame.pack()
goldFrame.place(relx=0.04, rely=0.30)
goldLabel.pack(side="left")
goldEntry.pack()

skystoneToBeUsed.pack()
skystoneToBeUsed.place(relx=0.04, rely=0.48)
goldToBeUsed.pack()
goldToBeUsed.place(relx=0.04, rely=0.65)
skystoneAmt.pack()
skystoneAmt.place(relx=0.45, rely=0.48)
goldAmt.pack()
goldAmt.place(relx=0.45, rely=0.65)

skystoneSubmit.pack()
goldSubmit.pack()
skystoneSubmit.place(relx=0.825, rely=0.085)
goldSubmit.place(relx=0.825, rely=.285)

root.title("Auto Secret Shop by Traase")
root.geometry("320x240")
root.resizable(False, False)
root.mainloop()