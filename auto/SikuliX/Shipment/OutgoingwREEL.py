import logging
from sikuli import *  # Importing Sikuli functions

#================================================================================
################################### SETTINGS ####################################
#================================================================================
# Values for the test
counter = 2
cycle = 4
QUAN = 1
reel_production_quantity = 2

w1 = 36000
w2 = 16000
net = 20000
OUT_w1 = 16000
OUT_w2 = 38000
OUT_net = 22000

quan = 12
quality_report = 1

penalty = 0
ppk = 10
OUT_ppk = 1000
extracost = 0
supplier_invoice_number = "-"
sales_invoice_number = "NA"
doc_info = "nothing at this point"
PO_comments = "PO nothing to report"
SO_comments = "SO no COMMENTS"
NEW_REEL_comments = "NEW REEL TOZIHAT AKA COMNT." 

materials = ["Akhal F", 
            "Core F", 
            "Starch F", 
            "AKD F", 
            "Starch F", 
            "Akhal F"]

units = ["Bale Akhal F", "Core F",  "Starch 25KG F", "AKD 20L F", "Starch 20KG F", "Bale Akhal F"]

comment = "Comment from New Raw Material"
#================================================================================
#================================================================================
#================================================================================

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
################################
URL_IMAGE = "URL_IMAGE.png"
SIDE_IMAGE = "SIDE_IMAGE.png"
################################
# Define constants for the images
CUS_NAME_BOX_IMAGE = "NAME_BOX_IMAGE.png"
ADDRESS_BOX_IMAGE = "ADDRESS_BOX_IMAGE.png"
PHONE_BOX_IMAGE = "PHONE_BOX_IMAGE.png"
COMMENT_BOX_IMAGE = "COMMENT_BOX_IMAGE.png"
################################
SUP_NAME_BOX_IMAGE = "NAME_BOX_IMAGE-1.png"
################################
USERNAME_BOX_IMAGE = "USERNAME_BOX_IMAGE.png"
################################

MATERIAL_TYPE = "MATERIAL_TYPE.png"
MATERIAL_TYPE_DD_IMG = "MATERIAL_TYPE_DD_IMG.png"
UNIT_BOX_IMG = "UNIT_BOX_IMG.png"
QUAN_BOX_IMG = "QUAN_BOX_IMG.png"
MATERIAL_NAME_BOX_IMG = "MATERIAL_NAME_BOX_IMG.png"
################################
LICENSE_DD_IMAGE = "LICENSE_DD_IMAGE.png"
INCOMING_DD_IMAGE = "INCOMING_DD_IMAGE.png"
SUPPLIER_DD_IMAGE = "SUPPLIER_DD_IMAGE.png"
CUSTOMER_DD_IMAGE = "CUSTOMER_DD_IMAGE.png"
MATERIAL_TYPE_DD_IMAGE = "MATERIAL_TYPE_DD_IMAGE.png"
MATERIAL_NAME_DD_IMAGE = "MATERIAL_NAME_DD_IMAGE.png"
################################
USERNAME_IMAGE = "USERNAME_IMAGE.png"
FORK_USERNAME_IMAGE = "FORK_USERNAME_IMAGE.png"
################################
CONFIRM_BUTTON_IMAGE = "CONFIRM_BUTTON_IMAGE.png"
RED_MESSAGE_IMAGE = "RED_MESSAGE_IMAGE.png"
GREEN_MESSAGE_IMAGE = "GREEN_MESSAGE_IMAGE.png"
################################
REEL_NUMBER_IMG = "REEL_NUMBER_IMG.png"
REEL_WIDTH_IMG = Pattern("REEL_WIDTH_IMG.png").similar(0.86).targetOffset(9,2)
REEL_GSM_IMG = "REEL_GSM_IMG.png"
REEL_L_IMG = "REEL_L_IMG.png"
REEL_BREAKS_IMG = "REEL_BREAKS_IMG.png"
REEL_Q_IMG = "REEL_Q_IMG.png"
REEL_qrCODE_IMG = Pattern("REEL_qrCODE_IMG.png").similar(0.59)
################################
WEIGHT_STATION_PANEL_IMAGE = "WEIGHT_STATION_PANEL_IMAGE.png"
WEIGHT1_BUTTON_IMAGE = "WEIGHT1_BUTTON_IMAGE.png"
WEIGHT1_PAGE_IMAGE = "WEIGHT1_PAGE_IMAGE.png"
WEIGHT1_BOX_IMAGE = Pattern("WEIGHT1_BOX_IMAGE.png").targetOffset(77,-1)
################################
FORKLIFT_PANEL_IMAGE = "FORKLIFT_PANEL_IMAGE.png"

