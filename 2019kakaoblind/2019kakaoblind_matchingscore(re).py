# re 파싱 사용. 내일 아침에 다시 해볼것
# re 파싱은 정규식 분리에서 여러가지로 사용 될 수 있음
# https://geonlee.tistory.com/84
# https://brownbears.tistory.com/506 re 모듈 사용법
import re
def solution(word, pages):
    answer =0
    meta_parser = re.compile('<meta(.+?)/>')
    a_parser = re.compile('<a(.+?)>')  #compile이 정규 표현을 정하는 것 
    page_infos= []
    page_dict = dict()
    link_dict = dict()
    out_links = []
    basic_score = []
    word = word.upper()
    cnt = -1
    for page in pages:
        cnt = cnt +1
        a_tags= a_parser.findall(page) #findall이 적용시켜서 찾는거 이걸로 찾으니까 <a > 는 날아가버림
        out_link = []
        for a_tag in a_tags :
            a_lines = a_tag.split('"') # ("\"") 로도 가능하다
            for a_line in a_lines :
                if re.search('https://' , a_line) :
                    out_link.append(a_line)
        out_links.append(out_link)


        my_tags= meta_parser.findall(page) #findall이 적용시켜서 찾는거
        for my_tag in my_tags :
            my_lines = my_tag.split('"') # ("\"") 로도 가능하다
            
            for i in range(1,len(my_lines)) :
                if re.search('https://' , my_lines[i]) and re.search('content' , my_lines[i-1]) :
                    page_infos.append(my_lines[i])
        wcnt =0
        page = page.upper()
        page = re.sub('[^A-Z]','.',page) #교체하는것 ^는 그것이 아닌 것
        page = page.split('.')
        for kia in page :
            if kia == word :
                wcnt= wcnt+1
        
        basic_score.append(wcnt) 
        
        page_dict.update({page_infos[cnt] : basic_score[cnt]})
        if len(out_links[cnt]) != 0 :
            link_dict.update({page_infos[cnt] : basic_score[cnt] / len(out_links[cnt]) })
        else :
            link_dict.update({page_infos[cnt] : 0  })



    for i in range(len(out_links)) :
        now_page = page_infos[i]
        for out_link in out_links[i] :

            if page_dict.get(out_link) != None :
                page_dict.update({out_link : (page_dict.get(out_link) + link_dict.get(now_page))})

    maxscore = 0 
    for i in range(len(page_infos)) :
        if maxscore < page_dict.get(page_infos[i]) :
            maxscore = page_dict.get(page_infos[i])
            answer = i
    return answer


solution(	"Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])