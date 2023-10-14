# Jarvis_Python

Introduction about Project :-

Jarvis AI is a powerful AI tool. Jarvis can be used for various task such as :
It can answering any type of question.
It can play music for you.
It can do searches for you.
It is capable of opening websites like Google, Youtube, etc., in a web browser.
It is capable of opening your code editor or IDE with a single voice command.

First of all you need to sign up from an api key from the openAi website.Than install the openAI python library using pip.Than
import the library and set API Key.

Defining Speak () :-
The first and foremost thing for an A.I. assistant is that it should be able to speak. To make our J.A.R.V.I.S. talk,
we will make a function called speak(). This function will take audio as an argument, and then it will pronounce it.
Now, the next thing we need is audio. We must supply audio so that we can pronounce it using the speak() function we made.
We are going to install a module called pyttsx3.  (pip install pyttsx3.)

Defining Wish me ():-
we will make a wishme() function that will make our J.A.R.V.I.S. wish or greet the user according to the time of computer or pc. 
To provide current or live time to A.I., we need to import a module called datetime. 
Import this module to your program.  (import datetime)

 Defining Take command ():-
The next most important thing for our A.I. assistant is that it should take command with the help of the microphone of the user's system. 
So, now we will make a takeCommand() function.  With the help of the takeCommand() function, our A.I. assistant will return a string output by taking microphone input from the user.
Before defining the takeCommand() function, we need to install a module called speechRecognition. Install this module by: 
pip install speechRecognition
After successfully installing this module, import this module into the program by writing an import statement.
import speechRecognition as sr

Creating Our main() function:-
We will create a main() function, and inside this main() Function, we will call our speak function.

Defining Task 1: To open YouTube site in a web-browser
 To open any website, we need to import a module called webbrowser. It is an in-built module,
 and we do not need to install it with a pip statement; 
 we can directly import it into our program by writing an import statement.

Defining Task 2: To open Google site in a web-browser
We are opening Google in a web-browser by applying the same logic that we used to open youtube. 

Defining Task 3: To open amazon site in a web-browser
We are opening amazon in a web-browser by applying the same logic used in above two.

Defining Task 3: To play music 
To play music, we need to import a module called os. Import this module directly with 
an import statement.e first opened our music directory and then listed all the songs
present in the directory with the os module's help. With the help of os.startfile, 
you can play any song of your choice. I am playing the first song in the directory.
However, you can also play a random song with the help of a random module.
Every time you command to play music, J.A.R.V.I.S. will play any random song
from the song directory.

Defining Task 5: To know the current time:-
we are using the datetime() function and storing the current or live system time into a variable called strTime.
After storing the time in strTime, we are passing this variable as an argument in speak function. Now, the time string will be converted into speech.

Defining Task 6: To open the VS Code Program
To open the VS Code or any other application, we need the code path of the application.
