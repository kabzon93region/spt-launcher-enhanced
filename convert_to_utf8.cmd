@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ========================================
echo    Конвертация файлов в UTF-8
echo ========================================
echo.

REM Проверяем наличие PowerShell
powershell -Command "Write-Output 'PowerShell доступен'" >nul 2>&1
if errorlevel 1 (
    echo [ОШИБКА] PowerShell не найден или недоступен!
    echo Убедитесь, что PowerShell установлен и доступен.
    pause
    exit /b 1
)

echo PowerShell найден, начинаем работу...
echo.

REM Определяем расширения текстовых файлов
set "extensions=.txt .md .cs .h .cpp .c .css .py .js .json .xml .html .htm .php .sql .ini .cfg .conf .log .bat .cmd .ps1 .sh .yaml .yml .toml .ini .properties .env .gitignore .dockerfile .dockerignore .editorconfig .eslintrc .prettierrc .babelrc .ts .tsx .jsx .vue .svelte .astro .rs .go .java .kt .scala .rb .pl .lua .r .m .swift .dart .elm .clj .hs .ml .fs .vb .pas .asm .s .S .cc .cxx .hpp .hxx .c++ .h++ .csproj .sln .vcxproj .vcproj .filters .user .props .targets .resx .xaml .axaml .config .app.config .web.config .packages.config .nuspec .csproj.user .sln.DotSettings .ruleset .editorconfig .gitattributes .gitmodules .travis.yml .appveyor.yml .azure-pipelines.yml .github/workflows/*.yml .github/workflows/*.yaml .vscode/settings.json .vscode/launch.json .vscode/tasks.json .vscode/extensions.json .vscode/snippets/*.json .idea/*.xml .idea/*.iml .idea/workspace.xml .idea/tasks.xml .idea/encodings.xml .idea/compiler.xml .idea/misc.xml .idea/modules.xml .idea/vcs.xml .idea/inspectionProfiles/*.xml .idea/scopes/*.xml .idea/dictionaries/*.xml .idea/shelf/*.xml .idea/libraries/*.xml .idea/artifacts/*.xml .idea/runConfigurations/*.xml .idea/dataSources/*.xml .idea/dataSources.ids .idea/dataSources.local.xml .idea/sqlDataSources.xml .idea/dynamic.xml .idea/uiDesigner.xml .idea/encodings.xml .idea/compiler.xml .idea/misc.xml .idea/modules.xml .idea/vcs.xml .idea/inspectionProfiles/*.xml .idea/scopes/*.xml .idea/dictionaries/*.xml .idea/shelf/*.xml .idea/libraries/*.xml .idea/artifacts/*.xml .idea/runConfigurations/*.xml .idea/dataSources/*.xml .idea/dataSources.ids .idea/dataSources.local.xml .idea/sqlDataSources.xml .idea/dynamic.xml .idea/uiDesigner.xml"

REM Счетчики
set /a total_files=0
set /a converted_files=0
set /a skipped_files=0
set /a error_files=0

echo Начинаем сканирование файлов...
echo.

REM Создаем временную папку для резервных копий
if not exist "utf8_backup" mkdir "utf8_backup"

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

REM Пытаемся конвертировать файл в UTF-8
powershell -Command "& {
    try {
        $filePath = '!file_path!'
        $content = Get-Content -Path $filePath -Raw -Encoding Default
        $utf8Content = [System.Text.Encoding]::UTF8.GetString([System.Text.Encoding]::Default.GetBytes($content))
        $utf8Bytes = [System.Text.Encoding]::UTF8.GetBytes($utf8Content)
        [System.IO.File]::WriteAllBytes($filePath, $utf8Bytes)
        Write-Output 'SUCCESS'
    } catch {
        Write-Output 'ERROR'
    }
}" >temp_result.txt 2>nul

REM Читаем результат
set "result="
if exist temp_result.txt (
    set /p result=<temp_result.txt
    del temp_result.txt >nul 2>&1
)

if "!result!"=="SUCCESS" (
    echo [OK] Конвертирован: !file_path!
    set /a converted_files+=1
) else (
    echo [ОШИБКА] Не удалось конвертировать: !file_path!
    set /a error_files+=1
    REM Восстанавливаем из резервной копии
    copy "!backup_path!" "!file_path!" >nul 2>&1
)

goto :eof

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
