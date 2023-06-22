import time

class OddNumber():
    """
    Class to generate an odd number.
    """
    def __init__(self):
        self.initial_odd_number = -1 

    def generate_number(self):
        """
        Method to update initial odd number.
        Returns;
            odd_number
        """
        self.initial_odd_number = self.initial_odd_number + 2
        return self.initial_odd_number
    
def main():
    odd_number_generator_object = OddNumber()
    while True:
        new_odd_number = odd_number_generator_object.generate_number()
        print(f"This is an odd number from odd_number_generator.py: {new_odd_number}")
        time.sleep(5)


if __name__ == '__main__':
    main()