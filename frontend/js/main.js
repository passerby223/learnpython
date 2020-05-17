$(function () {
    //新增project中“+”图片的点击事件
    $(".add_pro_img").click(function () {
        // $(".back").addClass("show");
        // $(".back").show();
        $(".back").fadeIn();
    });
    //填写新增project的form表单中“X”图片的点击事件
    $(".cancel_add_pro_img").click(function () {
        // $(".back").removeClass("show");
        // $(".back").hide();
        $(".back").fadeOut();
    });
    //填写新增project的form表单中“提交”按钮的点击事件
    $("#project_submit").click(function () {
        // $(".back").removeClass("show");
        // $(".back").hide();
        $(".back").fadeOut();
    });
    //左侧列表页下拉菜单
    $(".left_menu h3").click(function () {
        //通过添加属性：toggleClass可以重复切换样式
        // $(this).next().toggleClass("show").parent().siblings().children("ul").removeClass("show");
        // $(this).next().toggle().parent().siblings().children("ul").hide();

        //通过jQuery中的动画：
        $(this).next().fadeToggle().parent().siblings().children("ul").fadeOut();
    });
});