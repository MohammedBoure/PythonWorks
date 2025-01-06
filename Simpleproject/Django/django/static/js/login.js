document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // منع إعادة تحميل الصفحة

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // تحقق من اسم المستخدم وكلمة المرور
    if (username === "Pluto" && password === "K3cZE4tu") {
        // إذا كانت صحيحة، تخزين حالة تسجيل الدخول
        localStorage.setItem("isLoggedIn", "true");
        // إعادة التوجيه إلى لوحة التحكم
        window.location.href = "http://127.0.0.1:8000/admin"; // توجيه المستخدم إلى الرابط المطلوب
    } else {
        alert("اسم المستخدم أو كلمة المرور غير صحيحة!");
    }
});
