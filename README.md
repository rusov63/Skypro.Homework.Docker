## Модуль 8 от SkyPro. Docker. Для работы используется Linux Manjaro

## 27.2. Docker Compose. Домашние задание
### (ветка 27.2._HW_Docker_Compose)

### Реализовано в проекте:

#### 1. Установлен Docker, docker compose. 
        - sudo pacman -Syu
        - sudo pacman -S docker
            - docker --version
        - sudo pacman -S docker compose 
            - docker-compose --version

#### 2. Создан и описан в корне проекта: Dockerfile, docker-compose.yaml
        - python:3.11-slim-buster

#### 3. Собран образ и запущен контейнер
        - docker-compose build
        - docker-compose up

#### 4. Запуск проекта одной командой
        - docker-compose up -d --build

#### 5. Проверяем проект на работоспособность
        - localhost:8000