#chapter 4_data structure
#problem_14_hash 동명이인

# hashing with dictionary
def find_same_name(a):
    """
    두 번 이상 나온 이름 찾기
    입력 : 이름 n개 들어있는 리스트 a
    출력 : n개 중 반복되는 이름의 집합
    """
    name_dict = {}
    for name in a:
        name_dict[name] = name_dict.get(name,0) + 1
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))
# Tom

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))
# Tom, Mike

# exercise 14-1
def name_return(info,num):
    """
    학생 번호로 이름 찾기
    입력 : 번호와 이름으로 구성된 딕셔너리 info
    출력 : 이름 혹은 없을 경우 ?
    """
    try:
        return info[num]
    except:
        return "?"

num_hum = {39: "Justin", 14:"John", 67:"Mike", 105:"Summer"}
print(name_return(num_hum,105))
# Summer
print(name_return(num_hum,777))
# ?