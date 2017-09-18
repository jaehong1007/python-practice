
# 모듈과 패키지
## 모듈
파이썬 파일 하나가 하나의 모듈로 취급한다. (모듈 단위로 클로저를 가짐 > 전역 변수 환경)

```python
# shop.py
def buy_item():
    print('Buy item!')

buy_item()
```

```python
# game.py
def play_game():
    print('Play game!')

play_game()
```

```python
# lol.py
import game
import shop

print('= Turn on game =')
game.play_game()
shop.buy_item()
```

### __name__변수

`game`과 `shop`이 import되는 순간 해당 코드가 실행되어 버리는 문제가 있다.

각 모듈은 자신의 이름을 가지며, 모듈 이름은 모듈의 전역변수 `__name__`에서 확인 할 수 있다. 파이썬 인터프리터가 실행한 모듈의 경우, `__main__`이라는 이름을 가진다. 따라서 아래와 같이 처리해준다.
```python
# shop.py
def buy_item():
    print('Buy item!')

if __name__ == '__main__':
    buy_item()
```

### 네임스페이스 (Namespace)
각 모듈은 독립된 네임스페이스(이름공간)를 가진다. 메인으로 사용되고 있는 모듈이 아닌 import된 모듈의 경우, 해당 모듈의 네임스페이스를 사용해 모듈 내부의 데이터에 접근한다.

#### from을 사용해 모듈의 함수를 직접 import
`import 모듈명`의 경우, 모듈의 이름이 전역 네임스페이스에 등록되어 `모듈명.함수`로 사용가능하다.

모듈명을 생략하고 모듈 내부의 함수를 쓰고 싶다면, `from 모듈명 import 함수명`으로 불러들일 수 있다.

#### from 모듈명 * 을 사용해 모듈 내 모든 식별자 (변수, 함수) import
`from 모듈명 import` 또는 `import 모듈명`에서, 같은 모듈명이 존재하거나 혼동 될 수 있을 경우, 뒤에 `as`를 붙여 사용할 모듈명을 변경할 수 있다.

## 패키지
패키지는 모듈들을 모아 둔 특별한 폴더를 뜻한다. (일반적인 폴더와는 다르다)

폴더를 패키지로 만들면 계층 구조를 가질 수 있으며, 모듈들을 해당 패키지에 모을 수 있는 역할을 한다.

패키지를 만들 때는 패키지로 사용할 폴더에 `__init__.py`파일(패키지 초기화 파일)을 넣어주면, 해당 폴더는 패키지로 취급된다. (비어있어도 무관하다)

`shop.py`와 `game.py`를 func패키지에 넣어본다.

```
├── func
│   ├── __init__.py
│   ├── game.py
│   └── shop.py
└── lol.py
```

패키지는 모듈과 동일하게 import할 수 있다. 위와 같은 경우에는 `from func import game, shop`으로 기존 코드의 변경 없이 패키지에서 모듈을 가져오는 방식을 사용할 수 있다.

또는 단순히 import func후 func.game, func.shop을 사용하는 방식도 가능하다.

### `*`, `__all__`

패키지에 포함된 하위 패키지 및 모듈을 불러올 때, `*`을 사용하면 해당 모듈의 모든 식별자들을 불러온다.

이 때, 각 모듈에서 자신이 import될 때 불러와질 목록을 지정하고자 한다면 `__all__` 을 정의하면 된다.
```python
# comment.py
__all__ = (
    'Comment',
)
```

패키지 자체를 import시에 자동으로 가져오고 싶은 목록이 있다면, 패키지의 `__init__.py`파일에 해당 항목을 import해주면 된다.
```python
# __init__.py
from .comment import *
from .post import *
```