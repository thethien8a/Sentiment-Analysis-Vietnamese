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

### ✅ Checklist Bước 2:
- [ ] Thu thập bình luận từ video YouTube
- [ ] Lưu vào file raw_comments.csv
- [ ] Gắn nhãn 500-2000 bình luận mẫu
- [ ] Chia thành train/test set
- [ ] Làm sạch dữ liệu
- [ ] Lưu file preprocessed_data.csv

1. **Thu Thập Bình Luận**:
   - Sử dụng API của YouTube hoặc thư viện youtube-comment-downloader để lấy bình luận từ video. Đầu tiên, cài thư viện nếu chưa có (pip install youtube-comment-downloader). Sau đó, tạo một script Python để tải bình luận từ URL video (thay VIDEO_ID bằng ID thực tế của video). Lưu kết quả vào file raw_comments.csv với cột 'text' chứa nội dung bình luận. Đảm bảo tuân thủ điều khoản dịch vụ của YouTube để tránh vi phạm.

2. **Gắn Nhãn Thủ Công Cho Fine-Tuning**:
   - Chọn một phần dữ liệu (khoảng 500-2000 bình luận) từ raw_comments.csv và gắn nhãn thủ công bằng cách mở file trong Excel hoặc Google Sheets. Thêm cột 'label' với giá trị 0 cho Tiêu cực, 1 cho Trung lập, 2 cho Tích cực. Sau đó, chia file thành hai phần: 80% cho train (lưu thành train_labeled.csv) và 20% cho test (test_labeled.csv). Để tăng dữ liệu, bạn có thể tải dataset công khai như VLSP Sentiment từ Hugging Face và kết hợp.

3. **Tiền Xử Lý**:
   - Mở file raw_comments.csv trong Python sử dụng pandas. Tạo hàm preprocess để: Chuẩn hóa Unicode (NFC), chuyển về chữ thường, loại bỏ URL, mention, số, dấu câu bằng regex, loại bỏ khoảng trắng thừa, và phân đoạn từ bằng underthesea's word_tokenize (hoặc VnCoreNLP nếu dùng). Áp dụng hàm này cho cột 'text' để tạo cột 'cleaned'. Lọc bỏ bình luận ngắn (ít hơn 5 từ) hoặc trùng lặp. Lưu kết quả vào preprocessed_data.csv. Lặp lại cho file labeled nếu cần.

4. **Kết Quả**: Bạn sẽ có preprocessed_data.csv (dữ liệu sạch chưa gắn nhãn dùng cho suy luận), train_labeled.csv và test_labeled.csv (dữ liệu gắn nhãn cho fine-tune).

### Ví Dụ Gắn Nhãn:
| Bình luận | Nhãn | Giải thích |
|-----------|------|------------|
| "Bài hát tuyệt vời, nghe hoài không chán" | 2 (Positive) | Thể hiện sự yêu thích |
| "Hát dở quá, phí thời gian" | 0 (Negative) | Thể hiện không thích |
| "Bình thường, không có gì đặc biệt" | 1 (Neutral) | Không thiên về hướng nào |

### Kiểm Tra Kết Quả Bước 2:
- File raw_comments.csv có ít nhất 1000 bình luận
- File train_labeled.csv và test_labeled.csv đã được tạo
- Dữ liệu trong cột 'cleaned' không còn emoji, URL, ký tự lạ

### ⚠️ Lỗi Thường Gặp:
- **Không tải được bình luận**: Kiểm tra kết nối mạng, thử video khác
- **File CSV lỗi**: Mở bằng Excel, kiểm tra encoding UTF-8
- **Gắn nhãn sai**: Đọc kỹ hướng dẫn, nhờ người khác kiểm tra chéo

---

## Bước 3: Load Mô Hình Pre-trained
Load PhoBERT làm mô hình cơ sở. Bước này chuẩn bị mô hình đã được huấn luyện sẵn trên dữ liệu tiếng Việt lớn.

### ✅ Checklist Bước 3:
- [ ] Import thư viện transformers
- [ ] Load tokenizer từ PhoBERT
- [ ] Load model với 3 labels
- [ ] Kiểm tra model hoạt động

