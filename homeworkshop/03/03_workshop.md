1.  Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다. 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.



```python
def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return False
    return True

is_palindrome('abba')
```



```python
def is_palindrome(word):
	if word = word[::-1]:
        return True
    else:
        return False
    
is_palindrome('abba')
```
