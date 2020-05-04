// alert("外联js");


var name = "小花花";
var age = 21;
var gender;
// console.log()打印变量值到控制台
console.log("name:" + name);
console.log("age:" + age);
//同时给多个变量赋值
var a = 10, b = 20, c = 30;
console.log(a, b, c);
var bookName = "疯狂Python讲义";
var price = 59.99;
console.log("《" + bookName + "》" + "售价" + price + "元");//输出：《疯狂Python讲义》售价59.99元


//类似于Python中的列表，通过下标进行取值
var myArrayList = Array(1, 2, 3, "哈哈哈");
console.log(myArrayList[0]);
console.log(myArrayList[1]);
console.log(myArrayList[2]);
console.log(myArrayList[3]);
//length返回数组的长度
console.log("myArrayList数组的长度为：" + myArrayList.length);//myArrayList数组的长度为：4
//push向数组末尾插入元素
myArrayList.push("Go");
console.log(myArrayList);//[1, 2, 3, "哈哈哈", "Go"]
myArrayList.push("Python", "Java");
console.log(myArrayList);//[1, 2, 3, "哈哈哈", "Go", "Python", "Java"]
//pop删除数组中最后一个元素并将被删除的元素返回
console.log(myArrayList.pop());//Java
console.log(myArrayList);//[1, 2, 3, "哈哈哈", "Go", "Python"]
console.log(myArrayList.pop());//Python
console.log(myArrayList);//[1, 2, 3, "哈哈哈", "Go"]
console.log(myArrayList.pop());//Go
console.log(myArrayList);//[1, 2, 3, "哈哈哈"]

//null：空类型，类似于Python中的None
var myHobby = null;
//变量已声明未赋值，此变量不是空类型，是undefined
var myHeight;
console.log("myHobby:" + myHobby + ", myHeight:" + myHeight);//myHobby:null, myHeight:undefined

var areYouOK = true;
var areWeOK = false;
console.log("areYouOK:" + areYouOK);//areYouOK:true
console.log("areWeOK:" + areWeOK);//areWeOK:false