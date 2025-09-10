import customtkinter

#application
app = customtkinter.CTk()
app.geometry("800x750")

main_frame = customtkinter.CTkScrollableFrame(app)
main_frame.pack(fill="both", expand=True)

#global list
to_do_list = []
done = []

def text_mode_change():
    if customtkinter.get_appearance_mode() == "Light":
        return "🌚"
    else:
        return "🌝"

switch_text = customtkinter.StringVar(value=text_mode_change())
switch = customtkinter.CTkSwitch(main_frame, textvariable=switch_text, command=lambda: mode_change(), switch_width=40, switch_height=20, font=("Arial", 20))
switch.pack(pady=10, anchor="e")

def mode_change():
    if customtkinter.get_appearance_mode() == "Light":
        customtkinter.set_appearance_mode("Dark")
    else:
        customtkinter.set_appearance_mode("Light")
    # Mets à jour le texte du switch
    switch_text.set(text_mode_change())
    
def add_to_do_list(task, checkbox_widget=None):
    global to_do_list
    #Exception for empty or task already in to do list
    if task == "" or task in to_do_list and checkbox_widget == None:
        return
    else:
        to_do_list.append(task)
        #check if the call come from remove to do list or from the add button and destroy the previous checkbox of this task
        if checkbox_widget != None:
            checkbox_widget.destroy()
        else:
            entry.delete(0, "end")
        #create a checkbox with the name of the task 
        checkbox = customtkinter.CTkCheckBox(todo_frame, text=task, onvalue="on", offvalue="off", text_color=("white", "black"), border_color=("White", "Black"), font=("Arial", 15))
        checkbox.configure(command=lambda cb=checkbox: remove_to_do_list(task, cb))
        checkbox.pack(pady=10, anchor="w")

def remove_to_do_list(task, checkbox_widget):
      global to_do_list
      global done
      #find the task's position w²in to do list, add it in done list and delete it from to do list
      numb = to_do_list.index(task)
      done.append(task)
      del to_do_list[numb]
      #destroy the previous checkbox of this task
      checkbox_widget.destroy()
      #create a checkbox with the name of the task 
      var = customtkinter.StringVar(value="on")
      checkbox = customtkinter.CTkCheckBox(done_frame, text=task, variable=var ,onvalue="on", offvalue="off", text_color=("white", "black"), border_color=("White", "Black"), font=("Arial", 15))
      checkbox.configure(command=lambda cb=checkbox: add_to_do_list(task, cb))
      checkbox.pack(pady=10, anchor="w")
      
def delete(task):
    global to_do_list
    global done
    if task == "" :
        return
    elif task in to_do_list:
        numb = to_do_list.index(task)
        del to_do_list[numb]
        #destroy the previous checkbox of this task
        for widget in todo_frame.winfo_children():
            if widget.cget("text") == task:
                widget.destroy()
    elif task in done:
        numb = done.index(task)
        del done[numb]
        #destroy the previous checkbox of this task
        for widget in done_frame.winfo_children():
            if widget.cget("text") == task:
                widget.destroy()
    entry_delete.delete(0, "end")
    
#Name of list
title_to_do = customtkinter.CTkLabel(main_frame, text="To do :", font=("Arial", 25))
title_to_do.pack(pady=10)
todo_frame = customtkinter.CTkScrollableFrame(main_frame, fg_color=("darkgray", "lightgray"))
todo_frame.pack(pady=10, padx=10, fill="both", expand=True)

title_done = customtkinter.CTkLabel(main_frame, text="Tasks Done :", font=("Arial", 25))
title_done.pack(pady=10)
done_frame = customtkinter.CTkScrollableFrame(main_frame, fg_color=("darkgray", "lightgray"))
done_frame.pack(pady=10, padx=10, fill="both", expand=True)

#write a task
entry = customtkinter.CTkEntry(main_frame, placeholder_text="Please enter your task", width=400, font=("Arial", 20), justify="center")
entry.pack(pady=10 )
add_button = customtkinter.CTkButton(main_frame, text="Add Task", command=lambda: add_to_do_list(entry.get()), hover_color="green", font=("Arial", 17))
add_button.pack(pady=10)

entry_delete = customtkinter.CTkEntry(main_frame, placeholder_text="Enter the task to delete", width=400, font=("Arial", 20), justify="center")
entry_delete.pack(pady=10)
supp_button = customtkinter.CTkButton(main_frame, text="Delete Task", command=lambda: delete(entry_delete.get()), hover_color="red", font=("Arial", 17))
supp_button.pack(pady=10)

if __name__ == "__main__" :
   app.mainloop()