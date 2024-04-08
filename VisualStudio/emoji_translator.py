emoji_translation = {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍",
}  

sentence = input("Please enter a sentence:")
words = sentence.split()
current_word = ""
ans = ""
for parts in words:
    current_word = parts
    for keys in emoji_translation:
        if parts == keys:
            current_word = emoji_translation[keys]
    ans += current_word + " "
print(ans)