import time

class EvenNumber():
    """
    Class to generate an even number.
    """
    def __init__(self):
        self.initial_even_number = -2 

    def generate_number(self):
        """
        Method to update initial even number.
        Returns;
            even_number
        """
        self.initial_even_number = self.initial_even_number + 2
        return self.initial_even_number
    
def main():
    even_number_generator_object = EvenNumber()
    while True:
        new_even_number = even_number_generator_object.generate_number()
        print(f"This is an even number from even_number_generator.py: {new_even_number}")
        time.sleep(3)


if __name__ == '__main__':
    main()