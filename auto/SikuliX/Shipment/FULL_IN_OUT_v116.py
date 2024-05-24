import logging
from sikuli import *  # Importing Sikuli functions

testMODE = int(input("Enter 1 for TESTING MODE or 0 for FULL"))
if testMODE == 1:
    # Values for the test
    log_name = "TESTING..."
    start_counter = 1
    cycle = 1
    quan = 1
    reel_production_quantity = 1
    load_reel = 1
    max_entry = 4
    address = str(input("Enter server IP address: 192.168.0.108 "))
    preview_DB = 0
    preview = 0

else:
    # Values for the test
    log_name = str(input("Log Name"))
    start_counter = int(input("Enter the starting counter value: "))
    cycle = int(input("How many times to run the cycles?"))
    quan = int(input("What quantity for each shipment?"))
    reel_production_quantity = int(input("Enter the number of Reels to make per each counter: "))
    load_reel = int(input("Enter the number of Reels to LOAD:"))
    max_entry = int(input("Enter the max entry (from counter 1 to counter X): "))
    address = str(input("Enter server IP address: 192.168.0.108 "))
    preview_DB = int(input("Preview DataBase? Enter 0 for NO and 1 for YES"))
    preview = int(input("Preview Wait Time(s)?"))

#start_counter = 1  # Starting point (e.g., Customer or Supplier 3)
#cycle = 4  # How many cycles to run
#reel_production_quantity = 3 # number of Reels to make per each counter
#max_entry = 4 # from counter 1 to counter X

#================================================================================
################################### SETTINGS ####################################
#================================================================================

################################### SETTINGS ####################################
w1 = 36000
w2 = 16000
net = 20000
OUT_w1 = 16000
OUT_w2 = 38000
OUT_net = 22000
################################### SETTINGS ####################################
#quan = 24
QUAN = 1
quality_report = 1
################################### SETTINGS ####################################
penalty = 0
ppk = 8000
OUT_ppk = 15000
extracost = 0
supplier_invoice_number = "123X"
sales_invoice_number = "321X"
doc_info = "DOC Info"
PO_comments = "PO Comments"
SO_comments = "SO COMMENTS"
NEW_REEL_comments = "New Reel Comments" 
################################### SETTINGS ####################################
materials = ["Akhal F", 
            "Core F", 
            "Starch F", 
            "AKD F", 
            "Starch F", 
            "Akhal F"]

units = ["Bale Akhal F", "Core F",  "Starch 25KG F", "AKD 20L F", "Starch 25KG F", "Bale Akhal F"]
################################### SETTINGS ####################################
comment = "New Raw Material Comment"

################################### SETTINGS ####################################
# Setup logging with a file handler
FORMAT = '%(asctime)-15s %(message)s'
logger = logging.getLogger('FullCycleLogger')
logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG
file_handler = logging.FileHandler("ISM_LOG_"+ str(log_name) +".log")
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)
#================================================================================
################################### END SETTINGS ################################
#================================================================================

