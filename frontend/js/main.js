$(function () {
    //新增project中“+”图片的点击事件
    $(".add_pro_img").click(function () {
        $(".add_pro").addClass("show");
    });
    //填写新增project的form表单中“X”图片的点击事件
    $(".cancel_add_pro_img").click(function () {
        $(".add_pro").removeClass("show");
    });
    //填写新增project的form表单中“提交”按钮的点击事件
    $("#project_submit").click(function () {
        $(".add_pro").removeClass("show");
    });
    //
    $(".left_menu h3").click(function () {
        $(this).next().toggleClass("show");
    });
});