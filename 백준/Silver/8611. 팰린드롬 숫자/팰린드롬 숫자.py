def converter(number, n):
    answer = ""
    temp = list("0123456789ABCDEF")
    
    if number == 0:
        answer = "0"
    else:
        while number:
            answer += temp[number % n]
            number //= n
            
    return answer[::-1]


def check_palindrome(converted_number):
    is_palindrome = False
    
    if converted_number == converted_number[::-1]:
        is_palindrome = True
        
    return is_palindrome


def palindrome_number(number):
    answer_list = []
    for n in range(2, 11):
        converted_number = converter(
            number=number, n=n
        )
        
        is_palindrome = check_palindrome(
            converted_number=converted_number
        )
        
        if is_palindrome:
            answer_list.append((n, converted_number))
            
    return answer_list


def print_answer(answer_list):
    
    if not answer_list:
        print("NIE")
    
    for answer in answer_list:
        print(f"{answer[0]} {answer[1]}")
        
    
if __name__ == "__main__":
    number = int(input())
    
    answer_list = palindrome_number(number=number)
    
    print_answer(answer_list=answer_list)