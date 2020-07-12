# O(N)
import unittest


def pal_perm(phrase):
    odd_count = 0
    counts = {}
    
    for char in phrase:
        if not char.isalpha():
            continue
        
        lttr = char.lower()
        if lttr not in counts:
            counts[lttr] = 1
            odd_count += 1
        else:
            counts[lttr] += 1
            if counts[lttr] % 2:
                odd_count += 1
            else: 
                odd_count -= 1

    return odd_count == 0 or odd_count == 1


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
