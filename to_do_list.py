import customtkinter

#application
app = customtkinter.CTk()
app.geometry("400x700")

#global list
to_do_list = []
done = []

def add_to_do_list(task, checkbox_widget=None):
    global to_do_list
    #Exception for empty or task already in to do list
    if task == "" or task in to_do_list and checkbox_widget != None:
        checkbox_widget.destroy()
        return
    else:
        to_do_list.append(task)
        #check if the call come from remove to do list or from the add button and destroy the previous checkbox of this task
        if checkbox_widget != None:
            checkbox_widget.destroy()
        else:
            entry.delete(0, "end")
        #create a checkbox with the name of the task 
        checkbox = customtkinter.CTkCheckBox(todo_frame, text=task, onvalue="on", offvalue="off")
        checkbox.configure(command=lambda cb=checkbox: remove_to_do_list(task, cb))
        checkbox.pack(pady=10)

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
      checkbox = customtkinter.CTkCheckBox(done_frame, text=task, variable=var ,onvalue="on", offvalue="off")
      checkbox.configure(command=lambda cb=checkbox: add_to_do_list(task, cb))
      checkbox.pack(pady=10)

#Name of list
title_to_do = customtkinter.CTkLabel(app, text="To do :")
title_to_do.pack(pady=10)
todo_frame = customtkinter.CTkFrame(app)
todo_frame.pack(pady=10)

title_done = customtkinter.CTkLabel(app, text="Tasks Done :")
title_done.pack(pady=10)
done_frame = customtkinter.CTkFrame(app)
done_frame.pack(pady=10)

#write a task
entry = customtkinter.CTkEntry(app, placeholder_text="Please enter your task", width=200)
entry.pack(pady=10)
add_button = customtkinter.CTkButton(app, text="Add Task", command=lambda: add_to_do_list(entry.get()))
add_button.pack(pady=10)

if __name__ == "__main__" :
   app.mainloop()