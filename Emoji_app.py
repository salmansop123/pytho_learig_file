# message = input(">")
# words = message.split(" ")
# emojis = {
#     ":)" : "😄",
#     "):" : "😑"
# }

# output = ""
# for word in words:
#     output += emojis.get(word, "!") + " "
# print(output)


# Ex using functions without return
def messageFunction(user_message):
    words = user_message.split(" ")
    emojis = {
        ":)" : "😄",
        "):" : "😑"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)


message = input(">")
messageFunction(message)



#  
# Ex using functions with return 
# def messageFunction(user_message):
#     words = user_message.split(" ")
#     emojis = {
#         ":)" : "😄",
#         "):" : "😑"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output


# message = input(">")
# user_message = messageFunction(message)
# print(user_message)
