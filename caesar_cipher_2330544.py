''' This a python program that uses Caesar Cipher for encryption and decryption'''
def welcome():
    ''' This function is a non return type function.
It prints a welcome message to the user'''
    print('Welcome to the Caesar Cipher\nThis program encrypts and decrypts text.')
def enter_message():
    ''' This function asks the user to whether encrypt or decrypt the message.

      validation:
       It validates the user's input and allows retry if the user inputs invalid mode..

     error handling:
         This function uses try,excpect and else for error handling for shift value.'''

    mode=input('Would you like to encrypt(e) or decrypt(d)?').lower()
    #.lower() converts the user's input into lowercase
    while mode not in ('e', 'd'):
        #while loop is used to validate the user's selection of mode
        print('Invalid mode. Please select either encrypt(e) or decrypt(d)')
        mode=input('Would you like to encrypt(e) or decrypt(d)?').lower()
    message=input('What is your message?').upper()
    #creating a condition of loop.
    while True:
        #here try, expect and else is used for error handling.
        try:
            shift=int(input('Enter the shift value'))
        except ValueError:
            print('Invalid Shift')
        else:
            break
#calling the encrypt or decrypt function according to the user's choice of mode.
    if mode=='e':
        encrypt(message,shift)
    else:
        decrypt(message,shift)

def encrypt(message,shift):
    ''' This function encrypts the user's message.

       Arguments: This function takes two arguments i.e message and shift value.

       Loop: For loop is used to go through each characters in the message including space.

        ord() is used to find the ASCII value of the character
        chr() is used to convert ASCII value into corresponding characters.

        if else is used to check whether the character is space or not to avoid shifting space.'''

    encrypted_message=''
    for character in message:
        current_position=ord(character)
        if current_position==32:
            encrypted_message+=character
            #checking if the character is space or not
        else:
            new_position=(current_position+shift-65)%26+65
            new_character=chr(new_position)
            encrypted_message+=new_character

    print('The encrypted message is ' +encrypted_message)


def decrypt(message,shift):
    ''' This function decrypts the user's message.

       Arguments: This function takes two arguments i.e message and shift value.

       Loop: For loop is used to go through each characters in the message including space.

        ord() is used to find the ASCII value of the character
        chr() is used to convert ASCII value into corresponding characters.

        if else is used to check whether the character is space or not to avoid shifting space.'''
    decrypted_message=''
    for character in message:
        current_position=ord(character)
        if current_position==32:
            decrypted_message+=character
        else:
            new_position=(current_position-shift-65)%26+65
            new_character=chr(new_position)
            decrypted_message+=new_character

    print('The decrypted message is ' +decrypted_message)
def main():
    ''' This a main function where all the other functions are called to complete the program.
This function also confirms with the user whether they want to continue or not'''
    welcome()
    enter_message()
    choice=input('Do you want to encrypt or decrypt more message?(y/n)')
    while choice.lower()not in('y','n'):
        choice=input('Please enter either y for yes or n for no')
    while choice.lower()=='y':
        enter_message()
        choice=input('Do you want to encrypt or decrypt more message?(y/n)')
    print("'Thank you for using the program' -Saksham_Sharma")
if __name__=="__main__":
    main()
