# Phân Tích Doanh Thu và Lợi Nhuận Bán Lẻ (Superstore)

## 1. Giới thiệu dự án

Dự án thực hiện phân tích dữ liệu bán lẻ của chuỗi Superstore nhằm:
- Khám phá các yếu tố ảnh hưởng đến doanh thu (danh mục sản phẩm, phân khúc khách hàng, khu vực, thời gian...).
- Phân tích xu hướng doanh thu theo thời gian và phát hiện các điểm bất thường (outliers).
- Kiểm định giả thuyết thống kê, xây dựng mô hình hồi quy dự đoán và đề xuất các insight hỗ trợ quyết định kinh doanh.

- **Môn học:** Khoa học Dữ liệu
- **Đề tài:** Phân tích doanh thu và lợi nhuận bán lẻ (Đề tài số 9)

---

## 2. Cấu trúc thư mục dự án

```text
Phan-tich-doanh-thu-loi-nhuan-ban-le/
├── data/
│   ├── raw/                                     # Dữ liệu gốc ban đầu (train.csv, returns.csv, region_managers.csv)
│   └── processed/                               # Dữ liệu đã làm sạch (superstore_cleaned.csv)
├── notebooks/                                   # Các notebook phân tích theo thứ tự thực hiện
│   ├── 01_doc_va_kham_pha_du_lieu.ipynb         # Đọc dữ liệu và khám phá cấu trúc ban đầu
│   ├── 02_eda_phan_tich_kham_pha.ipynb          # Phân tích khám phá dữ liệu (EDA) và trực quan hóa
│   ├── 03_xu_ly_outlier.ipynb                   # Phát hiện và xử lý giá trị ngoại lai (IQR, Log transform)
│   ├── 04_diagnostic_va_hoan_thien.ipynb        # Phân tích chẩn đoán, làm sạch và xuất dữ liệu chuẩn
│   ├── 05_merge_du_lieu.ipynb                   # Kết hợp dữ liệu đơn hàng với dữ liệu trả hàng & quản lý khu vực
│   ├── 06_prescriptive_analysis.ipynb           # Phân tích đề xuất giải pháp kinh doanh
│   ├── 07_hoi_quy_tuyen_tinh.ipynb              # Xây dựng và đánh giá mô hình hồi quy tuyến tính
│   └── 08_kiem_dinh_thong_ke.ipynb              # Kiểm định giả thuyết thống kê
├── reports/                                     # Kết quả đầu ra từ quá trình phân tích
│   ├── figures/                                 # Biểu đồ trực quan xuất ra từ các notebook
│   ├── business_recommendations_final.csv       # Tổng hợp khuyến nghị kinh doanh
│   ├── hypothesis_testing_summary.csv           # Bảng tóm tắt kết quả kiểm định thống kê
│   ├── prescriptive_recommendations_*.csv       # Chi tiết các đề xuất tối ưu
│   ├── regression_coefficients.csv              # Hệ số của mô hình hồi quy
│   └── regression_metrics.csv                   # Chỉ số đánh giá độ chính xác mô hình (R2, MAE, RMSE)
├── requirements.txt                             # Danh sách thư viện Python cần thiết
└── README.md                                    # Tài liệu hướng dẫn cài đặt và chạy dự án
```

---

## 3. Nguồn dữ liệu

- **Tên dataset:** Superstore Sales (Sales Forecasting)
- **Nguồn:** [Kaggle - rohitsahoo/sales-forecasting](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)
- **Mô tả:** Dữ liệu giao dịch bán lẻ bao gồm thông tin đơn hàng, thời gian giao vận, khách hàng, khu vực, danh mục sản phẩm và doanh thu (kèm dữ liệu trả hàng và quản lý khu vực).
- **Kích thước:** 9.800 dòng, 18 cột (sau khi làm sạch giá trị thiếu ở cột `Postal Code` còn 9.789 dòng).

---

## 4. Cách chạy dự án từ đầu (Reproduce)

### Bước 1: Clone repository

```bash
git clone https://github.com/vilochaoqsqs-coder/Phan-tich-doanh-thu-loi-nhuan-ban-le.git
cd Phan-tich-doanh-thu-loi-nhuan-ban-le
```

