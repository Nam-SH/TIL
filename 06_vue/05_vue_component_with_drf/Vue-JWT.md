# 1.  헤더 (Header)

- **typ:** 토큰의 타입을 지정합니다. 바로 `JWT` 이죠.

- **alg:** 해싱 알고리즘을 지정합니다.  해싱 알고리즘으로는 보통 `HMAC SHA256` 혹은 `RSA` 가 사용되며, 이 알고리즘은, 토큰을 검증 할 때 사용되는 signature 부분에서 사용됩니다

```javascript
const header = {
  "typ": "JWT",
  "alg": "HS256"
};
```



# 2. 정보 (payload)

## #1 등록된 (registered) 클레임

- `iss`: 토큰 발급자 (issuer)
- `sub`: 토큰 제목 (subject)
- `aud`: 토큰 대상자 (audience)
- `exp`: 토큰의 만료시간 (expiraton), 시간은 NumericDate 형식으로 되어있어야 하며 (예: 1480849147370) 언제나 현재 시간보다 이후로 설정되어있어야합니다.
- `nbf`: Not Before 를 의미하며, 토큰의 활성 날짜와 비슷한 개념입니다. 여기에도 NumericDate 형식으로 날짜를 지정하며, 이 날짜가 지나기 전까지는 토큰이 처리되지 않습니다.
- `iat`: 토큰이 발급된 시간 (issued at), 이 값을 사용하여 토큰의 `age` 가 얼마나 되었는지 판단 할 수 있습니다.
- `jti`: JWT의 고유 식별자로서, 주로 중복적인 처리를 방지하기 위하여 사용됩니다. 일회용 토큰에 사용하면 유용합니다.



## #2 공개 (public) 클레임

공개 클레임들은 충돌이 방지된 (collision-resistant) 이름을 가지고 있어야 합니다. 충돌을 방지하기 위해서는, 클레임 이름을 `URI`형식으로 짓습니다.

```js
{
    "https://velopert.com/jwt_claims/is_admin": true
}
```



## #3 비공개 (private) 클레임

등록된 클레임도아니고, 공개된 클레임들도 아닙니다. 양 측간에 (보통 클라이언트 <->서버) 협의하에 사용되는 클레임 이름들입니다. 공개 클레임과는 달리 이름이 중복되어 충돌이 될 수 있으니 사용할때에 유의해야합니다.

```js
{
    "username": "velopert"
}
```



## #4 예제

```js
{
    "iss": "velopert.com",
    "exp": "1485270000000",
    "https://velopert.com/jwt_claims/is_admin": true,
    "userId": "11028373727102",
    "username": "velopert"
}
```



# 3.  서명 (signature)

- JSON Web Token 의 마지막 부분은 바로 서명(**signature**) 입니다. 이 서명은 헤더의 인코딩값과, 정보의 인코딩값을 합친후 주어진 비밀키로 해쉬를 하여 생성합니다.

- 서명 부분을 만드는 슈도코드(pseudocode)의 구조는 다음과 같습니다.

  ```js
  HMACSHA256(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    secret)
  ```

  