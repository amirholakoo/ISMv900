import logging
from sikuli import *  # Importing Sikuli functions

counter = 1
cycle = 2

# Setup logging with a file handler
logger = logging.getLogger('CustomerLogger')
logger.setLevel(logging.INFO)  # Set the log level to INFO
file_handler = logging.FileHandler('add_customer_test.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logger.addHandler(file_handler)

# Define constants for the images
NAME_BOX_IMAGE = "NAME_BOX_IMAGE.png"
ADDRESS_BOX_IMAGE = "ADDRESS_BOX_IMAGE.png"
PHONE_BOX_IMAGE = "PHONE_BOX_IMAGE.png"
COMMENT_BOX_IMAGE = "COMMENT_BOX_IMAGE.png"
USERNAME_BOX_IMAGE = "USERNAME_BOX_IMAGE.png"
ADD_BUTTON_IMAGE = "ADD_BUTTON_IMAGE.png"

CONFIRM_BUTTON_IMAGE = "1711643203063.png"
RED_MESSAGE_IMAGE = "RED_MESSAGE_IMAGE.png"
GREEN_MESSAGE_IMAGE = "GREEN_MESSAGE_IMAGE.png"
URL_IMAGE = "URL_IMAGE.png"

# Function to refresh the browser
def refreshBrowser():
    if exists(URL_IMAGE):
        type(Key.F5)
        wait(3)
        logger.info('Browser refreshed.')
    else:
        logger.info("Failed to find the correct URL")

# Function to interact with input boxes
def fillInputBox(image, text, counter):
    click(image)
    type(text)
    logger.info("Filled input box with image {} and text for Customer {}".format(image, counter))

# Main script to add customers

try:
    while counter <= cycle:
        refreshBrowser()
        fillInputBox(NAME_BOX_IMAGE, "Customer " + str(counter), counter)
        fillInputBox(ADDRESS_BOX_IMAGE, "Address " + str(counter), counter)
        fillInputBox(PHONE_BOX_IMAGE, "9" * counter, counter)
        fillInputBox(COMMENT_BOX_IMAGE, "Tozihat for Customer " + str(counter), counter)
        fillInputBox(USERNAME_BOX_IMAGE, "nk a c " + str(counter), counter)
        click(ADD_BUTTON_IMAGE)
        click(CONFIRM_BUTTON_IMAGE)

        if exists(RED_MESSAGE_IMAGE):
            logger.warning('Customer already exists for counter: {}'.format(counter))
        elif exists(GREEN_MESSAGE_IMAGE):
            logger.info('Customer added successfully for counter: {}'.format(counter))
        else:
            logger.info('Customer failed to add for Customer: {}'.format(counter))
        counter += 1
        wait(2)  # Wait for 2 seconds before the next iteration
finally:
    # Ensure the file handler is closed properly
    file_handler.close()
    logger.removeHandler(file_handler)
