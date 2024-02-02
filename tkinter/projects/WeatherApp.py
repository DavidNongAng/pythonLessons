from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title('Weather App')
root.iconbitmap('tkinter/default tkinter/img/favicon.ico')
root.geometry("600x100")

#Create zipcode lookup function
def zipLookup():
    #zip.get()
    #zipLabel = Label(root, text=zip.get())
    #zipLabel.grid(row=1, column=0, columnspan=2)
    
    try:
        #Connect to the API
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=76FF445B-8974-462D-B08D-17469FD56E6B")
        
        #Convert from json to a Python List.
        api = json.loads(api_request.content)
        
        #Get the Specific information we want from the output of the API
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        #Check what type of weather condition is right now and assign a color to it.
        if category == "Good": 
            weather_color = "#00e400"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff7e00"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#8f3f97"
        elif category == "Hazardous":
            weather_color = "#7e0023"
            
        root.configure(background=weather_color)

        #Create Label to display the results from the API
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
        myLabel.grid(row=1,column=0, columnspan=2)   

    except Exception as e:
        api = "error..."


zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command= zipLookup)
zipButton.grid(row=0, column=1,stick=W+E+N+S)


root.mainloop()
