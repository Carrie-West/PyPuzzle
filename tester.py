def test1(statement):
    try:
        statement = statement.replace("print(", "result=")[:-1]
        exec(statement, globals())
        if 'hello' in result:
            print("'''\nExcellent! Now we can start for real.\n'''\n")
            return 1
    except:
        print("'''\nuh oh, someone got an error.\n'''")
        return 0

def test2(statement):
    score = 0
    try:
        exec(statement, globals())
        for element in box:
            if type(element) == int or type(element) == float:
                print("'''\nSee! You've ruined it\n'''")

                raise Exception()
            elif str(element).replace('.', '').replace('-','').isnumeric():
                print("'''\n Oh you clever fool\n'''\n")
                score += 1
            score += 1

        print("'''\n Thank you! Much better\n'''")

    except:
        print("'''\nuh oh, someone got an error.\n'''")
        score = 0

    return score