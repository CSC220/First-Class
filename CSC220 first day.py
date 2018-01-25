# fancy banners

# get the string from user

# empty string? longer than 80 chars? - edge cases


def main():

    
    user_sentence = input("enter sentence")
    len_user_sen = len(user_sentence)

    if len_user_sen >= 80:
        print("please use shorter sentence! >:(")

    if len_user_sen == 0:
        print("you entered the empty string!") 

    else:
        num = len_user_sen+2
        print("*"*num)
        print("*" + user_sentence + "*")
        print("*"*num)
    
main()
