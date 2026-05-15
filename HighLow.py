import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    your_score = 0
    for i in range(NUM_ROUNDS):
        print(f"Round {i+1}")
        your_num = random.randint(1,100)
        computers_num = random.randint(1,100)
        print(f"Your number is {your_num}")

        choice = input(
            "Do you think your number is higher or lower than the computer's?: "
            )

        higher_and_correct = choice == "higher" and 
        your_num > computers_num
        lower_and_correct = choice == "lower" and 
        your_num < computers_num

        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computers_num}")
            your_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computers_num}")
        
        print(f"Your score is now {your_score}")
        print()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
