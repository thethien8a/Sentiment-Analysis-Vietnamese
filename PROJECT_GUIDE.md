# Hướng Dẫn Dự Án: Sentiment Analysis Cho Bình Luận Bài Hát Việt Nam Trên YouTube

## Giới Thiệu Tổng Quan

### Sentiment Analysis Là Gì?
Sentiment Analysis (Phân tích tình cảm) là kỹ thuật trong xử lý ngôn ngữ tự nhiên (NLP) để xác định cảm xúc trong văn bản. Với bài toán này, chúng ta sẽ phân loại bình luận YouTube thành:
- **Tích cực (Positive)**: "Bài hát hay quá!", "Nghe hoài không chán"
- **Tiêu cực (Negative)**: "Bài này dở", "Không hay như mong đợi"  
- **Trung lập (Neutral)**: "Bình thường", "Tạm được"

### Tại Sao Cần Sentiment Analysis Cho Bài Hát?
- Đánh giá nhanh phản hồi của khán giả mà không cần đọc hàng nghìn bình luận
- Giúp ca sĩ/nhà sản xuất hiểu được ý kiến người nghe
- Phân tích xu hướng âm nhạc được yêu thích

### Quy Trình Tổng Thể
```
Thu thập bình luận → Làm sạch dữ liệu → Gắn nhãn mẫu → Fine-tune mô hình → Dự đoán toàn bộ → Kết luận
```

### Yêu Cầu Kỹ Năng Tối Thiểu
- Biết sử dụng máy tính cơ bản
- Có thể cài đặt phần mềm theo hướng dẫn
- Hiểu biết cơ bản về Excel để gắn nhãn dữ liệu
- Không cần biết lập trình sâu (chỉ cần chạy theo hướng dẫn)

### Thời Gian Ước Tính
- Thiết lập môi trường: 30-60 phút
- Thu thập và làm sạch dữ liệu: 2-4 giờ
- Gắn nhãn thủ công: 2-3 giờ
- Fine-tune mô hình: 1-2 giờ
- Dự đoán và phân tích: 30 phút
- **Tổng cộng**: 1-2 ngày làm việc

---

## Thuật Ngữ Quan Trọng (Giải Thích Đơn Giản)

- **Pre-trained Model**: Mô hình đã được huấn luyện sẵn trên dữ liệu lớn. Giống như mua xe đã lắp ráp sẵn thay vì tự chế tạo từ đầu.
- **Fine-tuning**: Điều chỉnh mô hình cho phù hợp với dữ liệu của bạn. Như việc chỉnh ghế lái cho vừa với người sử dụng.
- **PhoBERT**: Mô hình AI được thiết kế riêng cho tiếng Việt, hiểu được ngữ cảnh và từ ghép tiếng Việt.
- **Tokenization**: Chia văn bản thành các đơn vị nhỏ mà máy tính có thể hiểu. Ví dụ: "ăn cơm" → ["ăn_cơm"].
- **Dataset**: Tập dữ liệu, trong trường hợp này là file chứa bình luận YouTube.
- **Label/Nhãn**: Đánh dấu bình luận là tích cực, tiêu cực hay trung lập.

---

Hướng dẫn này cung cấp lộ trình chi tiết, từng bước để thực hiện phân tích tình cảm (sentiment analysis) trên bình luận YouTube cho bài hát Việt Nam. Mục tiêu là tự động gắn nhãn bình luận là Tích cực (Positive), Tiêu cực (Negative), hoặc Trung lập (Neutral), sau đó tổng hợp kết quả để xác định bài hát có được yêu thích hay không. Chúng ta sử dụng mô hình pre-trained (PhoBERT) và fine-tune trên dữ liệu cụ thể của bạn để tăng độ chính xác, mà không cần train từ đầu.

