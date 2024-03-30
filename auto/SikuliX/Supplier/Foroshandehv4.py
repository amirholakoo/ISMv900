import logging
from sikuli import *  # Importing Sikuli functions

counter = 1
cycle = 2
QUAN = 1

materials = ["Akhal F", 
            "Core F", 
            "Starch F", 
            "AKD F", 
            "Starch F", 
            "Akhal F"]

units = ["Bale Akhal F", "Core F",  "Starch 25KG F", "AKD 20L F", "Starch 20KG F", "Bale Akhal F"]
comment = "Comment from New Raw Material"

# Setup logging with a file handler
FORMAT = '%(asctime)-15s %(message)s'
logger = logging.getLogger('ForshandehLogger')
logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG
file_handler = logging.FileHandler('forshandeh.log')
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)




# Define constants for the images
SIDE_IMAGE = "SIDE_IMAGE.png"
NAME_BOX_IMAGE = "NAME_BOX_IMAGE-1.png"
ADDRESS_BOX_IMAGE = "ADDRESS_BOX_IMAGE-1.png"
PHONE_BOX_IMAGE = "PHONE_BOX_IMAGE-1.png"
COMMENT_BOX_IMAGE = "COMMENT_BOX_IMAGE-1.png"
USERNAME_BOX_IMAGE = "USERNAME_BOX_IMAGE.png"
ADD_BUTTON_IMAGE = "ADD_BUTTON_IMAGE.png"

CONFIRM_BUTTON_IMAGE = "CONFIRM_BUTTON_IMAGE.png"
RED_MESSAGE_IMAGE = "RED_MESSAGE_IMAGE-1.png"
GREEN_MESSAGE_IMAGE = "GREEN_MESSAGE_IMAGE-1.png"
URL_IMAGE = "URL_IMAGE.png"

SUPPLIER_DD_IMAGE = "SUPPLIER_DD_IMAGE.png"
MATERIAL_TYPE = "MATERIAL_TYPE.png"
MATERIAL_TYPE_DD_IMG = "MATERIAL_TYPE_DD_IMG.png"
UNIT_BOX_IMG = "UNIT_BOX_IMG.png"
QUAN_BOX_IMG = "QUAN_BOX_IMG.png"
MATERIAL_NAME_BOX_IMG = "MATERIAL_NAME_BOX_IMG.png"


#TEST CASE IMAGES
LIC_11_IMG = "LIC_11_IMG.png"
LIC_22_IMG = "LIC_22_IMG.png"
LIC_33_IMG = "LIC_33_IMG.png" 
LIC_44_IMG = "LIC_44_IMG.png"
LIC_55_IMG = "LIC_55_IMG.png"

SH_TYPE_IN_IMG = "SH_TYPE_IN_IMG.png"
SH_TYPE_OUT_IMG = "SH_TYPE_OUT_IMG.png"

S_1_IMG = "S_1_IMG.png"
M_T_S_1_IMG = "M_T_S_1_IMG.png"
R_M_1_S_1_IMG = "R_M_1_S_1_IMG.png"
R_M_2_S_1_IMG = "R_M_2_S_1_IMG.png"
U_S_1_IMG = "U_S_1_IMG.png"

S_2_IMG = "S_2_IMG.png"
M_T_S_2_IMG = "M_T_S_2_IMG.png"
R_M_1_S_2_IMG = "R_M_1_S_2_IMG.png"
R_M_2_S_2_IMG = "R_M_2_S_2_IMG.png"
U_S_2_IMG = "U_S_2_IMG.png"

S_3_IMG = "S_3_IMG.png"
M_T_S_3_IMG = "M_T_S_3_IMG.png"
R_M_1_S_3_IMG = "R_M_1_S_3_IMG.png"
R_M_2_S_3_IMG = "R_M_2_S_1_IMG.png"
R_M_3_S_3_IMG = "R_M_3_S_3_IMG.png"
U_S_3_IMG = "U_S_3_IMG.png"

S_4_IMG = "S_4_IMG.png"
M_T_S_4_IMG = "M_T_S_4_IMG.png"
R_M_1_S_4_IMG = "R_M_1_S_4_IMG.png"
R_M_2_S_4_IMG = "R_M_2_S_4_IMG.png"
U_S_4_IMG = "U_S_4_IMG.png"

S_5_IMG = "S_5_IMG.png"
M_T_S_5_IMG = "M_T_S_3_IMG.png"
R_M_1_S_5_IMG = "R_M_1_S_3_IMG.png"
R_M_2_S_5_IMG = "R_M_2_S_1_IMG.png"
U_S_5_IMG = "U_S_5_IMG.png"

Anbar_Akhal_IMG = "Anbar_Akhal_IMG.png"
Anbar_Khamir_G_IMG = "Anbar_Khamir_G_IMG.png"
Anbar_Khamir_K_IMG = "Anbar_Khamir_K_IMG.png"
Anbar_Koochak_IMG = "Anbar_Koochak_IMG.png"
Anbar_Muhvateh_K_IMG = "Anbar_Muhvateh_K_IMG.png"
Anbar_Salon_T_IMG = "Anbar_Salon_T_IMG.png"
Anbar_Sangin_IMG = "Anbar_Sangin_IMG.png"

