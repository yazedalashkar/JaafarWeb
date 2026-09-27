@echo off
title ساحة الأساطير لألعاب البلايستيشن والتوقيت
chcp 65001 >nul
cls

:: الانتقال فوراً إلى مجلد المشروع لضمان عمل الاختصارات من سطح المكتب
cd /d "%~dp0"

echo ========================================================
echo        ساحة الأساطير لألعاب البلايستيشن والتوقيت
echo ========================================================
echo.
echo جاري فحص البيئة وتأمين نظام الحفظ التلقائي...
echo.

:: 1. فحص هل يوجد بايثون محمول داخل المجلد نفسه (بدون تثبيت)
if exist "%~dp0python\python.exe" (
    echo [OK] تم تشغيل الخادم عبر نسخة بايثون المحمولة المدمجة!
    echo [رابط التشغيل]: http://localhost:8080/index.html
    echo [ملف الحفظ الفعلي]: data.json
    start http://localhost:8080/index.html
    "%~dp0python\python.exe" server.py
    goto end
)

:: 2. فحص هل بايثون مثبت على نظام الويندوز
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [OK] تم تشغيل الخادم والحفظ التلقائي المباشر على القرص!
    echo [رابط التشغيل]: http://localhost:8080/index.html
    echo [ملف الحفظ الفعلي]: data.json
    start http://localhost:8080/index.html
    python server.py
    goto end
)

:: 3. في حال عدم وجود بايثون نهائياً، يفتح التطبيق مباشرة في المتصفح ويعمل عبر localStorage
echo [ملاحظة] بايثون غير مثبت، يعمل التطبيق فورا ومحليا 100%% عبر ذاكرة التخزين الدائمة...
start index.html

:end
