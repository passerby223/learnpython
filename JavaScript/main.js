// alert("外联js");


// var name = "小花花";
// var age = 21;
// var gender;
// // console.log()打印变量值到控制台
// console.log("name:" + name);
// console.log("age:" + age);
// //同时给多个变量赋值
// var a = 10, b = 20, c = 30;
// console.log(a, b, c);
// var bookName = "疯狂Python讲义";
// var price = 59.99;
// console.log("《" + bookName + "》" + "售价" + price + "元");//输出：《疯狂Python讲义》售价59.99元
//
//
// //类似于Python中的列表，通过下标进行取值
// var myArrayList = Array(1, 2, 3, "哈哈哈");
// console.log(myArrayList[0]);
// console.log(myArrayList[1]);
// console.log(myArrayList[2]);
// console.log(myArrayList[3]);
// //length返回数组的长度
// console.log("myArrayList数组的长度为：" + myArrayList.length);//myArrayList数组的长度为：4
// //push向数组末尾插入元素
// myArrayList.push("Go");
// console.log(myArrayList);//[1, 2, 3, "哈哈哈", "Go"]
// myArrayList.push("Python", "Java");
// console.log(myArrayList);//[1, 2, 3, "哈哈哈", "Go", "Python", "Java"]
// //pop删除数组中最后一个元素并将被删除的元素返回
// console.log(myArrayList.pop());//Java
// console.log(myArrayList);//[1, 2, 3, "哈哈哈", "Go", "Python"]
// console.log(myArrayList.pop());//Python
// console.log(myArrayList);//[1, 2, 3, "哈哈哈", "Go"]
// console.log(myArrayList.pop());//Go
// console.log(myArrayList);//[1, 2, 3, "哈哈哈"]
//
// //null：空类型，类似于Python中的None
// var myHobby = null;
// //变量已声明未赋值，此变量不是空类型，是undefined
// var myHeight;
// console.log("myHobby:" + myHobby + ", myHeight:" + myHeight);//myHobby:null, myHeight:undefined
//
// var areYouOK = true;
// var areWeOK = false;
// console.log("areYouOK:" + areYouOK);//areYouOK:true
// console.log("areWeOK:" + areWeOK);//areWeOK:false
//
// var bookPrice = 45.9;
// var bookPrice1 = "45.9";
// console.log(bookPrice == bookPrice1);//true
// console.log(bookPrice === bookPrice1);//false

//条件语句
/*
if语句
 */
// var age = 21;
// if (age > 21) {
//     console.log("年龄大于21岁!");
// } else if (age === 21) {
//     console.log("年龄等于21岁!");
// } else {
//     console.log("年龄小于21岁!");
// }
//输出：年龄等于21岁!

/*
switch 语句
 */
// var a = 9, b = 7;
// switch (a - b) {
//     case 4:
//         console.log(a + " - " + b + " = " + 4);
//         break;
//     case 2:
//         console.log(a + " - " + b + " = " + 2);
//         break;
//     case 3:
//         console.log(a + " - " + b + " = " + 3);
//         break;
//     default:
//         console.log(a + " - " + b + " = 默认值");
//         break;
// }
//输出：9 - 7 = 2

/*
函数定义不带参数
 */

//函数定义 使用function关键字
// function test() {
//     console.log("这是一个函数!");
// }
//
// //函数调用
// test();
// //输出：这是一个函数!

/*
函数定义 带参数
 */
// function addition(a, b) {
//     result = (a + b);
//     console.log(a + " + " + b + " = " + result);
// }
//
// //函数调用
// addition(100, 199);
// //输出：100 + 199 = 299


/*
函数定义 带参数 有返回值
 */

//在使用return语句时，程序执行到return语句时会立刻终止，并返回函数的返回值
// function addition(a, b) {
//     result = (a + b);
//     return result;
// }
//
// //函数调用
// var res = addition(100, 199);
// console.log("res = " + res);
// //输出：res = 299


/*
对象
 */
//操作对象的属性
// var objC = {name: "小华华", age: 21, gender: "男"};
// //获取objC对象的属性
// console.log(objC.name);//小华华
// console.log(objC["age"]);//21
// console.log(objC);//{name: "小华华", age: 21, gender: "男"}
// //修改objC对象的属性值
// objC.name = "小刚刚";
// console.log(objC);//{name: "小刚刚", age: 21, gender: "男"}
// objC["age"] = 22;
// console.log(objC);//{name: "小刚刚", age: 22, gender: "男"}
//
// //对象方法：对象方法是作为属性来存储的函数
// var objD = {
//     name: "小花花",
//     age: "21",
//     gender: "女",
//     func: function (a, b) {
//         alert("对象方法");
//         this.name = "大花花";//this来修改了objD对象的name属性的值为"大花花"
//         return a + b;
//     }
// };
//
// res = objD.func(10, 15);
// console.log(res);//25
// console.log(objD);//{name: "大花花", age: "21", gender: "女", func: ƒ}


/*
循环
 */

//while循环
// var a = 21;
// while (a <= 30) {
//     console.log(a);//输出：21到30
//     a++;
// }

//for循环
// for (var i = 1; i <= 10; i++) {
//     console.log(i);//输出1到10
// }

//for in循环
// var myArray = Array("小花花", 21, "女", "打羽毛球");
// for (j in myArray) {
//     // console.log(j);//输出0到3，输出的是myArray数组的元素下标
//     console.log(myArray[j]);//输出：小花花 21 女 打羽毛球
// }

//for in循环遍历对象
var objA = {
    name: "小花花",
    age: 21,
    gender: "女",
    hobby: "旅行"
};
for (n in objA) {
    // console.log(n);//输出的是对象的属性：name age gender hobby
    console.log(objA[n]);//输出对象的属性值：小花花 21 女 旅行
}
