# test_script.py
def main():
    print("Welcome to the Spiritual Gifts Test!")
    print("Please answer the following questions by rating each statement from 1 (strongly disagree) to 5 (strongly agree).")
    print("")

    questions = [
        "I enjoy organizing people, tasks, and events.",
        "I find it easy to understand and apply biblical truths.",
        "I am always ready to provide a helping hand to those in need.",
        "I am passionate about sharing the Gospel with others.",
        "I often encourage others to remain faithful and positive.",
        "I have a knack for financial management and generosity.",
        "I feel a strong call to serve within the church or community.",
        "I am often sought out for advice or wisdom."
    ]

    scores = {
        "Administration": 0,
        "Teaching": 0,
        "Helps": 0,
        "Evangelism": 0,
        "Exhortation": 0,
        "Giving": 0,
        "Service": 0,
        "Wisdom": 0
    }

    mapping = [
        ("Administration", 0),
        ("Teaching", 1),
        ("Helps", 2),
        ("Evangelism", 3),
        ("Exhortation", 4),
        ("Giving", 5),
        ("Service", 6),
        ("Wisdom", 7)
    ]

    for i, question in enumerate(questions):
        while True:
            try:
                answer = int(input(f"{question} (1-5): "))
                if 1 <= answer <= 5:
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
        
        for gift, index in mapping:
            if index == i:
                scores[gift] += answer

    print("\nYour Spiritual Gifts Scores:")
    for gift, score in scores.items():
        print(f"{gift}: {score}")

    highest_gift = max(scores, key=scores.get)
    print(f"\nYour primary spiritual gift is: {highest_gift}")

if __name__ == "__main__":
    main()
