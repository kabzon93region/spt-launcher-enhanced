@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ========================================
echo    Конвертация файлов в UTF-8 (Simple)
echo ========================================
echo.

REM Определяем расширения текстовых файлов
set "extensions=.txt .md .cs .h .cpp .c .css .py .js .json .xml .html .htm .php .sql .ini .cfg .conf .log .bat .cmd .ps1 .sh .yaml .yml .toml .properties .env .gitignore .dockerfile .dockerignore .editorconfig .eslintrc .prettierrc .babelrc .ts .tsx .jsx .vue .svelte .astro .rs .go .java .kt .scala .rb .pl .lua .r .m .swift .dart .elm .clj .hs .ml .fs .vb .pas .asm .s .S .cc .cxx .hpp .hxx .c++ .h++ .csproj .sln .vcxproj .vcproj .filters .user .props .targets .resx .xaml .axaml .config .app.config .web.config .packages.config .nuspec .csproj.user .sln.DotSettings .ruleset .editorconfig .gitattributes .gitmodules .travis.yml .appveyor.yml .azure-pipelines.yml"

REM Счетчики
set /a total_files=0
set /a converted_files=0
set /a skipped_files=0
set /a error_files=0

echo Начинаем сканирование файлов...
echo.

REM Создаем временную папку для резервных копий
if not exist "utf8_backup" mkdir "utf8_backup"

REM Основной цикл сканирования
echo Сканируем файлы в текущей директории и подпапках...
for /r %%f in (*) do (
    call :convert_file "%%f"
)

REM Если не найдено файлов, попробуем другой способ
if %total_files%==0 (
    echo Попытка альтернативного сканирования...
    for /r . %%f in (*.*) do (
        call :convert_file "%%f"
    )
)

echo.
echo ========================================
echo           РЕЗУЛЬТАТЫ КОНВЕРТАЦИИ
echo ========================================
echo Всего файлов обработано: %total_files%
echo Успешно конвертировано: %converted_files%
echo Пропущено (не текстовые): %skipped_files%
echo Ошибок: %error_files%
echo.
echo Резервные копии сохранены в папке: utf8_backup
echo.

REM Предлагаем удалить резервные копии
set /p "delete_backup=Удалить резервные копии? (y/n): "
if /i "!delete_backup!"=="y" (
    rmdir /s /q "utf8_backup" 2>nul
    echo Резервные копии удалены.
) else (
    echo Резервные копии сохранены в папке utf8_backup
)

echo.
echo Конвертация завершена!
pause

REM Функция для проверки, является ли файл текстовым
:is_text_file
set "file_ext=%~x1"
set "is_text=0"
for %%e in (%extensions%) do (
    if /i "!file_ext!"=="%%e" set "is_text=1"
)
goto :eof

REM Функция для конвертации файла
:convert_file
set "file_path=%~1"
set "file_name=%~nx1"
set "file_dir=%~dp1"

REM Пропускаем системные файлы и папки
if /i "!file_name!"=="convert_to_utf8.cmd" goto :eof
if /i "!file_name!"=="convert_to_utf8_simple.cmd" goto :eof
if /i "!file_name!"=="utf8_backup" goto :eof
if /i "!file_name!"==".git" goto :eof
if /i "!file_name!"=="node_modules" goto :eof
if /i "!file_name!"=="bin" goto :eof
if /i "!file_name!"=="obj" goto :eof
if /i "!file_name!"==".vs" goto :eof
if /i "!file_name!"==".idea" goto :eof

REM Проверяем, является ли файл текстовым
call :is_text_file "!file_path!"
if "!is_text!"=="0" goto :eof

set /a total_files+=1

REM Создаем резервную копию
set "backup_path=utf8_backup\!file_name!.backup"
copy "!file_path!" "!backup_path!" >nul 2>&1
if errorlevel 1 (
    echo [ОШИБКА] Не удалось создать резервную копию: !file_path!
    set /a error_files+=1
    goto :eof
)

REM Простая конвертация через type и перенаправление
type "!file_path!" > "!file_path!.tmp" 2>nul
if errorlevel 1 (
    echo [ОШИБКА] Не удалось прочитать файл: !file_path!
    set /a error_files+=1
    goto :eof
)

REM Заменяем оригинальный файл
move "!file_path!.tmp" "!file_path!" >nul 2>&1
if errorlevel 1 (
    echo [ОШИБКА] Не удалось заменить файл: !file_path!
    set /a error_files+=1
    REM Восстанавливаем из резервной копии
    copy "!backup_path!" "!file_path!" >nul 2>&1
) else (
    echo [OK] Конвертирован: !file_path!
    set /a converted_files+=1
)

goto :eof
