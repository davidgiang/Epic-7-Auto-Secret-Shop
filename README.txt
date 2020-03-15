1.) Open command prompt  as ADMIN and navigate to the src folder

	*INSTALL THESE DEPENDENCIES IF YOU DON'T HAVE THEM*
	
	To install them, just run these commands in src folder
	
	1.a) pip install pyautogui
	1.b) pip install opencv

2.) Type 'python' to open up python shell

3.) Run the following code to start ASS.

-If the image recognition does not work, you need to provide the pics yourself
-The first parameter value is the amount of skystones you wish to spend in the secret shop.
-The command prompt must be on the primary monitor (where your emulator screen is)
-Position the command prompt so that it is not blocking the refresh button and the items in the shop
-Dispatch mission can interfere

###

from ImageDetection import AutoSecretShop
ASS = AutoSecretShop(3, 'cov_bm.png', 'covbuybutton.png', 'mm_bm.png', 'mmbuybutton.png', 'refreshbutton.png', 'refreshconfirm.png')
ASS.startASS()

###