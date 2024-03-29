import logging
from sikuli import *  # Importing Sikuli functions


# Constants for image paths

URL_IMAGE = "URL_IMAGE.png"
SIDE_IMAGE = "SIDE_IMAGE.png"
LICENSE_DD_IMAGE = "LICENSE_DD_IMAGE.png"
INCOMING_DD_IMAGE = "INCOMING_DD_IMAGE.png"
SUPPLIER_DD_IMAGE = "SUPPLIER_DD_IMAGE.png"
MATERIAL_TYPE_DD_IMAGE = "MATERIAL_TYPE_DD_IMAGE.png"
MATERIAL_NAME_DD_IMAGE = "MATERIAL_NAME_DD_IMAGE.png"

USERNAME_IMAGE = "USERNAME_IMAGE.png"
FORK_USERNAME_IMAGE = "FORK_USERNAME_IMAGE.png"

ADD_BUTTON_IMAGE = "ADD_BUTTON_IMAGE.png"
CONFIRM_BUTTON_IMAGE = "CONFIRM_BUTTON_IMAGE.png"
RED_MESSAGE_IMAGE = "RED_MESSAGE_IMAGE.png"
GREEN_MESSAGE_IMAGE = "GREEN_MESSAGE_IMAGE.png"
WEIGHT_STATION_PANEL_IMAGE = "WEIGHT_STATION_PANEL_IMAGE.png"
WEIGHT1_BUTTON_IMAGE = "WEIGHT1_BUTTON_IMAGE.png"
WEIGHT1_PAGE_IMAGE = "WEIGHT1_PAGE_IMAGE.png"
WEIGHT1_BOX_IMAGE = "WEIGHT1_BOX_IMAGE.png"
FORKLIFT_PANEL_IMAGE = "FORKLIFT_PANEL_IMAGE.png"
UNLOADED_IMAGE = "UNLOADED_IMAGE.png"
UNLOADING_LOCATION_DD_IMAGE = "UNLOADING_LOCATION_DD_IMAGE.png"
UNIT_DD_IMAGE = "UNIT_DD_IMAGE.png"
QUANTITY_BOX_IMAGE = "QUANTITY_BOX_IMAGE.png"
QUALITY_BOX_IMAGE = "QUALITY_BOX_IMAGE.png"
WEIGHT2_BUTTON_IMAGE = "WEIGHT2_BUTTON_IMAGE.png"
WEIGHT2_PAGE_IMAGE = "WEIGHT2_PAGE_IMAGE.png"
WEIGHT2_BOX_IMAGE = "WEIGHT2_BOX_IMAGE.png"
NET_BOX_IMAGE = "NET_BOX_IMAGE.png"
SO_PAGE_IMAGE = "SO_PAGE_IMAGE.png"
PENALTY_BOX_IMAGE = "PENALTY_BOX_IMAGE.png"
PRICE_PER_KG_BOX_IMAGE = "PRICE_PER_KG_BOX_IMAGE.png"
VAT_DD_IMAGE = "VAT_DD_IMAGE.png"
VAT_0_IMAGE = "VAT_0_IMAGE.png"
EXTRA_COST_BOX_IMAGE = "EXTRA_COST_BOX_IMAGE.png"
INVOICE_STATUS_DD_IMAGE = "INVOICE_STATUS_DD_IMAGE.png"
INVOICE_STATUS_Re_IMAGE = "INVOICE_STATUS_Re_IMAGE.png"
INVOICE_STATUS_NA_IMAGE = "INVOICE_STATUS_NA_IMAGE.png"
INVOICE_NUMBER_BOX_IMAGE = "INVOICE_NUMBER_BOX_IMAGE.png"
PAYMENT_STATUS_DD_IMAGE = "PAYMENT_STATUS_DD_IMAGE.png"
PAYMENT_STATUS_T_IMAGE = "PAYMENT_STATUS_T_IMAGE.png"
PAYMENT_STATUS_P_IMAGE = "PAYMENT_STATUS_P_IMAGE.png"
DOC_INFO_BOX_IMAGE = "DOC_INFO_BOX_IMAGE.png"
COMMENTS_BOX_IMAGE = "COMMENTS_BOX_IMAGE.png"

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

