# 🎯 Sentiment Analysis Vietnamese

Dự án phân tích cảm xúc (Sentiment Analysis) cho tiếng Việt, tập trung vào việc phân tích comment YouTube của bài hát "Trạm dừng chân - J97"

## 📋 Mục Tiêu Dự Án

- **Phân tích cảm xúc** comment YouTube tiếng Việt
- **Xử lý ngôn ngữ tự nhiên** cho tiếng Việt với các đặc thù như teencode, emoji
- **So sánh hiệu suất** giữa các mô hình ML truyền thống và transformer models
- **Xây dựng pipeline** hoàn chỉnh từ thu thập dữ liệu đến triển khai model
- **Phân tích từ vựng** và trích xuất cụm từ quan trọng

## 🏗️ Cấu Trúc Dự Án

```
Sentiment-Analysis-Vietnamese/
├── 📊 data.ipynb                           # Thu thập dữ liệu từ YouTube API
├── 🤖 phoBert.ipynb                        # Training và fine-tuning PhoBERT model
├── 🧠 Training_with_ML_Algorithm.ipynb     # Training các thuật toán ML truyền thống
├── 📈 MostWords.ipynb                      # Phân tích từ vựng và trích xuất cụm từ
├── 🔀 shuffle.py                           # Xáo trộn dữ liệu training
├── 📁 comment_data/                        # Thư mục chứa dữ liệu
│   ├── Tram_dung_chan_Jack.csv            # Dữ liệu comment gốc
│   └── Tram_dung_chan_Jack_shuffled.xlsx  # Dữ liệu đã xáo trộn
├── 📝 vietnamese-stopwords-dash.txt        # Danh sách stop words tiếng Việt
├── 📋 GIT_GUIDELINES.md                    # Hướng dẫn làm việc với Git
├── 📄 .gitignore                           # Cấu hình Git ignore
└── 📖 README.md                            # Tài liệu chính này
```

## 🔧 Các Tính Năng Chính

### 1. **Thu Thập Dữ Liệu** (`data.ipynb`)
- Sử dụng YouTube Data API v3 để thu thập comment
- Xử lý pagination và rate limiting
- Lưu trữ dữ liệu với metadata đầy đủ:
  - `authorDisplayName`: Tên người comment
  - `textDisplay`: Nội dung comment
  - `likeCount`: Số lượt like
  - `publishedAt`: Thời gian đăng
  - `totalReplyCount`: Số lượt trả lời

### 2. **Tiền Xử Lý Dữ Liệu**
- **Chuẩn hóa teencode**: 50+ từ viết tắt phổ biến (ko→không, dc→được, etc.)
- **Xử lý emoji**: 12+ emoji được chuyển thành text mô tả
- **Làm sạch text**: Loại bỏ URL, HTML tags, ký tự đặc biệt
- **Chuẩn hóa tiếng Việt**: Xử lý dấu tiếng Việt và ký tự đặc biệt
- **Loại bỏ emoji trùng lặp**: Tối ưu hóa biểu tượng cảm xúc
- **Vietnamese Character Support**: Hỗ trợ đầy đủ ký tự tiếng Việt

### 3. **Mô Hình PhoBERT** (`phoBert.ipynb`)
- Fine-tuning PhoBERT cho sentiment analysis
- Sử dụng GPU để tăng tốc training
- Đánh giá hiệu suất với các metrics: accuracy, F1-score
- Visualization kết quả training
- Tokenization và padding cho tiếng Việt

### 4. **Thuật Toán ML Truyền Thống** (`Training_with_ML_Algorithm.ipynb`)
- **Logistic Regression**: Baseline model với class_weight='balanced'
- **Random Forest**: Ensemble method với class_weight='balanced'
- **SVM**: Support Vector Machine với kernel='linear'
- **Naive Bayes**: MultinomialNB classifier
- **Voting Classifier**: Kết hợp nhiều model
- **GridSearchCV**: Hyperparameter tuning
- **Cross-validation**: StratifiedKFold validation

### 5. **Phân Tích Từ Vựng & Cụm Từ** (`MostWords.ipynb`)
- **Phân tích từ đơn**: `get_top_words()` - Tìm top từ xuất hiện nhiều nhất
- **Phân tích bigrams**: `get_top_2words()` - Cụm 2 từ xuất hiện thường xuyên
- **Phân tích trigrams**: `get_top_3words()` - Cụm 3 từ có ý nghĩa
- **Word Cloud**: Visualization trực quan từ vựng
- **Underthesea Integration**: Sử dụng underthesea cho tiếng Việt
- **Phân tích theo sentiment**: So sánh từ vựng theo cảm xúc

## 🚀 Cách Sử Dụng

### Yêu Cầu Hệ Thống
```bash
# Python 3.8+
pip install -r requirements.txt
```

### Cài Đặt Dependencies
```bash
# Core libraries
pip install pandas numpy scikit-learn

# Deep Learning
pip install transformers torch

# Visualization
pip install matplotlib seaborn wordcloud

# Vietnamese NLP
pip install underthesea

# API & Data
pip install google-api-python-client openpyxl

# Additional
pip install tqdm datasets
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

# Phân tích từ vựng và cụm từ
jupyter notebook MostWords.ipynb
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
- **Vietnamese Character Support**: Hỗ trợ đầy đủ ký tự tiếng Việt

## 🎯 Kết Quả

### Model Performance
- **PhoBERT**: Accuracy cao nhất, phù hợp cho production
- **Random Forest**: Hiệu suất tốt, dễ interpret
- **Logistic Regression**: Baseline model, nhanh và ổn định
- **SVM**: Hiệu suất tốt với kernel linear
- **Voting Classifier**: Kết hợp nhiều model để tăng độ chính xác

### Phân Tích Từ Vựng
- **Top từ đơn**: Phát hiện từ khóa quan trọng
- **Top bigrams/trigrams**: Hiểu context và cụm từ phổ biến
- **Word Cloud**: Visualization trực quan
- **Sentiment-based analysis**: So sánh từ vựng theo cảm xúc

### Đặc Điểm Nổi Bật
- Xử lý tốt teencode và emoji tiếng Việt
- Pipeline hoàn chỉnh từ data collection đến model deployment
- So sánh hiệu suất giữa traditional ML và transformer models
- Phân tích từ vựng chi tiết với underthesea
- Code được tổ chức rõ ràng, dễ maintain

## 🔍 Tính Năng Mới

### Phân Tích Cụm Từ
- **Noun Phrase Extraction**: Trích xuất cụm danh từ tiếng Việt
- **Named Entity Recognition**: Nhận diện tên riêng, địa danh
- **Frequency-based Analysis**: Phân tích dựa trên tần suất xuất hiện
- **Pattern-based Extraction**: Trích xuất theo mẫu câu tiếng Việt

### Visualization Nâng Cao
- **Interactive Charts**: Biểu đồ tương tác cho phân tích từ vựng
- **Sentiment Distribution**: Phân bố từ vựng theo sentiment
- **Trend Analysis**: Phân tích xu hướng từ vựng theo thời gian

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
