import logging
from sikuli import *  # Importing Sikuli functions

#================================================================================
################################### SETTINGS ####################################
#================================================================================
# Values for the test
log_name = str(input("Log Name"))
#log_name = "Sat-815"
start_counter = int(input("Enter the starting counter value: "))
#start_counter = 1
cycle = int(input("Enter how many cycles to run: "))
#cycle = 4
#reel_production_quantity = int(input("Enter the number of Reels to make per each counter: "))
max_entry = int(input("Enter the max entry (from counter 1 to counter X): "))
#max_entry = 4
################################### SETTINGS ####################################
w1 = 36000
w2 = 16000
net = 20000
OUT_w1 = 16000
OUT_w2 = 38000
OUT_net = 22000
################################### SETTINGS ####################################
quan = 12
QUAN = 1
quality_report = 1
################################### SETTINGS ####################################
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
################################### SETTINGS ####################################
materials = ["Akhal F", 
            "Core F", 
            "Starch F", 
            "AKD F", 
            "Starch F", 
            "Akhal F"]

units = ["Bale Akhal F", "Core F",  "Starch 25KG F", "AKD 20L F", "Starch 20KG F", "Bale Akhal F"]
################################### SETTINGS ####################################
comment = "New Raw Material"


#================================================================================
################################### END SETTINGS ################################
#================================================================================

# Setup logging with a file handler
FORMAT = '%(asctime)-15s %(message)s'
logger = logging.getLogger('TCSLogger')
logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG
file_handler = logging.FileHandler("ISM_LOG_"+ str(log_name) +".log")
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)




# Define constants for the images
TWO_DIGIT_BOX_IMAGE = "FIRST_2D_IMAGE.png"
THREE_DIGIT_BOX_IMAGE ="FIRST_3D_IMAGE.png"
FIRST_BOX_IMAGE = "FIRST_BOX_IMAGE.png"
SECOND_BOX_IMAGE = "SECOND_BOX_IMAGE.png"
THIRD_BOX_IMAGE = "THIRD_BOX_IMAGE.png"
LAST_BOX_IMAGE = Pattern("LAST_BOX_IMAGE.png").similar(0.63)
CHECK_BUTTON_IMAGE = "1714116007468.png"
ADD_BUTTON_IMAGE = "ADD_BUTTON_IMAGE.png"
CORRECT_BUTTON_IMAGE = "CORRECT_BUTTON_IMAGE.png"
CONFIRM_BUTTON_IMAGE = "CONFIRM_BUTTON_IMAGE.png"
RED_INDICATOR_IMAGE = "SUCCESS_INDICATOR_IMAGE.png"
################################
URL_IMAGE = Pattern("URL_IMAGE.png").targetOffset(194,0)
SIDE_IMAGE = "SIDE_IMAGE.png"
################################
# Define constants for the images
CUS_NAME_BOX_IMAGE = "CUS_NAME_BOX_IMAGE.png"
ADDRESS_BOX_IMAGE = "ADDRESS_BOX_IMAGE.png"
PHONE_BOX_IMAGE = "PHONE_BOX_IMAGE.png"
COMMENT_BOX_IMAGE = Pattern("COMMENT_BOX_IMAGE.png").similar(0.61)
################################
SUP_NAME_BOX_IMAGE = "SUP_NAME_BOX_IMAGE.png"
################################
USERNAME_BOX_IMAGE = "USERNAME_BOX_IMAGE.png"
################################

