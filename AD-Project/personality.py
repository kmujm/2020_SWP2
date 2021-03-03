bestpartner = {'ESTJ' :	'INTP', 'ENTJ' : 'INFP', 'ENTP' : 'INFJ', 'ENFP' : 'INTJ', 'ISTJ' :	'ESFP', 'ESFJ' : 'ISTP',
               'ENFJ' : 'ISFP', 'ESTP' : 'ISFJ'}

bestpartner.update({value : key for key, value in bestpartner.items()})

info = [{"MBTI" : "ESTJ", "ability" : "\'일처리하기\'", "character" : "\"자뻑 일잘러\"", "filename" : "jabbeok"},
        {"MBTI" : "ENTJ", "ability" : "\'일벌이기\'", "character" : "\"워커홀릭 야근요정\"", "filename" : "workaholic"},
        {"MBTI" : "ENTP", "ability" : "\'이기기\'", "character" : "\"까칠한 나르시스트\"", "filename" : "lovemyself"},
        {"MBTI" : "ENFP", "ability" : "\'기웃거리기\'", "character" : "\"성수동 갬성 힙스터\"", "filename" : "hipsters"},
        {"MBTI" : "INFP", "ability" : "\'멍때리기\'", "character" : "\"방구석 몽상가\"", "filename" : "ilovemyhome"},
        {"MBTI" : "ISTJ", "ability" : "\'돈세기\'", "character" : "\"시크한 머니콜렉터러\"", "filename" : "showmethemoney"},
        {"MBTI" : "ESFJ", "ability" : "\'메시지보내기\'", "character" : "\"섬세한 프로디엠러\"", "filename" : "prodmer"},
        {"MBTI" : "ENFJ", "ability" : "\'부추기기\'", "character" : "\"열정 만수르\"", "filename" : "ihatedaechung"},
        {"MBTI" : "INFJ", "ability" : "\'꿰둟어보기\'", "character" : "\"수줍은 궁예\"", "filename" : "shy"},
        {"MBTI" : "INTJ", "ability" : "\'한우물파기\'", "character" : "\"혼자 심각한 지식인 \"", "filename" : "whysoserious"},
        {"MBTI" : "INTP", "ability" : "\'뼈때리기\'", "character" : "\"팩폭 마스터\"", "filename" : "hitthebone"},
        {"MBTI" : "ISFP", "ability" : "\'눈치보기\'", "character" : "\"땀많은 아티스트\"", "filename" : "sweatingartist"},
        {"MBTI" : "ISTP", "ability" : "\'손쓰기\'", "character" : "\"망치든 예술가\"", "filename" : "artistwithhammer"},
        {"MBTI" : "ESTP", "ability" : "\'돈쓰기\'", "character" : "\"욜로 소비엔젤\"", "filename" : "takemymoney"},
        {"MBTI" : "ISFJ", "ability" : "\'좋아요누르기\'", "character" : "\"좋아요 인간봇\"", "filename" : "likeit"},
        {"MBTI" : "ESFP", "ability" : "\'잘먹고 잘자기\'", "character" : "\"코노 매니아\"", "filename" : "4songs1000won"}
]



def find(mbti):
    for i in range(len(info)):
        if info[i]["MBTI"] == mbti:
            return i

def getTextfile(idx):
    return info[idx]["filename"] + '.txt'