# Values for the test
w1 = 36000
w2 = 16000
net = 20000
quan = 12
quality_report = 1
penalty = 0
ppk = 10
extracost = 0
supplier_invoice_number = "-"
doc_info = "nothing at this point"
PO_comments = "PO nothing to report"

#################################################################################
#################################################################################
#################################################################################
#################################################################################


# Setup logging with a file handler
FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logger = logging.getLogger('AddShipmentLogger')
logger.setLevel(logging.INFO)  # Capture all messages of INFO level and above
file_handler = logging.FileHandler('AddShipment.log')
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)

# Helper function to log messages
def log(message, level="info"):
    if level.lower() == "info":
        logger.info(message)
    elif level.lower() == "warning":
        logger.warning(message)
    elif level.lower() == "error":
        logger.error(message)
    print(message)  # Also print to console for real-time feedback

# Define constants for the images
# Add all necessary image constants here...

# Helper functions for interaction
def refreshBrowser():
    click(URL_IMAGE)
    type(Key.F5)
    wait(3)
    log('Browser refreshed.')

def fillInputBox(image, text):
    click(image)
    if isinstance(text, int):  # Check if the value is an integer
        text = str(text)  # Convert integer to string for typing
    type(text)
    wait(1)
    click(SIDE_IMAGE)
    #logger.info("Input box successful for image: " + str(image))
    log("Input box %s filled with text: %s" % (image, text))

def selectDropdownAndVerify(image, verification_image):
    click(image)
    wait(1)
    if exists(verification_image):
        click(verification_image)
        click(SIDE_IMAGE)
        log("Dropdown %s selected and verified with %s" % (image, verification_image))
    
    else:
        log("Failed to verify selection for %s" % image, "error")

def selectMenuAndClick(menu, choice_image):
    if exists(menu):
        click(choice_image)
        log("Menu %s selected and selected with %s" % (menu, choice_image))
    
    else:
        log("Failed to verify Menu and selection for %s" % menu, "error")

def validateAndLog(action_desc):
    if exists(GREEN_MESSAGE_IMAGE):
        log('Success: %s' % action_desc)
    elif exists(RED_MESSAGE_IMAGE):
        log('Error encountered during %s' % action_desc, "error")
    else:
        log('Status unknown after %s' % action_desc, "warning")

#################################################################################
#################################################################################
#################################################################################
#################################################################################


