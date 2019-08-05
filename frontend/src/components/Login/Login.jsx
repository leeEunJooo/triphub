import React from 'react';
import '../../static/logbase.css';

const Login = () => {


  return (
    <>
      <form>
        <svg id="ddugi" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
            <path d="M0,150 C0,65 120,65 120,150" fill="skyblue" stroke="#000" strokeWidth="2.5" />
            {/* structure */}
            <circle cx="60" cy="60" r="40" fill="skyblue" stroke="#000" strokeWidth="2.5" />
            {/* rgb(81, 151, 181) */}
            {/* eyes */}
            <g className="eyes">
                {/* 왼쪽 눈 */}
                <circle cx="40" cy="55" r="6" fill="#000"/>
                <circle cx="40" cy="55" r="4" fill="rgb(24, 49, 72)"/>
                <circle cx="44" cy="52" r="1" fill="#fff"/>

                {/* 오른쪽 눈 */}
                <circle cx="80" cy="55" r="6" fill="#000"/>
                <circle cx="80" cy="55" r="4" fill="rgb(24, 49, 72)"/>
                <circle cx="84" cy="52" r="1" fill="#fff"/>
            </g>

            {/* mouse */}
            <g className="muzzle">
                <path d="M60,66 C58.5,61 49,63 49,69 C49,75 58,77 60,71 M60,66 C61.5,61 71,63 71,69 C71,75 62,77 60,71" fill="#fff" />
                <path d="M60,66 C58.5,61 49,63 49,69 C49,75 58,77 60,71 M60,66 C61.5,61 71,63 71,69 C71,75 62,77 60,71" fill="#fff" stroke="#000" strokeWidth="2.5" strokeLinejoin="round" strokeLinecap="round" />

                <circle cx="60" cy="64" r="4" fill="#000"/>
                
            </g>
          </svg>
        <div className="opacity-logo">Triphub</div>

        {{form.as_p}}
        {% csrf_token %}
        <ul id="Login_sign">
            <li><a href="{% url 'register'%}" id="Sign">회원가입</a></li>
            <li><input id="Login_button" type="submit" value="로그인"></li>
        </ul>
        <a href="1.html" id="Lost">비밀번호를 잊어버리셨나요?</a>


      </form>

      
    </>
  );
};

export default Login;