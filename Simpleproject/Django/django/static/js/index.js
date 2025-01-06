// القائمة التي تحتوي على المنتجات
const products = [

];

// دالة لإنشاء بطاقات المنتجات
function createProductCards() {
    const productContainer = document.getElementById("productContainer");

    // تكرار العناصر في القائمة لإنشاء بطاقة لكل منتج
    products.forEach(product => {
        const productCard = document.createElement("div");
        productCard.className = "product";

        // إضافة الصورة
        const image = document.createElement("img");
        image.src = product.imageUrl;
        productCard.appendChild(image);

        // إضافة اسم المنتج
        const productName = document.createElement("h3");
        productName.textContent = product.name;
        productCard.appendChild(productName);

        // إضافة زر للانتقال إلى صفحة المنتج
        const button = document.createElement("button");
        button.textContent = "عرض التفاصيل";
        button.onclick = () => {
            window.location.href = product.pageUrl; // توجيه المستخدم عند النقر
        };
        productCard.appendChild(button);

        productContainer.appendChild(productCard);
    });
}

// استدعاء الدالة لإنشاء بطاقات المنتجات
createProductCards();
