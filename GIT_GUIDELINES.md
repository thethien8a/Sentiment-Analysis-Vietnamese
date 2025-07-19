# 📋 Hướng Dẫn Sử Dụng Git/GitHub Cho Team

> **Mục đích**: Đảm bảo việc phối hợp làm việc mượt mà và tránh xung đột code trong dự án Sentiment Analysis Vietnamese

## 🎯 Quy Trình Làm Việc Cơ Bản

### 1. Thiết Lập Ban Đầu

```bash
# Clone repository về máy
git clone https://github.com/thethien8a/Sentiment-Analysis-Vietnamese.git

# Di chuyển vào thư mục dự án
cd Sentiment-Analysis-Vietnamese

# Kiểm tra remote
git remote -v

# Thêm upstream (nếu fork từ repo gốc)
git remote add upstream https://github.com/thethien8a/Sentiment-Analysis-Vietnamese.git
```

### 2. Cập Nhật Code Mới Nhất

**⚠️ LUÔN LÀM ĐIỀU NÀY TRƯỚC KHI BẮT ĐẦU LÀM VIỆC MỚI:**

```bash
# Chuyển về branch main
git checkout main

# Lấy code mới nhất từ remote
git pull origin main

# Hoặc nếu có upstream
git pull upstream main
```

## 🌿 Quy Trình Branch

### Tạo Branch Mới Cho Feature/Bug Fix

```bash
# Tạo và chuyển sang branch mới
git checkout -b feature/ten-feature-moi

# Hoặc cho bug fix
git checkout -b fix/ten-bug-can-sua

# Hoặc cho hotfix
git checkout -b hotfix/ten-loi-cap-thiet
```

### Quy Tắc Đặt Tên Branch

- **Feature**: `feature/mo-ta-ngan-gon`
- **Bug fix**: `fix/mo-ta-loi`
- **Hotfix**: `hotfix/mo-ta-loi-nghiem-trong`
- **Improvement**: `improve/mo-ta-cai-tien`

**Ví dụ:**
- `feature/data-preprocessing`
- `fix/model-accuracy-bug`
- `improve/code-documentation`

## 💾 Commit và Push

### Commit Best Practices

```bash
# Xem trạng thái hiện tại
git status

# Thêm file cần commit
git add .
# Hoặc thêm file cụ thể
git add path/to/file.py

# Commit với message rõ ràng
git commit -m "feat: thêm chức năng tiền xử lý dữ liệu"
```

### Quy Tắc Viết Commit Message

Sử dụng format: `type: mô tả ngắn gọn`

**Types:**
- `feat`: Tính năng mới
- `fix`: Sửa lỗi
- `docs`: Cập nhật tài liệu
- `style`: Thay đổi format code (không ảnh hưởng logic)
- `refactor`: Tái cấu trúc code
- `test`: Thêm hoặc sửa test
- `chore`: Công việc bảo trì

**Ví dụ:**
```bash
git commit -m "feat: thêm model LSTM cho sentiment analysis"
git commit -m "fix: sửa lỗi encoding UTF-8 cho tiếng Việt"
git commit -m "docs: cập nhật hướng dẫn cài đặt"
```

### Push Code

```bash
# Push branch lên remote
git push origin feature/ten-branch-cua-ban

# Lần đầu push branch mới
git push -u origin feature/ten-branch-cua-ban
```

## 🔄 Pull Request (PR) Process

### 1. Tạo Pull Request

1. Vào GitHub repository
2. Click "New Pull Request"
3. Chọn branch của bạn để merge vào `main`
4. Điền thông tin PR:

**Template PR Description:**
```markdown
## Mô Tả
Mô tả ngắn gọn về thay đổi

## Loại Thay Đổi
- [ ] Feature mới
- [ ] Bug fix
- [ ] Cải thiện hiệu năng
- [ ] Tái cấu trúc code
- [ ] Cập nhật documentation

## Checklist
- [ ] Code đã được test
- [ ] Không có conflict với main branch
- [ ] Code style tuân theo quy tắc của project
- [ ] Đã thêm/cập nhật documentation nếu cần

## Screenshots (nếu có)
<!-- Thêm ảnh minh họa nếu có UI changes -->
```