MATERIAL_TYPE = "MATERIAL_TYPE.png"
MATERIAL_TYPE_DD_IMG = "MATERIAL_TYPE_DD_IMG.png"
UNIT_BOX_IMG = "UNIT_BOX_IMG.png"
QUAN_BOX_IMG = "QUAN_BOX_IMG.png"
MATERIAL_NAME_BOX_IMG = "MATERIAL_NAME_BOX_IMG.png"
################################
################################
LICENSE_DD_IMAGE = Pattern("LICENSE_DD_IMAGE.png").targetOffset(-23,2)
INCOMING_DD_IMAGE = "INCOMING_DD_IMAGE.png"
SUPPLIER_DD_IMAGE = "SUPPLIER_DD_IMAGE.png"
CUSTOMER_DD_IMAGE = "CUSTOMER_DD_IMAGE.png"
MATERIAL_TYPE_DD_IMAGE = "MATERIAL_TYPE_DD_IMAGE.png"
MATERIAL_NAME_DD_IMAGE = "MATERIAL_NAME_DD_IMAGE.png"
################################
USERNAME_IMAGE = "USERNAME_IMAGE.png"
FORK_USERNAME_IMAGE = "FORK_USERNAME_IMAGE.png"
################################
EDIT_BUTTON_IMAGE = "EDIT_BUTTON_IMAGE.png"
RED_MESSAGE_IMAGE = Pattern("RED_MESSAGE_IMAGE.png").similar(0.90)
GREEN_MESSAGE_IMAGE = Pattern("GREEN_MESSAGE_IMAGE.png").similar(0.91)
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
S_4_IMG = Pattern("S_4_IMG.png").similar(0.97)
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
LANG_ENG_IMG = "LANG_ENG_IMG.png"
#################################################################################
#################################################################################
#################################################################################
#################################################################################


# Function to interact with input boxes
def fillInputBox(image, text, counter):
    wait(1)
    click(image)
    wait(1)
    type(text)
    wait(1)
    click(SIDE_IMAGE)
   
    log("INFO:    BOX %s selected: %s" % (image, text), "info")

def selectDropdownAndVerify(image, verification_image):
    wait(1)
    click(image)
    wait(1)
    if exists(verification_image):
        wait(1)
        click(verification_image)
        wait(1)
        click(SIDE_IMAGE)
        wait(1)
        log("INFO:    Dropdown %s selected and verified with %s" % (image, verification_image), "info")
    
    else:
        log("ERROR:   Failed to verify selection for %s" % image, "error")
        
def fillInputBox2C(image, text, counter):
    wait(1)
    if exists(image):
        wait(1)
        doubleClick (image)
        wait(1)
        type(text)
        wait(1)
        log("INFO:    Entered input Box(double click) with image %s and text %s for %s" % (image, text, counter), "info")
    else:
        log("ERROR:   Failed to verify Box and Double Clike for %s" % image, "error")

def switchKeyboardLayout():
    wait(1)
    type(Key.SHIFT, KeyModifier.ALT)  # Simulates pressing Alt + Shift
    log("INFO:    KEYBOARD SWITCH...", "info")
    wait(1)  # Wait a bit for the layout to switch

def resetKeyboardENG():
    if exists():
        switchKeyboardLayout()
        wait(1)
    else:
        log("ERROR:   Failed to find ENG layout icon" , "error")
#################################################################################
def add_And_confirm(counter):
    wait(1)
    click(ADD_BUTTON_IMAGE)
    wait(1)
    click(CONFIRM_BUTTON_IMAGE)
    wait(1)
    log("INFO:    Data confirmed and added." , "info")
#################################################################################
def add_And_edit(counter):
    wait(1)            
    click(ADD_BUTTON_IMAGE)
    wait(1)
    click(EDIT_BUTTON_IMAGE)
    wait(1)
    log("INFO:    Data edit requested." , "info")
#################################################################################
def addTruck_EN(counter):
        
    ################################################################################# 
    # Navigate to the shipment page
    click(URL_IMAGE)
    type("http://192.168.0.108:8000/myapp/addTruck/")
    type(Key.ENTER)
    wait(1)
    #################################################################################
    
    fillInputBox2C(TWO_DIGIT_BOX_IMAGE, str(counter) + str(counter), counter)
    fillInputBox2C(THREE_DIGIT_BOX_IMAGE, str(counter) * 3, counter)
    click(CHECK_BUTTON_IMAGE)

    if exists(RED_INDICATOR_IMAGE):
        # Increment if the truck exists and retry
        log("ERROR:   Truck already exists for counter: %s" % counter, "error")
    else:
        fillInputBox(FIRST_BOX_IMAGE, "Truck " + str(counter), counter)
        fillInputBox(SECOND_BOX_IMAGE, "Lic Nm. " + str(counter), counter)
        fillInputBox(THIRD_BOX_IMAGE, "0912111111" + str(counter) , counter)
        fillInputBox(LAST_BOX_IMAGE, "nk a t " , counter)
        add_And_confirm(counter)
        


