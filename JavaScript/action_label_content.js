window.onload = function () {
    var div1 = document.getElementsByClassName("div1")[0];
    //输出被选择标签(div1)内的所有HTML内容
    console.log(div1.innerHTML);
    /*
    div1.innerHTML输出：
    <ul>
        <li>li1</li>
        <li>li2</li>
        <li>li3</li>
        <li>li4</li>
        <li>li5</li>
    </ul>
    <h3>哈啊啊啊啊啊啊啊</h3>
     */

    //只获取被选择标签(div1)内的HTML内容的文本
    console.log(div1.innerText);
    /*
    div1.innerText输出：
    li1
    li2
    li3
    li4
    li5
    哈啊啊啊啊啊啊啊
     */

    /**
     * innerHTML写入节点文本
     */
    //innerHTML修改被选择标签里的内容
    div1.innerHTML = "<h1>人生苦短，Let's Go!</h1>";
    //输出被选择标签(div1)内的所有HTML内容
    console.log(div1.innerHTML);//console控制台输出：<h1>人生苦短，Let's Go!</h1>
    //只获取被选择标签(div1)内的HTML内容的文本
    console.log(div1.innerText);//console控制台输出：人生苦短，Let's Go!

    /**
     * 修改元素属性
     */
    var a = document.getElementById("baidu1");
    //将a标签的超链接`https:www.baidu.com`改为`https:www.jd.com`
    a["href"] = "https:www.jd.com";
    //将a标签的文本`百度一下`改为`点我跳转至京东`
    a["text"] = "点我跳转到京东";
    //修改a标签的class属性名(两种方式都可以修改)
    a["className"] = "a_CLASS";
    //操作Class的时候，需要将`class`修改为`className`
    a.className = "a_CLASS1";

    var input = document.getElementById("input1");
    //input文本输入框修改为密码输入框
    input.type = "password";
    /**
     * 修改元素CSS样式
     */
    var div2 = document.getElementsByClassName("div2")[0];
    div2.style.background = "pink";
    div2.style.width = "50%";
    div2.style["height"] = "100px";


};