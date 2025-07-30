ef cal_ratings(rating):
    if rating==0:
        print("No ratings are available")
        return
    positive = [r for r in ratings if r >= 4]
    percentage = (len(positive) / len(ratings)) * 100
    print(f"Positive Feedback: {round(percentage, 2)}%")
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
cal_ratings(ratings)
