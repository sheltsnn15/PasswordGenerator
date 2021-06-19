import random, string


class PswGenerate:
    # constructor with password data
    def __init__(self, length=0, digit=True, uppercase=True, lowercase=True, punctuation=True):
        self.length = length
        self.digit = digit
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.punctuation = punctuation

    # generate password method
    def generate(self):
        # store password data
        data = []
        # store with a list password data objects
        storeobj = []
        if self.digit: # check if digits need to be added to password
            storeobj.append(string.digits)
        if self.uppercase: # check if uppercase letters need to be added to password
            storeobj.append(string.ascii_uppercase)
        if self.lowercase: # check if lowercase letters need to be added to password
            storeobj.append(string.ascii_lowercase)
        if self.punctuation: # check if punctuation need to be added to password
            storeobj.append(string.punctuation)
        # compile password data with given length
        for i in range(self.length):
            # get password data choices
            ch = random.choice(storeobj)
            data.append(str(random.choice(ch)))
        # randomly shuffle password data
        random.shuffle(data)
        password = ''
        # append data to a password
        for i in data:
            password = password + i
        return password

