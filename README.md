# Caroubot

## Background
This project is to help automate the process of uploading listings onto Carousell -- a consumer marketplace for buying and selling new and secondhand goods.
Instead of spending a few minutes coming up with a title, description, and clicking on all the mandatory buttons, I have spent about 15 hours writing this script that automates the whole process for me!

## Libraries/APIs used
To help me with the clicking of buttons, I used Selenium to help me emulate a ChromeDriver and its actions to click on buttons as well as send text.
As for the generation of the descriptions, I used OpenAI's API for their LLM (ChatGPT3.5-Turbo) to come up with engaging descriptions for me based on some descriptors.

## Inputs
1. Image file with the file name of "[ListingTitle];[Brand];[Price].jpg/png".
2. Save the image file under the "to list" folder.
3. Run the script and a ChromeDriver would pop up (emulated Chrome browser).
4. After logging in using your Carousell details, a CaPTCHA would load and you will have some time to complete it.
5. Ta, da! Just sit back and watch the script do its thing!

## To be changed by user
1. File paths in main.py
2. API key, Carousell Email & Password

## How it works
To minimise the user input, the script would extract the respective information directly from the file name of the image.
Once the listing has been uploaded, the image would be moved from the "to list" folder to the "listed" folder. This ensures that there are no duplicate listings! (Note that the script will upload all the images in the "to list" folder onto Carousell. There is currently NO scheduling implemented.)