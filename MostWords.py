import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import warnings

TEENCODE_DICT = {
    'ko': 'không', 'k': 'không', 'kh': 'không', 'bt': 'biết',
    'dc': 'được', 'đc': 'được', "ak":"à", "àh":"à",
    "uk":"ừ","uh":"ừ", "cmnl":"con mẹ nó luôn",
    'ad': 'admin', 'ntn': 'như thế nào',
    'v': 'vậy', 'r': 'rồi', "qtr":"quá trời",
    'cx': 'cũng',
    'ib': 'inbox',
    'rep': 'trả lời',
    'mn': 'mọi người',
    "goy":"rồi","xl":"xin lỗi",
    "j":"gì",
    "gòy":"rồi",
    'cmt': 'comment',
    'b': 'bạn',
    "tr":"trời",
    "hk":"không",
    "tt":"truyền thông",
    'e': 'em',
    'a': 'anh',
    "ng":"người", "lm":"làm", "cầu đặc": "đầu cặc", "kẹc":"cặc", "đ":"đéo", "gđ":"gia đình", "cằk":"cặc","cặk":"cặc", 'okela':'ok', "djt":"địt",
    "trây":"jack",  "bn":"bao nhiêu","bnh":"bao nhiêu", "cmm":"con mẹ","cm":"chúng mày","clm":"cái lồn má", 'vc':'vãi cả', 'cc':'cục cứt', 'loz':'lồn', 'l':'lồn', "lol":"lồn","lòn":"lồn", "lôn":"lồn",
    'vl':'vãi lồn',"vcl":"vãi cả lồn","vkl":"vãi cả lồn", "đcm":"địt con mẹ","đm":"địt mẹ","đcmm":"địt con mẹ","đcmmm":"địt con mẹ", "đb":"đầu buồi",
    'deo':'đéo','dell':'đéo', 'vcc':"vãi cả cứt", "occho":"óc chó", "t":"tôi", "chx":"chưa", "xg":"xong",
    "vcd":"vãi cả đái","vcđ":"vãi cả đái",
    "ae":"anh em", "j":"gì",
    "soll":"son","sol":"son",
    "vaiz":"vãi",
    "mn":"mọi người","mng":"mọi người",
    "bth":"bình thường",
    "m":"mày",
    "cm":"chúng mày",
    "mn":"mọi người",
    "st":"Sơn Tùng",
    "ch":"chưa",
    "vs":"với",
    "sv":"súc vật",
    "c":"cứt",
    "t.o.p":"top","to.p":"top",
    "ncc":"như cục cứt",
    "dit":"địt","djt":"địt",
    "hth":"hiếu thứ hai",
    "qc":"quảng cáo",
    "vn":"việt nam", "vaiz":"vãi",
    "r":"rồi", "nge":"nghe", "tiktok":"tik tok", "ytb":"youtube", "fb":"facebook", "vcut":"vãi cứt","shit":"cứt", "fl":"follow"
}

EMOJI_DICT = {
    "😢":" bieu_tuong_buon ",
    "🎉":" bieu_tuong_chuc_mung ",
    "❤":" bieu_tuong_trai_tim ",
    "🤣":" bieu_tuong_mat_cuoi ",
    "😂":" bieu_tuong_mat_cuoi ",
    "😭":" bieu_tuong_khoc ",
    "🔥":" bieu_tuong_chay ",
    "💩":" bieu_tuong_cut ",
    "🥰":" bieu_tuong_yeu_thuong ",
    "😮":" bieu_tuong_ngac_nhien ",
    "😅":" bieu_tuong_lo_lang ",
    "<3":" bieu_tuong_trai_tim "
}

STOP_WORDS = set()
with open('./vietnamese-stopwords-dash.txt', 'r', encoding='utf-8') as file:
    for line in file:
        word = line.strip()  
        if word:  
            STOP_WORDS.add(word)
            
warnings.filterwarnings('ignore')



# Hàm làm sạch cơ bản:
def preprocessing_basic(text):
  text = text.lower()
  text = re.sub(r'http\S+','',text)
  text = re.sub(r'<.*?>', '', text)
  text = text.strip()
  text = text.replace("t o p","top").replace("tốp","top")
  text = text.replace("v i e w","view").replace("c à y","cày")
  text = text.replace("đốn lòm","đóm lồn").replace("đốm lòn","đóm lồn")
  return text

def replace_teencode(text,teencode_dict):
  words = text.split()

  for idx,each_word in enumerate(words):
    if each_word in teencode_dict:
      words[idx] = teencode_dict[each_word]

  return ' '.join(words)


def replace_emoji(text,emoji_dict):
  for emoji, word in emoji_dict.items():
      text = text.replace(emoji, word)

  text = re.sub(r'\s+', ' ', text).strip()
  return text


def keep_chars(text):
  vietnamese_chars = 'àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ'
  # Whitelist bao gồm: chữ cái a-z, chữ cái tiếng Việt, và dấu gạch dưới
  allowed_chars = vietnamese_chars + 'a-z_'

  # Tạo pattern để tìm các ký tự KHÔNG thuộc whitelist (và cũng không phải khoảng trắng)
  unwanted_chars_pattern = re.compile(rf'[^{allowed_chars}\s]')
  text = unwanted_chars_pattern.sub(' ', text)
  
  text = re.sub(r'\s+',' ',text)
  text = text.strip()
  return text