## ⚡ Tránh Xung Đột Code

### 1. Cập Nhật Thường Xuyên

```bash
# Hàng ngày trước khi làm việc
git checkout main
git pull origin main

# Merge main vào branch đang làm việc
git checkout feature/your-branch
git merge main
```

### 2. Commit Nhỏ và Thường Xuyên

```bash
# Thay vì commit 1 lần lớn, chia nhỏ:
git add specific-file.py
git commit -m "feat: thêm function đọc dữ liệu"

git add another-file.py  
git commit -m "feat: thêm function tiền xử lý text"
```

### 3. Phân Chia Công Việc Rõ Ràng

- **Không** cùng lúc sửa cùng 1 file
- **Thông báo** trong team chat khi làm việc trên module nào
- **Chia nhỏ** task để tránh overlap

## 🔧 Xử Lý Conflict

### Khi Gặp Conflict

```bash
# Khi pull hoặc merge gặp conflict
git status  # Xem files bị conflict

# Mở file conflict, tìm các dòng:
<<<<<<< HEAD
Code hiện tại của bạn
=======
Code từ branch khác
>>>>>>> branch-name

# Chỉnh sửa và giữ lại code đúng
# Sau đó:
git add conflicted-file.py
git commit -m "resolve: giải quyết conflict trong file preprocessing"
```

### Conflict Prevention

```bash
# Trước khi push, luôn:
git checkout main
git pull origin main
git checkout your-branch
git rebase main  # Hoặc git merge main
git push origin your-branch
```

## 📁 Cấu Trúc File và Folders

### Quy Tắc Tổ Chức

``` DEMO CẤU TRÚC FILE
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
└── README.md             # Hướng dẫn chính
```

### Gitignore Quan Trọng

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/

# Jupyter Notebook
.ipynb_checkpoints

# Data files (thường không commit)
*.csv
*.json
*.pkl
*.h5

# Model files (dùng Git LFS hoặc external storage)
*.model
*.weights

# Environment
.env
.venv/

# IDE
.vscode/
.idea/
```

## 🚨 Các Lệnh Git Cấp Cứu

### Hoàn Tác Commit

```bash
# Hoàn tác commit cuối (giữ changes)
git reset --soft HEAD~1

# Hoàn tác commit và xóa changes
git reset --hard HEAD~1

# Hoàn tác file specific
git checkout -- filename.py
```

### Xem Lịch Sử

```bash
# Xem commit history
git log --oneline

# Xem changes giữa 2 commit
git diff commit1 commit2

# Xem changes trong file
git diff filename.py
```

### Stash Changes

```bash
# Lưu tạm changes khi cần chuyển branch
git stash

# Xem stash list
git stash list

# Apply stash
git stash pop
```

## 👥 Workflow Cho Team

### Daily Workflow

1. **Sáng**: Pull latest main
2. **Coding**: Commit thường xuyên
3. **Cuối ngày**: Push branch, tạo PR nếu done
4. **Review**: Check PR của teammates

### Weekly Tasks

- **Cleanup**: Xóa merged branches
- **Sync**: Đảm bảo local sync với remote
- **Backup**: Push all working branches

## 📞 Khi Cần Hỗ Trợ

### Team Support

1. **Slack/Discord**: Hỏi trong channel development
2. **GitHub Issues**: Tạo issue cho bugs/questions
3. **Code Review**: Tag teammates trong PR comments
4. **Pair Programming**: Share screen khi stuck

### Useful Resources

- [Git Cheat Sheet](https://github.com/github/training-kit/blob/master/downloads/github-git-cheat-sheet.pdf)
- [Vietnamese Git Tutorial](https://rogerdudler.github.io/git-guide/index.vi.html)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)

## ✅ Checklist Trước Khi Submit PR

- [ ] Code chạy được và pass tests
- [ ] Commit messages rõ ràng
- [ ] Không có sensitive data (API keys, passwords)
- [ ] Code style consistent
- [ ] Documentation updated nếu cần
- [ ] No merge conflicts với main
- [ ] PR description đầy đủ thông tin

---

**🎉 Chúc team làm việc vui vẻ và hiệu quả! Mọi thắc mắc xin liên hệ team lead.** 