# Define constants for the images
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
URL_IMAGE = Pattern("1716285126921.png").targetOffset(198,2)
SIDE1_IMAGE = "SIDE1_IMAGE.png"
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
LICENSE_DD_IMAGE = Pattern("LICENSE_DD_IMAGE.png").targetOffset(-25,3)
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
EDIT_BUTTON_IMAGE = "EDIT_BUTTON_IMAGE.png"
RED_MESSAGE_IMAGE = Pattern("RED_MESSAGE_IMAGE.png").similar(0.88)
GREEN_MESSAGE_IMAGE = Pattern("GREEN_MESSAGE_IMAGE.png").similar(0.66).targetOffset(-12,-22)
################################
REEL_NUMBER_IMG = "REEL_NUMBER_IMG.png"
REEL_WIDTH_IMG = Pattern("REEL_WIDTH_IMG.png").targetOffset(2,33)
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
PRICE_PER_KG_BOX_IMAGE = Pattern("PRICE_PER_KG_BOX_IMAGE.png").targetOffset(-83,0)
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
LIC_11_IMG = Pattern("LIC_11_IMG.png").similar(0.81)
LIC_22_IMG = Pattern("LIC_22_IMG.png").similar(0.74)
LIC_33_IMG = Pattern("LIC_33_IMG.png").similar(0.80) 
LIC_44_IMG = Pattern("LIC_44_IMG.png").similar(0.77)
LIC_55_IMG = Pattern("LIC_55_IMG.png").similar(0.71)
################################
SH_TYPE_IN_IMG = Pattern("SH_TYPE_IN_IMG.png").similar(0.62)
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
C_1_IMG = Pattern("C_1_IMG.png").exact()
C_2_IMG = Pattern("C_2_IMG.png").similar(0.97)
C_3_IMG = Pattern("C_3_IMG.png").similar(0.97)
C_4_IMG = Pattern("C_4_IMG.png").similar(0.97)
################################
Anbar_Akhal_IMG = Pattern("Anbar_Akhal_IMG.png").similar(0.63)
Anbar_Khamir_G_IMG = "Anbar_Khamir_G_IMG.png"
Anbar_Khamir_K_IMG = "Anbar_Khamir_K_IMG.png"
Anbar_Koochak_IMG = "Anbar_Koochak_IMG.png"
Anbar_Muhvateh_K_IMG = "Anbar_Muhvateh_K_IMG.png"
Anbar_Salon_Tolid_IMG = Pattern("Anbar_Salon_Tolid_IMG.png").similar(0.69).targetOffset(-43,0)
Anbar_Sangin_IMG = "Anbar_Sangin_IMG.png"
################################
Truck_DB_IMG = "Truck_DB_IMG.png"
Customer_DB_IMG = "Customer_DB_IMG.png"
Supplier_DB_IMG = "Supplier_DB_IMG.png"
MaterialType_DB_IMG = "MaterialType_DB_IMG.png"
Unit_DB_IMG = "Unit_DB_IMG.png"
RawMaterial_DB_IMG = "RawMaterial_DB_IMG.png"
Shipments_DB_IMG = Pattern("Shipments_DB_IMG.png").similar(0.62)
Anbar_Akhal_DB_IMG = "Anbar_Akhal_DB_IMG.png"
Purchases_DB_IMG = "Purchases_DB_IMG.png"
Cons_Profile_DB_IMG = "Cons_Profile_DB_IMG.png"
Products_DB_IMG = "Products_DB_IMG.png"
Anbar_Salon_Tolid_DB_IMG = Pattern("Anbar_Salon_Tolid_DB_IMG.png").similar(0.64)
Sales_DB_IMG = "Sales_DB_IMG.png"
ConsumptionDB_DB_IMG = Pattern("ConsumptionDB_DB_IMG.png").similar(0.59)
refresh_DB_IMG = Pattern("refresh_DB_IMG.png").targetOffset(-37,2)


#################################################################################

    #################################################################################
    # Interact with input boxes
def fillInputBox2C(image, text, counter):
    if exists(image):
        doubleClick (image)
        type(text)
        log("INFO:    Entered input Box(double click) with image %s and text %s for %s" % (image, text, counter), "info")
    else:
        log("ERROR:   Failed to verify Box and Double Clike for %s" % image, "error")
    #################################################################################
    # Interact with menu
def selectMenuAndClick(menu, choice_image):
    if exists(menu):
        #wait(1)
        click(choice_image)
        #wait(1)
        log("INFO:    Menu %s selected then selected with %s" % (menu, choice_image), "info")
    
    else:
        log("ERROR:   Failed to verify Menu and selection for %s" % menu, "error")
    #################################################################################
def fillInputBox(image, text, counter):
    if exists(image):
        #wait(1)
        click(image)
        #wait(1)
        type(text)
        click(SIDE_IMAGE)
        log("INFO:    Entered input box with image %s and text for %s" % (image, counter), "info")
    else:
        log("ERROR:   Failed to verify image and selection for %s" % image, "error")
    #################################################################################
