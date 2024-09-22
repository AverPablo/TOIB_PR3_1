import hashlib

def hash_password(password):
    password_bytes = password.encode('utf-8') #преобразуем строку пароля в байтовый формат, который необходим для хеширования.
    hash = hashlib.sha256(password_bytes) #cоздаем объект хеша с использованием алгоритма SHA-256.
    password_hash = hash.hexdigest() #Получаем шестнадцатеричное представление хеша.
    return password_hash

password = input("Введите пароль: ")
hashed_password = hash_password(password)
print(f"Хешированное представление пароля: {hashed_password}")