def addCustomer_EN(counter): 
    ################################################################################# 
    # Navigate to the Add Customer page
    click(URL_IMAGE)
    type("http://192.168.0.108:8000/myapp/addCustomer/")
    type(Key.ENTER)
    wait(1)
    #################################################################################

    fillInputBox(CUS_NAME_BOX_IMAGE, "Customer " + str(counter), counter)
    fillInputBox(ADDRESS_BOX_IMAGE, "Address " + str(counter), counter)
    fillInputBox(PHONE_BOX_IMAGE,  "0912111111" + str(counter) , counter)
    fillInputBox(COMMENT_BOX_IMAGE, "Tozihat for Customer " + str(counter), counter)
    fillInputBox(USERNAME_BOX_IMAGE, "nk a c " , counter)
   
def addSupplier_EN(counter):
    ################################################################################# 
    # Navigate to the Add Supplier page
    click(URL_IMAGE)
    type("http://192.168.0.108:8000/myapp/addSupplier/")
    type(Key.ENTER)
    wait(1)
    #################################################################################
    
    fillInputBox(SUP_NAME_BOX_IMAGE, "Forshandeh " + str(counter), counter)
    fillInputBox(ADDRESS_BOX_IMAGE, "Address " + str(counter), counter)
    fillInputBox(PHONE_BOX_IMAGE,  "0912111111" + str(counter) , counter)
    fillInputBox(COMMENT_BOX_IMAGE, "Tozihat for Forshandeh " + str(counter), counter)
    fillInputBox(USERNAME_BOX_IMAGE, "nk a f " , counter)
    
def addRawMaterialType_EN(counter):
    ################################################################################# 
    # Navigate to the Add Material Type page
    click(URL_IMAGE)
    type("http://192.168.0.108:8000/myapp/addMaterialType/")
    type(Key.ENTER)
    wait(1)
    #################################################################################
    
    # Select the material based on the counter, adjusting for zero-based index
    material = materials[counter - 1]
    
    selectDropdownAndVerify(SUPPLIER_DD_IMAGE, "S_" + str(counter) + "_IMG")
    fillInputBox(MATERIAL_TYPE, material + str(counter), counter)
    fillInputBox(USERNAME_BOX_IMAGE, "nk a m t ", counter)
    
def addUnit_EN(counter):
    ################################################################################# 
    # Navigate to the Add Unit page
    click(URL_IMAGE)
    type("http://192.168.0.108:8000/myapp/addUnit/")
    type(Key.ENTER)
    wait(1)
    #################################################################################

    selected_unit = units[counter - 1]
    
    selectDropdownAndVerify(SUPPLIER_DD_IMAGE, "S_" + str(counter) + "_IMG")
    selectDropdownAndVerify(MATERIAL_TYPE_DD_IMG, "M_T_S_" + str(counter) + "_IMG")
    fillInputBox(UNIT_BOX_IMG, selected_unit + str(counter), counter)
    fillInputBox(QUAN_BOX_IMG, str(QUAN), counter)
    fillInputBox(USERNAME_BOX_IMAGE, "nk a u ", counter)

def addNewRawMaterial_EN(counter):
    ################################################################################# 
    # Navigate to the Add New Material page
    click(URL_IMAGE)
    type("http://192.168.0.108:8000/myapp/addRawMaterial/")
    type(Key.ENTER)
    wait(1)
    #################################################################################
    unit = units[counter - 1]
    
    
    selectDropdownAndVerify(SUPPLIER_DD_IMAGE, "S_" + str(counter) + "_IMG")
    selectDropdownAndVerify(MATERIAL_TYPE_DD_IMG, "M_T_S_" + str(counter) + "_IMG")
    fillInputBox(MATERIAL_NAME_BOX_IMG, unit + str(counter) , counter)
    fillInputBox(COMMENT_BOX_IMAGE, "Tozihat box: " + comment + str(counter), counter)
    fillInputBox(USERNAME_BOX_IMAGE, "nk a u ", counter)