def selectDropdownAndVerify(image, verification_image):
    if exists (image):
        #wait(1)
        click(image)
        #wait(1)
        if exists(verification_image):
            #wait(1)
            click(verification_image)
            #wait(1)
            click(SIDE_IMAGE)
            log("INFO:    Dropdown %s selected and clicked on selected image %s" % (image, verification_image), "info")
        
        else:
            log("ERROR:   Failed to verify 2nd image for %s" % verification_image, "error")
    else:
        log("ERROR:   Failed to verify 1st image for %s" % image, "error")        
    #################################################################################
def selectDropdownAndVerify_SLOWMOTIOM(image, verification_image):
    if exists (image):
        #wait(1)
        click(image)
        #wait(1)
        click(image)
        #wait(1)
        if exists(verification_image):
            #wait(1)
            click(verification_image)
            #wait(1)
            click(SIDE_IMAGE)
            log("INFO:    BOX %s selected and clicked on selected image %s" % (image, verification_image), "info")
        
        else:
            log("ERROR:   Failed to verify 2nd image for %s" % verification_image, "error")
    else:
        log("ERROR:   Failed to verify 1st image for %s" % image, "error")
    #################################################################################
def selectDBandRefresh_PASS(image, refresh_image):
    pass

def selectDBandRefresh(image, refresh_image):
    if preview_DB == 0:
        pass
    else:
        if exists (image):
            #wait(1)
            click(image)
            if exists(refresh_image):
                click(refresh_image)
                #wait(1)
                click(SIDE_IMAGE)
                log("INFO:    Database %s selected and Refresed" % (image), "info")
                #wait(preview)
            
            else:
                log("ERROR:   Failed to find refresh button for %s" % image, "error")
        else:
            log("ERROR:   Failed to image for DB %s" % image, "error")
    
    #################################################################################
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
        log('SUCCESS: %s ' % action_desc)
    elif exists(RED_MESSAGE_IMAGE):
        log('ERROR:   Error encountered during %s' % action_desc, "error")
    else:
        log('Status unknown after %s' % action_desc, "warning")
    #################################################################################
def addShipment_IN(counter):
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/addShipment/")
    type(Key.ENTER)
    wait(1)
    # Adding IN shipments
    selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")
    selectDropdownAndVerify(INCOMING_DD_IMAGE, SH_TYPE_IN_IMG)
    selectDropdownAndVerify(SUPPLIER_DD_IMAGE, "S_" + str(counter) + "_IMG")
    selectDropdownAndVerify(MATERIAL_TYPE_DD_IMAGE, "M_T_S_" + str(counter) + "_IMG")
    selectDropdownAndVerify(MATERIAL_NAME_DD_IMAGE, "R_M_1_S_" + str(counter) + "_IMG")
    #selectDropdownAndVerify_SLOWMOTIOM(USERNAME_IMAGE, verification_image) 
    fillInputBox(USERNAME_IMAGE, "nk IN  a s", counter)
    
def addWeight1_IN(counter):
    #################################################################################
    # Navigate to the IN Weight Station Panel page
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/weightStationPanel/")
    type(Key.ENTER)
    wait(1)
    #refreshBrowser()
    #################################################################################
    
    # IN Weight Station Panel
    selectMenuAndClick(WEIGHT_STATION_PANEL_IMAGE, WEIGHT1_BUTTON_IMAGE)    
    selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")    
    fillInputBox(WEIGHT1_BOX_IMAGE, str(w1), counter)
    fillInputBox(USERNAME_IMAGE, "nk IN w1 by Cy"  + str(counter), counter)
    wait(1)
def addUnloaded_IN(counter):
    #################################################################################
    # IN Forklift Panel
    # Navigate to the Forklift Panel page
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/forkliftPanel/")
    type(Key.ENTER)
    wait(1)
    #refreshBrowser()
    #################################################################################
    
    # IN Unloaded
    selectMenuAndClick(FORKLIFT_PANEL_IMAGE,UNLOADED_IMAGE)    
    selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")
    selectDropdownAndVerify(UNLOADING_LOCATION_DD_IMAGE, Anbar_Akhal_IMG)
    selectDropdownAndVerify(UNIT_DD_IMAGE, "U_S_" + str(counter) + "_IMG")
    fillInputBox(QUANTITY_BOX_IMAGE, str(quan), counter)
    fillInputBox(QUALITY_BOX_IMAGE, str(quality_report), counter)
    fillInputBox(FORK_USERNAME_IMAGE, "unFK IN" , counter)
    wait(1)
