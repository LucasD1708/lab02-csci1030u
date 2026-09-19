# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    inHours = total_seconds // 3600 #there are 3600 seconds in an hour so we must divide
    inMinutes = (total_seconds % 3600) // 60 #rounding and converting again
    inSeconds = total_seconds % 60 #doing the same thing again four our :SS
    return f"{inHours}:{inMinutes:02d}:{inSeconds:02d}" #returning the new values in the correct format



def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    #we need to check every age range and associate it with the right price
    if age <=3: #pretty much repeating the same thing for all age ranges
        return 0
    elif age <= 12: 
        return 8
    elif age <= 64:
        return 15
    else:
        return 10 #will return 10 for the senior price aka any age 65 and up



def sum_multiples(limit):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    sum = 0 #establishing "sum"

    for num in range(limit): #makes sure it only works when the number is in the range we want 
        if num % 3 == 0 or num % 5 == 0: #essentially just checking for remainders to ensure they are a facotr/multiple of 3 or 5
            sum += num #adding the numbers together that fit our criteria to get the sum or total

    return sum



def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    total = 0
    for posCheck in numbers:
        if posCheck > 0:
            total += posCheck
    return total


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    # print(seconds_to_hms(3661))            # 1:01:01
     #print(admission_price(10))             # 8
     #print(sum_multiples(10))               # 23
     #print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()
