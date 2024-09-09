from speech_recognizer import SpeechRecognizer
from notion import NotionClient
from auth_checker import AuthChecker
import os
import colorful


print(colorful.green("Welcome to Noty, the best verbal note taking app out there"))
print(colorful.green("### We record your notes and write them directly in your Notion database, sounds awesome right?"))
print(colorful.red("\tUsage instructions:"))
print(colorful.purple("\t1. Insert your Notion token: "))
print(colorful.purple("\t\tTo get your Notion token: "))
print(colorful.cyan("""\t\t\t 1- Go to your Notion account settings\n\t\t\t 2- Go to connections section 
\t\t\t 3- Create new integration named (Speech Recognition) 
\t\t\t 4- Enter the new integration then reveal your Notion token """))
print(colorful.purple("\t2. Insert your Notion database Id: "))
print(colorful.purple("\t\tTo get your page's Notion database id: "))
print(colorful.cyan("""\t\t\t 1- Create a new page then insert a new table
\t\t\t 2- The table should contain three colums and three rows\n\t\t\t 3- The first colum name must be (Description) with a title type
\t\t\t 4- The second colum name must be (Date) with a date type
\t\t\t 5- The third colum name must be (Status) with a text type
\t\t\t 6- Start copying from after the back slash (\) until before the question mark (?)"""))




client = NotionClient() # an object of class NotionClient
recognizer = SpeechRecognizer() # an object of class SpeechRecognizer
checker = AuthChecker() # an object of class AuthChecker

token, database_id = checker.get_auth_data() # getting token and database id of the user
print(colorful.orange(f"""To start the program you will have to say the activation command : 
{recognizer.activation_command}, And to shut down the program you will have to say the deactivation command : 
{recognizer.deactivation_command}"""))
print(colorful.orange("""After saying the activation command you can take notes
as long as you want until you say the deactivation command"""))

while True: # created a while loop to make sure that the program is always running until it gets stopped by the user
    a = recognizer.get_audio() # getting audio from the user's mic
    command = recognizer.audio_to_text(a)  # passing the audio to convert it to text 

    if recognizer.activation_command in command: # checking if the activation command was mentioned in the audio
        
        while True:
            
            print("Active")
            recognizer.play_sound("What can I do for you?")
            note = recognizer.get_audio() 
            note = recognizer.audio_to_text(note)

            if recognizer.deactivation_command in note: #checking if the deactivation command mentioned in the audio if not it will keep taking notes until hearing the deactivation command
                print('You have terminated the program.')
                recognizer.play_sound("Shutting down")
                os._exit(0)

            if note:
                recognizer.play_sound(note) # playing the user's note to let him know it was recognized correctly
                res = client.create_note(token, database_id, note, status="Created by Speech Recognition") # creating a note with the user's data

                if res.status_code == 200: # if status code is OK
                    recognizer.play_sound("I stored your new note successfully!")
                    print("A new note has been added successfully!")
                    
                else:
                    recognizer.play_sound("An error ocurred: ")

    else:
        print(colorful.pink(f"To start the program you will have to say the activation command : {recognizer.activation_command}, And to shut down the program you will have to say the deactivation command : {recognizer.deactivation_command}"))
        recognizer.play_sound("You have to say the displayed activation command to start the program")