#################################################################################
#################################################################################
#################################################################################
#################################################################################



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

def selectDropdownAndVerify(image, verification_image):
    click(image)
    wait(1)
    if exists(verification_image):
        click(verification_image)
        click(SIDE_IMAGE)
        log("Dropdown %s selected and verified with %s" % (image, verification_image))
    
    else:
        log("Failed to verify selection for %s" % image, "error")

        
# Main script to add forshandehs

try:
    
    while counter <= cycle:
        #refreshBrowser()
        ################################################################################# 
        # Navigate to the Add Supplier page
        click(URL_IMAGE)
        type("http://127.0.0.1:8000/myapp/addSupplier/")
        type(Key.ENTER)
        #refreshBrowser()
        #################################################################################
        
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


        ################################################################################# 
        # Navigate to the Add Material Type page
        click(URL_IMAGE)
        type("http://127.0.0.1:8000/myapp/addMaterialType/")
        type(Key.ENTER)
        #refreshBrowser()
        #################################################################################
        
        # Select the material based on the counter, adjusting for zero-based index
        material = materials[counter - 1]
        
        selectDropdownAndVerify(SUPPLIER_DD_IMAGE, "S_" + str(counter) + "_IMG")
        fillInputBox(MATERIAL_TYPE, material + str(counter), counter)
        fillInputBox(USERNAME_BOX_IMAGE, "nk a m t " + str(counter), counter)
        click(ADD_BUTTON_IMAGE)
        click(CONFIRM_BUTTON_IMAGE)

        if exists(RED_MESSAGE_IMAGE):
            logger.debug('Material Type already exists for counter: {}'.format(counter))
        elif exists(GREEN_MESSAGE_IMAGE):
            logger.debug('Material Type added successfully for counter: {}'.format(counter))
        else:
            logger.debug('Material Type failed to add for counter: {}'.format(counter))
            
        ################################################################################# 
        # Navigate to the Add Unit page
        click(URL_IMAGE)
        type("http://127.0.0.1:8000/myapp/addUnit/")
        type(Key.ENTER)
        type(Key.F5)
        #refreshBrowser()
        #################################################################################
  
        selected_unit = units[counter - 1]
        
        selectDropdownAndVerify(SUPPLIER_DD_IMAGE, "S_" + str(counter) + "_IMG")
        selectDropdownAndVerify(MATERIAL_TYPE_DD_IMG, "M_T_S_" + str(counter) + "_IMG")
        fillInputBox(UNIT_BOX_IMG, selected_unit + str(counter), counter)
        fillInputBox(QUAN_BOX_IMG, str(QUAN), counter)
        fillInputBox(USERNAME_BOX_IMAGE, "nk a u " + str(counter), counter)

        click(ADD_BUTTON_IMAGE)
        click(CONFIRM_BUTTON_IMAGE)

        if exists(RED_MESSAGE_IMAGE):
            logger.debug('Unit already exists for counter: {}'.format(counter))
        elif exists(GREEN_MESSAGE_IMAGE):
            logger.debug('Unit added successfully for counter: {}'.format(counter))
        else:
            logger.debug('Unit failed to add for counter: {}'.format(counter))

        ################################################################################# 
        # Navigate to the Add New Material page
        click(URL_IMAGE)
        type("http://127.0.0.1:8000/myapp/addRawMaterial/")
        type(Key.ENTER)
        #type(Key.F5)
        #refreshBrowser()
        #################################################################################
  
        
        
        selectDropdownAndVerify(SUPPLIER_DD_IMAGE, "S_" + str(counter) + "_IMG")
        selectDropdownAndVerify(MATERIAL_TYPE_DD_IMG, "M_T_S_" + str(counter) + "_IMG")
        fillInputBox(MATERIAL_NAME_BOX_IMG, selected_unit + str(counter) , counter)
        fillInputBox(COMMENT_BOX_IMAGE, comment + str(counter), counter)
        fillInputBox(USERNAME_BOX_IMAGE, "nk a u " + str(counter), counter)

        click(ADD_BUTTON_IMAGE)
        click(CONFIRM_BUTTON_IMAGE)

        if exists(RED_MESSAGE_IMAGE):
            logger.debug('Raw Material already exists for counter: {}'.format(counter))
        elif exists(GREEN_MESSAGE_IMAGE):
            logger.debug('Raw Material added successfully for counter: {}'.format(counter))
        else:
            logger.debug('Raw Material failed to add for counter: {}'.format(counter))
        
        counter += 1
        wait(2)  # Wait for 2 seconds before the next iteration

finally:
    # Ensure the file handler is closed properly
    file_handler.close()
    logger.removeHandler(file_handler)
