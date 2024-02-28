def bodyFat(weight, height, age, gender):
    try:
        assert gender in [0, 1]
    except: AssertionError
    def bmi(weight, height):
        return weight / pow(height, 2)
    return 1.294*bmi(weight, height)+0.2*age-11.4*gender-0.8
print(bodyFat(1,2,3,0))
