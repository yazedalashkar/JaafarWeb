@echo off
title صالة جعفر لألعاب البلايستيشن والتوقيت
chcp 65001 >nul
cls
echo ========================================================
echo        صالة جعفر لألعاب البلايستيشن والتوقيت
echo ========================================================
echo.
echo جاري بدء تشغيل النظام...
echo.
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [OK] تم تشغيل خادم محلي ثابت على http://localhost:8080
    start http://localhost:8080/index.html
    python -m http.server 8080
) else (
    echo [OK] جاري فتح التطبيق مباشرة بالمتصفح الافتراضي...
    start index.html
)