def addWeight2_IN(counter):
    #################################################################################
    # Navigate to the IN Weight Station Panel page
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/weightStationPanel/")
    type(Key.ENTER)
    wait(1)
    #refreshBrowser()
    #################################################################################

    # IN  Weight Station Panel
    selectMenuAndClick(WEIGHT_STATION_PANEL_IMAGE, WEIGHT2_BUTTON_IMAGE)
    selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")    
    fillInputBox(WEIGHT2_BOX_IMAGE, str(w2), counter)
    fillInputBox(NET_BOX_IMAGE, str(net), counter)
    fillInputBox(USERNAME_IMAGE, "nk IN w2" , counter)
    wait(1)
def addPO_IN(counter):
    #################################################################################
    # Navigate to the PO page
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/createPurchaseOrder/")
    type(Key.ENTER)
    wait(1)
    #wheel(WHEEL_UP, 3)
    #refreshBrowser()
    #################################################################################

    # IN Create Purchase Order
       
    selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")
    fillInputBox(PENALTY_BOX_IMAGE, str(penalty), counter)
    fillInputBox(PRICE_PER_KG_BOX_IMAGE, str(ppk), counter)
    #wait(2)
    type(Key.PAGE_DOWN)
    wait(1)
    selectDropdownAndVerify(VAT_DD_IMAGE, VAT_0_IMAGE)
    fillInputBox(EXTRA_COST_BOX_IMAGE, str(extracost), counter)
    selectDropdownAndVerify(INVOICE_STATUS_DD_IMAGE, INVOICE_STATUS_Re_IMAGE)
    fillInputBox(INVOICE_NUMBER_BOX_IMAGE, str(supplier_invoice_number), counter)
    selectDropdownAndVerify(PAYMENT_STATUS_DD_IMAGE, PAYMENT_STATUS_P_IMAGE)
    fillInputBox(DOC_INFO_BOX_IMAGE, str(doc_info), counter)
    fillInputBox(COMMENTS_BOX_IMAGE, str(PO_comments), counter)
    fillInputBox(USERNAME_IMAGE, "nk c PO" , counter)
    wait(1)
def addNewReel(counter):
    #################################################################################
    # OUT Navigate to the New REEL page
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/addNewReel/")
    type(Key.ENTER)
    wait(1)
    #refreshBrowser()
    #################################################################################
    
    # Adding NEW REEL
    
    fillInputBox2C(REEL_WIDTH_IMG, "2"  + str(counter) + "0", counter)
    fillInputBox(COMMENTS_BOX_IMAGE, str(NEW_REEL_comments), counter)                
    fillInputBox(USERNAME_IMAGE, "nk a OUT", counter)
    wait(1)
def addShipment_OUT(counter):
    ################################################################################# 
    # OUT Navigate to the shipment page
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/addShipment/")
    type(Key.ENTER)
    wait(1)
    #refreshBrowser()
    #################################################################################
    
    # OUT Adding shipments
    selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")
    selectDropdownAndVerify(INCOMING_DD_IMAGE, SH_TYPE_OUT_IMG)
    selectDropdownAndVerify(CUSTOMER_DD_IMAGE, "C_" + str(counter) + "_IMG")
    fillInputBox(USERNAME_IMAGE, "nk a OUT", counter)
    wait(1)
def addWeight1_OUT(counter):
    #################################################################################
    # OUT Navigate to the Weight Station Panel page
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/weightStationPanel/")
    type(Key.ENTER)
    wait(1)
    #refreshBrowser()
    #################################################################################
    
    # OUT Weight Station Panel
    selectMenuAndClick(WEIGHT_STATION_PANEL_IMAGE, WEIGHT1_BUTTON_IMAGE)
    
    selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")    
    fillInputBox(WEIGHT1_BOX_IMAGE, str(OUT_w1), counter)
    fillInputBox(USERNAME_IMAGE, "nk OUT w1" , counter)
    wait(1)