**Giả Định**:
- Python 3.7+ đã cài đặt.
- Tập dữ liệu: File CSV với bình luận YouTube (cột: "comment").
- Phần cứng: CPU/GPU (khuyến nghị Google Colab cho GPU miễn phí).
- Nhãn: 3 lớp (Positive=2, Neutral=1, Negative=0). Điều chỉnh nếu cần.

**Công Cụ/Thư Viện**:
- Hugging Face Transformers (cho PhoBERT).
- underthesea hoặc VnCoreNLP (cho tiền xử lý tiếng Việt).
- pandas, scikit-learn, datasets (cho xử lý dữ liệu/đánh giá).

---

## Bước 1: Thiết Lập Môi Trường
Chuẩn bị công cụ và môi trường để đảm bảo thực hiện suôn sẻ.

### ✅ Checklist Bước 1:
- [ ] Tạo thư mục dự án youtube-sentiment
- [ ] Cài đặt Python (nếu chưa có)
- [ ] Cài đặt các thư viện cần thiết
- [ ] Tải PhoBERT (tùy chọn)
- [ ] Thiết lập Google Colab (nếu cần)

1. **Tạo Thư Mục Dự Án**:
   - Mở thư mục làm việc của bạn (workspace) tại đường dẫn `/d:/Practice/Machine Learning Project/Sentiment-Analysis-Vietnamese`. Tạo một thư mục con mới tên là `youtube-sentiment` để chứa tất cả file liên quan đến dự án này. Thư mục này sẽ giúp tổ chức code, dữ liệu và kết quả một cách gọn gàng.

2. **Cài Đặt Các Gói Phụ Thuộc**:
   - Mở terminal (hoặc command prompt trên Windows) và chạy lệnh cài đặt các thư viện cần thiết. Các thư viện này bao gồm transformers cho mô hình PhoBERT, torch cho tính toán, pandas cho xử lý dữ liệu, scikit-learn cho đánh giá, underthesea cho tiền xử lý tiếng Việt, datasets cho tải dữ liệu, tqdm cho hiển thị tiến độ, và vncorenlp cho phân đoạn từ thay thế. Lệnh cài đặt là: pip install transformers torch pandas scikit-learn underthesea datasets tqdm vncorenlp. Nếu bạn dùng Google Colab, mở một notebook mới và chạy lệnh này trong cell.
   - Tiếp theo, cài đặt VnCoreNLP cho việc phân đoạn từ (nếu không dùng underthesea). Tạo thư mục vncorenlp/models/wordsegmenter, sau đó tải các file cần thiết từ GitHub của VnCoreNLP và lưu vào thư mục đó. Các file bao gồm VnCoreNLP-1.1.1.jar, vi-vocab, và wordsegmenter.rdr.

3. **Tải Pre-trained PhoBERT**:
   - Mô hình PhoBERT sẽ tự động tải khi chạy code, nhưng nếu bạn muốn tải thủ công để dùng offline, hãy tải file PhoBERT_base_transformers.tar.gz từ trang public.vinai.io, sau đó giải nén vào thư mục pretrained trong dự án của bạn.

4. **(Tùy Chọn) Thiết Lập Google Colab**:
   - Nếu máy tính của bạn không có GPU mạnh, hãy sử dụng Google Colab. Mở trình duyệt, truy cập colab.research.google.com, tạo notebook mới. Để kết nối với Google Drive (nơi lưu dữ liệu), thêm lệnh mount Drive vào cell đầu tiên. Colab cung cấp GPU miễn phí, giúp fine-tune nhanh hơn.

### Kiểm Tra Kết Quả Bước 1:
- Mở terminal, gõ `python --version` để kiểm tra Python đã cài đặt
- Gõ `pip list` để xem các thư viện đã cài
- Thư mục dự án đã được tạo và sẵn sàng

### ⚠️ Lỗi Thường Gặp:
- **Lỗi "pip not found"**: Cài đặt lại Python và chọn "Add to PATH"
- **Lỗi khi cài thư viện**: Chạy terminal với quyền Administrator
- **Máy yếu/chậm**: Chuyển sang dùng Google Colab

