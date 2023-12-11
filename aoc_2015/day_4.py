"""Day 4: The Ideal Stocking Stuffer."""

import hashlib

if __name__ == "__main__":

    secret_key = 'yzbqklnj'
    index = 0
    
    
    lowest_number_found = False

    while not lowest_number_found:
        input_str = f'{secret_key}{index}' 
        hash_result = hashlib.md5(input_str.encode()).hexdigest()

        if hash_result[:6] == "000000":
            print(hash_result)
            print(index)
            lowest_number_found = True
        
        index += 1
        

    

