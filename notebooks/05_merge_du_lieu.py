import os
import pandas as pd
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

print("=== 1. TỰ ĐỘNG ĐỌC VÀ XÁC ĐỊNH ĐƯỜNG DẪN DỮ LIỆU ===")
# Tương thích linh hoạt dù bạn chạy từ thư mục gốc hay trong thư mục notebooks/
if os.path.exists("../data/raw/train.csv"):
  data_dir = "../data/raw"
elif os.path.exists("data/raw/train.csv"):
  data_dir = "data/raw"
else:
  data_dir = "../../data/raw"

df_train = pd.read_csv(os.path.join(data_dir, "train.csv"))
df_returns = pd.read_csv(os.path.join(data_dir, "returns.csv"))

# Xử lý đường dẫn cho file region_managers (có thể có hoặc không có đuôi .csv)
region_path = os.path.join(data_dir, "region_managers")
if not os.path.exists(region_path) and os.path.exists(region_path + ".csv"):
  region_path += ".csv"
df_regions = pd.read_csv(region_path)

print(f"- Đã tải train.csv thành công: {df_train.shape} dòng")
print(f"- Đã tải returns.csv thành công: {df_returns.shape} dòng")
print(f"- Đã tải region_managers thành công: {df_regions.shape} dòng\n")


print("=== 2. THỰC HIỆN MERGE CÁC BẢNG DỮ LIỆU ===")
# Left join bảng đơn hàng với bảng trả hàng theo 'Order ID'
df_merged = pd.merge(df_train, df_returns, on="Order ID", how="left")

# Điền giá trị mặc định cho các đơn hàng không bị trả lại
df_merged["Returned"] = df_merged["Returned"].fillna("No")
df_merged["Return Reason"] = df_merged["Return Reason"].fillna("None")

# Merge tiếp với bảng quản lý khu vực theo 'Region'
df_merged = pd.merge(df_merged, df_regions, on="Region", how="left")

print(f"-> Kích thước dữ liệu sau khi merge toàn bộ: {df_merged.shape}")
print("-> Thống kê trạng thái đơn hàng bị trả lại:")
print(df_merged["Returned"].value_counts(), "\n")


print("=== 3. THỐNG KÊ DOANH THU SO VỚI TARGET THEO KHU VỰC ===")
region_performance = (
    df_merged.groupby(["Region", "Regional Manager", "Target Sales 2017"])["Sales"]
    .sum()
    .reset_index()
)
region_performance.rename(columns={"Sales": "Actual Sales"}, inplace=True)
region_performance["Achievement (%)"] = (
    region_performance["Actual Sales"]
    / region_performance["Target Sales 2017"]
    * 100
)
print(region_performance.round(2), "\n")


print("=== 4. VẼ BIỂU ĐỒ TRỰC QUAN HÓA VÀ LƯU KẾT QUẢ ===")
sns.set_style("whitegrid")
plt.figure(figsize=(10, 5))

# Vẽ biểu đồ doanh thu theo khu vực so sánh với Target
sns.barplot(
    x="Region",
    y="Actual Sales",
    data=region_performance,
    palette="Blues_d",
    hue="Region",
    legend=False,
)
plt.title(
    "So sánh Doanh thu thực tế (Actual Sales) theo Khu vực",
    fontsize=13,
    fontweight="bold",
)
plt.xlabel("Khu vực (Region)")
plt.ylabel("Doanh thu (USD)")

plt.tight_layout()
chart_path = "15_region_sales_performance.png"
plt.savefig(chart_path, dpi=150, bbox_inches="tight")
plt.show()
print(f"- Đã lưu biểu đồ thành công tại: {chart_path}")

# Lưu file kết quả gộp ra thư mục data/processed hoặc thư mục hiện tại
output_dir = "../data/processed"
if not os.path.exists(output_dir):
  os.makedirs(output_dir, exist_ok=True)
output_csv = os.path.join(output_dir, "train_merged_complete.csv")
df_merged.to_csv(output_csv, index=False)
print(f"- Đã lưu file dữ liệu gộp thành công tại: {output_csv}")

# Hỗ trợ tự động tải về nếu chạy trên Google Colab
try:
  from google.colab import files

  files.download(chart_path)
  files.download(output_csv)
  print("\n=> Đã tự động kích hoạt tải file về máy thành công qua Colab!")
except:
  pass
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
