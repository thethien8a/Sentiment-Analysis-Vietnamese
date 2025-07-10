# 🚀 Sentiment Analysis Vietnamese

Dự án phân tích cảm xúc (sentiment analysis) cho văn bản tiếng Việt sử dụng các kỹ thuật Machine Learning và Deep Learning hiện đại.

## 📋 Mô Tả Dự Án

Đây là dự án nghiên cứu và phát triển hệ thống phân tích cảm xúc tự động cho văn bản tiếng Việt. Mục tiêu của dự án là xây dựng một model có khả năng phân loại cảm xúc (tích cực, tiêu cực, trung tính) từ các đoạn văn bản tiếng Việt.

## 🎯 Mục Tiêu

- Xây dựng dataset tiếng Việt chất lượng cao cho sentiment analysis
- Phát triển và so sánh hiệu quả của các model khác nhau (LSTM, BERT, PhoBERT, v.v.)
- Tạo ra một API endpoint để sử dụng model trong thực tế
- Đạt độ chính xác cao trên dữ liệu test

## 🛠️ Công Nghệ Sử Dụng

- **Python 3.8+**
- **TensorFlow/Keras** - Deep Learning framework
- **PyTorch** - Alternative deep learning framework  
- **Transformers** - Hugging Face library cho BERT models
- **Pandas & NumPy** - Data manipulation
- **Scikit-learn** - Traditional ML algorithms
- **FastAPI** - API development
- **Jupyter Notebook** - Data exploration và prototyping

## 📁 Cấu Trúc Dự Án

```
Sentiment-Analysis-Vietnamese/
├── data/                   # Dữ liệu
│   ├── raw/               # Dữ liệu thô
│   ├── processed/         # Dữ liệu đã xử lý
│   └── external/          # Dữ liệu từ nguồn khác
├── models/                # Các model đã train
├── notebooks/             # Jupyter notebooks
├── src/                   # Source code chính
│   ├── data/             # Scripts xử lý dữ liệu
│   ├── models/           # Model definitions
│   ├── features/         # Feature engineering
│   └── utils/            # Utility functions
├── tests/                 # Test files
├── docs/                 # Documentation
├── requirements.txt       # Dependencies
├── GIT_GUIDELINES.md     # Hướng dẫn Git cho team
└── README.md             # File này
```

## 🚀 Hướng Dẫn Cài Đặt

### 1. Clone Repository

```bash
git clone https://github.com/thethien8a/Sentiment-Analysis-Vietnamese
cd Sentiment-Analysis-Vietnamese
```

### 2. Tạo Virtual Environment

```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Cài Đặt Dependencies

```bash
pip install -r requirements.txt
```

## 👥 Quy Trình Làm Việc Team

**📖 [Đọc kỹ hướng dẫn Git/GitHub tại đây](GIT_GUIDELINES.md)**

Trước khi bắt đầu đóng góp vào dự án, vui lòng đọc kỹ tài liệu `GIT_GUIDELINES.md` để hiểu rõ quy trình làm việc nhóm và tránh xung đột code.

### Quy Trình Ngắn Gọn:

1. **Fork** repository này về GitHub của bạn
2. **Clone** fork về máy local
3. Tạo **branch mới** cho feature/bugfix
4. **Commit** thường xuyên với message rõ ràng
5. **Push** branch lên GitHub
6. Tạo **Pull Request** để merge vào main branch
7. Đợi **code review** và approval

## 🎯 Roadmap

### Phase 1: Data Collection & Preprocessing ⏳
- [ ] Thu thập dữ liệu từ các nguồn khác nhau
- [ ] Làm sạch và tiền xử lý dữ liệu
- [ ] Tạo dataset chuẩn cho training

### Phase 2: Model Development ⏳
- [ ] Implement baseline models (Naive Bayes, SVM)
- [ ] Develop LSTM/GRU models
- [ ] Fine-tune BERT/PhoBERT models
- [ ] Model comparison và evaluation

### Phase 3: API Development ⏳
- [ ] Xây dựng REST API với FastAPI
- [ ] Containerize với Docker
- [ ] Deploy lên cloud platform

### Phase 4: Frontend & Demo ⏳
- [ ] Tạo web interface đơn giản
- [ ] Demo notebook với examples
- [ ] Documentation hoàn chỉnh

## 🤝 Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng:

1. Đọc [Git Guidelines](GIT_GUIDELINES.md) trước khi bắt đầu
2. Tạo issue để thảo luận feature mới
3. Follow coding standards của dự án
4. Viết tests cho code mới
5. Update documentation khi cần thiết

## 📄 License

[Thêm license phù hợp - MIT, Apache 2.0, etc.]

## 👨‍💻 Team

- **Team Lead**: Nguyễn Thế Thiện
- **Data Scientists**: Hà Đức Mạnh, Nguyễn Thế Thiện
- **ML Engineers**: Hà Đức Mạnh, Nguyễn Thế Thiện

## 📧 Liên Hệ

**Email**: thethien04.work@gmail.com

---

**Happy Coding! 🎉**