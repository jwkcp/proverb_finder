import sys
import os


def file_to_wordmatrix(file_path):
    """
    일반 문자열로 되어 있는 파일을 입력받아서 2차원 배열을 만듭니다.
    """
    # 경로가 유효하지 않거나 공백이면 실패
    if not file_path or file_path == "":
        return false

    word_matrix = None

    # 파일을 읽어 2차원 배열을 만듭니다.
    with open(file_path, 'r') as f:
        lines = f.readlines()

        word_matrix = [[ch for ch in line.strip()] for line in lines]

    return word_matrix


def find_sentence(target):
    """
    속담 사전에서 일치 문자열을 찾습니다.
    """
    wl = len(target)

    # 찾은 결과
    results = {}

    # 대각선 찾기(LR, 왼쪽 위에서 오른쪽 아래로 탐색)
    for col in range(cols-1, -1, -1):
        # 길이 자체가 안되므로 통과
        if cols-col < wl - 1:
            continue

        tmp_word = ""
        for step in range(0, cols - col + 1):
            try:
                tmp_word += word_matrix[step][col+step]
            except:
                # 대각선 탐색 시 인덱스 벗어날 경우 무시
                pass

        if target in tmp_word:
            results[target] = "대각선LR/정방향:{}번째 줄 중".format(col)
        elif target in tmp_word[::-1]:
            results[target] = "대각선LR/역방향:{}번째 줄 중".format(col)
        else:
            pass

    for row in range(1, rows):
        tmp_word = ""
        for step in range(0, cols):
            try:
                tmp_word += word_matrix[row+step][step]
            except Exception as e:
                # 대각선 탐색 시 인덱스 벗어날 경우 무시
                pass

        if target in tmp_word:
            results[target] = "대각선LR/정방향:{}번째 줄 중".format(col)
        elif target in tmp_word[::-1]:
            results[target] = "대각선LR/역방향:{}번째 줄 중".format(col)
        else:
            pass

    # 대각선 찾기(RL - 오른쪽 위에서 왼쪽 아래로 탐색)
    for col in range(0, cols):
        # 길이 자체가 안되므로 통과
        if col < wl - 1:
            continue

        tmp_word = ""
        for step in range(0, col + 1):
            try:
                tmp_word += word_matrix[step][col-step]
            except:
                # 대각선 탐색 시 인덱스 벗어날 경우 무시
                pass

        if target in tmp_word:
            results[target] = "대각선RL/정방향:{}번째 줄 중".format(col)
        elif target in tmp_word[::-1]:
            results[target] = "대각선RL/역방향:{}번째 줄 중".format(col)
        else:
            pass

    for row in range(1, rows):
        tmp_word = ""
        for step in range(0, cols):
            try:
                tmp_word += word_matrix[row+step][cols-step-1]
            except Exception as e:
                # 대각선 탐색 시 인덱스 벗어날 경우 무시
                pass

        if target in tmp_word:
            results[target] = "대각선RL/정방향:{}번째 줄 중".format(col)
        elif target in tmp_word[::-1]:
            results[target] = "대각선RL/역방향:{}번째 줄 중".format(col)
        else:
            pass

    # 가로 찾기
    for row in range(0, rows):
        for col in range(0, cols-wl+1):
            tmp_word = ""
            for j in range(wl):
                tmp_word += word_matrix[row][col+j]

            if target in tmp_word:
                results[target] = "가로/정방향:({}, {})".format(row+1, col+1)
            elif target in tmp_word[::-1]:
                results[target] = "가로/역방향:({}, {})".format(row+1, col+1)
            else:
                pass

    # 세로 찾기
    for col in range(0, cols):
        for row in range(0, rows-wl+1):
            tmp_word = ""
            for j in range(wl):
                tmp_word += word_matrix[row+j][col]

            if target in tmp_word:
                results[target] = "세로/정방향:({}, {})".format(row+1, col+1)
            elif target in tmp_word[::-1]:
                results[target] = "세로/역방향:({}, {})".format(row+1, col+1)
            else:
                pass

    return results


try:
    if len(sys.argv) < 3:
        print("Usage: find_sentence.py SOURCE_FILE_PATH DICTIONARY_FILE_PATH")
        sys.exit()

    word_matrix_file_path = sys.argv[1]
    dict_file_path = sys.argv[2]

    if not word_matrix_file_path:
        print("가로 세로 단어 매트릭스가 올바르지 않습니다.")
        sys.exit()

    if not os.path.exists(os.path.abspath(word_matrix_file_path)):
        print("가로 세로 단어 매트릭스 파일을 찾을 수 없습니다.")
        sys.exit()

    if not dict_file_path:
        print("사전 매트릭스가 올바르지 않습니다.")
        sys.exit()

    if not os.path.exists(os.path.abspath(dict_file_path)):
        print("사전 매트릭스 파일을 찾을 수 없습니다.")
        sys.exit()

    # 가로 세로 단어 매트릭스 생성
    word_matrix = file_to_wordmatrix(word_matrix_file_path)

    rows = len(word_matrix)
    cols = len(word_matrix[0])

    # 찾은 결과
    results = {}

    # 사전에서 검사
    with open('./dict.txt', 'r') as f:
        lines = f.readlines()
        lines_cnt = len(lines)

        for idx, line in enumerate(lines):
            line = line.strip()

            if line and line != "":
                results.update(find_sentence(line))
                print("{}/{} [{}] 속담 검사 중...".format(idx + 1, lines_cnt, line))

    # 결과
    print("\n\n________________________ 결과 {}________________________\n".format(
        len(results)))

    for idx, key in enumerate(results.keys()):
        print("{:3}) {:30}\t\t{}".format(idx + 1, key, results[key]))

except Exception as e:
    print(e)
