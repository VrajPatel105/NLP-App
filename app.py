from tkinter import *
from mydatabase import Database
from tkinter import messagebox
from myapi import API
from PIL import Image
import requests

class NLPApp:
    
    def __init__(self):

        #create a database object
        self.dbo = Database() # dbo = database object
        self.apio = API()
        
        #Load login GUI.
        self.root = Tk() # making a object or tkinter class and named it as root. You can name it as anything..
        self.root.title('NLP Application') # title
        self.root.iconbitmap('resources/favicon.ico') # own icon for the application
        self.root.geometry('800x800') # own resolution
        self.root.configure(bg = '#a4a5a5') # own background color. you can write any color or it's hex code.

        self.login_gui()

        self.root.mainloop() # this will hold the GUI internface. If you dont write this then the GUI will disappear in split second.

    def login_gui(self):
        # firstly, clear the existing GUI
        self.clear_gui()
        
        heading = Label(self.root, text = 'NLPApp', bg = '#a4a5a5', fg = 'white') # own title that you want to show on the GUI screen.
        heading.pack(pady=(30,30)) # to display the label, we can call pack or grit which will display the output on the GUI. Here we have used the pack because it's intelligent enough.
        # pady will leave 30 30 pixel gap from top and bottom.
        heading.configure(font = ('verrdana', 24 , 'bold'))


        label1 = Label(self.root, text = 'Enter Email')
        label1.pack(pady=(10,10))
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10), ipady=4)
        

        label2 = Label(self.root, text = 'Enter Password')
        label2.pack(pady=(10,10))
        self.password_input = Entry(self.root, width=50, show='*') # show is when you type something in the password input, it will show the words in form of the symbol..
        self.password_input.pack(pady=(5,10), ipady=4)

        login_button = Button(self.root, text = 'Login', width = 20, height=2, command= self.perform_login)
        login_button.pack(pady=(10,10))

        label3 = Label(self.root, text = 'Not a member?')
        label3.pack(pady=(20,10))
        redirect_button = Button(self.root, text = 'Register Now', command=self.register_gui) # here the command is used as an event listener.. and when the button is clicked, it redirects you to the function that you want it to be redirected.
        redirect_button.pack(pady=(10,10))


    def register_gui(self):
        # firstly, clear the existing GUI
        self.clear_gui()

        heading = Label(self.root, text = 'NLPApp', bg = '#a4a5a5', fg = 'white') # own title that you want to show on the GUI screen.
        heading.pack(pady=(30,30)) # to display the label, we can call pack or grit which will display the output on the GUI. Here we have used the pack because it's intelligent enough.
        # pady will leave 30 30 pixel gap from top and bottom.
        heading.configure(font = ('verrdana', 24 , 'bold'))

        label0 = Label(self.root, text = 'Enter Name')
        label0.pack(pady=(10,10))
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5,10), ipady=4)

        label1 = Label(self.root, text = 'Enter Email')
        label1.pack(pady=(10,10))
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10), ipady=4)
        

        label2 = Label(self.root, text = 'Enter Password')
        label2.pack(pady=(10,10))
        self.password_input = Entry(self.root, width=50, show='*') # show is when you type something in the password input, it will show the words in form of the symbol..
        self.password_input.pack(pady=(5,10), ipady=4)

        register_button = Button(self.root, text = 'Register', width = 20, height=2, command= self.perform_registration)
        register_button.pack(pady=(10,10))

        label3 = Label(self.root, text = 'Already a member?')
        label3.pack(pady=(20,10))
        redirect_button = Button(self.root, text = 'Login Now', command=self.login_gui) # here the command is used as an event listener.. and when the button is clicked, it redirects you to the function that you want it to be redirected.
        redirect_button.pack(pady=(10,10))
        

    # since we have to clean the gui a lot of times, we are creating a function.
    def clear_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_registration(self):
        #firstly we have to fetch the data from the gui that the user entered
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success', 'Registratoin Successful. You can login now')
        else:
            messagebox.showerror('Error','User already exists')

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect Email/Password')



    def home_gui(self):
        
        self.clear_gui()

        heading = Label(self.root, text = 'NLPApp', bg = '#a4a5a5', fg = 'white') 
        heading.pack(pady=(30,30))
        heading.configure(font = ('verrdana', 24 , 'bold'))

        sentiment_button = Button(self.root, text = 'Sentiment Analysis', width = 20, height=2, command= self.sentiment_gui)
        sentiment_button.pack(pady=(10,10))

        image_button = Button(self.root, text = 'Image Generator', width = 20, height=2, command= self.image_gui)
        image_button.pack(pady=(10,10))

        emotion_button = Button(self.root, text = 'Headline Generator', width = 20, height=2, command= self.headline_generator_gui)
        emotion_button.pack(pady=(10,10))

        logout_button = Button(self.root, text = 'Logout', width = 10, height=2, command= self.login_gui)
        logout_button.pack(pady=(10,10))



    def sentiment_gui(self):

        self.clear_gui()

        heading = Label(self.root, text = 'NLPApp', bg = '#a4a5a5', fg = 'white') 
        heading.pack(pady=(30,30))
        heading.configure(font = ('verrdana', 24 , 'bold'))

        heading1 = Label(self.root, text = 'Sentiment Analysis', bg = '#a4a5a5', fg = 'white') 
        heading1.pack(pady=(10,20))
        heading1.configure(font = ('verrdana', 20))

        label1 = Label(self.root, text = 'Enter the text below')
        label1.pack(pady=(10,10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5,10), ipady=4)

        sentiment_button = Button(self.root, text = 'Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_button.pack(pady=(10,10))

        self.sentiment_result = Label(self.root, text = '', background='#a4a5a5', fg = 'white')
        self.sentiment_result.pack(pady=(10,10)) 
        self.sentiment_result.configure(font=('verdana', 16))

        goback_button = Button(self.root, text = 'Go Back', command= self.home_gui)
        goback_button.pack(pady=(10,10))
        

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        if 'scored_labels' in result:
            final_result = "\n".join([f"{item['label']} -> {item['score']}" for item in result['scored_labels']])
        else:
            final_result = "Unexpected API response format"
        self.sentiment_result.config(text=final_result)
        

    def image_gui(self):
        pass

    def headline_generator_gui(self):
         
         self.clear_gui()

         heading = Label(self.root, text = 'NLPApp', bg = '#a4a5a5', fg = 'white') 
         heading.pack(pady=(30,30))
         heading.configure(font = ('verrdana', 24 , 'bold'))

         heading1 = Label(self.root, text = 'Title Generator', bg = '#a4a5a5', fg = 'white') 
         heading1.pack(pady=(10,20))
         heading1.configure(font = ('verrdana', 20))

         label1 = Label(self.root, text = 'Enter the Paragraph below')
         label1.pack(pady=(10,10))

         self.para_input = Entry(self.root, width=50)
         self.para_input.pack(pady=(5,10), ipady=4)

         para_button = Button(self.root, text = 'Generate Headline', command=self.generate_headline)
         para_button.pack(pady=(10,10))

         self.para_result = Label(self.root, text = '', background='#a4a5a5', fg = 'white')
         self.para_result.pack(pady=(10,10)) 
         self.para_result.configure(font=('verdana', 16))

         goback_button = Button(self.root, text = 'Go Back', command= self.home_gui)
         goback_button.pack(pady=(10,10))
        

    def generate_headline(self):
        text = self.para_input.get()  # Get the input text from the Entry widget
        result = self.apio.headline_generator(text)  # Call the API to generate a headline
        
        # Check if 'summary_text' exists in the result and extract its value
        if 'summary_text' in result:
            headline = result['summary_text']  # Extract the summarized text
        else:
            headline = "Error: Could not generate headline"  # Fallback message if key is missing
        
        # Display the headline in the para_result label
        self.para_result.config(text=headline)



    def image_gui(self):

        self.clear_gui()

        heading = Label(self.root, text = 'NLPApp', bg = '#a4a5a5', fg = 'white') 
        heading.pack(pady=(30,30))
        heading.configure(font = ('verrdana', 24 , 'bold'))

        heading1 = Label(self.root, text = 'Image Generator', bg = '#a4a5a5', fg = 'white') 
        heading1.pack(pady=(10,20))
        heading1.configure(font = ('verrdana', 20))

        label1 = Label(self.root, text = 'Enter the imaginary input below')
        label1.pack(pady=(10,10))

        self.image_input = Entry(self.root, width=50)
        self.image_input.pack(pady=(5,10), ipady=4)

        image_button = Button(self.root, text = 'Generate Image', command=self.get_generated_image)
        image_button.pack(pady=(10,10))

        self.image_result = Label(self.root, text = '', background='#a4a5a5', fg = 'white')
        self.image_result.pack(pady=(10,10)) 
        self.image_result.configure(font=('verdana', 16))

        goback_button = Button(self.root, text = 'Go Back', command= self.home_gui)
        goback_button.pack(pady=(10,10))


    def get_generated_image(self):
        try:
            text = self.image_input.get()
            result = self.apio.image_analysis(text)  # Call the API

            # Check if the 'url' key exists in the response
            if "url" in result:
                image_url = result["url"]  # Get the URL of the generated image

                # Download the image
                response = requests.get(image_url)
                if response.status_code == 200:
                    # Save the image locally
                    image_path = "generated_image.png"
                    with open(image_path, "wb") as f:
                        f.write(response.content)

                    # Open the saved image
                    image = Image.open(image_path)
                    image.show()

                    # Update GUI to indicate success
                    self.image_result.config(text="Image generated and saved as 'generated_image.png'")
                else:
                    self.image_result.config(text="Failed to download the image")
            else:
                self.image_result.config(text="No image URL in API response")
        except Exception as e:
            self.image_result.config(text="Error generating image: " + str(e))


    

nlp = NLPApp()