from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes

class Encrypt:

    def generate_key(self):
        return get_random_bytes(32)

    def generate_key_from_mkey(self, mkey, email):
        return PBKDF2(mkey, email, 32, 1000000, hmac_hash_module=SHA512)


    def create_encrypted_vault_key(self, mkey, email) -> tuple:
        vkey = self.generate_key()
        true_mkey = self.generate_key_from_mkey(mkey, email)
        cipher = AES.new(true_mkey, AES.MODE_CFB)
        iv = cipher.iv

        encrypted_vkey = cipher.encrypt(vkey)

        return encrypted_vkey, iv

    def decrypt_vault_key(self, vkey, iv, mkey):
        cipher = AES.new(mkey, AES.MODE_CFB, iv)
        return cipher.decrypt(vkey)

    def encrypt_data(self, data, vkey):
        key = self.generate_key()
        data_cipher = AES.new(key, AES.MODE_CFB)
        key_cipher = AES.new(vkey, AES.MODE_CFB)
        return data_cipher.encrypt(data), key_cipher.encrypt(key), data_cipher.iv, key_cipher.iv

    def decrypt_data(self, data, data_key, vkey, data_iv, key_iv):
        key_cipher = AES.new(vkey, AES.MODE_CFB, key_iv)
        decrypted_key = key_cipher.decrypt(data_key)
        data_cipher = AES.new(decrypted_key, AES.MODE_CFB, data_iv)
        return data_cipher.decrypt(data)

