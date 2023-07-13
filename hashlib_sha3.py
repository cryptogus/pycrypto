import hashlib

def hash_func(data):
    # hashlib 모듈을 사용하여 해시 객체를 생성합니다.
    hash_object = hashlib.sha3_256() # hash_object = hashlib.sha3_256(data.encode('utf-8')) 이렇게도 사용가능, 이러면 update해줄 필요 X

    # 데이터를 바이트로 변환하여 해시 객체에 업데이트합니다.
    hash_object.update(data.encode('utf-8'))

    # 해시 값을 반환합니다.
    return hash_object.hexdigest()

# 해시 함수를 사용하는 예시
data = input("해시할 데이터를 입력하세요: ")
hash_value = hash_func(data)
print("해시 값:", hash_value)

# shake_128 -> 출력 길이를 정해줘야함
# http://wiki.hash.kr/index.php/SHA3-256
# 테스트 가능한 사이트
# https://asecuritysite.com/hash/shake
# def calculate_shake128_hash(data, output_length):
#     # hashlib 모듈을 사용하여 SHAKE128 해시 객체를 생성합니다.
#     hash_object = hashlib.shake_128()

#     # 데이터를 바이트로 변환하여 해시 객체에 업데이트합니다.
#     hash_object.update(data.encode('utf-8'))

#     # 지정된 출력 길이로 해시 값을 가져옵니다.
#     hash_value = hash_object.digest(output_length)

#     # 해시 값을 반환합니다.
#     return hash_value.hex()

# # SHAKE128 해시 함수 사용 예시
# data = input("해시할 데이터를 입력하세요: ")
# output_length = int(input("출력 길이를 입력하세요 (비트 단위): "))

# hash_value = calculate_shake128_hash(data, output_length)
# print("해시 값:", hash_value)