LOADED_IMAGE = "LOADED_IMAGE.png"
USED_IMAGE = "USED_IMAGE.png"
MOVED_IMAGE = "MOVED_IMAGE.png"
RETURNED_IMAGE = "RETURNED_IMAGE.png"
################################
UNLOADING_LOCATION_DD_IMAGE = "UNLOADING_LOCATION_DD_IMAGE.png"
UNIT_DD_IMAGE = "UNIT_DD_IMAGE.png"
QUANTITY_BOX_IMAGE = "QUANTITY_BOX_IMAGE.png"
QUALITY_BOX_IMAGE = "QUALITY_BOX_IMAGE.png"
UNLOADED_IMAGE = "UNLOADED_IMAGE.png"
################################
LOADED_DD_IMAGE = "LOADED_IMAGE.png"
WIDTH_DD_IMAGE = "WIDTH_DD_IMAGE.png"
W_200_IMG = "W_200_IMG.png"
W_210_IMG = "W_210_IMG.png"
W_220_IMG = "W_220_IMG.png"
W_230_IMG = "W_230_IMG.png"
W_240_IMG = "W_240_IMG.png"
W_250_IMG = "W_250_IMG.png"
REEL_CHKBOX_BLANK_IMG = Pattern("REEL_CHKBOX_BLANK_IMG.png").targetOffset(-15,0)
REEL_CHKBOX_SELECTED_IMG = "REEL_CHKBOX_SELECTED_IMG.png"
################################
WEIGHT2_BUTTON_IMAGE = "WEIGHT2_BUTTON_IMAGE.png"
WEIGHT2_PAGE_IMAGE = "WEIGHT2_PAGE_IMAGE.png"
WEIGHT2_BOX_IMAGE = "WEIGHT2_BOX_IMAGE.png"
NET_BOX_IMAGE = "NET_BOX_IMAGE.png"
################################
SO_PAGE_IMAGE = "SO_PAGE_IMAGE.png"
PENALTY_BOX_IMAGE = "PENALTY_BOX_IMAGE.png"
PRICE_PER_KG_BOX_IMAGE = "PRICE_PER_KG_BOX_IMAGE.png"
VAT_DD_IMAGE = "VAT_DD_IMAGE.png"
VAT_0_IMAGE = "VAT_0_IMAGE.png"
VAT_9_IMAGE = "VAT_9_IMAGE.png"
EXTRA_COST_BOX_IMAGE = "EXTRA_COST_BOX_IMAGE.png"
INVOICE_STATUS_DD_IMAGE = "INVOICE_STATUS_DD_IMAGE.png"
INVOICE_STATUS_Re_IMAGE = "INVOICE_STATUS_Re_IMAGE.png"
INVOICE_STATUS_NA_IMAGE = "INVOICE_STATUS_NA_IMAGE.png"
INVOICE_STATUS_Se_IMAGE = "INVOICE_STATUS_Se_IMAGE.png"
INVOICE_NUMBER_BOX_IMAGE = "INVOICE_NUMBER_BOX_IMAGE.png"
SALES_INVOICE_NUMBER_BOX_IMG = Pattern("SALES_INVOICE_NUMBER_BOX_IMG.png").targetOffset(14,-1)
PAYMENT_STATUS_DD_IMAGE = "PAYMENT_STATUS_DD_IMAGE.png"
PAYMENT_STATUS_T_IMAGE = "PAYMENT_STATUS_T_IMAGE.png"
PAYMENT_STATUS_P_IMAGE = "PAYMENT_STATUS_P_IMAGE.png"
DOC_INFO_BOX_IMAGE = "DOC_INFO_BOX_IMAGE.png"
COMMENTS_BOX_IMAGE = "COMMENTS_BOX_IMAGE.png"
################################
ADD_PROFILE_LIST_IMG = "ADD_PROFILE_LIST_IMG.png"
PROFILE_NAME_IMG = "PROFILE_NAME_IMG.png"
################################
LIC_11_IMG = "LIC_11_IMG.png"
LIC_22_IMG = "LIC_22_IMG.png"
LIC_33_IMG = "LIC_33_IMG.png" 
LIC_44_IMG = "LIC_44_IMG.png"
LIC_55_IMG = "LIC_55_IMG.png"
################################
SH_TYPE_IN_IMG = "SH_TYPE_IN_IMG.png"
SH_TYPE_OUT_IMG = "SH_TYPE_OUT_IMG.png"
################################
S_1_IMG = "S_1_IMG.png"
M_T_S_1_IMG = "M_T_S_1_IMG.png"
R_M_1_S_1_IMG = "R_M_1_S_1_IMG.png"
U_S_1_IMG = "U_S_1_IMG.png"
################################
S_2_IMG = "S_2_IMG.png"
M_T_S_2_IMG = "M_T_S_2_IMG.png"
R_M_1_S_2_IMG = "R_M_1_S_2_IMG.png"
#R_M_2_S_2_IMG = 
U_S_2_IMG = "U_S_2_IMG.png"
################################
S_3_IMG = "S_3_IMG.png"
M_T_S_3_IMG = "M_T_S_3_IMG.png"
R_M_1_S_3_IMG = "R_M_1_S_3_IMG.png"
#R_M_5_S_3 = 
#R_M_2_S_3_IMG = 
#R_M_3_S_3_IMG =  
#R_M_4_S_3_IMG = 
U_S_3_IMG = "U_S_3_IMG.png"
################################
S_4_IMG = "S_4_IMG.png"
M_T_S_4_IMG = "M_T_S_4_IMG.png"
#R_M_3_S_4_IMG = 
#R_M_2_S_4_IMG = 
R_M_1_S_4_IMG = "R_M_1_S_4_IMG.png"
U_S_4_IMG = "U_S_4_IMG.png"
################################
S_5_IMG = "S_5_IMG.png"
M_T_S_5_IMG = "M_T_S_3_IMG.png"
R_M_1_S_5_IMG = "R_M_1_S_3_IMG.png"
R_M_2_S_5_IMG = "R_M_2_S_1_IMG.png"
R_M_5_S_5_IMG = "M_T_S_3_IMG.png"
U_S_5_IMG = "U_S_5_IMG.png"
################################
C_1_IMG = "C_1_IMG.png" 
C_2_IMG = "C_2_IMG.png"
C_3_IMG = "C_3_IMG.png"
C_4_IMG = "C_4_IMG.png"
################################
Anbar_Akhal_IMG = "Anbar_Akhal_IMG.png"
Anbar_Khamir_G_IMG = "Anbar_Khamir_G_IMG.png"
Anbar_Khamir_K_IMG = "Anbar_Khamir_K_IMG.png"
Anbar_Koochak_IMG = "Anbar_Koochak_IMG.png"
Anbar_Muhvateh_K_IMG = "Anbar_Muhvateh_K_IMG.png"
Anbar_Salon_Tolid_IMG = Pattern("Anbar_Salon_Tolid_IMG.png").targetOffset(-19,-4)
Anbar_Sangin_IMG = "Anbar_Sangin_IMG.png"
################################


