import logging
from sikuli import *  # Importing Sikuli functions

counter = 1
cycle = 2

# Setup logging with a file handler
FORMAT = '%(asctime)-15s %(message)s'
logger = logging.getLogger('AddTruckLogger')
logger.setLevel(logging.WARNING)  # Set the log level to WARNING
file_handler = logging.FileHandler('AddTruck.log')
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)


# Define constants for the images - replace these with your actual image filenames


TWO_DIGIT_BOX_IMAGE = "FIRST_2D_IMAGE.png"
THREE_DIGIT_BOX_IMAGE ="FIRST_3D_IMAGE.png"
FIRST_BOX_IMAGE = "FIRST_BOX_IMAGE.png"
SECOND_BOX_IMAGE = "SECOND_BOX_IMAGE.png"
THIRD_BOX_IMAGE = "THIRD_BOX_IMAGE.png"
LAST_BOX_IMAGE = "LAST_BOX_IMAGE.png"
CHECK_BUTTON_IMAGE = "CHECK_BUTTON_IMAGE.png"
ADD_BUTTON_IMAGE = "ADD_BUTTON_IMAGE.png"
CORRECT_BUTTON_IMAGE = "CORRECT_BUTTON_IMAGE.png"
RED_INDICATOR_IMAGE = "SUCCESS_INDICATOR_IMAGE.png"


URL_IMAGE = "URL_IMAGE.png"

# Function to refresh the browser
def refreshBrowser():
    if exists (URL_IMAGE):
        type(Key.F5)
        wait(3)
        logging.debug('Browser refreshed.')
    else:
        logging.debug("Filled to find correct URL")

# Function to fill input boxes
def fillInputBox(image, text):
    doubleClick(image)
    type(text)
    logger.debug("Filled input box with image {} and text {} for Truck {}".format(image, text, counter))

# Interact with input boxes
def fillInputBox1C(image, text):
    click(image)
    type(text)
    logger.debug("Filled input box with image {} and text {} for Truck {}".format(image, text, counter))
    
# Main script


try:
    while counter <= cycle:  # Add different trucks
        refreshBrowser()
        fillInputBox(TWO_DIGIT_BOX_IMAGE, str(counter) + str(counter))
        fillInputBox(THREE_DIGIT_BOX_IMAGE, str(counter) * 3)
        click(CHECK_BUTTON_IMAGE)
    
        if exists(RED_INDICATOR_IMAGE):
            counter += 1  # Increment if the truck exists and retry
            logger.debug('Truck already exists for counter: {}'.format(counter))
        else:
            # Fill out the form
            fillInputBox1C(FIRST_BOX_IMAGE, "Truck " + str(counter))
            fillInputBox1C(SECOND_BOX_IMAGE, "Lic Nm. " + str(counter))
            fillInputBox1C(THIRD_BOX_IMAGE, "9" * counter)
            fillInputBox1C(LAST_BOX_IMAGE, "nk a t " + str(counter))
            click(ADD_BUTTON_IMAGE)
            click(CORRECT_BUTTON_IMAGE)
            counter += 1  # Increment for the next truck
            logger.debug('Truck added successfully for counter: {}'.format(counter))
    
        wait(2)  # Wait for 2 seconds before the next iteration
finally:
    file_handler.close()
    logger.removeHandler(file_handler)
