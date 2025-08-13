average_score=int(input("Enter the average score to print the result: "))
if average_score <= 100:
   print("result is distinction with score", average_score)
elif average_score >=0 and average_score <= 59:
        print("result is failed with score", average_score)
elif average_score >= 60 and average_score <= 84:
      print("result is second class score", average_score)
elif average_score >= 85 and average_score <= 95:
        print("result is first class score", average_score)
else:
      print("Invalid average score")