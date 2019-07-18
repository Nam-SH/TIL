1. 양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요

```python
def my_sqrt(n):
    from math import isclose
      
x, y = 0, 0
for i in range(1, n//2):
    for j in range(1, n//2):
        if i**2 < n < j**2:
            x = i
            y = j
            
result = 0
while not isclose(result**2, n):
    result = (x+y)/2
    if result**2 < n:
        x = result
    else:
        y = result
return result


my_sqrt(16)
```

