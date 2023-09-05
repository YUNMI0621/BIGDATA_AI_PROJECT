# 현재 상영중인 영화
movie={1:'악마들', 2:'인디아나존스', 3:'스파이더맨', 4: '엘리멘탈', 5: '범죄도시', 6:'귀공자'}
total_seats=100
reserved_seats=0
total_price=0
       

def movie_info():
    global reserved_seats
    global total_seats
    global total_price
# ============================= 영화 선택 ===========================================    
    print('='*30)
    while True:
        movie_num=int(input(''' <현재 상영중인 영화>
1.악마들 2.인디아나존스, 3. 스파이더맨 4.엘리멘탈 5.범죄도시 6.귀공자
영화 번호 입력 : '''))
        if movie_num in movie:
            print(f'선택된 영화 : {movie.get(movie_num)}')
            break
        else : print('=====해당 영화는 존재하지 않습니다. 다시 입력해주세요.=====')
    price_child=14_000
    price_adult=16_000
# ============================= 인원수 입력 =========================================
    movie_num_child=int(input('어린이 및 청소년 수를 입력해주세요. (가격 : 14,000)'))
    print(f'어린이 수 : {movie_num_child}')
    movie_num_adult=int(input('어른의 수를 입력해주세요. (가격 : 16,000)'))
    print(f'어른 수 : {movie_num_adult}')

    total_people=movie_num_child+movie_num_adult
    if reserved_seats+total_people>total_seats:
        print('===== 예약 가능한 좌석이 없습니다. 다른 영화를 선택해주세요. (1.네 / 2.아니오) =====')
        answer=input().strip()
        if answer=='1':
            return movie_info()
        else:
            return '종료하겠습니다.'
        
    reserved_seats+=total_people
    total_price+=movie_num_child*price_child+movie_num_adult*price_adult

    return f'''고객님이 선택하신 영화는 "{movie.get(movie_num)}"이고 어린이 및 청소년 {movie_num_child}명, 어른 {movie_num_adult}명으로 가격은 {total_price}입니다.
전체 좌석 중 잔역 좌석은 {total_seats-total_people}석입니다.''' 
