

from googletrans import Translator

def translate_to_target_language(text, target_language_code):
    translator = Translator()
    translation = translator.translate(text, src='bn', dest=target_language_code)
    translated_text = translation.text
    return translated_text

# Language Translation App

def translate_bangla_word():
    print(" ভাষা রূপান্তরের এপে আপনাকে স্বাগতম। একটি বাংলা শব্দকে আপনি ভিন্ন ছয়টি ভাষায় রূপান্তর করতে পারবেন!")
    print(" কাঙ্ক্ষিত নম্বরটি নির্বাচন করুন:")
    print("১. English")
    print("২. Chinese")
    print("৩. Italian")
    print("৪. Spanish")
    print("৫. Greek")
    print("৬. Japanese")
    print("বের হয়ে যেতে চাইলে 'বের হবো' লিখুন")

    while True:
        target_language = input("কাঙ্ক্ষিত নম্বরটি নির্বাচন করুন: ")

        if target_language.lower() == "বের হবো":
            print("এপটি থেকে আপনি বের হয়ে যাচ্ছেন!")
            feel = input("আপনার অনুভূতি কেমন?")
            print(f"ধন্যবাদ আপনাকে !")
            break

        if target_language in ["১", "২", "৩", "৪", "৫", "৬"]:
            target_language_code = {"১": "en", "২": "zh-CN", "৩": "it", "৪": "es", "৫": "el", "৬": "ja"}[target_language]
        else:
            print("সঠিক নম্বরটি নির্বাচন করুন")
            continue

        bangla_word = input("বাংলা শব্দটি দিনঃ ")

        translated_word = translate_to_target_language(bangla_word, target_language_code)

        print(f" অনুবাদটি হলো ({target_language}): {translated_word}")

if __name__ == "__main__":
    translate_bangla_word()
