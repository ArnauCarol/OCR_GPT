import os
import time
from PIL import ImageGrab, Image
import cv2
import pytesseract
import openai
import subprocess
#from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
#from PyQt5.QtCore import Qt  # Import Qt constants
#from widget import widget_box

def analyze (image_filename):

   
    image_filename = image_filename
    # Load the image
    img = cv2.imread(image_filename)

    # Perform OCR on the image
    extracted_text = pytesseract.image_to_string(img)

    # Print the extracted text for each frame

    print(extracted_text)
    print('=' * 40)  # Add a separator for clarity
    
    return(extracted_text)




def texts_identical(text1, text2):
    try:
        if text1 == text2:
            pass
        else:
            print(text1)
    except Exception:
        pass



def chat_gpt(extracted_text):
    openai.api_key ='Chat-gpt key'

# Define the multiple-choice question as a string
    question = f"Can you give me the correct answer? {extracted_text}"

# Define the conversation with the user message (the question)
    conversation = [
        {"role": "user", "content": question}
    ]

# Send the conversation to the model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=50,  # You can adjust the max_tokens to limit the response length
    )

# Get the model's reply
    model_reply = response["choices"][0]["message"]["content"]

    #widget_box(model_reply)
    #with open("extracted_text.txt", "a") as file:
    # Write the extracted text to the file
                #file.write("\n Answers")
                #file.write(model_reply)

    print(model_reply)


def cropp ():

# Load the image (or capture a screenshot)
    image = cv2.imread("./screenshots/screenshot_0.png")

# Define the coordinates of the region you want to crop (x, y, width, height)
    x = 380 # Starting x-coordinate
    y = 110   # Starting y-coordinate
    width = 700  # Width of the region
    height = 650  # Height of the region

# Crop the image to the specified region
    cropped_image = image[y:y+height, x:x+width]

    cv2.imwrite("cropped_image.png", cropped_image)
  





def screen_recorder (time_screen, last_text=""):
# Create a directory to save the screenshots
    if not os.path.exists("screenshots"):
      os.makedirs("screenshots")
    ##print('\n Starting in 3 seconds  \n')
    ##time.sleep(3)
    print(' ----------------------')
    print(' Screen recording')
    print(' ---------------------- \n')

    
    #print('      ---------    \n    |          |    \n    |          |    \n    |          |    \n      ---------    \n')
    # Define the number of screenshots to capture
    #num_screenshots = 20
    #with open("extracted_text.txt", "w") as file:
        #file.write("\n")
    #file.close()
            
    num_screenshots = int((time_screen)/3)
  
    for i in range(num_screenshots):
    # Capture a screenshot
        #print(' Screenshot nº' + str(i))
        #print('\n')       
    
    # Capture the entire screen
        screenshot = ImageGrab.grab()

# Save the screenshot as an image file
        #screenshot.save(f"screenshots/screenshot_{i}.png")
    
    
        #  image_filename = "/screenshots/screenshot_" + str(i) + ".png"
    # Load the image
        #img = cv2.imread(image_filename)
        img = screenshot
    
    #Cropping the image
   # x = 380 # Starting x-coordinate
    #y = 110   # Starting y-coordinate
    #width = 700  # Width of the region
   # height = 650  # Height of the region

# Crop the image to the specified region
    #cropped_image = img[y:y+height, x:x+width]
    #identifier = i

    #cv2.imwrite("output_cropped_{identifier}.png", cropped_image)
    

    # Perform OCR on the image
        extracted_text = pytesseract.image_to_string(img)
    
    
    
    # Print the extracted text for each frame
        if last_text != extracted_text:


    # The command to clear the console screen (Linux/Unix/macOS)
            command = "clear"

    # Execute the clear command
            subprocess.run(command, shell=True)



# Close the file
            #file.close()
        
            #print(extracted_text)
            chat_gpt(extracted_text)
                    # Open the file in write mode
            #with open("extracted_text.txt", "a") as file:
    # Write the extracted text to the file

                #file.write("\n")
                #file.write(extracted_text)
        else:
            time.sleep(3)
            continue
    
        last_text = extracted_text 
    
    
    # You can add a delay here to control the capture rate if needed
    
        #time.sleep(2)
        print('\n')
    print('\n Stop recording \n')






screen_recorder(60)




