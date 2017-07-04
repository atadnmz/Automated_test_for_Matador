
switchApp("dd.txt - Notepad")
switchApp("matador")
testCount = 1
wait(1)
Settings.WaitScanRate = 10
Settings.MoveMouseDelay = 0
def switchCheck(image):
    switch = True
    while(switch):
        focus("MATADOR")
        if exists(image):            
            switch = False
    return    
def MessageBoxSelect(image,str):
    MessageBox = True
    while(MessageBox):
        switchApp("Rodeo :: Test Driver for Matador - 2.2.0")
        if(find("1499086577897.png")):  
            type("1499086014992.png",str)            
            check = True
            count = 0
            while(check and count<25):
                if(exists(image,0)):
                    check = False
                type(Key.DOWN)
                count= count+1
            type(Key.UP)
            type(Key.ENTER)
        #if(find(image)):
         #   type("1499087187403.png","n")        
          #  click(Pattern("1499087096892.png").similar(0.60))
        #    type(Key.ENTER)
            MessageBox = False
    return
MessageBoxSelect(Pattern("IM-1.PNG").similar(0.95),"I")
click("1499104325413.png")
MessageBoxSelect("KM.PNG","k")
type("1499104414963.png","n")
type(Key.ENTER)
click("1499104325413.png")
click("1499110294997.png")

click("1499108791334.png")
click("1499108819861.png")
click("1499108867406.png")
click("1499108976780.png")
if not exists("1499105128109.png"):  
    popup("Error found at requirement "+str(testCount))########## 1
testCount=testCount+1
type("1499109492150.png","g")
type(Key.ENTER)
click("1499109534270.png")
switchApp("Rodeo :: Test Driver for Matador - 2.2.0")
if not exists("1499110422261.png"):
    popup("Error found at requirement "+str(testCount))########## 2
testCount=testCount+1
click("1499110771370.png")
click("1499108791334.png")
click("1499110861538.png")
doubleClick("1499110896096.png")
type("54")
type(Key.ENTER)
if not exists("1499111313556.png"):
    popup("Error found at requirement "+str(testCount))########## 3
testCount=testCount+1
doubleClick("1499110896096.png")
type("54,5")
if not exists(Pattern("1499111713879.png").similar(0.90)):
    popup("Error found at requirement "+str(testCount))########## 4
testCount=testCount+1
doubleClick("1499111960332.png")
type("32") 
type(Key.ENTER)
if not exists("1499112219489.png"):
    popup("Error found at requirement "+str(testCount))########## 5
testCount=testCount+1
doubleClick("1499111960332.png")
type("32,5")
if not exists("1499112322777.png"):
    popup("Error found at requirement "+str(testCount))########## 6
testCount=testCount+1
doubleClick("1499111960332.png")
type("181") 
type(Key.ENTER)
if not exists("1499112219489.png"):
    popup("Error found at requirement "+str(testCount))########## 7
testCount=testCount+1
doubleClick("1499111960332.png")
type("180") 
type(Key.ENTER)
if not exists("1499112546055.png"):
    popup("Error found at requirement "+str(testCount))########## 8
testCount=testCount+1
doubleClick("1499112611135.png")
type("181") 
type(Key.ENTER)
if not exists("1499112611135.png"):
    popup("Error found at requirement "+str(testCount))########## 9
testCount=testCount+1
doubleClick("1499112611135.png")
type("180") 
type(Key.ENTER)
if not exists("1499112745900.png"):
    popup("Error found at requirement "+str(testCount))########## 10
testCount=testCount+1
doubleClick("1499112866883.png")
type("-70") 
type(Key.ENTER)
doubleClick("1499112919605.png")
type("50") 
type(Key.ENTER)
if not exists(Pattern("1499112958643.png").exact()):
    popup("Error found at requirement "+str(testCount))########## 11
testCount=testCount+1
doubleClick("1499113023698.png")
type("-1") 
type(Key.ENTER)
if not exists("1499113066650.png"):
    popup("Error found at requirement "+str(testCount))########## 12
testCount=testCount+1
doubleClick("1499113023698.png")
type("-1") 
type(Key.ENTER)
if not exists("1499113066650.png"):
    popup("Error found at requirement "+str(testCount))########## 13
testCount=testCount+1

    
    

popup("No Error found")

            
        