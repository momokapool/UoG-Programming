import tkinter as tk

from check_videos import CheckVideos


def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(window))


window = tk.Tk()
window.geometry("520x150")
window.title("Video Player")



header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_video_list_btn = tk.Button(window, text="Create Video List")
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_videos_btn = tk.Button(window, text="Update Videos")
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