def remove_duplicated_emoji(text):
    emoji_pattern = r'bieu_tuong_[a-zA-Z_]+'
    words = text.split()
    seen = set()
    complete_text = []
    for word in words:
        if re.fullmatch(emoji_pattern, word):
            if word not in seen:
                complete_text.append(word)
                seen.add(word)
        else:
            complete_text.append(word)
    return ' '.join(complete_text)
                

def preprocess_comment(text):
    global TEENCODE_DICT
    global EMOJI_DICT
    global STOP_WORDS

    text = preprocessing_basic(text)
    text = replace_teencode(text, TEENCODE_DICT)
    text = replace_emoji(text,EMOJI_DICT)
    text = keep_chars(text)
    text = remove_duplicated_emoji(text)
    
    return text


## Do không cài được underthesea để tokenize nên dùng cách này7
def get_top_bigrams(comments_series, top_n=20, min_length=2):
    all_bigrams = []
    
    for comment in comments_series:
        words = comment.split()
        filtered_words = [word for word in words 
                        if len(word) >= min_length and word not in STOP_WORDS]
        
        # Tạo bigrams
        for i in range(len(filtered_words) - 1):
            bigram = f"{filtered_words[i]} {filtered_words[i+1]}"
            all_bigrams.append(bigram)
    
    bigram_counts = Counter(all_bigrams)
    
    bigram_df = pd.DataFrame(bigram_counts.most_common(top_n), 
                            columns=['bigram', 'count'])
    
    total_bigrams = len(all_bigrams)
    bigram_df['percentage'] = (bigram_df['count'] / total_bigrams * 100).round(2)
    
    return bigram_df

def get_top_trigrams(comments_series, top_n=20, min_length=2):
    all_trigrams = []
    
    for comment in comments_series:
        if pd.notna(comment) and comment.strip():
            words = comment.split()
            # Lọc từ
            filtered_words = [word for word in words 
                           if len(word) >= min_length and word not in STOP_WORDS]
            
            # Tạo trigrams
            for i in range(len(filtered_words) - 2):
                trigram = f"{filtered_words[i]} {filtered_words[i+1]} {filtered_words[i+2]}"
                all_trigrams.append(trigram)
    
    trigram_counts = Counter(all_trigrams)

    trigram_df = pd.DataFrame(trigram_counts.most_common(top_n), 
                             columns=['trigram', 'count'])
    
    total_trigrams = len(all_trigrams)
    trigram_df['percentage'] = (trigram_df['count'] / total_trigrams * 100).round(2)
    
    return trigram_df

def visualize_top_words(word_df, title="Top 20 Từ Xuất Hiện Nhiều Nhất"):
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    bars = plt.barh(range(len(word_df)), word_df['count'])
    plt.yticks(range(len(word_df)), word_df['word'])
    plt.xlabel('Số lần xuất hiện')
    plt.title(title)

    for i, bar in enumerate(bars):
        width = bar.get_width()
        plt.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
                f'{word_df.iloc[i]["count"]}', ha='left', va='center')
    
    # Vẽ pie chart cho top 10
    plt.subplot(2, 1, 2)
    top_10 = word_df.head(10)
    plt.pie(top_10['percentage'], labels=top_10['word'], autopct='%1.1f%%')
    plt.title('Phân Bố Top 10 Từ (Theo %)')
    
    plt.tight_layout()
    plt.show()

def create_wordcloud(comments_series, title="Word Cloud - Từ Vựng Comment"):
    """
    Tạo word cloud từ comments
    """
    # Tách tất cả từ
    all_words = []
    for comment in comments_series:
        if pd.notna(comment) and comment.strip():
            words = comment.split()
            filtered_words = [word for word in words 
                           if len(word) >= 2 and word not in STOP_WORDS]
            all_words.extend(filtered_words)
    
    # Tạo text cho wordcloud
    text = ' '.join(all_words)
    
    # Tạo wordcloud
    wordcloud = WordCloud(
        width=800, 
        height=400, 
        background_color='white',
        max_words=100,
        colormap='viridis',
        font_path='arial.ttf'  
    ).generate(text)
    
    # Vẽ wordcloud
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=16)
    plt.show()

if __name__ == "__main__":
  # Đọc dữ liệu
  comments_df = pd.read_csv('./comment_data/Tram_dung_chan_Jack.csv', encoding='utf-8')

  # Lọc seeding (Loại những người comment nhiều lần)
  print("Số lượng comment ban đầu: ", len(comments_df))
  comments_df.drop_duplicates(subset=['authorDisplayName'], inplace=True)
  comments_df.dropna(subset=['textDisplay'], inplace=True)
  print("Số lượng comment sau khi lọc: ", len(comments_df))

  # Lấy chỉ comment
  comments_only = comments_df["textDisplay"]

  # Làm sạch
  comments_only = comments_only.apply(preprocess_comment)

  # 2. Top bigrams
  print("\n2. TOP 15 BIGRAMS (CỤM 2 TỪ) XUẤT HIỆN NHIỀU NHẤT:")
  top_bigrams = get_top_bigrams(comments_only, top_n=15)
  print(top_bigrams)
  
  # 3. Top trigrams
  print("\n3. TOP 10 TRIGRAMS (CỤM 3 TỪ) XUẤT HIỆN NHIỀU NHẤT:")
  top_trigrams = get_top_trigrams(comments_only, top_n=10)
  print(top_trigrams)
  
  # 4. Visualization
  print("\n4. TẠO BIỂU ĐỒ VÀ WORD CLOUD...")
  create_wordcloud(comments_only)






