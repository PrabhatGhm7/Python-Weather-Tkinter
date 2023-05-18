import tkinter as tk
import Mainapp

def get_weather():
    city = entry.get()  # Get the city name from the Entry widget
    try:
        weather_data = Mainapp.get_weather_report(city)  # Call the function in Mainapp module to get the weather report
        output1.config(text=weather_data["current_temperature"])
        output2.config(text=weather_data["feels_like_temperature"])
        output3.config(text=weather_data["weather_description"])
    except(KeyError):
        label= tk.Label(root, text="Wrong City Name",font=("Arial",12))
        label.pack(padx=10,pady=10)

root = tk.Tk()
root.title("Weather Report")
root.geometry("300x300")
root.configure(
    bg= "#FFE4B5"
)

# Top label
label = tk.Label(root, text="Weather Report", font=('Helvetica', 15))
label.pack(padx=10, pady=10)
label.configure(bg="#FFDB9C")

# City entry
entry = tk.Entry(root, font=('Arial', 10))
entry.pack(padx=10, pady=5)

# Button to get weather report
button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack(padx=10, pady=5)
button.configure(bg="white")



# Output
output1 = tk.Label(root, text="", font=('MS Sans Serif', 10))
output1.pack(padx=10, pady=10)
output1.configure(bg="#FFDB9C")

output2 = tk.Label(root, text="", font=('MS Sans Serif', 10))
output2.pack(padx=10, pady=10)
output2.configure(bg="#FFDB9C")

output3 = tk.Label(root, text="", font=('MS Sans Serif', 10))
output3.pack(padx=10, pady=10)
output3.configure(bg="#FFDB9C")

root.mainloop()
