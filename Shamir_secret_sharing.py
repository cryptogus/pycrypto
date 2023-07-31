"""
Reference
https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing
https://ehdvudee.tistory.com/27
https://cryptography.fandom.com/wiki/Shamir%27s_Secret_Sharing#Usage
"""
"""
pip install pycryptodome
pycryptodome 라이브러리에 구현되어있는 Secret Sharing Schemes 이용방법
https://www.pycryptodome.org/src/protocol/ss
"""
import random
import pandas as pd

def float_to_fixed_point(value, precision):
    return int(value * (10 ** precision))

def fixed_point_to_float(value, precision):
    return float(value) / (10 ** precision)

def generate_polynomial(secret, threshold, prime):
    coefficients = [secret] + [random.randint(1, prime - 1) for _ in range(threshold - 1)]
    return coefficients

def evaluate_polynomial(coefficients, x, prime):
    result = 0
    for i in range(len(coefficients)):
        result = (result + coefficients[i] * pow(x, i, prime)) % prime
    return result

def split_secret(secret, num_shares, threshold, prime, precision):
    if threshold > num_shares:
        raise ValueError("Threshold should be less than or equal to the number of shares.")
    
    scaled_secret = float_to_fixed_point(secret, precision)
    coefficients = generate_polynomial(scaled_secret, threshold, prime)
    # print(f"coefficients: {coefficients}")
    shares = [(i, evaluate_polynomial(coefficients, i, prime)) for i in range(1, num_shares + 1)]
    # print(f"shares: {shares}")
    return shares

def reconstruct_secret(shares, prime, precision):
    if len(shares) < 4:
        raise ValueError("At least 4 shares are required for reconstruction.")
    
    x_values, y_values = zip(*shares) # unzip
    secret = 0
    for i in range(len(shares)):
        numerator, denominator = 1, 1
        for j in range(len(shares)):
            if i != j:
                numerator = (numerator * (0 - x_values[j])) % prime
                denominator = (denominator * (x_values[i] - x_values[j])) % prime
        secret = (secret + (y_values[i] * numerator * pow(denominator, -1, prime)) % prime) % prime
    # print("secret",secret)
    return fixed_point_to_float(secret, precision)

# def read_excel_data(file_path, sheet_name):
#     try:
#         # 엑셀 파일 읽기
#         df = pd.read_excel(file_path, sheet_name=sheet_name)
#         return df
#     except Exception as e:
#         print("Error occurred while reading the Excel file:", e)
#         return None
    
if __name__ == "__main__":
    prime = 25190923363   # A large prime number
    secret1 = 36.9357309  # Latitude
    secret2 = 127.0430941 # Longitude
    num_shares = 5    # Number of shares to generate
    threshold = 4     # Number of shares required to reconstruct the secret
    precision = 8     # Turns a secret into an integer, but smaller than prime (float 자료형을 정수로 바꿔준 후 복구할 때 다시 float형으로)

    shares1 = split_secret(secret1, num_shares, threshold, prime, precision) # Create shares
    print("Shares:", shares1)
    
    selected_shares = random.sample(shares1, threshold) # Select shares
    reconstructed_secret = reconstruct_secret(selected_shares, prime, precision)
    print("Reconstructed Secret:", reconstructed_secret)
    
    # shares2 = split_secret(secret2, num_shares, threshold, prime, precision)
    # print("Shares:", shares2)

    # selected_shares = random.sample(shares2, threshold)