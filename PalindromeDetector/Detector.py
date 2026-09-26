class Detector():
    def is_palin_bi(string):
        return string == string[:: -1];

    def is_palin_no_bi(string):
        left = 0
        right = len(string) - 1
        
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True


