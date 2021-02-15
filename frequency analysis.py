#빈도수가 높은 순서로 정렬후 출력
def frequency_analysis(msg):
    fa = {}
    for c in msg:
        if c in fa:
            fa[c] += 1
        else:
            fa[c] = 1
    
    print(sorted(fa.items(), key = lambda x:x[1], reverse = True))

if __name__ == "__main__":
    msg = "53%%#..........;%?;" #암호문
    frequency_analysis(msg)