import customtkinter as ctk

# Khởi tạo cửa sổ chính
app = ctk.CTk()
app.title("Thàm Vinh Thành")
app.geometry("800x600")  

# Tạo frame chứa toàn bộ nội dung
main_frame = ctk.CTkFrame(master=app)
main_frame.pack(fill="both", expand=True)

# Tạo 2 frame ngang để chứa 4 frame con
top_frame = ctk.CTkFrame(master=main_frame)
top_frame.pack(fill="both", expand=True)

bottom_frame = ctk.CTkFrame(master=main_frame)
bottom_frame.pack(fill="both", expand=True)

# Tạo 4 frame con với màu sắc khác nhau
frame1 = ctk.CTkFrame(master=top_frame, fg_color="red")
frame2 = ctk.CTkFrame(master=top_frame, fg_color="green")
frame3 = ctk.CTkFrame(master=bottom_frame, fg_color="blue")
frame4 = ctk.CTkFrame(master=bottom_frame, fg_color="yellow")

# Sắp xếp 2 frame đầu theo chiều ngang trong top_frame
frame1.pack(side="left", fill="both", expand=True)
frame2.pack(side="left", fill="both", expand=True)

# Sắp xếp 2 frame còn lại theo chiều ngang trong bottom_frame
frame3.pack(side="left", fill="both", expand=True)
frame4.pack(side="left", fill="both", expand=True)

# Bắt đầu vòng lặp chính
app.mainloop()