---

## Bước 2: Thu Thập Và Tiền Xử Lý Dữ Liệu
Thu thập bình luận thô và làm sạch để xử lý đặc thù tiếng Việt và nhiễu YouTube. Bước này rất quan trọng vì dữ liệu thô thường có lỗi chính tả, emoji, và từ ghép tiếng Việt cần phân đoạn.

### 🔄 Quy Trình Chia File Dữ Liệu (Quan Trọng!)

**Từ 1 file gốc → 3 file cuối cùng:**

```
File gốc: raw_comments.csv (tất cả bình luận)
    ↓
Bước 1: Chọn một phần nhỏ để gắn nhãn thủ công (500-2000 bình luận)
    ↓
Bước 2: Chia phần đã gắn nhãn thành train (80%) và test (20%)
    ↓
Bước 3: Phần còn lại (chưa gắn nhãn) dùng để dự đoán sau này

KẾT QUẢ CUỐI CÙNG:
📁 train_labeled.csv (400-1600 bình luận có nhãn) → Để train model
📁 test_labeled.csv (100-400 bình luận có nhãn) → Để kiểm tra model
📁 preprocessed_data.csv (phần lớn bình luận chưa có nhãn) → Để dự đoán
```

**Ví dụ cụ thể:**
- Bạn có 10,000 bình luận từ YouTube
- Chọn 1,000 bình luận để gắn nhãn thủ công
- Chia 1,000 này thành: 800 train + 200 test
- 9,000 bình luận còn lại để dự đoán sau

### ✅ Checklist Bước 2:
- [ ] Thu thập bình luận từ video YouTube
- [ ] Lưu vào file raw_comments.csv
- [ ] **Chọn một phần nhỏ (500-2000 bình luận) để gắn nhãn thủ công**
- [ ] **Chia phần đã gắn nhãn thành train (80%) và test (20%)**
- [ ] **Làm sạch tất cả dữ liệu (cả phần có nhãn và chưa có nhãn)**
- [ ] **Lưu thành 3 file: train_labeled.csv, test_labeled.csv, preprocessed_data.csv**

### Các Bước Chi Tiết:

1. **Thu Thập Bình Luận**:
   - Sử dụng API của YouTube hoặc thư viện youtube-comment-downloader để lấy bình luận từ video. Đầu tiên, cài thư viện nếu chưa có (pip install youtube-comment-downloader). Sau đó, tạo một script Python để tải bình luận từ URL video (thay VIDEO_ID bằng ID thực tế của video). Lưu kết quả vào file raw_comments.csv với cột 'text' chứa nội dung bình luận. Đảm bảo tuân thủ điều khoản dịch vụ của YouTube để tránh vi phạm.

2. **Gắn Nhãn Thủ Công Cho Fine-Tuning**:
   - **🎯 MỤC ĐÍCH**: Tạo dữ liệu mẫu để dạy model hiểu cách phân loại
   - **CÁCH LÀM**: 
     - Mở file raw_comments.csv trong Excel hoặc Google Sheets
     - Chọn ngẫu nhiên 500-2000 bình luận (không cần nhiều hơn)
     - Thêm cột 'label' bên cạnh cột 'text'
     - Gắn nhãn: 0 = Tiêu cực, 1 = Trung lập, 2 = Tích cực
     - Lưu phần đã gắn nhãn thành file riêng tên labeled_comments.csv
   - **LƯU Ý**: Chỉ gắn nhãn một phần nhỏ, không phải toàn bộ!

3. **Chia Train/Test Set**:
   - **🎯 MỤC ĐÍCH**: Chia dữ liệu đã gắn nhãn để train và kiểm tra model
   - **CÁCH LÀM**:
     - Mở file labeled_comments.csv
     - Chia ngẫu nhiên: 80% đầu → train_labeled.csv, 20% cuối → test_labeled.csv
     - Hoặc dùng công thức Excel: =RAND() để trộn ngẫu nhiên rồi chia
   - **VÍ DỤ**: 1000 bình luận có nhãn → 800 train + 200 test