def addLoaded_OUT(counter):
    #################################################################################
    # OUT Forklift Panel
    # Navigate to the Forklift Panel page
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/forkliftPanel/")
    type(Key.ENTER)
    wait(1)
    #refreshBrowser()
    #################################################################################
    
    # OUT Loaded
    selectMenuAndClick(FORKLIFT_PANEL_IMAGE,LOADED_IMAGE)
    selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")
    click(LOADED_DD_IMAGE)
    click("1711864884899.png")
    click("1711864884899.png")
    click("1711864884899.png")
    wait(1)
    click(Anbar_Salon_Tolid_IMG)
    click(SIDE_IMAGE)
    selectDropdownAndVerify(WIDTH_DD_IMAGE, "W_2" + str(counter) + "0_IMG")
    for _ in range(load_reel):
        click(REEL_CHKBOX_BLANK_IMG)
    fillInputBox(FORK_USERNAME_IMAGE, "loFK", counter)

def addWeight2_OUT(counter):
    #################################################################################
    # OUT Navigate to the Weight Station Panel page
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/weightStationPanel/")
    type(Key.ENTER)
    wait(1)
    #################################################################################

    # OUT Weight Station Panel
    selectMenuAndClick(WEIGHT_STATION_PANEL_IMAGE, WEIGHT2_BUTTON_IMAGE)
    
    selectDropdownAndVerify(LICENSE_DD_IMAGE, "LIC_" +str(counter)+str(counter)+ "_IMG")    
    fillInputBox(WEIGHT2_BOX_IMAGE, str(OUT_w2), counter)
    fillInputBox(NET_BOX_IMAGE, str(OUT_net), counter)
    fillInputBox(USERNAME_IMAGE, "nk OUT w2", counter)
    wait(1)
def addSO_OUT(counter):
    #################################################################################
    # OUT Navigate to the SO page
    click(URL_IMAGE)
    type("http://" + str(address) + ":8000/myapp/createSalesOrder/")
    type(Key.ENTER)
    wait(1)
    #################################################################################

    # OUT Create Sales Order
       
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
    fillInputBox(USERNAME_IMAGE, "nk c SO", counter)
#################################################################################
#################################################################################
#################################################################################
#                                     IN
#################################################################################
#################################################################################
def incomingShipment (counter):
    click(SIDE_IMAGE)     
    addShipment_IN(counter)
    add_And_confirm(counter)    
    validateAndLog("adding IN shipment")
    selectDBandRefresh(Shipments_DB_IMG, refresh_DB_IMG)

            
    addWeight1_IN(counter)
    add_And_confirm(counter)    
    validateAndLog("adding IN Weight1")
    selectDBandRefresh(Shipments_DB_IMG, refresh_DB_IMG)

    
    addUnloaded_IN(counter)
    add_And_confirm(counter)    
    validateAndLog("Unloaded")
    selectDBandRefresh(Shipments_DB_IMG, refresh_DB_IMG)
    selectDBandRefresh(Anbar_Akhal_DB_IMG, refresh_DB_IMG)

    
    addWeight2_IN(counter)
    add_And_confirm(counter)    
    validateAndLog("adding IN Weight2")
    selectDBandRefresh(Shipments_DB_IMG, refresh_DB_IMG)

    
    addPO_IN(counter)
    add_And_confirm(counter)
    click(SIDE_IMAGE)
    type(Key.PAGE_UP)
    type(Key.PAGE_UP)
    validateAndLog("Created IN PO")
    selectDBandRefresh(Shipments_DB_IMG, refresh_DB_IMG)
    selectDBandRefresh(Truck_DB_IMG, refresh_DB_IMG)
    selectDBandRefresh(Purchases_DB_IMG, refresh_DB_IMG)
