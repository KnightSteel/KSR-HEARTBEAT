@echo off
:: 1. Lanzamos el motor de la AURA en segundo plano
start /b python app.py

:: 2. Tiempo de gracia para que el socket 9999 se active
timeout /t 5 /nobreak > nul

:: 3. Abrimos con BRAVE en Modo App (Limpio, Senior, Seguro)
:: Nota: Si tu Brave está en otra ruta, solo ajusta el path.
start "" "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --app=http://localhost:9999 --window-size=1200,800

exit