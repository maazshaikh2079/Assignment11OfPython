# Info:-
# Name   : Maaz 
# Dept   : CO-B
# Batch  : 4
# Sub    : Python Assignment-10
# Topic  :-
# Create a gui based form to take input from the user and then navigate to the particular site from where the 
# user came to know about the content
# for example:
# create a form where the user is enquiring about the respective course
# and in the form there is an option for asking where the user came to know about it, for eg: instagram ads 
# or YouTube ads
# and then when clicking the submit button
# take the user to the faq page of that site
# Date   : 19-07-2023

# Program:-
import tkinter as tk
import webbrowser

def submit_form():
    course = entry.get()
    source = sourcevar.get()
    if source == "Facbook Ads":
        webbrowser.open(
            "https://developers.facebook.com/docs/app-ads/support/")
    elif source == "YouTube Ads":
        webbrowser.open(
            "https://support.google.com/youtube/thread/677314/%F0%9F%94%8D-youtube-faqs-need-help-start-here?hl=en")
    elif source == "Instgram Ads":
        webbrowser.open("https://help.instagram.com/")


window = tk.Tk()
window.title("Course Enrollment Form")
label1 = tk.Label(window, text="Course:")
label1.pack()
entry = tk.Entry(window)
entry.pack()
label2 = tk.Label(window, text="Source:")
label2.pack()
sources = ["Facebook Ads", "YouTube Ads", "Instagram Ads"]
sourcevar = tk.StringVar(window)
sourcevar.set(sources[0])
dropdown = tk.OptionMenu(window, sourcevar, *sources)
dropdown.pack()
button = tk.Button(window, text="Submit", command=submit_form)
button.pack()
window.mainloop()
