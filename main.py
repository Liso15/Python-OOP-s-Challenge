# main.py

from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet("Buddy")

    # Interact with the pet
    my_pet.get_status()
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.get_status()

    # Bonus: Teach tricks
    my_pet.train("Roll over")
    my_pet.train("Fetch")
    my_pet.show_tricks()

if __name__ == "__main__":
    main()