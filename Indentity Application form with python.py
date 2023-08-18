import tkinter as tk
from tkinter import StringVar
from tkinter import ttk




def submit_form():
    # This function will be called when the user submits the form
    # Add your form submission logic here
    pass


# Get a list of country names
nationality_options = [
    "", "USA", "Canada", "UK", "Australia", "India", "Germany", "France", 
    "China", "Japan", "South Korea", "Brazil", "Mexico", "Italy", "Spain", 
    "Russia", "Saudi Arabia", "Egypt", "Nigeria", "South Africa", "Kenya",
    "Morocco", "Ghana"
    # Add more nationalities as needed
]

# Create the main application window
root = tk.Tk()
root.title("Application Form")


# Create a style for the labels
label_style = ttk.Style()
label_style.configure("Label.TLabel", font=("Helvetica", 12, "bold"))


# Create frames and widgets within the window
user_info_frame = ttk.Frame(root, padding=20)
user_info_frame.pack(padx=20, pady=20, anchor="w")  # Align the frame to the left

# Column weights to make the form responsive

user_info_frame.grid_columnconfigure(1, weight=1)

# Create and place widgets inside the frame
first_name_label = ttk.Label(user_info_frame, text="First Name:", style="Label.TLabel")
first_name_entry = ttk.Entry(user_info_frame, font=("Helvetica", 12))
first_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

last_name_label = ttk.Label(user_info_frame, text="Last Name:", style="Label.TLabel")
last_name_entry = ttk.Entry(user_info_frame, font=("Helvetica", 12))
last_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
last_name_entry.grid(row=1, column=1, padx=10, pady=5)



title_label = ttk.Label(user_info_frame, text="Title:", style="Label.TLabel")
title_var = StringVar()
title_options = ["", "Mr", "Mrs", "Ms", "Dr"]
title_combobox = ttk.Combobox(user_info_frame, textvariable=title_var, values=title_options, font=("Helvetica", 12))
title_var.set(title_options[0])  # Set default value
title_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
title_combobox.grid(row=2, column=1, padx=10, pady=5)

age_label = ttk.Label(user_info_frame, text="Age:", style="Label.TLabel")
age_var = StringVar()
age_options = [""] + [str(age) for age in range(18, 120)]  # From 18 to 120
age_combobox = ttk.Combobox(user_info_frame, textvariable=age_var, values=age_options, font=("Helvetica", 12))
age_var.set(age_options[0])  # Set default value
age_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
age_combobox.grid(row=3, column=1, padx=10, pady=5)


city_label = ttk.Label(user_info_frame, text="City:", style="Label.TLabel")
city_entry = ttk.Entry(user_info_frame, font=("Helvetica", 12))
city_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")


state_label = ttk.Label(user_info_frame, text="State:", style="Label.TLabel")
state_entry = ttk.Entry(user_info_frame, font=("Helvetica", 12))
state_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")


postcode_label = ttk.Label(user_info_frame, text="Post Code:", style="Label.TLabel")
postcode_entry = ttk.Entry(user_info_frame, font=("Helvetica", 12))
postcode_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")


gender_label = ttk.Label(user_info_frame, text="Gender:", style="Label.TLabel")
gender_var = StringVar()
gender_options = ["", "Male", "Female", "Other"]
gender_combobox = ttk.Combobox(user_info_frame, textvariable=gender_var, values=gender_options, font=("Helvetica", 12))
gender_var.set(gender_options[0])  # Set default value
gender_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender_combobox.grid(row=3, column=1, padx=10, pady=5)

ethnicity_label = ttk.Label(user_info_frame, text="Ethnicity:", style="Label.TLabel")
ethnicity_var = StringVar()
ethnicity_options = ["", "Asian", "Black", "Hispanic", "White", "Other"]
ethnicity_combobox = ttk.Combobox(user_info_frame, textvariable=ethnicity_var, values=ethnicity_options, font=("Helvetica", 12))
ethnicity_var.set(ethnicity_options[0])  # Set default value
ethnicity_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
ethnicity_combobox.grid(row=3, column=1, padx=10, pady=5)

