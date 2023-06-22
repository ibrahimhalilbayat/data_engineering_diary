from threading import Thread
import even_number_generator
import odd_number_generator 

def main():
    print('This is the main function of thread_script.py')

    # Create the threads you want 
    thread_even_number_generator = Thread(target=even_number_generator.main)
    thread_odd_number_generator = Thread(target=odd_number_generator.main)


    # Now let's start the threads 
    thread_even_number_generator.start()
    thread_odd_number_generator.start()

    # Now we should join the threads
    thread_even_number_generator.join()
    thread_odd_number_generator.join()


if __name__ == "__main__":
    main()