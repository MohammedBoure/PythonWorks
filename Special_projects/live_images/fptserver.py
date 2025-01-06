from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server(ip, port, username, password, directory):
    try:
        # إعداد صلاحيات المستخدم
        authorizer = DummyAuthorizer()
        authorizer.add_user(username, password, directory, perm="elradfmw")  # الصلاحيات: القراءة والكتابة

        # تهيئة معالج الخادم
        handler = FTPHandler
        handler.authorizer = authorizer

        # إنشاء الخادم
        server = FTPServer((ip, port), handler)

        print(f"تم بدء تشغيل خادم FTP على {ip}:{port}")
        print(f"اسم المستخدم: {username}, كلمة المرور: {password}")
        print(f"المجلد المشترك: {directory}")

        # تشغيل الخادم
        server.serve_forever()

    except Exception as e:
        print(f"حدث خطأ أثناء تشغيل الخادم: {e}")


ftp_ip = "192.168.105.240"       # عنوان IP (استخدم "0.0.0.0" لجعل الخادم متاحًا للجميع)
ftp_port = 2121                  # المنفذ الذي سيتم تشغيل الخادم عليه
ftp_username = "user"            # اسم المستخدم للوصول
ftp_password = "12345"           # كلمة المرور
ftp_directory = "name"           # المجلد المشترك (سيتم استخدام مجلد محلي)

# بدء الخادم
start_ftp_server(ftp_ip, ftp_port, ftp_username, ftp_password, ftp_directory)
