class credit_check():

    def __init__(self):
        self.check()

    def check(self):
        number = int(input("Enter credit card number: "))

        if len(str(number)) != 16:
            print("Invalid")

        elif len(str(number)) == 16:
            odd_strings = str(number) 
            odd_strings = odd_strings[0::2]
            odd_sum = 0

            for i in range(0,len(odd_strings)):
                calc = int(odd_strings[i]) * 2
                if calc > 9:
                    calc = str(calc)
                    calc = int(calc[0]) + int(calc[1])
                odd_sum = odd_sum + calc
            
            even_string = str(number)
            even_string = even_string[1::2]
            even_sum = 0

            for i in range(0,len(even_string)):
                even_sum = even_sum + int(even_string[i])

            if (odd_sum + even_sum) % 10 == 0:
                print("Card is valid")
            else:
                print("Invalid card")


main = credit_check()
