import time

def display_instructions():
    print("डार्क साइकॉलॉजी मूल्यांकन में आपका स्वागत है।")
    print("यह टूल आपके व्यक्तित्व के डार्क ट्राइट (नार्सिसिज्म, मैनिपुलेशन, और साइकोपैथी) और आपके कैरियर, परिवार, और वित्तीय व्यवहार की पहचान करने के लिए डिज़ाइन किया गया है।")
    print("कृपया सभी प्रश्नों के ईमानदारी से उत्तर दें। यह जानकारी गोपनीय रखी जाएगी।\n")
    time.sleep(2)

def ask_question_with_custom_option(question, options):
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}) {option}")
    print(f"{len(options) + 1}) अपना उत्तर दर्ज करें")  # Custom option

    while True:
        try:
            choice = int(input("अपना उत्तर चुनें (1/2/3/...): "))
            if 1 <= choice <= len(options):
                return (choice, options[choice - 1])
            elif choice == len(options) + 1:
                custom_answer = input("अपना उत्तर दर्ज करें: ")
                return (len(options) + 1, custom_answer)
            else:
                print("कृपया वैध विकल्प चुनें।")
        except ValueError:
            print("कृपया संख्या दर्ज करें।")

def evaluate_score(scores):
    print("\n** परिणाम **")

    traits = {
        "narcissism": "नार्सिसिज्म",
        "manipulation": "मैनिपुलेशन",
        "psychopathy": "साइकोपैथी",
        "career": "कैरियर",
        "family": "परिवार",
        "financial": "वित्तीय सोच"
    }

    for trait, score in scores.items():
        print(f"{traits[trait]} स्कोर: {score}")
        if score <= 30:
            print(f"   - {traits[trait]} में आपकी प्रवृत्तियां सामान्य और संतुलित हैं।")
        elif score <= 60:
            print(f"   - {traits[trait]} में आपकी प्रवृत्तियां थोड़ी असंतुलित हो सकती हैं।")
        else:
            print(f"   - {traits[trait]} में आपकी प्रवृत्तियां उच्च स्तर की हैं। इसे सुधारने के लिए ध्यान दें।")

    total_score = sum(scores.values())
    print(f"\nकुल स्कोर: {total_score}/480")
    if total_score <= 160:
        print("   - आपका स्कोर बहुत कम है। आप एक सहानुभूतिपूर्ण और संतुलित व्यक्ति हैं।")
    elif total_score <= 320:
        print("   - आपका स्कोर मध्यम स्तर पर है। आप कभी-कभी मैनिपुलेटिव या आत्म-केंद्रित हो सकते हैं।")
    else:
        print("   - आपका स्कोर उच्च है। यह सलाह दी जाती है कि आप पेशेवर मनोवैज्ञानिक से सलाह लें।")

def dark_psychology_test():
    display_instructions()

    questions = {
        "narcissism": [
            ("क्या आप अपनी उपलब्धियों को बढ़ा-चढ़ाकर पेश करना पसंद करते हैं?",
             ["बिल्कुल नहीं", "कभी-कभी", "अक्सर", "हमेशा"]),
            ("क्या आपको ध्यान का केंद्र बनना पसंद है?",
             ["बिल्कुल नहीं", "कभी-कभी", "अक्सर", "हमेशा"]),
        ],
        "manipulation": [
            ("क्या आप दूसरों को अपने फायदे के लिए मैनिपुलेट करना उचित मानते हैं?",
             ["बिल्कुल नहीं", "कभी-कभी", "अक्सर", "हमेशा"]),
            ("क्या आप दूसरों की भावनाओं को नियंत्रित करने की कोशिश करते हैं?",
             ["कभी नहीं", "कभी-कभी", "अक्सर", "लगातार"]),
        ],
        "career": [
            ("क्या आप अपनी सफलता के लिए टीम वर्क को कम महत्व देते हैं?",
             ["बिल्कुल नहीं", "कभी-कभी", "अक्सर", "हमेशा"]),
            ("क्या आप अपने सहकर्मियों की मेहनत का श्रेय लेना चाहते हैं?",
             ["कभी नहीं", "कभी-कभी", "अक्सर", "लगातार"]),
        ],
        "family": [
            ("क्या आप परिवार के सदस्यों की जरूरतों को प्राथमिकता नहीं देते?",
             ["हमेशा देते हैं", "कभी-कभी देते हैं", "कभी-कभी नहीं देते", "कभी नहीं देते"]),
            ("क्या आप परिवार में अपनी इच्छाओं को सबसे अधिक महत्व देते हैं?",
             ["बिल्कुल नहीं", "कभी-कभी", "अक्सर", "हमेशा"]),
        ],
        "financial": [
            ("क्या आप वित्तीय निर्णय लेने में जोखिम उठाने में झिझकते नहीं हैं?",
             ["हमेशा झिझकते हैं", "कभी-कभी", "बहुत कम", "बिल्कुल नहीं"]),
            ("क्या आप दूसरों से पैसे उधार लेने में संकोच नहीं करते?",
             ["हमेशा संकोच करते हैं", "कभी-कभी", "बहुत कम", "बिल्कुल नहीं"]),
        ]
    }

    scores = {key: 0 for key in questions}

    for trait, trait_questions in questions.items():
        for question, options in trait_questions:
            answer_index, answer = ask_question_with_custom_option(question, options)
            if answer_index <= len(options):  # If the answer is from predefined options
                scores[trait] += (answer_index - 1) * 10  # Score calculation for predefined options
            else:
                print(f"आपने कस्टम उत्तर दिया: {answer}")
                scores[trait] += 5  # Custom answer default score

    evaluate_score(scores)

# मुख्य प्रोग्राम
if __name__ == "__main__":
    dark_psychology_test()