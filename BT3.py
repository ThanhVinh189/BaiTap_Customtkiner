import customtkinter as ctk

# Tạo cửa sổ chính
root = ctk.CTk()
root.title("Thàm Vinh Thành")
root.geometry("300x500")

# Tạo Scrollable Frame để chứa các nút
scrollable_frame = ctk.CTkScrollableFrame(root, width=480, height=480)
scrollable_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Hàm tạo các nút theo đợt
def create_buttons(start, end):
    for i in range(start, end):
        btn = ctk.CTkButton(scrollable_frame, text=f"Button {i}")
        btn.pack(pady=2)

    # Cập nhật sau mỗi khoảng thời gian nhất định (5000 ms = 5 giây)
    if end < 1000:
        root.after(5000, create_buttons, end, min(end + 50, 1000))

# Khởi tạo ứng dụng với 50 nút đầu tiên
create_buttons(0, 50)

# Vòng lặp chính
root.mainloop()
