def main():
    item_prices = {"Water": 1, "Cappucino": 4, "Black Coffee": 2, "Coke": 3}
    print("Hello, welcome to Coffee Shop!!")
    name = input("What is your name?")
    print(f"Hello {name}, thank you so much for coming in today.")
    print(f"{name}, What would you like to order from our menu today? We offer: ")
    for key, value in item_prices.items():
        print(key, f"is {value} euro.")
    order = input()
    print(f"{name} Great! Your {order} is on its way!")
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            answer = int(input(f"How many {order}'s would you like?"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue
        else:
            # age was successfully parsed!
            # we're ready to exit the loop.
            break

    total = order_ammount(order, answer, item_prices)
    print(f"Thank you, your total would be {total}")


def order_ammount(order, answer, item_prices):
    # print(item_prices[order])
    total = item_prices[order] * int(answer)
    return total


if __name__ == "__main__":
    main()
