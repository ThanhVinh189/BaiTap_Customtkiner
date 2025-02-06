import customtkinter as ctk

# Tạo cửa sổ chính
root = ctk.CTk()
root.title("Thàm Vinh Thành")
root.geometry("300x500")

# Tạo Scrollable Frame để chứa 1000 nút
scrollable_frame = ctk.CTkScrollableFrame(root, width=480, height=480)
scrollable_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Tạo 1000 nút trong frame
for i in range(1000):
    btn = ctk.CTkButton(scrollable_frame, text=f"Button {i}")
    btn.pack(pady=2)

root.mainloop()
