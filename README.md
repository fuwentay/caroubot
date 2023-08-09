# Caroubot

## Background
This project is to help automate the process of uploading listings onto Carousell -- a consumer marketplace for buying and selling new and secondhand goods.
Instead of spending a few minutes coming up with a title, description, and clicking on all the mandatory buttons, I have spent about 15 hours writing this script that automates the whole process for me!

## Libraries/APIs used
To help me with the clicking of buttons, I used Selenium to help me emulate a ChromeDriver and its actions to click on buttons as well as send text.
As for the generation of the descriptions, I used OpenAI's API for their LLM (ChatGPT3.5-Turbo) to come up with engaging descriptions for me based on some descriptors.

## Inputs
#### 1. Image file with the file name of "[ListingTitle];[Brand];[Price].jpg/png".
#### 2. Save the image file under the "to list" folder.
#### 3. Run the script and a ChromeDriver would pop up (emulated Chrome browser).
#### 4. After logging in using your Carousell details, a CaPTCHA would load and you will have some time to complete it.
#### 5. Ta, da! Just sit back and watch the script do its thing!

## To be changed by user
#### 1. File paths in main.py
#### 2. API key, Carousell Email & Password

## How it works
To minimise the user input, the script would extract the respective information directly from the file name of the image.
Once the listing has been uploaded, the image would be moved from the "to list" folder to the "listed" folder. This ensures that there are no duplicate listings! (Note that the script will upload all the images in the "to list" folder onto Carousell. There is currently NO scheduling implemented.)

## Limitations and Future Work
### 1. Google's ReCAPTCHA
To prevent robots from flooding and putting stress on servers, ReCAPTCHA was built to hinder automation web testing. This appears to be a problem that we face when we initialise this script as we are faced with a ReCAPTCHA that we need to solve. This means that whenever this script is initialised, the user would have to solve the ReCAPTCHA manually, proving to be an obstacle for automation, not allowing this process to be fully autonomous. However, one could look into ReCAPTCHA bot detection algorithm to make the robot less suspicious (e.g. implement more time.sleep(), set ChromeDriver to fullscreen, use Selenium-stealth).
### 2. "Category" is set as "Men's Activewear"
Based on which "Category" is chosen, the web structure would change meaning that the XPath of the elements would change. Thus, buttons and fields thereafter cannot be referenced by using the same identifier. As such, this code is not robust and only works for the "Category" of "Men's Activewear". What could be done is to identify elements by using the text contained within the element as it would not change when the web structure is different.

## Live Demo
[Click here](https://www.loom.com/share/cff5aea893ae4d1586af7cfa01ce251f?sid=b47c9bf2-ba3b-4763-b466-cb8ef4776ed5)