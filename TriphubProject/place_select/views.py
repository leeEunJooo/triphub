from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.

def place_select(request):
    return render(request , 'place_select.html')


def attraction(request):
    attraction_get = []
    total = {}
    if request.method == 'GET':
        pick = request.GET['select_place']
        
                
        req = requests.get('https://m.search.naver.com/search.naver?where=m&query=%EC%A0%84%EA%B5%AD+%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&x_trv=Ml8wMF8wXw%3D%3D&sm=mtb_trv')
        html = req.text
        soup = bs(html, 'html.parser')

        divs = soup.findAll('div' , {"class" : "map_marker"})
        

        for div in divs:
            
            links = div.find_all('a', {'href':True})
            
            for link in links:
                linkname = link.findAll('span' , {'class' : 'spot'})
        
                for yo in linkname:
                    name_only = yo.text
            
                    if name_only == pick:
                    
                        req2 = requests.get("https://m.search.naver.com"+link['href'])
                        html2 = req2.text

                        soup2 =bs(html2,'html.parser')

                        attractions = soup2.findAll('div' , {'class' : 'info'})
                        
                        for attraction in attractions:
                            attraction_name = attraction.find_all('strong' ,{'class' : 'tit'})
                            introduction= attraction.find_all('span' ,{'class' : 'txt'})
                            
                            for i,v in zip(attraction_name,introduction):
                                total[i.text]=v.text

                        

    return render(request , 'place_select.html' , {'attraction' : total, 'value' : pick})




def next_select_page(request):
    if request.method == 'GET':
        pick = request.GET['hi']
        
        return render(request , 'next_select/' + pick + '.html' ,{'value' : pick})



def attraction2(request):
    attraction_get = []
    total = {}

    if request.method == 'GET':
        pick = request.GET['select_place2']
        # 강원 안에 있는 강릉
        area = request.GET['this_val']
        # 강원을 가져옴
        
                
        req = requests.get('https://m.search.naver.com/search.naver?where=m&query=%EC%A0%84%EA%B5%AD+%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&x_trv=Ml8wMF8wXw%3D%3D&sm=mtb_trv')
        html = req.text
        soup = bs(html, 'html.parser')
        # 맨첨 페이지에 들어가서

        divs = soup.findAll('div' , {"class" : "map_marker"})
        
        
        for div in divs:
            
            links = div.find_all('a', {'href':True})
            
            for link in links:
                linkname = link.findAll('span' , {'class' : 'spot'})
        
                for yo in linkname:
                    name_only = yo.text
            
                    if name_only == area:
                    
                        req2 = requests.get("https://m.search.naver.com"+link['href'])
                        html2 = req2.text

                        soup2 =bs(html2,'html.parser')

                        # 여기까지 해서 강원안에 들어감
                        # 이제 여기서부터 다시 들어가야함


                        inner_attractions = soup2.findAll('div' , {"class" : "map_marker"})
                        for in_at in inner_attractions:

                            links2 = in_at.find_all('a', {'href':True})
                                        
                            for link2 in links2:
                                linkname2 = link2.findAll('span' , {'class' : 'spot'})
                        
                                for yo2 in linkname2:
                                    name_only2 = yo2.text
                            
                                    if name_only2 == pick:
                                    
                                        req3 = requests.get("https://m.search.naver.com"+link2['href'])
                                        html3 = req3.text

                                        soup3 =bs(html3,'html.parser')
                                        
                                        inner_attractions2=soup3.findAll('div' , {'class' : 'info'})

                                        for inner in inner_attractions2:
                                            inner2 = inner.find_all('strong' ,{'class' : 'tit'})
                                            introduction= inner.find_all('span' ,{'class' : 'txt'})
                                            
                                            for i,v in zip(inner2,introduction):
                                                total[i.text]=v.text


                                            


                                
    return render(request , 'next_select/' + area + '.html' , {'attraction' : total , 'value' : area})