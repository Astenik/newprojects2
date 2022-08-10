def mails(mail):
    string = mail
    ind = mail.index('@')
    _string = mail[:ind]
    while _string != None:
      if (('.' and '+') in _string) and (string.index('.') < string.index('+')):
        if '.' in _string:
              ind0 = string.index('.')
              _str = ''
              for num in range(ind0):
                  _str += string[num]
              for  num1 in range(ind0 + 1, len(string)):
                  _str += string[num1]
              string = _str 
              _string = string[ind0 + 1:string.index('@')]
        elif '+' in _string:
            ind1 = string.index('+')
            _str = ''
            for  i in range(ind1):
               _str += string[i]
            ind2 = string.index('@')
            for j in range(ind2, len(string)):
               _str += string[j]
            string = _str
            _string = None 
        else:
             _string = None
      elif  (('.' and '+') in _string) and (string.index('.') > string.index('+')):
            if '+' in _string:
                ind1 = string.index('+')
                _str = ''
                for  i in range(ind1):
                   _str += string[i]
                ind2 = string.index('@')
                for j in range(ind2, len(string)):
                    _str += string[j]
                string = _str
                _string = None 
    return string 
def count_of_mails(_mails):
     count = 0
     for ind in range(len(_mails)):
             for ind1 in range(ind + 1, len(_mails)):
                    if mails(_mails[ind]) != mails(_mails[ind1]):
                         count += 1
     return count
print(count_of_mails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
