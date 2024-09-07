import logging

# Configure logging settings
logging.basicConfig(filename='CaesarCipher.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

class CaesarCipher:

    def __init__(self):
        self.direction = ""  # Direction of encoding or decoding / エンコードまたはデコードの方向
        self.text = ""  # Text to be encoded or decoded / エンコードまたはデコードするテキスト
        self.shift = 0  # Number of positions to shift in the alphabet / アルファベットでシフトする位置の数

    def input_parameter(self):
        self.direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt and 'exit' to leave:\n"
        )
        if self.direction == 'exit':  # Check if 'exit' is entered / 'exit'が入力されたか確認
            logger.info("Exiting the program.")  # Notify user that the program is exiting / プログラムが終了することを通知
            return False  # Indicate to stop the loop / ループを停止することを示す
        if self.direction not in [
            'encode', 'decode'
        ]:  # Check if the direction is valid / 方向が有効か確認
            logger.error("Invalid direction. Please type 'encode' or 'decode'.")  # Notify user of invalid input / 無効な入力を通知
            return True  # Continue the loop to ask for input again / 再び入力を求めるためにループを続ける

        self.text = input("Type your message:\n").lower()  # Get the message and convert it to lowercase / メッセージを取得し、小文字に変換
        self.shift = int(input("Type the shift number:\n"))  # Get the shift number / シフト番号を取得
        return True  # Indicate to continue the loop / ループを続けることを示す

    def Crypto(self):
        text_chars = [i for i in self.text]  # Convert text to a list of characters / テキストを文字のリストに変換

        if self.direction == "decode":
            self.shift = -self.shift  # Adjust shift for decoding / デコードのためにシフトを調整

        result = []  # List to store the result / 結果を保存するためのリスト
        for i in range(len(text_chars)):
            if text_chars[i] in alphabet:  # Check if the character is in the alphabet / 文字がアルファベットに含まれているか確認
                current_index = alphabet.index(text_chars[i])  # Get the current index of the character / 文字の現在のインデックスを取得
                new_index = (current_index + self.shift) % len(alphabet)  # Calculate the new index / 新しいインデックスを計算
                result.append(alphabet[new_index])  # Append the shifted character to the result / シフトされた文字を結果に追加
            else:
                result.append(text_chars[i])  # Append non-alphabet characters without changes / 非アルファベット文字を変更せずに追加

        return ''.join(result)  # Join the list into a single string and return it / リストを1つの文字列に結合して返す

if __name__ == "__main__":
    cipher = CaesarCipher()
    logger.info('Started')
    while True:  # Loop to continue until 'exit' is entered / 'exit'が入力されるまでループを続ける
        if not cipher.input_parameter():  # Check if the loop should stop / ループを停止するか確認
            break
        result = cipher.Crypto()  # Execute the cipher operation / 暗号化操作を実行
        logger.info(f'Result: {result}')  # Log the result / 結果を記録
        print(f'Result: {result}')  # Also print the result to the console / コンソールに結果を表示
