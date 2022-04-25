import tester
score = 0
print("'''\n"
      "Hello, I am certain you are raring to show off your skills, but let's start simple.\n" 
      "Aren't you going to say hello back?\n" 
      "'''\n")

score += tester.test1(input())

print("'''\n"
      "I have a box here [], but it feels a little empty.\n"
      "Could you fill it please? But be careful, its very fragile and\n"
      "I am worried your clumsy fingers would do a number in it\n"
      "'''\n")

original_statement = "box = []\n"

score += tester.test2(original_statement + input())

print(score)

