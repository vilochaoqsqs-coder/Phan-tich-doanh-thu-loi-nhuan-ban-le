# Báo cáo Đề xuất Hành động Chiến lược (Prescriptive Analysis — Slide Defense)

> **Mục tiêu**: Tổng hợp xuyên suốt kết quả từ **Descriptive (EDA & Merge)**, **Diagnostic (Outlier & Kiểm định Thống kê)** và **Predictive (Linear Regression)** để đưa ra 5 khuyến nghị hành động cụ thể, có định lượng dẫn chứng và ma trận ưu tiên hóa (Impact vs. Effort) sẵn sàng đưa vào Slide bảo vệ đồ án (Defense).

---

## 1. Tóm tắt 4 Insight Cốt lõi từ Dữ liệu & Mô hình

1. **Quy luật Tập trung Pareto & Ngành hàng (Descriptive + Predictive)**:
   - Tổng doanh thu tập dữ liệu sạch ($9,789$ dòng đơn) đạt **`$2,252,607.41`**. Top $25\%$ giao dịch lớn nhất ($\ge \$210.39$) chiếm tới **$83.28\%$ tổng doanh thu** (`$1,875,912.29`); riêng $1,141$ đơn hàng Outlier ($\ge \$500.11$, chiếm $11.66\%$ số đơn) đóng góp **$64.23\%$ doanh thu** (`$1,446,753.57`).
   - Hai ngành hàng `Technology` (`$827,426.47` — Mean `$456.39`/đơn) và `Furniture` (`$723,538.48` — Mean `$348.53`/đơn) tạo ra **$68.85\%$ tổng doanh thu** dù chỉ chiếm $39.70\%$ số lượng đơn. Ngược lại, `Office Supplies` chiếm tới **$60.30\%$ tổng số đơn** (`5,903` đơn) nhưng trung vị chỉ đạt **`$27.36`/đơn**.
   - Trong mô hình **Linear Regression ($R^2 = 0.4463$)**, các biến kéo doanh thu đơn hàng tăng mạnh nhất là `Sub-Category_Copiers` ($\beta = +2.291$), `Machines` ($\beta = +1.680$), `Tables` ($\beta = +1.340$), `Chairs` ($\beta = +1.123$) và sức mua lịch sử của khách hàng `Log_Cust_Mean_Sales` ($\beta = +0.336$); trong khi `Fasteners` ($\beta = -2.160$), `Labels` ($\beta = -1.791$), `Art` ($\beta = -1.722$) và `Binders` ($\beta = -1.454$) kéo giảm mạnh giá trị giỏ hàng.

