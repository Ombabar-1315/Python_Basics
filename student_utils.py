def calculate_total(marks):
    total = 0
    for mark in  marks:
        total += mark

    return total


def calculate_average(marks):
    total = 0
    for mark in  marks:
            total += mark

    avgerage = total / len(marks)
    return avgerage


def check_result(average):

     if average >= 35:
          return "Pass"

     else:
          return "Fail"


def find_highest(marks):

     high = 0

     for mark in marks:
          if mark >  high:
               high = mark
     return high


