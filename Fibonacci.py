'''Author=Ben Mathew Nainan
   Program=Fibonacci
   Date=03/12/2024'''


def generate_fibonacci(n):
    sequence=[]
    first_number,second_number=0,1
    for i in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence



