@echo off
REM Create NodifyGamers project structure

REM Root folder
mkdir NodifyGamers
cd NodifyGamers

REM Main files
type nul > main.py
type nul > config.py

REM UI folder and files
mkdir ui
type nul > ui\dashboard.py
type nul > ui\news_panel.py
type nul > ui\update_panel.py

REM Modules folder and files
mkdir modules
type nul > modules\game_library.py
type nul > modules\game_updates.py
type nul > modules\news_events.py
type nul > modules\download_links.py
type nul > modules\achievements.py

REM Database folder and files
mkdir database
type nul > database\db_handler.py
type nul > database\nodify.db

REM Utils folder and files
mkdir utils
type nul > utils\api_fetch.py
type nul > utils\helpers.py

echo NodifyGamers folder structure created successfully!
pause