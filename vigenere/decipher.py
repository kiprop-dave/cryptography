# Python code to implement
# Vigenere Cipher
 
# This function generates the
# key in a cyclic manner until
# it's length is equal to
# the length of original text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

# Driver code
if __name__ == "__main__":
    string = (input("Enter text to be decrypted: "))
    keyword = (input("Enter the decryption key: "))
    key = generateKey(string, keyword)
    text_origin=originalText(string,key)
    print("Original/Decrypted Text :",text_origin)    