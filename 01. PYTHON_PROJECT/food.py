# 음식 종류
food={1:'팝콘', 2:'음료', 3:'즉석구이오징어', 4:'싱글콤보', 5:'더블콤보'}
total_price=0
def store():
    global total_price

    popcorn=5000
    drink=2800
    squid=5000
    while True:
# ======================== 음식 선택 ====================================
        food_num=int(input('''<음식>
1.팝콘 2.음료 3.버터구이오징어 4.싱글콤보 5.더블콤보
음식 선택 : '''))
        
        if food_num in food:
            print('='*30)
            while True:
# ========================== 사이즈 선택 =================================
                if food_num==1:
                    food_size=int(input('''<사이즈 선택>
1.M 2.L (+500) : '''))
                    if food_size==1:
                        total_price+=popcorn
                        print(f'팝콘(M) 가격 : {popcorn}원')
                        break
                    elif food_size==2:
                        total_price+=popcorn+500
                        print(f'팝콘(L) 가격 : {popcorn+500}원')
                        break
                    else:print(f'사이즈를 다시 선택해주세요')
                elif food_num==2:
                    food_size=int(input('''<사이즈 선택>
1.M 2.L (+500) : '''))
                    if food_size==1:
                        total_price+=drink
                        print(f'음료(M) 가격 : {drink}원')
                        break
                    elif food_size==2:
                        total_price+=drink+500
                        print(f'음료(M) 가격 : {drink+500}원')
                        break
                    else:
                        print(f'사이즈를 다시 선택해주세요')
                elif food_num==3:
                    total_price+=squid
                    print(f'버터구이 오징어 가격 : {squid}')
                    break
                elif food_num==4:
                    total_price+=popcorn+drink-500
                    print(f'싱글콤보는 500원 할인된 가격으로 {popcorn+drink-500}원입니다.')
                    break
                    
                elif food_num==5:
                    total_price+=popcorn+500+2800+2800-1000
                    print(f'더블콤보는 1000원 할인된 가격으로 {popcorn+500+2800+2800-1000}원입니다.')
                    break
                else:
                    raise Exception('해당 음식은 존재하지 않습니다.')
            try:
# =========================== 음식 추가 ============================================
                add_food=input('음식을 추가하시겠습니까 ? (1.Yes 2.No)')
                if add_food=='1':
                    continue
                elif add_food=='2':break
                else:
                    raise Exception('1과 2만 입력해주세요')
                    # continue
            except: print('1과 2만 입력해주세요')
                
            # break
        else:
            print('=====해당 음식은 없습니다. 다시 입력해주세요 =====')


    return total_price

print(store())