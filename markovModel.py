
import random


# Class defining a Markov Model for modeling human text

class MarkovModel():

    # Markov model of order k from given text
    # TODO: Throw exception if length of text less than k

    def __init__(self, text, k):
        
        self.text = text
        self.k = k
        self.kgrams_dict = {}
    
    
        # Create the kgrams_dict from the text and order k
        
        d = {}
        # add the first k characters to the end so it is circular
        t = text + text[0:k] 
        
        # Loop through the text and grab every possible slice of length k.
        # These are all the possible kgrams in the text.  Now we create a
        # dictionary of dictionaries to record several key pieces of
        # information.  The outer dictionary will have all the possible kgrams
        # as keys, and the values will be dictionaries of all the possible
        # characters that can follow a given kgram along with the number of
        # times the character follows the given kgram.        
        
        for i in range(len(t)-k):
            kgram = t[i:i+k]
            c = t[i+k]          # the char following the kgram slice
            if kgram not in d:  # create an inner dict for each kgram
                d[kgram] = {}   
            d[kgram][c] = d[kgram].get(c,0) + 1   # fill in that inner dict
                     
        self.kgrams_dict = d
    
 
    
    
    # Return order k of Markov model

    def order(self):
        return self.k




    # Return number of times the kgram occurs in the text. Used with optional
    # argument c returns number of times the kgram was followed by character c

    # TODO: Throw exception if kgram is not of length k

    def freq(self, kgram, c=None):
        if c:
            return self.kgrams_dict[kgram][c]
        else:
            return sum(self.kgrams_dict[kgram].values())




    # Return random character following given kgram

    # TODO: Throw exception if kgram is not of length k
    # TODO: Throw exception if no such kgram

    def rand(self, kgram):
    
        l = []
        for char in self.kgrams_dict[kgram].keys():
            for i in range(self.kgrams_dict[kgram][char]):
                l.append(char)
    
        r = random.Random()
        return r.choice(l)




    # Return a String of given length characters by simulating a trajectory
    # through the corresponding Markov chain. The first k characters of the
    # newly generated String should be the argument kgram.

    # TODO: Throw exception if kgram is not of length k.
    # TODO: Throw exception if length is less than k.

    def generate_string(self, kgram, length):
    
        s = kgram
        for i in range(length - self.k):
            s = s + self.rand(s[len(s) - self.k :])
        
        return s
        




if __name__ == "__main__":

    welcome_text = """
    Welcome to the Markov Model random text generator.
    Here you will be able to generate random text based
    on a sample you provide.  You will be prompted for
    the following information:

    1. Sample text you can type in or read from a file.

    2. The length in characters of the text you want to
    generate.

    3. A number called "order k" that the model will use
    to determine how close the random text should look
    to the sample.  A small number will produce very 
    random text and a large one will end up reproducing
    the sample text verbatim.  Try an order k of 5 or 6
    to start with.

    """

    print welcome_text

    text = ""
    length = 0
    order_k = 0

    user_finished = False
    while user_finished is False:

        input_one = raw_input("""1. Please enter the sample text or a .txt filename.
If nothing is entered, a default text will be used: """)

        if input_one == "":
            text = welcome_text
        elif input_one[len(input_one)-4:] == ".txt":
            file_opened = False
            while file_opened is False:
                try:
                    f = open(input_one)
                    file_opened = True
                except IOError:
                    print 'Could not find file with name', input_one, 'in this directory.'
                    input_one = raw_input("Enter the filename: ")
            text =  f.read()
        else:
            text = input_one


        num_entered = False
        while num_entered is False:    
            try:
                input_two = raw_input("""2. Please enter a number for the length in 
characters of the text you want to generate: """)
                length = int(input_two)
                num_entered = True
            except ValueError:
                print 'The value entered was not a number. '
    
    
        num_entered = False
        while num_entered is False:    
            try:
                input_three = raw_input("""2. Please enter a number for order k.
Try 5 or 6: """)
                order_k = int(input_three)
                num_entered = True
            except ValueError:
                print 'The value entered was not a number. '


        my_markov = MarkovModel(text, order_k)
        print """
        Here is your randomly generated text:
         """
        print my_markov.generate_string(text[:order_k], length)
    
        input_four = raw_input("""
Hit any key to try again or type \"exit\" to quit: 
        """)
        if input_four == "exit":
            user_finished = True


        
        
        