### Bước 2: Cài đặt môi trường ảo và thư viện

**Trên Windows (Command Prompt / PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Trên macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Bước 3: Thứ tự chạy các Notebook và luồng dữ liệu

Mở các file trong thư mục `notebooks/` bằng VS Code hoặc Jupyter Notebook và chạy lần lượt theo thứ tự từ `01` đến `08`:

1. **`01_doc_va_kham_pha_du_lieu.ipynb`**
   - **Mô tả:** Kiểm tra kích thước, kiểu dữ liệu, thống kê mô tả và phát hiện giá trị thiếu ban đầu.
   - **Đầu vào:** `data/raw/train.csv` *(Lưu ý: cần đảm bảo đường dẫn đọc file trỏ tới `../data/raw/train.csv`)*.
   - **Đầu ra:** Báo cáo tổng quan dữ liệu hiển thị trực tiếp trong notebook.

2. **`02_eda_phan_tich_kham_pha.ipynb`**
   - **Mô tả:** Làm sạch sơ bộ, trích xuất đặc trưng thời gian (`Year`, `Month`, `Quarter`, `DayOfWeek`) và trực quan hóa xu hướng doanh thu.
   - **Đầu vào:** `data/raw/train.csv`
   - **Đầu ra:** Biểu đồ phân tích EDA.

3. **`03_xu_ly_outlier.ipynb`**
   - **Mô tả:** Phát hiện ngoại lai trên biến `Sales` bằng phương pháp IQR và xử lý bằng biến đổi Log (`Log_Sales`) & IQR Capping.
   - **Đầu vào:** `data/raw/train.csv`
   - **Đầu ra:** Biểu đồ phân phối trước và sau khi xử lý outlier.

4. **`04_diagnostic_va_hoan_thien.ipynb`** *(Bắt buộc chạy trước Notebook 08)*
   - **Mô tả:** Thực hiện phân tích chẩn đoán, hoàn thiện làm sạch dữ liệu và tự động tạo thư mục lưu trữ kết quả.
   - **Đầu vào:** `data/raw/train.csv`
   - **Đầu ra:** `data/processed/superstore_cleaned.csv` và các biểu đồ lưu tại `reports/figures/`.

5. **`05_merge_du_lieu.ipynb`**
   - **Mô tả:** Ghép nối (merge) dữ liệu đơn hàng với dữ liệu hoàn trả và thông tin quản lý từng khu vực.
   - **Đầu vào:** `data/raw/train.csv`, `data/raw/returns.csv`, `data/raw/region_managers.csv`
   - **Đầu ra:** Bảng dữ liệu tổng hợp phục vụ phân tích tỷ lệ trả hàng và hiệu suất khu vực.

6. **`06_prescriptive_analysis.ipynb`**
   - **Mô tả:** Phân tích đề xuất (Prescriptive Analytics) nhằm tối ưu danh mục sản phẩm, khu vực và chiến lược bán hàng.
   - **Đầu vào:** `data/raw/train.csv` (hoặc `data/processed/superstore_cleaned.csv`)
   - **Đầu ra:** `reports/business_recommendations_final.csv`, `reports/prescriptive_recommendations_*.csv`

7. **`07_hoi_quy_tuyen_tinh.ipynb`**
   - **Mô tả:** Tiền xử lý biến phân loại (`OneHotEncoder`) và huấn luyện mô hình hồi quy tuyến tính (`LinearRegression`) dự đoán doanh thu.
   - **Đầu vào:** Dữ liệu đã làm sạch từ `data/processed/` hoặc `data/raw/`
   - **Đầu ra:** `reports/regression_coefficients.csv`, `reports/regression_metrics.csv`

8. **`08_kiem_dinh_thong_ke.ipynb`**
   - **Mô tả:** Thực hiện các kiểm định giả thuyết thống kê với mức ý nghĩa $\alpha = 0.05$ và rút ra kết luận kinh doanh.
   - **Đầu vào:** `data/processed/superstore_cleaned.csv`
   - **Đầu ra:** `reports/hypothesis_testing_summary.csv`
