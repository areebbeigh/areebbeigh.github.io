echo '> Building...'
python3 build.py

watchmedo shell-command \
    --patterns="*.jinja2;*.css;*.svg;*.html" \
    --command='echo "\n> Changes detected, rebuilding..."; \
                echo "> File: ${watch_src_path}"; \
                python3 build.py; \
                echo "> Watching for changes";' \
    --recursive \
    --ignore-pattern="output/**" \
    --drop
