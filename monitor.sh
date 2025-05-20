#!/bin/bash

# Przejdź do katalogu projektu
cd /home/maple/projects/computer_performance_project

# Aktywuj środowisko venv
source venv/bin/activate

# Uruchom skrypt
python main.py >> /home/maple/projects/computer_performance_project/monitor_log.log 2>&1

#cronjob: */1 * * * * /home/maple/projects/computer_performance_project/monitor.sh