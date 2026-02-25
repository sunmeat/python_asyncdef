from django.apps import AppConfig


class weatherConfig(AppConfig): # створюємо клас конфігурації додатку, який успадковує AppConfig
    name = 'weather' # вказуємо ім'я додатку, яке має відповідати назві папки з додатком
    # це потрібно для того, щоб Django міг знайти цей додаток і зареєструвати його в системі