disability_label = ttk.Label(user_info_frame, text="Disability Status:", style="Label.TLabel")
disability_var = StringVar()
disability_options = ["", "Yes", "No"]
disability_combobox = ttk.Combobox(user_info_frame, textvariable=disability_var, values=disability_options, font=("Helvetica", 12))
disability_var.set(disability_options[0])  # Set default value
disability_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
disability_combobox.grid(row=3, column=1, padx=10, pady=5)

nationality_label = ttk.Label(user_info_frame, text="Nationality:", style="Label.TLabel")
nationality_var = StringVar()
nationality_combobox = ttk.Combobox(user_info_frame, textvariable=nationality_var, values=nationality_options, font=("Helvetica", 12))
nationality_var.set(nationality_options[0])  # Set default value
nationality_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
nationality_combobox.grid(row=3, column=1, padx=10, pady=5)

drop_option_label = ttk.Label(user_info_frame, text="Drop Option:", style="Label.TLabel")
drop_option_var = StringVar()
drop_option_options = ["", "Yes", "No"]
drop_option_combobox = ttk.Combobox(user_info_frame, textvariable=drop_option_var, values=drop_option_options, font=("Helvetica", 12))
drop_option_var.set(drop_option_options[0])  # Set default value


# Pack or grid widgets within the frame
first_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

last_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

title_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
title_combobox.grid(row=2, column=1, padx=10, pady=5)

age_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
age_combobox.grid(row=3, column=1, padx=10, pady=5)

ethnicity_label.grid(row=10, column=0, padx=10, pady=5, sticky="w")
ethnicity_combobox.grid(row=10, column=1, padx=10, pady=5)

#address_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")
#address_entry.grid(row=5, column=1, padx=10, pady=5)

city_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
city_entry.grid(row=6, column=1, padx=10, pady=5)

state_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
state_entry.grid(row=7, column=1, padx=10, pady=5)

postcode_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
postcode_entry.grid(row=8, column=1, padx=10, pady=5)

gender_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
gender_combobox.grid(row=9, column=1, padx=10, pady=5)

disability_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
disability_combobox.grid(row=11, column=1, padx=10, pady=5)

nationality_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
nationality_combobox.grid(row=4, column=1, padx=10, pady=5)


# Consent and Agreement section
consent_text = (
    "I hereby confirm that the information provided in this application form is accurate and complete. "
    "I understand that any false or misleading information may lead to the rejection of my application."
)
consent_label = ttk.Label(user_info_frame, text="Consent and Agreement:", style="Label.TLabel")
consent_text_widget = tk.Text(user_info_frame, height=5, width=40, wrap=tk.WORD, font=("Helvetica", 12))
consent_text_widget.insert(tk.END, consent_text)
consent_text_widget.config(state=tk.DISABLED)  # Set the state to disabled

consent_check_var = tk.BooleanVar()
consent_checkbutton = tk.Checkbutton(user_info_frame, text="I agree to the terms and conditions", variable=consent_check_var)

# Pack or grid widgets within the frame
# ... (other fields)
consent_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
consent_text_widget.grid(row=11, column=1, padx=10, pady=5, columnspan=2)
consent_checkbutton.grid(row=12, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Submit button
submit_button = ttk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=15)


# Set the width for the comboboxes to make them equal
combobox_width = 18
combobox_style = ttk.Style()
combobox_style.configure("TCombobox", width=combobox_width)

title_combobox.config(width=combobox_width)
age_combobox.config(width=combobox_width)
nationality_combobox.config(width=combobox_width)
drop_option_combobox.config(width=combobox_width)
gender_combobox.config(width=combobox_width)
ethnicity_combobox.config(width=combobox_width)
disability_combobox.config(width=combobox_width)

# Start the main event loop
root.mainloop()