# Main automation script
try:
    
    ################################################################################# 
    # Navigate to the shipment page
    click(URL_IMAGE)
    type("http://127.0.0.1:8000/myapp/addShipment/")
    type(Key.ENTER)
    #refreshBrowser()
    #################################################################################
    
    # Adding shipments
    selectDropdownAndVerify(LICENSE_DD_IMAGE, LIC_11_IMG)
    selectDropdownAndVerify(INCOMING_DD_IMAGE, SH_TYPE_IN_IMG)
    selectDropdownAndVerify(SUPPLIER_DD_IMAGE, S_1_IMG)
    selectDropdownAndVerify(MATERIAL_TYPE_DD_IMAGE, M_T_S_1_IMG)
    selectDropdownAndVerify(MATERIAL_NAME_DD_IMAGE, R_M_1_S_1_IMG)
    fillInputBox(USERNAME_IMAGE, "nk a s")
    
    click(ADD_BUTTON_IMAGE)
    click(CONFIRM_BUTTON_IMAGE)
    validateAndLog("adding New shipment")
    wait(2)

    #################################################################################
    # Navigate to the Weight Station Panel page
    click(URL_IMAGE)
    type("http://127.0.0.1:8000/myapp/weightStationPanel/")
    type(Key.ENTER)
    #refreshBrowser()
    #################################################################################
    
    # Weight Station Panel
    selectMenuAndClick(WEIGHT_STATION_PANEL_IMAGE, WEIGHT1_BUTTON_IMAGE)
    
    selectDropdownAndVerify(LICENSE_DD_IMAGE, LIC_11_IMG)    
    fillInputBox(WEIGHT1_BOX_IMAGE, w1)
    fillInputBox(USERNAME_IMAGE, "nk w1")
    
    click(ADD_BUTTON_IMAGE)
    click(CONFIRM_BUTTON_IMAGE)
    validateAndLog("adding Weight1")
    wait(2)
    
    #################################################################################
    # Forklift Panel
    # Navigate to the Forklift Panel page
    click(URL_IMAGE)
    type("http://127.0.0.1:8000/myapp/forkliftPanel/")
    type(Key.ENTER)
    #refreshBrowser()
    #################################################################################
    
    # Unloaded
    selectMenuAndClick(FORKLIFT_PANEL_IMAGE,UNLOADED_IMAGE)
    
    selectDropdownAndVerify(LICENSE_DD_IMAGE, LIC_11_IMG)
    selectDropdownAndVerify(UNLOADING_LOCATION_DD_IMAGE, Anbar_Akhal_IMG)


    selectDropdownAndVerify(UNIT_DD_IMAGE, U_S_1_IMG)
    fillInputBox(QUANTITY_BOX_IMAGE, quan)
    fillInputBox(QUALITY_BOX_IMAGE, quality_report)
    fillInputBox(FORK_USERNAME_IMAGE, "unFK")
    
    click(ADD_BUTTON_IMAGE)
    click(CONFIRM_BUTTON_IMAGE)
    validateAndLog("Unloaded")
    wait(2)

    #################################################################################
    # Navigate to the Weight Station Panel page
    click(URL_IMAGE)
    type("http://127.0.0.1:8000/myapp/weightStationPanel/")
    type(Key.ENTER)
    #refreshBrowser()
    #################################################################################

    # Weight Station Panel
    selectMenuAndClick(WEIGHT_STATION_PANEL_IMAGE, WEIGHT2_BUTTON_IMAGE)
    
    selectDropdownAndVerify(LICENSE_DD_IMAGE, LIC_11_IMG)    
    fillInputBox(WEIGHT2_BOX_IMAGE, w2)
    fillInputBox(NET_BOX_IMAGE, net)
    fillInputBox(USERNAME_IMAGE, "nk w2")
    
    click(ADD_BUTTON_IMAGE)
    click(CONFIRM_BUTTON_IMAGE)
    validateAndLog("adding Weight2")
    wait(2)

    
    #################################################################################
    # Navigate to the PO page
    click(URL_IMAGE)
    type("http://127.0.0.1:8000/myapp/createPurchaseOrder/")
    type(Key.ENTER)
    #wheel(WHEEL_UP, 3)
    #refreshBrowser()
    #################################################################################

    # Create Purchase Order
       
    selectDropdownAndVerify(LICENSE_DD_IMAGE, LIC_11_IMG)
    fillInputBox(PENALTY_BOX_IMAGE, penalty)
    fillInputBox(PRICE_PER_KG_BOX_IMAGE, ppk)
    selectDropdownAndVerify(VAT_DD_IMAGE, VAT_0_IMAGE)
    fillInputBox(EXTRA_COST_BOX_IMAGE, extracost)
    wheel(WHEEL_DOWN, 3)
    wait(1)
    selectDropdownAndVerify(INVOICE_STATUS_DD_IMAGE, INVOICE_STATUS_Re_IMAGE)
    fillInputBox(INVOICE_NUMBER_BOX_IMAGE, supplier_invoice_number)
    selectDropdownAndVerify(PAYMENT_STATUS_DD_IMAGE, PAYMENT_STATUS_P_IMAGE)
    fillInputBox(DOC_INFO_BOX_IMAGE, doc_info)
    fillInputBox(COMMENTS_BOX_IMAGE, PO_comments)
    fillInputBox(USERNAME_IMAGE, "nk c PO")
    
    click(ADD_BUTTON_IMAGE)
    click(CONFIRM_BUTTON_IMAGE)
    wheel(WHEEL_UP, 5)
    validateAndLog("Created PO")
    wait(2)


except FindFailed as e:
    log("Sikuli could not find an image on the screen: %s" % str(e), "error")

# Cleanup
file_handler.close()
logger.removeHandler(file_handler)
