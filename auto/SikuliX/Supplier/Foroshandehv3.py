import logging
from sikuli import *  # Importing Sikuli functions

counter = 1
cycle = 2

# Setup logging with a file handler
FORMAT = '%(asctime)-15s %(message)s'
logger = logging.getLogger('ForshandehLogger')
logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG
file_handler = logging.FileHandler('forshandeh.log')
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)

# Define constants for the images
NAME_BOX_IMAGE = "NAME_BOX_IMAGE.png"
ADDRESS_BOX_IMAGE = "ADDRESS_BOX_IMAGE.png"
PHONE_BOX_IMAGE = "PHONE_BOX_IMAGE.png"
COMMENT_BOX_IMAGE = "COMMENT_BOX_IMAGE.png"
USERNAME_BOX_IMAGE = "USERNAME_BOX_IMAGE.png"
ADD_BUTTON_IMAGE = "ADD_BUTTON_IMAGE.png"

CONFIRM_BUTTON_IMAGE = Pattern("1711646451805.png").similar(0.89)
RED_MESSAGE_IMAGE = "RED_MESSAGE_IMAGE.png"
GREEN_MESSAGE_IMAGE = "GREEN_MESSAGE_IMAGE.png"
URL_IMAGE = "URL_IMAGE.png"

# Function to refresh the browser
def refreshBrowser():
    if exists(URL_IMAGE):
        type(Key.F5)
        wait(3)
        logger.debug('Browser refreshed.')
    else:
        logger.debug("Failed to find the correct URL")

# Function to interact with input boxes
def fillInputBox(image, text, counter):
    click(image)
    type(text)
    logger.debug("Filled input box with image {} and text for Forshandeh {}".format(image, counter))

# Main script to add forshandehs

try:
    while counter <= cycle:
        refreshBrowser()
        fillInputBox(NAME_BOX_IMAGE, "Forshandeh " + str(counter), counter)
        fillInputBox(ADDRESS_BOX_IMAGE, "Address " + str(counter), counter)
        fillInputBox(PHONE_BOX_IMAGE, "9" * counter, counter)
        fillInputBox(COMMENT_BOX_IMAGE, "Tozihat for Forshandeh " + str(counter), counter)
        fillInputBox(USERNAME_BOX_IMAGE, "nk a f " + str(counter), counter)
        click(ADD_BUTTON_IMAGE)
        click(CONFIRM_BUTTON_IMAGE)

        if exists(RED_MESSAGE_IMAGE):
            logger.debug('Forshandeh already exists for counter: {}'.format(counter))
        elif exists(GREEN_MESSAGE_IMAGE):
            logger.debug('Forshandeh added successfully for counter: {}'.format(counter))
        else:
            logger.debug('Forshandeh failed to add for counter: {}'.format(counter))
        counter += 1
        wait(2)  # Wait for 2 seconds before the next iteration
finally:
    # Ensure the file handler is closed properly
    file_handler.close()
    logger.removeHandler(file_handler)
