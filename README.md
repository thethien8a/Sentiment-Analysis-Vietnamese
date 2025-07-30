# 🎯 Sentiment Analysis Vietnamese

Dự án phân tích cảm xúc (Sentiment Analysis) cho tiếng Việt, tập trung vào việc phân tích comment YouTube và các văn bản tiếng Việt trên mạng xã hội.

## 📋 Mục Tiêu Dự Án

- **Phân tích cảm xúc** comment YouTube tiếng Việt
- **Xử lý ngôn ngữ tự nhiên** cho tiếng Việt với các đặc thù như teencode, emoji
- **So sánh hiệu suất** giữa các mô hình ML truyền thống và transformer models
- **Xây dựng pipeline** hoàn chỉnh từ thu thập dữ liệu đến triển khai model

## 🏗️ Cấu Trúc Dự Án

```
Sentiment-Analysis-Vietnamese/
├── 📊 data.ipynb                           # Thu thập dữ liệu từ YouTube API
├── 🤖 phoBert.ipynb                        # Training và fine-tuning PhoBERT model
├── 🧠 Training_with_ML_Algorithm.ipynb     # Training các thuật toán ML truyền thống
├── 📈 MostWords.py                         # Phân tích từ vựng và tạo word cloud
├── 🔀 shuffle.py                           # Xáo trộn dữ liệu training
├── 📁 comment_data/                        # Thư mục chứa dữ liệu
│   ├── Tram_dung_chan_Jack.csv            # Dữ liệu comment gốc
│   └── Tram_dung_chan_Jack_shuffled.xlsx  # Dữ liệu đã xáo trộn
├── 📝 vietnamese-stopwords-dash.txt        # Danh sách stop words tiếng Việt
├── 📋 GIT_GUIDELINES.md                    # Hướng dẫn làm việc với Git
└── 📖 README.md                            # Tài liệu chính này
```

## 🔧 Các Tính Năng Chính

### 1. **Thu Thập Dữ Liệu** (`data.ipynb`)
- Sử dụng YouTube Data API v3 để thu thập comment
- Xử lý pagination và rate limiting
- Lưu trữ dữ liệu với metadata đầy đủ

### 2. **Tiền Xử Lý Dữ Liệu**
- **Chuẩn hóa teencode**: Chuyển đổi các từ viết tắt thành từ đầy đủ
- **Xử lý emoji**: Chuyển emoji thành text mô tả
- **Làm sạch text**: Loại bỏ URL, HTML tags, ký tự đặc biệt
- **Chuẩn hóa tiếng Việt**: Xử lý dấu tiếng Việt và ký tự đặc biệt

### 3. **Mô Hình PhoBERT** (`phoBert.ipynb`)
- Fine-tuning PhoBERT cho sentiment analysis
- Sử dụng GPU để tăng tốc training
- Đánh giá hiệu suất với các metrics: accuracy, F1-score
- Visualization kết quả training

### 4. **Thuật Toán ML Truyền Thống** (`Training_with_ML_Algorithm.ipynb`)
- **Logistic Regression**: Baseline model
- **Random Forest**: Ensemble method
- **SVM**: Support Vector Machine
- **Naive Bayes**: Probabilistic classifier
- **Voting Classifier**: Kết hợp nhiều model

### 5. **Phân Tích Từ Vựng** (`MostWords.py`)
- Tạo word cloud từ comment
- Phân tích tần suất từ vựng
- Visualization phân bố từ vựng theo sentiment

## 🚀 Cách Sử Dụng

### Yêu Cầu Hệ Thống
```bash
# Python 3.8+
pip install -r requirements.txt
```

### Cài Đặt Dependencies
```bash
pip install pandas numpy scikit-learn
pip install transformers torch
pip install matplotlib seaborn wordcloud
pip install underthesea
pip install google-api-python-client
pip install openpyxl
```

### Chạy Từng Bước

#### 1. Thu Thập Dữ Liệu
```bash
# Chạy notebook data.ipynb để thu thập comment YouTube
jupyter notebook data.ipynb
```

#### 2. Xử Lý Dữ Liệu
```bash
# Xáo trộn dữ liệu cho training
python shuffle.py

# Phân tích từ vựng
python MostWords.py
```

#### 3. Training Models
```bash
# Training PhoBERT model
jupyter notebook phoBert.ipynb

# Training ML algorithms
jupyter notebook Training_with_ML_Algorithm.ipynb
```

## 📊 Dữ Liệu

### Dataset
- **Nguồn**: Comment YouTube từ video "Trấm Đứng Chân Jack"
- **Kích thước**: ~5.8MB (CSV), ~3.6MB (Excel)
- **Cấu trúc**: 
  - `textDisplay`: Nội dung comment
  - `label`: Nhãn sentiment (positive/negative/neutral)
  - `authorDisplayName`: Tên người comment
  - `likeCount`: Số lượt like
  - `publishedAt`: Thời gian đăng

### Tiền Xử Lý
- **Teencode Dictionary**: 50+ từ viết tắt phổ biến
- **Emoji Dictionary**: 12+ emoji được chuyển thành text
- **Stop Words**: 1000+ từ dừng tiếng Việt
- **Text Cleaning**: Loại bỏ URL, HTML, ký tự đặc biệt

## 🎯 Kết Quả

### Model Performance
- **PhoBERT**: Accuracy cao nhất, phù hợp cho production
- **Random Forest**: Hiệu suất tốt, dễ interpret
- **Logistic Regression**: Baseline model, nhanh và ổn định

### Đặc Điểm Nổi Bật
- Xử lý tốt teencode và emoji tiếng Việt
- Pipeline hoàn chỉnh từ data collection đến model deployment
- So sánh hiệu suất giữa traditional ML và transformer models
- Code được tổ chức rõ ràng, dễ maintain

## 👥 Đóng Góp

Xem [GIT_GUIDELINES.md](./GIT_GUIDELINES.md) để biết chi tiết về quy trình làm việc và đóng góp vào dự án.

### Quy Trình Đóng Góp
1. Fork repository
2. Tạo feature branch
3. Commit changes với message rõ ràng
4. Tạo Pull Request
5. Code review và merge

## 📝 License

Dự án này được phát triển cho mục đích học tập và nghiên cứu.

## 🤝 Liên Hệ

- **Repository**: [GitHub](https://github.com/thethien8a/Sentiment-Analysis-Vietnamese)
- **Issues**: Tạo issue trên GitHub để báo cáo bugs hoặc đề xuất tính năng

---

**🎉 Cảm ơn bạn đã quan tâm đến dự án Sentiment Analysis Vietnamese!**
