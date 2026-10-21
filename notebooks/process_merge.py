import os
import pandas as pd

# 1. Tạo thư mục interim và processed ở ổ đĩa hiện tại (hoặc thư mục làm việc)
os.makedirs("data/interim", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# 2. Đọc các bảng dữ liệu (Trỏ thẳng tới thư mục chứa file, ví dụ trong thư mục Downloads hoặc cùng cấp)
# *Lưu ý: Nếu 3 file đang nằm ở C:\Users\minhvg\Downloads\, bạn dùng đường dẫn này:*
path_dir = r"C:\Users\minhvg\Downloads"

df_orders = pd.read_csv(os.path.join(path_dir, "train.csv"))
df_returns = pd.read_csv(os.path.join(path_dir, "returns.csv"))
df_managers = pd.read_csv(os.path.join(path_dir, "region_managers.csv"))

print(f"Số đơn hàng gốc (Orders): {len(df_orders)}")
print(f"Số bản ghi trả hàng (Returns): {len(df_returns)}")

# 3. MERGE BẢNG 1: Orders + Returns (Khoá chung: 'Order ID')
df_merged = pd.merge(df_orders, df_returns, on="Order ID", how="left")

# Điền giá trị cho các đơn KHÔNG bị trả hàng
df_merged["Returned"] = df_merged["Returned"].fillna("No")
df_merged["Return Reason"] = df_merged["Return Reason"].fillna("None")

# 4. MERGE BẢNG 2: Orders + Region Managers (Khoá chung: 'Region')
df_merged = pd.merge(df_merged, df_managers, on="Region", how="left")

# 5. Kiểm tra kết quả sau Merge
print(f"Kích thước DataFrame sau khi Merge: {df_merged.shape}")
print("Các cột mới được bổ sung vào bộ dữ liệu:")
print(
    df_merged[
        ["Order ID", "Returned", "Return Reason", "Regional Manager"]
    ].head()
)

# 6. Lưu file đã Merge vào thư mục data/processed/
output_path = "data/processed/train_merged.csv"
df_merged.to_csv(output_path, index=False)
print(f"Đã xuất file dữ liệu sạch hoàn chỉnh vào: {output_path}")