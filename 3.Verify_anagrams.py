#/usr/bin/python

def prep_dict(word):
   """Takes a word and returns a dict with letters as keys
      and counts as values"""
   counts = {}
   for l in word.lower():
       if l!=" ":
           counts[l] = counts.get(l,0) + 1
   return counts

def verify_anagrams(first_word, second_word):
    """Take two words and returns True if the words 
       are anagrams or else returns False"""
    first = prep_dict(first_word)
    second = prep_dict(second_word)
    #print first, second
    for k,v in first.iteritems():
        try:
            if second[k] == v:
                pass
            else:
                return False
        except:
                return False
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams(u"a", u"z"), bool), "Boolean!"
    assert verify_anagrams(u"Programming", u"Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams(u"Hello", u"Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams(u"Kyoto", u"Tokyo") == True, "The global warming crisis of 3002"

