scoreList = [
    {"name":"홍길동", "kor":90, "eng":80, "mat":90},
    {"name":"둘리", "kor":100, "eng":40, "mat":90},
    {"name":"임꺽정", "kor":100, "eng":100, "mat":100},
    {"name":"장길산", "kor":70, "eng":60, "mat":70},
    {"name":"도우너", "kor":90, "eng":80, "mat":90},
]

#총점, 평균, 학점
def process(score):
    score["total"] = score["kor"] + score["eng"] + score ["mat"]
    score["avg"] = round(score["total"] / 3, 2)
    score["grade"]=""
    if score["avg"]>=90:
        score["grade"]='수'
    elif score["avg"]>=80:
        score["grade"]='우'
    elif score["avg"]>=70:
        score["grade"]='미'
    elif score["avg"]>=60:
        score["grade"]='양'
    else:
        score["grade"]='가'

#한명만 출력
def output(s):
    print(f"{s['name']}", end=' ')
    print(f"{s['kor']}", end=' ')
    print(f"{s['eng']}", end=' ')
    print(f"{s['mat']}", end=' ')
    print(f"{s['total']}", end=' ')
    print(f"{s['avg']}", end=' ')
    print(f"{s['grade']}")

def processAll():
    for score in scoreList:
        process(score)
    
def outputAll():
    for score in scoreList:
        output(score)

processAll()
outputAll()

#검색함수
def search():
    name = input("찾을이름 : ")
    #result = list( filter(lambda x : x["name"]==name, scoreList))
    result = [x for x in scoreList if x["name"]==name]
    if len(result)==0:
        print(f"{name}을 찾을 수 없습니다")
        return
     
    for item in result:
        output(item)

#수정
def modify():
    name = input("수정할 이름 : ")
    result = [x for x in scoreList if x["name"]==name]
    if len(result)==0:
        print(f"{name}을 찾을 수 없습니다")
        return
     
    result[0]['name']=input("바꿀 이름은 : ")
    result[0]['kor']=input("국어 : ")
    result[0]['eng']=input("영어 : ")
    result[0]['mat']=input("수학 : ")
    process(result[0]) #다시 계산하기 - 총점하고 평균을
    
#삭제
def delete():
    name = input("삭제할 이름 : ")
    result = [x for x in scoreList if x["name"]==name]
    if len(result)==0:
        print(f"{name}을 찾을 수 없습니다")
        return
    
    scoreList.remove(result[0])
    
#search()
#modify()
#delete
#outputAll()

def sort():
    sel = input("1.이름 2.총점 3.국어성적 ")
    if sel=="1":
        key="name"
        reverse=False
    elif sel=="2":
        key="total"
        reverse=True
    else:
        reverse=True
        key="kor"
    
    sortedList = sorted(scoreList, key=lambda score:score[key])
    for s in sortedList:
        output(s)

def append():
    score = dict()  #score {}
    score ["name"]=input('이름 : ')
    score ["kor"]=input('국어 : ')
    score ["eng"]=input('영어 : ')
    score ["mat"]=input('수학 : ')
    process(score)
    scoreList.append( score )
    
def menuDisplay():
    menus = ['1.추가', '2.출력', '3.검색', '4.수정', '5.삭제', '6.정렬', '0.종료']
    for menu in menus:
        print(menu)
        
def start():
    functionList = [None, append, outputAll,search, modify, delete, sort]
    processAll()
    while True:
        menuDisplay()
        sel = int(input('선택 : '))
        if sel<1 or sel>len(functionList):
            print('프로그램을 종료합니다')
            return #함수종료
        
        functionList[sel]() #함수호출
        
start()
