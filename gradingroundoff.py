def nextmultiple(num: int):
    q = num // 5
    rem = num % 5
    if rem == 0:
        # it is itself next multiple of 5
        return num
    else:
        #we have nearest multiple of 5
        # q is lower limit so q+1 will be next multiple
        return 5 * (q + 1)


def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] < 38:
            # no rounding off
            pass
        else:
            nextnum = nextmultiple(grades[i])
            if nextnum - grades[i] < 3:
                grades[i] = nextnum
    return grades


x=gradingStudents([4, 73, 67, 38, 33])
print(x)