import React, { Component } from 'react';

import '../../static/Loading.css';

class Loading extends Component {
    render() {
        return (
            <div className='loading'>
                <div className="loading-head">
                    <div className="loading-img">
                        <div className="loading-imgf">
                            <div className="loading-txt">
                                <p>모두가<br/>선택을 완료할 때까지<br/>기다려 주세요.</p>
                            </div>     
                        </div>
                    </div>
                                  
                </div>
                <div className="loading-foot">
                    <div className="loading-list">
                        <a href='/'>MY LIST 수정</a>
                    </div>
                    <div className="loading-home">
                        <a href='/'>HOME 으로 이동</a>
                    </div>
                </div>
            </div>
        );
    }
}

export default Loading;