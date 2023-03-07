
# a = 10
# b = 20
# if a > b:
#     largest = a
# else:
#     largest = b
# print("The largest number is:", largest)

# number = int(input("Enter a number: "))
# print("Multiplication table for", number)
# for i in range(1, 11):
#     print(number, "x", i, "=", number * i)

# number = int(input("Enter a number: "))
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(number, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")
# else:
#     print(number, "is not a prime number")

# import random
# responses = ["I'm fine!", "Not too bad, how about you?", "I'am good"]
# def generate_response(message):
#     message = message.lower()
    
#     if "hello" in message or "hi" in message:
#         return "Hi there! How are you doing?"
#     elif "how are you" in message:
#         return random.choice(responses)
#     elif "what's your name" in message:
#         return "My name is Chatbot. What's yours?"
#     elif "goodbye" in message:
#         return "Goodbye! Have a great day!"
#     else:
#         return "I'm sorry, I didn't understand what you said."

# print("Hi there! I'm Chatbot. What's your name?")

# while True:
#     message = input(">> ")
#     response = generate_response(message)
#     print(response)
#     if "goodbye" in message:
#         break

# import random
# number = random.randint(1, 100)
# while True:
#     try:
#         guess = int(input("Guess the number between 1 and 100: "))
#         break
#     except ValueError:
#         print("Please enter a valid number.")
# while guess != number:
#     if guess > number:
#         print("You guessed too high. Try again!")
#     else:
#         print("You guessed too low. Try again!")
#     guess = int(input("Guess the number between 1 and 100: "))
# print("Congratulations! You guessed the correct number.")

jug1_capacity = 4
jug2_capacity = 3

jug1_current = jug1_capacity  # fill jug1 to its maximum capacity
jug2_current = 0  # empty jug2

while jug2_current != 2:  # loop until there are exactly 2 liters in jug2
    # ask the user how much water to pour from jug1 to jug2
    try:
        amount_to_pour = int(input(f"How much water to pour from the {jug1_capacity}-liter jug to the {jug2_capacity}-liter jug? "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    # check if the input is within the valid range
    if amount_to_pour < 0 or amount_to_pour > jug1_current:
        print(f"Please enter a number between 0 and {jug1_current}.")
        continue

    # pour water from jug1 to jug2
    jug1_current -= amount_to_pour
    jug2_current += amount_to_pour

    if jug2_current == 2:
        break  # exit the loop if there are exactly 2 liters in jug2

    # if jug2 is full, pour it out
    if jug2_current == jug2_capacity:
        jug2_current = 0

    # if jug1 is empty, fill it up
    if jug1_current == 0:
        jug1_current = jug1_capacity

print(f"Exactly 2 liters are in the {jug2_capacity}-liter jug. The state of the jugs is: {jug1_current}L, {jug2_current}L")
