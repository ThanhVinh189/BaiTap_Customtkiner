import customtkinter as ctk

# Khởi tạo cửa sổ chính
app = ctk.CTk()
app.title("Thàm Vinh Thành")
app.geometry("800x600")  


# Cấu hình lưới (grid) cho cửa sổ chính
app.grid_rowconfigure((0, 1), weight=1)
app.grid_columnconfigure((0, 1), weight=1)

# Tạo 4 frame với màu sắc khác nhau
frame1 = ctk.CTkFrame(master=app, fg_color="red")
frame2 = ctk.CTkFrame(master=app, fg_color="green")
frame3 = ctk.CTkFrame(master=app, fg_color="blue")
frame4 = ctk.CTkFrame(master=app, fg_color="yellow")

# Đặt các frame vào lưới (grid)
frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=1, sticky="nsew")
frame3.grid(row=1, column=0, sticky="nsew")
frame4.grid(row=1, column=1, sticky="nsew")

# Bắt đầu vòng lặp chính
app.mainloop()