#################################################################################
#################################################################################
#################################################################################
#                                     OUT
#################################################################################
#################################################################################
def outgoingShipment (counter):
    for new_reel in range(reel_production_quantity):
            addNewReel(counter)
            add_And_confirm(counter)
            wait(1)
            #click(REEL_qrCODE_IMG)
            validateAndLog("$$$: adding OUT NEW REEL")
            selectDBandRefresh(Anbar_Salon_Tolid_DB_IMG, refresh_DB_IMG)
            selectDBandRefresh(Products_DB_IMG, refresh_DB_IMG)
            selectDBandRefresh(Anbar_Akhal_DB_IMG, refresh_DB_IMG)
            selectDBandRefresh(ConsumptionDB_DB_IMG, refresh_DB_IMG)
    addShipment_OUT(counter)
    add_And_confirm(counter)
    validateAndLog("adding OUT shipment")
    selectDBandRefresh(Shipments_DB_IMG, refresh_DB_IMG)
    
    addWeight1_OUT(counter)
    add_And_confirm(counter)
    validateAndLog("adding OUT Weight1")
    selectDBandRefresh(Shipments_DB_IMG, refresh_DB_IMG)
        
    addLoaded_OUT(counter)
    add_And_confirm(counter)    
    validateAndLog("Loaded")
    selectDBandRefresh(Shipments_DB_IMG, refresh_DB_IMG)
    selectDBandRefresh(Products_DB_IMG, refresh_DB_IMG)
    selectDBandRefresh(Anbar_Salon_Tolid_DB_IMG, refresh_DB_IMG)
    
    addWeight2_OUT(counter)
    add_And_confirm(counter)
    validateAndLog("adding OUT Weight2")
    selectDBandRefresh(Shipments_DB_IMG, refresh_DB_IMG)
    
    addSO_OUT(counter)
    add_And_confirm(counter)
    click(SIDE_IMAGE)
    type(Key.PAGE_UP)
    type(Key.PAGE_UP)
    validateAndLog("Created OUT SO")
    selectDBandRefresh(Truck_DB_IMG, refresh_DB_IMG)
    selectDBandRefresh(Shipments_DB_IMG, refresh_DB_IMG)
    selectDBandRefresh(Products_DB_IMG, refresh_DB_IMG)
    selectDBandRefresh(Anbar_Salon_Tolid_DB_IMG, refresh_DB_IMG)
    selectDBandRefresh(Sales_DB_IMG, refresh_DB_IMG)
#################################################################################
def add_And_confirm(counter):
    click(ADD_BUTTON_IMAGE)
    click(CONFIRM_BUTTON_IMAGE)
    log("INFO:    Data confirmed and added." , "info")
#################################################################################
def add_And_edit(counter):
    click(ADD_BUTTON_IMAGE)
    click(EDIT_BUTTON_IMAGE)
    log("INFO:    Data edit requested." , "info")
#################################################################################
def timed_pop_ask(message, timeout):
    # Show the popup without waiting indefinitely
    answer = None
    for _ in range(timeout):  # Check the response every second
        answer = popAsk(message)
        if answer is not None:
            break
        wait(1)  # Wait for 1 second before checking again
    return answer



#################################################################################
#################################################################################
#################################################################################
#                           Main script
#################################################################################
#################################################################################
#################################################################################


try:
    log("INFO:    Enter the starting counter value:                   %s" % (start_counter), "info")
    log("INFO:    Enter how many cycles to run:                       %s" % (cycle), "info")
    log("INFO:    Enter the number of Reels to make per each counter: %s" % (reel_production_quantity), "info")
    log("INFO:    Enter the max entry (from counter 1 to counter X):  %s" % (max_entry), "info") 
    
    counter = start_counter
    for _ in range(cycle):
        
        #################################################################################
        #################################################################################
        #                                     IN
        #################################################################################
        #################################################################################
        
        
        incomingShipment (counter)
                
        #################################################################################
        #################################################################################
        #                                     OUT
        #################################################################################
        #################################################################################
        
        
        outgoingShipment (counter)
        
        


        counter += 1
        if counter > max_entry:
            counter = 1
finally:
    # Ensure the file handler is closed properly
    file_handler.close()
    logger.removeHandler(file_handler)
