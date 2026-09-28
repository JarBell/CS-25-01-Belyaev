from words_data import *

def massage_checker (user_ID, users_massage):
    
    white_ID_flag = 0
    short_massage_flag = 0
    empty_massage_flag = 0
    greek_symbols_flag = 0
    spam_words_flag = 0
    bad_words_flag = 0
    clean_massage_flag = 0

    if int(user_ID) in white_ids:
        white_ID_flag = 1
    else:
        if 0 < len(users_massage) < 5:
            short_massage_flag = 1
        elif len(users_massage) == 0:
            empty_massage_flag = 1
        elif len(users_massage) >= 5:
            for i in bad_words:
                if users_massage.count(i) != 0:
                    bad_words_flag = 1
            for i in letters_greek_set:
                if users_massage.count(i) != 0:
                    greek_symbols_flag = 1
            for i in spam_words:
                if users_massage.count(i) != 0:
                    spam_words_flag = 1
        else:
            clean_massage_flag += 1
        
    massage_checker_result = [white_ID_flag, short_massage_flag, 
                                   empty_massage_flag, greek_symbols_flag, 
                                   spam_words_flag, bad_words_flag, clean_massage_flag]
    return massage_checker_result

def status_indicator(massage_checker_result):

    massage_status = str()
    massage_cause = str()

    if massage_checker_result[0] != 0 or massage_checker_result [6] != 0:
        massage_status = "OK"
        massage_cause = "clean"
    elif massage_checker_result[1] != 0 or massage_checker_result[2] != 0:
        massage_status = "suspicious"
        if massage_checker_result[1] != 0:
            massage_cause = "short"
        elif massage_checker_result[2] != 0:
            massage_cause = "empty"
    elif massage_checker_result[5] != 0:
        massage_status = "suspicious"
        massage_cause = "bad words"
    elif  massage_checker_result[3] != 0 or  massage_checker_result[4] != 0:
        massage_status = "spam"
        if massage_checker_result[3] != 0:
            massage_cause = "greek"
        elif massage_checker_result[4] != 0:
            massage_cause = "spam words"
    elif massage_checker_result.count(1) == 0:
        massage_status = "OK"
        massage_cause = "clean"
    print(f"{massage_status}\n{massage_cause}")