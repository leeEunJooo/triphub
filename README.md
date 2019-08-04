Triphub 페이지는 두 가지 서버로 나누어져 있습니다.

첫번째 django를 구동하는 8000번 포트의 백엔드 서버
두번째 react.js를 구동하는 3000번 포트의 프론트엔드 서버

따라서, VSCODE 실행시에 터미널을 두개로 분할하여 각각 서버를 돌려야 프론트와 백엔드가 모두 구동되는 것을 알 수 있습니다.


## 백엔드 구동방법

가상환경 돌립니다.

혹시나 설치안되어 있는 pip package가 있다면 설치합니다.

> /triphub/backend/TriphubProject

**manage.py가 속한 triphubproject 디렉터리 안에서**

다음 명령어를 칩니다.

~~~shell
python manage.py runserver
~~~

그럼 백엔드 서버가 작동이되고 프론트 서버도 만약 돌렸을 경우 데이터 요청이나 http요청시에

백엔드 서버를 돌리는 terminal에서 로그가 생기는 것을 확인할 수 있습니다.

## 프론트 엔드 구동방법
우선적으로는 yarn이라는 프로그램을 설치해야합니다.
그건 구글에 yarn download 치면 사양에 맞게 다운 받으면 되겠죠?

yarn이 설치되었다면

> /triphub/frontend

**package.json파일이 속한 frontend 디렉터리 안에서**

다음 명령어를 칩니다.

~~~shell
yarn install
~~~

잠시만 기다리면 필요한 프로그램들이 다 설치되었을 겁니다.(gitignore에 등록해놔서 어쩔 수 없어요)

mac과 window에서 호환안되는 애들 있을까봐 다름.

그리고는 바로 실행합니다.

~~~shell
yarn start
~~~

`참고로 맥과 윈도우 모두 yarn start를 통해 3000번 포트에서 열리도록 설정해놨습니다`

또 잠시만 기다리면 새 창이 열리면서 **리액트 연동 테스트앱**이라는 화면을 볼 수 있을 겁니다.

개발은 3000번 포트에서 하고 있으며 build를 통해 호스팅을 위한 준비가 완료될 시에

8000번 포트에서도 반영되도록 설정되어 있으니 각각 프론트와 백엔드가 개별적으로 나뉘어 서로 다른 화면을 보면서 테스트할 수 있으니

유지 보수가 쉬워졌죠?

이상입니다.

# 화이팅!

## Member of TripHub
1. 박성우
2. 김태훈
3. 이은주
4. 최정혜
5. 강동기