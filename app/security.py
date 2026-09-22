from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
# создает объект для безопасного хеширования и проверки паролей
# с использованием актуальных и надежных алгоритмов по умолчанию


def get_password_hash(password: str):
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)
    # проверяем совпадает ли пароль из базы с хешированным
