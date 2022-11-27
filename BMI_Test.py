# Yair Davidof: ID: 314792714.
# Elyasaf Sinvani: ID: 318551628
import re


def tdd(h, w, end):
    if type(w) == str:
        print(f'The weight <<{w}>> is a string, dont worry well fix that.')
        w = float(re.sub('\D', '', w))
        return h, w, end

    if type(h) == str:
        print(f'The weight <<{h}>> is a string, dont worry well fix that.')
        h = float(re.sub('\D', '', h))
        return h, w, end
    if h < 0:
        h *= (-1)
        print(f'The number of height was negative.')
        return h, w, end
    if w < 0:
        w *= (-1)
        print(f'The number of weight was negative.')
        return h, w, end

    if h == 0:
        raise ZeroDivisionError(f'The number of height is Zero, that is invalid digit.')
    if w == 0:
        raise Exception(f'The number is Zero invalid digit.')
    return h, w, True


def calcBmi(height, weight):
    BMI = weight / (height/100)**2
    if BMI <= 18.4:
        return BMI, "You are underweight."
    elif BMI <= 24.9:
        return BMI, "You are healthy."
    elif BMI <= 29.9:
        return BMI, "You are over weight."
    elif BMI <= 34.9:
        return BMI , "You are severely over weight."
    elif BMI <= 39.9:
        return BMI, "You are obese."
    else:
        return BMI, "You are severely obese."


def main():
    test_details = [[192.0, 90], [55, -60], ['999', 0], [0, 80], [8, 3], [-36, 90],
               ['asdf951', 90], [183, 110]]
    for i in test_details:
        end = 1
        h, w = i[0], i[1]
        while end != 0:
            print(f'Temp number {end}')
            try:
                h, w, end = tdd(h, w, end)
                if end is True:
                    end = 0
                    print(f'Case pass, For height: {h}cm, and weight: {w}kg, BMI is:{calcBmi(h, w)} !\n')
            except Exception or ZeroDivisionError as ex:
                end = 0
                print(f'    Case fail!! For height: {i[0]}, and weight: {i[1]}, because {ex}.\n')
            if end != 0:
                end += 1

if __name__ == '__main__':
    main()
