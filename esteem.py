def main():

    question_1 = input("1. I feel that I am a person of worth, at least on an equal plane with others.\nEnter D, d, a, or A: ")
    question_2 = input("2. I feel that I have a number of good qualities. \nEnter D, d, a, or A: ")
    question_3 = input("3. All in all, I am inclined to feel that I am a failure. \nEnter D, d, a, or A: ")
    question_4 = input("4. I am able to do things as well as most other people.\nEnter D, d, a, or A: ")
    question_5 = input("5. I feel I do not have much to be proud of.\nEnter D, d, a, or A: ")
    question_6 = input("6. I take a positive attitude toward myself.\nEnter D, d, a, or A: ")
    question_7 = input("7. On the whole, I am satisfied with myself.\nEnter D, d, a, or A: ")
    question_8 = input("8. I wish I could have more respect for myself.\nEnter D, d, a, or A: ")
    question_9 = input("9. I certainly feel useless at times.\nEnter D, d, a, or A: ")
    question_10 = input("10. At times I think I am no good at all.\nEnter D, d, a, or A: ")

    total_sum = get_positive_points(question_1, question_2, question_4, question_6, question_7) + get_negative_points(question_3, question_5, question_8, question_9, question_10)
    print(f"Your score is {total_sum}.")
    print("A score below 15 may indicate problematic low self-esteem.")
def get_positive_points(question_1, question_2, question_4, question_6, question_7):
    """numbers 1, 2, 4 , 6, 7
    """
    positive_questions = [question_1, question_2, question_4, question_6, question_7]
    positive_sum = 0
    for i in positive_questions:
        if i == "d":
            positive_sum += 1
        elif i == "a":
            positive_sum += 2
        elif i == "A":
            positive_sum += 3
        else:
            pass
    
    return positive_sum

def get_negative_points(question_3, question_5, question_8, question_9, question_10):
    """numbers 3, 5, 8, 9, 10
    """
    negative_questions = [question_3, question_5, question_8, question_9, question_10]
    negative_sum = 0
    for i in negative_questions:
        if i == "a":
            negative_sum += 1
        elif i == "d":
            negative_sum += 2
        elif i == "D":
            negative_sum += 3
        else:
            pass
    
    return negative_sum

if __name__ == "__main__":
    main()