2. **Sự phân hóa Khu vực & Điểm nghẽn Hoàn trả hàng (Diagnostic + Merge)**:
   - Kiểm định **One-way ANOVA trên `Log_Sales`** ($F = 8.72, p = 8.99 \times 10^{-6}$) và **Kruskal-Wallis** ($H = 25.18, p = 1.42 \times 10^{-5}$) khẳng định sự chênh lệch giá trị đơn hàng giữa 4 vùng có ý nghĩa thống kê: khu vực `Central` có trung vị đơn thấp nhất toàn quốc (**`$45.94`** vs **`$61.00`** tại `West`, Welch's t-test $p = 5.56 \times 10^{-7}$).
   - Kết quả Merge với bảng trả hàng (`returns.csv`) phát hiện toàn hệ thống có **`818/9,789` đơn bị hoàn trả ($8.36\%$)**, làm thất thoát **`$202,116.72`** doanh thu — lớn hơn tổng số tiền thiếu hụt KPI của cả 4 khu vực cộng lại (`$77,392.59`)! Trong đó khu vực `West` mất nhiều doanh thu hoàn trả nhất (`$69,154.68`, trong khi chỉ thiếu `$39,780.32` để đạt $100\%$ Target `$750,000`), còn `South` ($9.26\%$) và `Central` ($9.13\%$) có tỷ lệ đơn trả cao nhất.

3. **Nghịch lý Phân khúc Khách hàng `Segment` (Statistical Testing)**:
   - Dù phân khúc `Consumer` chiếm $50.92\%$ tổng doanh thu (`$1,146,708.15`), kiểm định **ANOVA** ($F = 0.20, p = 0.8150 > 0.05$) và **Kruskal-Wallis** ($H = 0.40, p = 0.8176 > 0.05$) chứng minh giá trị trung bình và trung vị mỗi đơn hàng giữa `Consumer` (Med `$53.98`), `Corporate` (Med `$56.30`) và `Home Office` (Med `$52.44`) **không có sự khác biệt có ý nghĩa thống kê**. Khách hàng doanh nghiệp hiện đang mua lẻ từng đơn nhỏ giống hệt khách hàng cá nhân.

4. **Tính Mùa vụ Đỉnh – Đáy rõ rệt (Time-series EDA)**:
   - Doanh thu Quý 4 (Tháng 9, 11, 12) chiếm tới **$37.9\%$ tổng doanh thu cả năm** (đỉnh Tháng 11 đạt `$345,028.19` và Tháng 12 đạt `$321,480.17`), trong khi Tháng 2 rơi xuống đáy `$59,371.12` (thấp hơn $82.8\%$ so với Tháng 11).

---

## 2. Năm Khuyến nghị Hành động Cụ thể (Prescriptive Recommendations)

| Mã Đề xuất | Trụ cột Chiến lược | Khuyến nghị Hành động Cụ thể | Dẫn chứng Dữ liệu & Mô hình | KPI Mục tiêu (Định lượng) | Impact | Effort | Nhóm Ưu tiên |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **REC-01** | **Sản phẩm & Giỏ hàng (Cross-sell / Bundling)** | Đóng gói Combo giữa `Office Supplies` với `Technology`/`Furniture`; dừng bán lẻ đơn chiếc nhóm `Fasteners`/`Labels` dưới `$15`; áp dụng ngưỡng **Free-Shipping từ `$75`** tại vùng `Central`. | `Office Supplies` chiếm $60.3\%$ số đơn nhưng Med chỉ `$27.36`; `Fasteners` ($\beta=-2.16$), `Labels` ($\beta=-1.79$) kéo giảm `Log_Sales`. Trung vị đơn tại `Central` thấp nhất (`$45.94`, $p = 5.56 \times 10^{-7}$). | Nâng trung vị đơn tại `Central` từ `$45.94` lên **`$58.00` (+26%)**, giúp `Central` vượt $107\%$ Target `$500K`. | **High** (9.5) | **Low** (2.2) | **P1 — Quick Wins** |
| **REC-02** | **Khách hàng VIP & Ngành hàng Mũi nhọn** | Thiết lập chương trình **VIP Account Management** cho Top $20\%$ khách có `Cust_Mean_Sales >= $350`; ưu đãi nâng cấp giao hàng nhanh & lắp đặt cho đơn `Copiers`, `Machines`, `Chairs`, `Tables`. | Top $25\%$ đơn đóng góp $83.28\%$ doanh thu; $11.66\%$ đơn Outlier ($\ge \$500.11$) chiếm $63.15\%$ doanh thu (`$1.423M`). `Copiers` ($\beta=+2.29$), `Machines` ($\beta=+1.68$), `Log_Cust_Mean_Sales` ($\beta=+0.34$) dẫn đầu mô hình hồi quy. | Tăng $15\%$ tỷ lệ giữ chân khách VIP; tăng doanh thu `Technology` & `Furniture` thêm **8–10% (`+$120K/năm`)**. | **High** (9.0) | **Low** (2.6) | **P1 — Quick Wins** |
| **REC-03** | **Chiến lược Giá B2B (`Segment`)** | Thiết lập **Biểu giá chiết khấu bậc thang theo quy mô đơn (Tiered Volume Discount)** và hợp đồng cung ứng theo Quý cho phân khúc `Corporate` & `Home Office` (giảm $5\%$ đơn $\ge \$500$, giảm $10\%$ đơn $\ge \$1,200$). | Kiểm định ANOVA ($p = 0.8150$) chỉ ra khách hàng doanh nghiệp `Corporate` (Med `$56.30`) và `Home Office` (Med `$52.44`) đang đặt đơn nhỏ ngang khách lẻ `Consumer` (Med `$53.98`). | Nâng giá trị giỏ hàng trung bình (AOV) khối B2B từ `~$235` lên **`~$285` (+21%)**. | **High** (8.4) | **Low** (3.0) | **P1 — Quick Wins** |
| **REC-04** | **Vận hành & Kiểm soát Hoàn trả (`Returns`)** | Chuẩn hóa quy trình đóng gói chống sốc 2 lớp cho nhóm `Furniture` và xác nhận kỹ thuật trước khi giao `Technology` ở kênh `Standard Class` tại cả 4 vùng (`West`, `South`, `Central`, `East`). | Toàn chuỗi có `818` đơn hoàn trả ($8.36\%$), làm mất **`$202,116.72`** doanh thu (riêng `West` mất `$69,154.68` khi chỉ thiếu `$39,780` để đạt Target `$750K`; tỷ lệ trả tại `South` $9.26\%$ và `Central` $9.13\%$). | Giảm tỷ lệ hoàn trả toàn chuỗi từ $8.36\%$ xuống **$<4.5\%$**, thu hồi **`+$95,000/năm`**, đưa cả 4 vùng vượt $100\%$ Target. | **High** (9.1) | **High** (6.6) | **P2 — Major Projects** |
| **REC-05** | **Tồn kho Mùa vụ & Mở rộng vùng `South`** | Tăng $40\%$ tồn kho an toàn (Safety Stock) từ cuối Tháng 8 cho Top 5 tiểu mục (`Phones`, `Chairs`, `Storage`, `Tables`, `Binders`); tăng $30\%$ ngân sách thu hút khách mới tại vùng `South`; tung gói kích cầu Quý 1. | Quý 4 chiếm $37.9\%$ doanh thu năm (T11 đạt `$345.0K` vs T2 `$59.4K`). Vùng `South` có Mean đơn cao nhất (`$243.52`, $\beta=+0.188$) nhưng số đơn ít nhất (`1,598` đơn). | Tăng $15\%$ số lượng đơn tại `South` (`+240` đơn $pprox$ **`+$58,000`**); tăng doanh thu Quý 1 thêm **$20\%$**. | **Medium-High** (8.1) | **Medium** (5.8) | **P2 — Major Projects** |

---

## 3. Lộ trình Triển khai Đề xuất trên Slide Defense (Implementation Roadmap)

- **Giai đoạn 1 — Quick Wins (Tháng 1 – Tháng 3)**:
  - Triển khai ngay **REC-01** (Bundling văn phòng phẩm + Ngưỡng Free-ship `$75` tại `Central`), **REC-02** (Chăm sóc VIP Top $20\%$ khách hàng có `Cust_Mean_Sales` cao) và **REC-03** (Biểu giá chiết khấu sỉ B2B cho `Corporate` & `Home Office`). Không tốn chi phí hạ tầng, tác động trực tiếp vào AOV và tỷ lệ mua lặp lại.
- **Giai đoạn 2 — Tối ưu Vận hành & Mở rộng (Tháng 4 – Tháng 8)**:
  - Thực hiện **REC-04** (Chuẩn hóa đóng gói & giảm $50\%$ đơn hoàn trả) và chuẩn bị tồn kho theo **REC-05** trước ngày 25/08 để sẵn sàng đón đỉnh doanh thu Quý 4 (Tháng 9 – Tháng 12).
