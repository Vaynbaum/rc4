class Cipher:
    def __init__(self):
        self.__COUNT_PERMUTATION = 256

    def __init_s_block(self, key: str):
        """Инициализация S-блока (key-scheduling algorithm KSA)"""
        key_length = len(key)
        s_block = [i for i in range(self.__COUNT_PERMUTATION)]
        j = 0
        for i in range(self.__COUNT_PERMUTATION):
            j = (j + s_block[i] + ord(key[i % key_length])) % self.__COUNT_PERMUTATION
            s_block[i], s_block[j] = s_block[j], s_block[i]
        return s_block

    def __generationp_pseudo_random(self, s_block: list, i: int, j: int):
        """Генерация псевдослучайного слова K
        (pseudo-random generation algorithm, PRGA)"""
        i = (i + 1) % self.__COUNT_PERMUTATION
        j = (j + s_block[i]) % 256
        s_block[i], s_block[j] = s_block[j], s_block[i]
        return s_block[(s_block[i] + s_block[j]) % self.__COUNT_PERMUTATION], i, j

    def Process(self, text: str, key: str):
        s_block = self.__init_s_block(key)
        i = 0
        j = 0
        result = ""
        for ch in text:
            word, i, j = self.__generationp_pseudo_random(s_block, i, j)
            result += chr(ord(ch) ^ word)
        return result
