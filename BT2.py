import customtkinter as ctk

# Tạo cửa sổ chính
root = ctk.CTk()
root.title("Thàm Vinh Thành")
root.geometry("700x400")

# Tạo frame chứa danh sách sản phẩm và thanh cuộn
frame = ctk.CTkScrollableFrame(root, width=550, height=350)
frame.pack(pady=10, padx=10, fill="both", expand=True)

# Thêm 20 sản phẩm giả định
for i in range(80):
    btn = ctk.CTkButton(frame, text=f"iPhone {i+1}")
    btn.grid(row=i//4, column=i % 4, padx=10, pady=10)

root.mainloop()