1. **Load Mô Hình/Tokenizer**:
   - Sử dụng thư viện transformers để tải AutoModelForSequenceClassification và AutoTokenizer từ mô hình "vinai/phobert-base". Đặt num_labels=3 để phù hợp với 3 lớp sentiment.

2. **Chuẩn Bị Dữ Liệu**:
   - Sử dụng thư viện datasets để tải dữ liệu từ CSV và áp dụng tokenizer để chuyển văn bản thành định dạng mô hình có thể hiểu (token IDs, attention masks).

### Kiểm Tra Kết Quả Bước 3:
- Model và tokenizer load thành công không báo lỗi
- Thử tokenize một câu mẫu để kiểm tra

### ⚠️ Lỗi Thường Gặp:
- **Lỗi kết nối khi tải model**: Kiểm tra internet, thử lại sau
- **Out of memory**: Dùng Google Colab hoặc giảm batch size

---

## Bước 4: Fine-Tune Mô Hình
Điều chỉnh PhoBERT cho dữ liệu YouTube của bạn (fine-tune, không train đầy đủ). Bước này giúp mô hình học đặc thù của bình luận bài hát, chỉ cần dữ liệu nhỏ và vài epochs.

### ✅ Checklist Bước 4:
- [ ] Load dataset từ CSV
- [ ] Tokenize toàn bộ dataset
- [ ] Thiết lập training arguments
- [ ] Chạy fine-tuning
- [ ] Lưu model đã train

1. **Load Và Tokenize Dataset**:
   - Tải dataset từ train_labeled.csv và test_labeled.csv bằng load_dataset. Tạo hàm tokenize để áp dụng tokenizer cho cột 'cleaned', với truncation và padding đến max_length=256. Áp dụng hàm này cho toàn bộ dataset theo batch.

2. **Thiết Lập Train**:
   - Sử dụng TrainingArguments để đặt tham số: thư mục output './results', 3 epochs, batch size 16 cho train và eval, đánh giá mỗi epoch, learning rate 2e-5, load mô hình tốt nhất cuối cùng dựa trên metric 'f1'. Tạo Trainer với mô hình, arguments, và dataset tokenized.

3. **Chạy Fine-Tune**:
   - Gọi trainer.train() để bắt đầu huấn luyện. Sau đó lưu mô hình vào './fine_tuned_phobert'. Nếu dữ liệu nhỏ, sử dụng 5-fold cross-validation để đánh giá ổn định hơn. Thời gian ước tính: 30-90 phút trên GPU cho 1k-5k mẫu.

### Theo Dõi Quá Trình Training:
- Loss giảm dần qua mỗi epoch là tốt
- Nếu loss tăng đột ngột, dừng lại kiểm tra
- Thời gian còn lại sẽ hiển thị trên progress bar

---

## Bước 5: Đánh Giá Mô Hình
Đo lường hiệu suất trên tập test để đảm bảo mô hình đáng tin cậy.

### ✅ Checklist Bước 5:
- [ ] Chạy prediction trên test set
- [ ] Tính các metrics
- [ ] Phân tích kết quả
- [ ] Quyết định có cần cải thiện không

1. **Tính Toán Metrics**:
   - Sử dụng trainer.predict trên tập test tokenized để lấy dự đoán. Tính classification_report và macro F1-score bằng scikit-learn để xem accuracy, precision, recall cho từng lớp (Negative, Neutral, Positive).

2. **Phân Tích**:
   - Mục tiêu là macro F1 >80%. Nếu thấp, thêm dữ liệu hoặc tăng epochs. Kiểm tra lỗi bằng cách xem các bình luận bị dự đoán sai (ví dụ: châm biếm thường bị nhầm), và điều chỉnh nếu cần.

### Đọc Hiểu Kết Quả:
- **Accuracy**: Tỷ lệ dự đoán đúng tổng thể
- **Precision**: Trong những cái model dự đoán positive, bao nhiêu % là đúng
- **Recall**: Trong những cái thực sự positive, model tìm được bao nhiêu %
- **F1-score**: Trung bình của precision và recall

---

## Bước 6: Suy Luận Và Tổng Hợp
Áp dụng mô hình cho toàn bộ dataset và kết luận độ yêu thích bài hát.

### ✅ Checklist Bước 6:
- [ ] Load model đã fine-tune
- [ ] Dự đoán cho toàn bộ bình luận
- [ ] Tính tỷ lệ positive/negative/neutral
- [ ] Đưa ra kết luận về bài hát