#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################






#################################################################################
# Setup logging with a file handler
FORMAT = '%(asctime)-15s %(message)s'
logger = logging.getLogger('FullCycleLogger')
logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG
file_handler = logging.FileHandler('IncomingFullCycle.log')
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)
#################################################################################
# Interact with input boxes
def fillInputBox2C(image, text, counter):
    doubleClick (image)
    type(text)
    log("Entered input box with image %s and text %s for %s" % (image, text, counter), "info")
#################################################################################
# Interact with menu
def selectMenuAndClick(menu, choice_image):
    if exists(menu):
        click(choice_image)
        log("Menu %s selected and selected with %s" % (menu, choice_image), "info")
    
    else:
        log("Failed to verify Menu and selection for %s" % menu, "error")
#################################################################################
# Function to interact with input boxes
def fillInputBox(image, text, counter):
    click(image)
    type(text)
    click(SIDE_IMAGE)
    log("Entered input box with image %s and text for %s" % (image, counter), "info")
#################################################################################
def selectDropdownAndVerify(image, verification_image):
    click(image)
    wait(1)
    if exists(verification_image):
        click(verification_image)
        click(SIDE_IMAGE)
        log("Dropdown %s selected and verified with %s" % (image, verification_image), "info")
    
    else:
        log(" ERROR: Failed to verify selection for %s" % image, "error")
