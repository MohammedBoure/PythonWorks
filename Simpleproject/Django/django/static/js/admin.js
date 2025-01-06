// دالة للتحقق من حالة تسجيل الدخول
function checkLoginStatus() {
    const isLoggedIn = localStorage.getItem("isLoggedIn") === "true"; // تحقق من حالة تسجيل الدخول

    if (!isLoggedIn) {
        // إعادة التوجيه إلى صفحة تسجيل الدخول
        window.location.href = 'http://127.0.0.1:8000/adminlogin/';
    }
}

// استدعاء الدالة عند تحميل الصفحة
window.onload = checkLoginStatus;

// إضافة مستمع الحدث لتسجيل الخروج
document.getElementById("logoutButton").addEventListener("click", function() {
    // تعيين حالة تسجيل الدخول إلى "false" في localStorage
    localStorage.setItem("isLoggedIn", "false");
    
    // إعادة التوجيه إلى صفحة تسجيل الدخول
    window.location.href = 'http://127.0.0.1:8000/adminlogin/';
});