1. **Dự Đoán Tình Cảm**:
   - Tải file preprocessed_data.csv bằng pandas. Load mô hình fine-tune từ './fine_tuned_phobert' và tokenizer từ "vinai/phobert-base". Tạo hàm predict để tokenize văn bản từ cột 'cleaned' và dự đoán nhãn (Negative, Neutral, Positive). Áp dụng hàm cho toàn bộ cột để tạo cột 'sentiment' mới. Lưu kết quả vào labeled_comments.csv.

2. **Tổng Hợp Và Kết Luận**:
   - Tính tỷ lệ phần trăm bình luận Tích cực. Nếu >60%, kết luận bài hát "Được Yêu Thích"; ngược lại "Không Được Yêu Thích". In kết quả để xem.

### Cách Đọc Kết Quả Cuối Cùng:
- **>70% Positive**: Bài hát rất được yêu thích
- **60-70% Positive**: Bài hát được yêu thích
- **40-60% Positive**: Ý kiến trái chiều
- **<40% Positive**: Bài hát không được yêu thích

---

## Phương Án Thay Thế Cho Người Không Muốn Code

### 1. Sử Dụng Google Cloud AutoML
- Truy cập console.cloud.google.com
- Upload dữ liệu đã gắn nhãn
- Chọn "Sentiment Analysis" 
- Nhấn Train và đợi kết quả

### 2. Sử Dụng Dịch Vụ Online
- MonkeyLearn.com: Có giao diện kéo thả
- Aylien.com: Hỗ trợ tiếng Việt
- RapidAPI: Nhiều API sentiment analysis

### 3. Thuê Freelancer
- Đăng dự án trên Upwork/Fiverr
- Cung cấp dữ liệu và yêu cầu
- Chi phí: $50-200 tùy độ phức tạp

---

## FAQ - Câu Hỏi Thường Gặp

**Q: Tôi không biết lập trình, có làm được không?**
A: Được, hướng dẫn này viết cho người không biết code. Chỉ cần làm theo từng bước, copy và chạy lệnh.

**Q: Cần máy tính cấu hình như thế nào?**
A: Máy thông thường là được. Nếu yếu, dùng Google Colab miễn phí.

**Q: Độ chính xác khoảng bao nhiêu là tốt?**
A: Với bài toán này, 75-85% là tốt. Trên 85% là rất tốt.

**Q: Có thể phân tích bình luận tiếng Anh không?**
A: Được, nhưng cần đổi model sang BERT hoặc RoBERTa cho tiếng Anh.

**Q: Mất bao lâu để có kết quả?**
A: Nếu làm liên tục, khoảng 1-2 ngày có kết quả đầy đủ.

---

## Troubleshooting - Xử Lý Sự Cố

### Vấn Đề Về Dữ Liệu
- **Bình luận quá ít**: Tìm video phổ biến hơn, hoặc gộp nhiều video
- **Nhiều bình luận spam**: Lọc bình luận trùng lặp, quá ngắn
- **Bình luận không phải tiếng Việt**: Lọc hoặc dịch sang tiếng Việt

### Vấn Đề Về Model
- **Model dự đoán sai nhiều**: Tăng dữ liệu training, kiểm tra lại nhãn
- **Training quá lâu**: Giảm batch size, dùng GPU
- **Out of memory**: Giảm max_length, dùng model nhỏ hơn

### Vấn Đề Kỹ Thuật
- **Lỗi cài đặt thư viện**: Update pip, dùng virtual environment
- **Lỗi encoding tiếng Việt**: Lưu file với UTF-8
- **Không kết nối được internet**: Tải model offline trước

---

## Tổng Kết

Sau khi hoàn thành hướng dẫn này, bạn sẽ có:
1. Một mô hình AI có thể phân tích tình cảm bình luận tiếng Việt
2. File kết quả với nhãn sentiment cho từng bình luận
3. Kết luận về độ yêu thích của bài hát
4. Kiến thức cơ bản về NLP và sentiment analysis

Chúc bạn thành công! Nếu gặp khó khăn, đừng ngần ngại tìm kiếm trợ giúp từ cộng đồng hoặc thuê chuyên gia. 