#################################################################################
# Helper function to log messages
def log(message, level="info"):
    if level.lower() == "info":
        logger.info(message)
    elif level.lower() == "warning":
        logger.warning(message)
    elif level.lower() == "error":
        logger.error(message)
    #print(message)  # Also print to console for real-time feedback
#################################################################################
def validateAndLog(action_desc):
    if exists(GREEN_MESSAGE_IMAGE):
        log(' SUCCESS: %s ' % action_desc)
    elif exists(RED_MESSAGE_IMAGE):
        log('Error encountered during %s' % action_desc, "error")
    else:
        log('Status unknown after %s' % action_desc, "warning")
#################################################################################
#################################################################################
#################################################################################
#                           Main script
#################################################################################
#################################################################################
#################################################################################

try:
    
    while counter <= cycle:
        
        ################################################################################# 
        # Navigate to the New REEL page
        click(URL_IMAGE)
        type("http://127.0.0.1:8000/myapp/addNewReel/")
        type(Key.ENTER)
        #refreshBrowser()
        #################################################################################
        
        new_reel = 0
        while new_reel < reel_production_quantity:
            #do this:
            # Adding NEW REEL
            fillInputBox2C(REEL_WIDTH_IMG, "2"  + str(counter) + "0", counter)
            fillInputBox(COMMENTS_BOX_IMAGE, str(NEW_REEL_comments), counter)                
            fillInputBox(USERNAME_IMAGE, "nk a OUT s"  + str(counter), counter)
            
            click(ADD_BUTTON_IMAGE)
            click(CONFIRM_BUTTON_IMAGE)
            wait(1)
            click(REEL_qrCODE_IMG)
            validateAndLog("adding NEW REEL")
            #then
            new_reel += 1

        wait(1)
        
        ################################################################################# 
        # Navigate to the shipment page
        click(URL_IMAGE)
        type("http://127.0.0.1:8000/myapp/addShipment/")
        type(Key.ENTER)
        #refreshBrowser()
        #################################################################################
        
        # Adding shipments
        selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")
        selectDropdownAndVerify(INCOMING_DD_IMAGE, SH_TYPE_OUT_IMG)
        selectDropdownAndVerify(CUSTOMER_DD_IMAGE, "C_" + str(counter) + "_IMG")
        
        fillInputBox(USERNAME_IMAGE, "nk a OUT s"  + str(counter), counter)
        
        click(ADD_BUTTON_IMAGE)
        click(CONFIRM_BUTTON_IMAGE)
        validateAndLog("adding OUTGOING shipment")
        wait(1)
    
        #################################################################################
        # Navigate to the Weight Station Panel page
        click(URL_IMAGE)
        type("http://127.0.0.1:8000/myapp/weightStationPanel/")
        type(Key.ENTER)
        #refreshBrowser()
        #################################################################################
        
        # Weight Station Panel
        selectMenuAndClick(WEIGHT_STATION_PANEL_IMAGE, WEIGHT1_BUTTON_IMAGE)
        
        selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")    
        fillInputBox(WEIGHT1_BOX_IMAGE, str(OUT_w1), counter)
        fillInputBox(USERNAME_IMAGE, "nk OUT w"  + str(counter), counter)
        
        click(ADD_BUTTON_IMAGE)
        click(CONFIRM_BUTTON_IMAGE)
        validateAndLog("adding OUT Weight1")
        wait(1)
        
        #################################################################################
        # Forklift Panel
        # Navigate to the Forklift Panel page
        click(URL_IMAGE)
        type("http://127.0.0.1:8000/myapp/forkliftPanel/")
        type(Key.ENTER)
        #refreshBrowser()
        #################################################################################
        
        # Loaded
        selectMenuAndClick(FORKLIFT_PANEL_IMAGE,LOADED_IMAGE)
        selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")
        click(LOADED_DD_IMAGE)
        click("1711864884899.png")
        click("1711864884899.png")
        click("1711864884899.png")
        click(Anbar_Salon_Tolid_IMG)
        click(SIDE_IMAGE)
        selectDropdownAndVerify(WIDTH_DD_IMAGE, "W_2" + str(counter) + "0_IMG")
        click(REEL_CHKBOX_BLANK_IMG)
        click(REEL_CHKBOX_BLANK_IMG)
        fillInputBox(FORK_USERNAME_IMAGE, "loFK" + str(counter), counter)
        
        click(ADD_BUTTON_IMAGE)
        click(CONFIRM_BUTTON_IMAGE)
        validateAndLog("Loaded")
        wait(1)
    
        #################################################################################
        # Navigate to the Weight Station Panel page
        click(URL_IMAGE)
        type("http://127.0.0.1:8000/myapp/weightStationPanel/")
        type(Key.ENTER)
        #refreshBrowser()
        #################################################################################
    
        # Weight Station Panel
        selectMenuAndClick(WEIGHT_STATION_PANEL_IMAGE, WEIGHT2_BUTTON_IMAGE)
        
        selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")    
        fillInputBox(WEIGHT2_BOX_IMAGE, str(OUT_w2), counter)
        fillInputBox(NET_BOX_IMAGE, str(OUT_net), counter)
        fillInputBox(USERNAME_IMAGE, "nk OUT w" + str(counter), counter)
        
        click(ADD_BUTTON_IMAGE)
        click(CONFIRM_BUTTON_IMAGE)
        validateAndLog("adding OUT Weight2")
        wait(1)
    
        
        #################################################################################
        # Navigate to the SO page
        click(URL_IMAGE)
        type("http://127.0.0.1:8000/myapp/createSalesOrder/")
        type(Key.ENTER)
        #################################################################################
    
        # Create Sales Order
           
        selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")
        fillInputBox(PRICE_PER_KG_BOX_IMAGE, str(OUT_ppk), counter)
        click(SIDE_IMAGE)
        type(Key.PAGE_DOWN)
        wait(1)        
        
        selectDropdownAndVerify(VAT_DD_IMAGE, VAT_0_IMAGE)
        fillInputBox(EXTRA_COST_BOX_IMAGE, str(extracost), counter)
        
        selectDropdownAndVerify(INVOICE_STATUS_DD_IMAGE, INVOICE_STATUS_NA_IMAGE)
        fillInputBox(SALES_INVOICE_NUMBER_BOX_IMG, str(sales_invoice_number), counter)
        selectDropdownAndVerify(PAYMENT_STATUS_DD_IMAGE, PAYMENT_STATUS_P_IMAGE)
        fillInputBox(DOC_INFO_BOX_IMAGE, str(doc_info), counter)
        fillInputBox(COMMENTS_BOX_IMAGE, str(SO_comments), counter)
        fillInputBox(USERNAME_IMAGE, "nk" + str(counter) + " c SO" , counter)
        
        click(ADD_BUTTON_IMAGE)
        click(CONFIRM_BUTTON_IMAGE)
        type(Key.PAGE_UP)
        type(Key.PAGE_UP)
        validateAndLog("Created SO")

        
        
        counter += 1
        wait(1)  # Wait for 2 seconds before the next iteration

finally:
    # Ensure the file handler is closed properly
    file_handler.close()
    logger.removeHandler(file_handler)
