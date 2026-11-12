@echo off
echo Запуск проекта АСКУЭ-Лайт...
echo Открывается Git Bash и запускаются все сервисы.

start "" "C:\Program Files\Git\git-bash.exe" -c "cd ~/askue-gitbash && bash start_all.sh"
