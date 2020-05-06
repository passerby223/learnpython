//等到页面全部加载完成后再执行
window.onload = function () {
    //通过id选择元素
    var div2 = document.getElementById("div2");
    div2.style.backgroundColor = 'red';
    div2.style.width = "50px";
    div2.style.height = "50px";

    //通过class选择元素，返回的是选择集
    var div4_col = document.getElementsByClassName('div4');
    console.log("div4_col:", div4_col);//HTMLCollection [div.div4]
    var div4 = document.getElementsByClassName('div4')[0];
    div4.style.background = '#9297a2';

    //通过tagName标签名字来选择，返回的是选择集
    var div3_col = document.getElementsByTagName('li');
    console.log("div3_col:", div3_col);
    for (var j = 0; j < div3_col.length; j++) {
        if (j % 2 !== 0) {
            console.log(div3_col[j]);
            div3_col[j].style.backgroundColor = 'pink';
        }

    }
};