#!/bin/bash

export $(grep -v '^#' .env | xargs)

# Przejdź do katalogu projektu
cd $PROJECT_PATH

# Aktywuj środowisko venv
source venv/bin/activate

# Uruchom skrypt
python main.py >> $PROJECT_PATH/monitor_log.log 2>&1

