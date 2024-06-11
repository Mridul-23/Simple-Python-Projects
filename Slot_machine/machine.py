import random
symbols = ["❄️ ", "💣" , "🎖️"]

def main() -> None:
    
    def game() -> None:
        # Game logic     
        tokens = 150
        print("Welcome to the Slot Game🎰")
        while tokens>0:
            print()
            print(f"You have {tokens} coins.")
            try:
                bet = int(input("Bet amount: "))
            except:
                print("Please enter a positive number of coins.")
                continue
            if bet > tokens:
                print("Not enough coins!")
            else:
                tokens -=bet
                sq_one = random.choice(symbols)
                sq_two = random.choice(symbols)
                sq_three = random.choice(symbols)
                sq_four = random.choice(symbols)
                sq_five = random.choice(symbols)
                sq_six = random.choice(symbols)
                sq_seven = random.choice(symbols)
                sq_eight = random.choice(symbols)
                sq_nine = random.choice(symbols)

                print()

                print("|", sq_one, "|", sq_two, "|", sq_three, "|" )
                print(" -------------- ")

                print( "|", sq_four, "|", sq_five, "|", sq_six, "|")
                print(" -------------- ")

                print("|", sq_seven, "|", sq_eight, "|", sq_nine, "|")

                print()

                if (sq_four == sq_five == sq_six) or (sq_one==sq_two==sq_three) or (sq_seven==sq_eight==sq_nine):
                    if (sq_four == sq_five == sq_six):
                        won = bet*2
                    else:
                        won = 0
                    if (sq_one==sq_two==sq_three):
                        alt = bet
                    else:
                        alt = 0
                    if (sq_seven==sq_eight==sq_nine):
                        nalt = bet
                    else:
                        nalt = 0
                    if alt!=0 or nalt!=0:
                        print("Your bet money is saved!")
                        if alt+nalt==bet*2:
                            fwon = won + nalt
                        else:
                            fwon = won
                    else:
                        fwon = won 
                    print(f"You won {fwon} coins🪙.")
                    tokens += won + alt + nalt
                else:
                    print("You lost this time.")

        print("You are out of coins!")
        print("Thank you for playing:)")
        print()
        main()

    user = input("Press any button to play (q for quit & d for details)")

    if user=='q':
        print("Thank you for playing")
        exit()
    elif user=='d':
        print("Details: ")
        print("If you won in middle line you'll have double the coints you had bet on.")
        print("If you won on other rows, your coins will not get wasted.")
        print("Have fun")
    else:
        game()

    
if __name__=="__main__":
    main()