4. **Tiền Xử Lý Toàn Bộ Dữ Liệu**:
   - **🎯 MỤC ĐÍCH**: Làm sạch tất cả bình luận (cả có nhãn và chưa có nhãn)
   - **CÁCH LÀM**:
     - Áp dụng quy trình làm sạch cho tất cả file:
       - Chuẩn hóa Unicode (NFC)
       - Chuyển về chữ thường
       - Loại bỏ URL, mention (@), số, emoji, dấu câu
       - Loại bỏ khoảng trắng thừa
       - Phân đoạn từ bằng underthesea hoặc VnCoreNLP
     - Lọc bỏ bình luận quá ngắn (< 5 từ) hoặc trùng lặp
   - **KẾT QUẢ**: Tất cả file đều có thêm cột 'cleaned'

5. **Lưu File Cuối Cùng**:
   - **train_labeled.csv**: Dữ liệu train đã sạch, có cột 'text', 'cleaned', 'label'
   - **test_labeled.csv**: Dữ liệu test đã sạch, có cột 'text', 'cleaned', 'label'
   - **preprocessed_data.csv**: Tất cả bình luận đã sạch, có cột 'text', 'cleaned' (không có 'label')

### Ví Dụ Cấu Trúc File:

**train_labeled.csv:**
```
text,cleaned,label
"Bài hát hay quá!!!","bài hát hay quá",2
"Dở tệ","dở tệ",0
"Bình thường thôi","bình thường thôi",1
```

**test_labeled.csv:**
```
text,cleaned,label
"Tuyệt vời","tuyệt vời",2
"Không thích","không thích",0
```

**preprocessed_data.csv:**
```
text,cleaned
"Nghe cả ngày không chán","nghe cả ngày không chán"
"Không hay lắm","không hay lắm"
"Bài này ổn","bài này ổn"
```

### Ví Dụ Gắn Nhãn:
| Bình luận | Nhãn | Giải thích |
|-----------|------|------------|
| "Bài hát tuyệt vời, nghe hoài không chán" | 2 (Positive) | Thể hiện sự yêu thích |
| "Hát dở quá, phí thời gian" | 0 (Negative) | Thể hiện không thích |
| "Bình thường, không có gì đặc biệt" | 1 (Neutral) | Không thiên về hướng nào |

### Kiểm Tra Kết Quả Bước 2:
- [ ] File raw_comments.csv có ít nhất 1000 bình luận
- [ ] File train_labeled.csv có 400-1600 bình luận với nhãn
- [ ] File test_labeled.csv có 100-400 bình luận với nhãn  
- [ ] File preprocessed_data.csv có phần lớn bình luận chưa có nhãn
- [ ] Tất cả file đều có cột 'cleaned' không còn emoji, URL, ký tự lạ
- [ ] Tỷ lệ train:test xấp xỉ 80:20

### ⚠️ Lỗi Thường Gặp:
- **Nhầm lẫn về số lượng file**: Nhớ là 3 file cuối cùng, không phải chia toàn bộ dữ liệu
- **Gắn nhãn quá nhiều**: Chỉ cần 500-2000 bình luận, không cần gắn nhãn hết
- **Không tải được bình luận**: Kiểm tra kết nối mạng, thử video khác
- **File CSV lỗi**: Mở bằng Excel, kiểm tra encoding UTF-8
- **Gắn nhãn sai**: Đọc kỹ hướng dẫn, nhờ người khác kiểm tra chéo

### 💡 Mẹo Quan Trọng:
- **Chọn bình luận đa dạng**: Đừng chỉ chọn bình luận tích cực, hãy cân bằng 3 loại
- **Gắn nhãn nhất quán**: Cùng một người gắn nhãn để đảm bảo tiêu chuẩn thống nhất
- **Backup dữ liệu**: Lưu bản sao file gốc trước khi xử lý 