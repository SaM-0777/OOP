class InvalidAgeError(Exception):
    def __init__(self, arg):
        self.msg = arg

def Vote_Eligibility(age):
    if age < 18:
        raise InvalidAgeError("Not Eligible to vote : " + str(age))
    else:
        print("Eligible for Vote : " + str(age))
try:
    Vote_Eligibility(22)
    Vote_Eligibility(14)
except InvalidAgeError as error:
    print(error)
