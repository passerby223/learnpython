// JavaScript历史背景介绍
// 布兰登 • 艾奇（Brendan Eich，1961年～），1995年在网景公司，发明的JavaScript。
// 一开始JavaScript叫做LiveScript，但是由于当时Java这个语言特别火，所以为了傍大牌，就改名为JavaScript。如同“北大”和“北大青鸟”的关系。“北大青鸟”就是傍“北大”大牌。
// 同时期还有其他的网页语言，比如VBScript、JScript等等，但是后来都被JavaScript打败了，所以现在的浏览器中，只运行一种脚本语言就是JavaScript。

// 什么是JavaScript
// JavaScript是web上一种功能强大的编程语言，用于开发交互式的web页面。它不需要进行编译，而是直接嵌入在HTML页面中，由浏览器执行。

// JavaScript被设计用来向HTML页面添加交互行为。
// JavaScript是一种脚本语言（脚本语言是一种轻量级的编程语言）。
// JavaScript由数行可执行计算机代码组成。
// JavaScript通常被直接嵌入HTML页面。
// JavaScript是一种解释性语言（就是说代码执行不进行预编译）。

// JavaScript的组成：
// 核心（ECMAscript）：语法，语句。
// 文档对象模型（DOM）：document object model，操作文档中的元素和内容。
// 浏览器对象模型（BOM）：浏览器对象。

// JavaScript的作用
// 使用JavaScript添加页面动画效果，提供用户操作体验。
// 主要应用有：嵌入动态文本于HTML页面、对浏览器事件作出响应、读取HTML元素、验证提交数据、检测访客的浏览器信息等。

// JavaScript的引入
// 在HTML文件中引入JavaScript有两种方式，一种是在HTML文档直接嵌入JavaScript脚本，称为内嵌式，另一种是链接外部JavaScript脚本文件，称为外联式。
// 1.内嵌式，在HTML文档中，通过<script>标签引入，如下：
// <html>
//     <head>
//         <script type="text/javascript">
//             此处为JavaScript代码
// </script>
// <title></title>
// </head>
// <body>
//
// </body>
// </html>
// 2.外联式，在HTML文档中，通过<script src="">标签引入.js文件，如下：
// <html>
//     <head>
//         <script src="js/ad.js" type="text/javascript" charset="UTF-8"></script>
//         <title></title>
//     </head>
//     <body>
//
//     </body>
// </html>


//基本语法

// 变量命名规则
// 必须以字母或下划线开头，中间可以是数字、字符或下划线。
// 变量名不能包含空格等符号。
// 不能使用JavaScript关键字作为变量名，如：function。
// JavaScript严格区分大小写。

// 变量声明，使用var关键字 JavaScript变量可以不声明，直接使用。默认值：undefined
var name;
// 变量赋值
var age = 21;//JavaScript变量是弱类型，及同一个变量可以存放不同类型的数据

//数据类型
// 数据类型包括：基本数据类型和引用数据类型。
// 基本数据类型指的是简单的数据段，引用数据类型指的是有多个值构成的对象。
// 当我们把变量赋值给一个变量时，解析器首先要确认的就是这个值是基本类型值还是引用类型值。

// 基本类型
// 1.number
var a = 10;
// typeof 检查当前变量是什么数据类型
console.log(typeof a);
// 特殊情况
var a1 = 5 / 0;
console.log(typeof a1);//Infinity 无限大. number类型

//2.string
var str1 = '中国';
console.log(typeof str1);

//3.boolean
var _result = true;

//4.null
var money = null;//空对象 object

//5.undefined
var ss;
//表示变量未定义
console.log(typeof ss);

// 引用类型
// 引用类型通常叫做类（class），也就是说，遇到引用值，所处理的就是对象。
// JavaScript是基于对象而不是面向对象。对象类型的默认值是null。
// JavaScript提供众多预定义引用类型（内置对象）。
// 后面的文章会讲解。

// 运算符
// JavaScript的运算符合python差不多