def addTruck_FA(counter):
                
    resetKeyboardENG()
            
    ################################################################################# 
    # Navigate to the shipment page
    click(URL_IMAGE)
    type("http://192.168.0.108:8000/myapp/addTruck/")
    type(Key.ENTER)
    wait(1)
    #################################################################################
    
    fillInputBox2C(TWO_DIGIT_BOX_IMAGE, str(counter) + str(counter), counter)
    fillInputBox2C(THREE_DIGIT_BOX_IMAGE, str(counter) * 3, counter)
    click(CHECK_BUTTON_IMAGE)

    if exists(RED_INDICATOR_IMAGE):
        # Increment if the truck exists and retry
        logger.debug('Truck already exists for counter: {}'.format(counter))
    else:
        # Fill out the form
        switchKeyboardLayout()
        fillInputBox(FIRST_BOX_IMAGE, "Mr. Truck" + str(counter), counter)
        switchKeyboardLayout()
        fillInputBox(SECOND_BOX_IMAGE, "Lic Nm. " + str(counter), counter)
        switchKeyboardLayout()
        fillInputBox(THIRD_BOX_IMAGE, "09121111111" + str(counter), counter)
        switchKeyboardLayout()
        fillInputBox(LAST_BOX_IMAGE, "mk a trucks" + str(counter), counter)
        add_And_confirm()
        
        logger.debug('Truck added successfully for counter: {}'.format(counter))                        

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
    wait(1)
    if exists(GREEN_MESSAGE_IMAGE):
        wait(1)
        log('SUCCESS: %s ' % action_desc)
        wait(1)
    elif exists(RED_MESSAGE_IMAGE):
        wait(1)
        log('ERROR:   Already Exists when %s' % action_desc, "error")
        wait(1)
    else:
        wait(1)
        log('Status unknown after %s' % action_desc, "warning")
        wait(1)
    #################################################################################
def bede_6 (counter):
    new_counter = 3
    addTruck_EN(counter)
        
    validateAndLog("TESTING B6 FOR" + str(counter) + " EN NEW Truck")
    
    addCustomer_EN(counter)
    add_And_confirm(counter)
    validateAndLog("TESTING B6 FOR" + str(counter) + " EN NEW Customer")
    
    addSupplier_EN(counter)
    add_And_confirm(counter)
    validateAndLog("TESTING B6 FOR" + str(counter) + "EN NEW Supplier")
    
    addRawMaterialType_EN(counter)
    add_And_confirm(counter)
    validateAndLog("TESTING B6 FOR" + str(counter) + "EN NEW Material TYPE")        
    
    addUnit_EN(counter)
    add_And_confirm(counter)
    validateAndLog("TESTING B6 FOR" + str(counter) + "EN NEW Unit")    
    
    addNewRawMaterial_EN(counter)
    add_And_confirm(counter)
    validateAndLog("TESTING B6 FOR" + str(counter) + "EN NEW Raw Material")
    #################################################################################
def tcsFull (counter):
    addTruck_EN(counter)
        
    validateAndLog("adding EN NEW Truck")

    addCustomer_EN(counter)
    add_And_confirm(counter)
    validateAndLog("adding EN NEW Customer")
    
    addSupplier_EN(counter)
    add_And_confirm(counter)
    validateAndLog("adding EN NEW Supplier")

    addRawMaterialType_EN(counter)
    add_And_confirm(counter)
    validateAndLog("adding EN NEW Material TYPE")        

    addUnit_EN(counter)
    add_And_confirm(counter)
    validateAndLog("adding EN NEW Unit")    
    
    addNewRawMaterial_EN(counter)
    add_And_confirm(counter)
    validateAndLog("adding EN NEW Raw Material")
        
#################################################################################
#################################################################################
#                           Main script
#################################################################################

try:

    log("INFO:    Enter the starting counter value:                   %s" % (start_counter), "info")
    log("INFO:    Enter how many cycles to run:                       %s" % (cycle), "info")
    #log("INFO:    Enter the number of Reels to make per each counter: %s" % (reel_production_quantity), "info")
    log("INFO:    Enter the max entry (from counter 1 to counter X):  %s" % (max_entry), "info") 
    
    counter = start_counter
    for _ in range(cycle):
        
        #################################################################################
        #################################################################################
        #                                     ENTERING DATA
        #################################################################################
        #################################################################################
        #if counter == 5:
            #bede_6 (counter)

        tcsFull (counter)        
        
        
        
        #################################################################################
        counter += 1
        if counter > max_entry:
            counter = 1
        
finally:
    # Ensure the file handler is closed properly
    file_handler.close()
    logger.removeHandler(file_handler)
