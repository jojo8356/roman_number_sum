# roman_number_sum

1. The initial data set includes lists of tuples named int_rom, double, single, singles, and triples. These lists of tuples represent values ​​and their Roman numeral equivalents, groups of special Roman numerals (like CM for 900), single Roman numerals, Roman numerals that can occur at most once, and Roman numerals that can occur at most once thrice.

2. The nb_to_roman(n) function takes an integer n and converts it to Roman numerals by iterating through the int_rom list and subtracting the corresponding values ​​from n until n is reduced to zero. The matching roman numerals are added to the roman string which is then returned.

3. The roman_to_nb(roman) function takes a roman numeral string and converts it to an integer by iterating through the roman string, checking for double roman numeral combinations (like CM, XL, etc.) and adding the corresponding values ​​to the roman_to_nb(roman) function. whole whole. It returns the resulting integer value.

4. The verif_roman(roman) function checks if all characters in the string roman belong to the unique Roman numerals defined in unique. If yes, it returns True, otherwise it returns False.

5. The is_decreasing(sequence) function checks if the sequence passed as an argument is decreasing. It goes through the sequence and compares each element with the next two elements. If at any point, an element is smaller than the next two elements, the function returns False, otherwise it returns True.

6. The function verif_croissant_roman(roman) takes a string of roman roman numerals, converts it to numeric values ​​using roman_to_nb, and then checks if these values ​​are in double (meaning they are special roman numerals) or if they are in descending order using is_decreasing. If any of these conditions are met, it returns True, otherwise it returns False.

7. The function verif_mulitple_same_element(element, list) checks if an element appears more than once in a given list. If the element does not appear more than once, it returns True, otherwise it returns False.

8. The function verif_multiple_same_letter(novel, nb_same, list) checks if a character appears more than a certain number of times (nb_same) in the novel string. She goes through each character in the novel and counts how many times each character appears. If one of these characters appears more than nb_same times and is part of the list list, it returns True, otherwise it returns False.

9. The sum_roman(sum) function takes a sum string that is assumed to be an addition of Roman numerals (eg, "X + IV"). It first checks if the operation is an addition, if the Roman numerals are valid with verif_roman, if they are in descending order with verif_croissant_roman, and if no Roman numeral repeats more than twice for single digits with verif_multiple_same_letter. Then it adds the Roman numerals using sum and checks if the result is between 1 and the maximum allowed is 3999. If all conditions are met, it returns the result in Roman numerals using nb_to_roman. Otherwise, it returns an error message. Finally, a list of tests is defined, and the sum_roman function is called for each test, displaying the result.
