import random

def roll():
    # Tạo xúc xắc random từ 1 đến 6
    rolls = random.choices([1,2,3,4,5,6])
    return rolls[0]

while True:
    tongSoPlayer = input("Nhập số người chơi (2-40 người) : ")
    # Kiểm tra số player có phải số
    if tongSoPlayer.isdigit():
        tongSoPlayer = int(tongSoPlayer)
        if 2<= tongSoPlayer <=40:
            break     
        else:
            print("Số người chơi phải là số từ 2 đến 40 vui lòng nhập lại")
    else: 
        print("Số không hợp lệ")


max_scrore = 50
# Tạo danh sách điểm cho các player
player_scrores = [0 for _ in range(tongSoPlayer)]
print(player_scrores)

# kiểm tra xem ai max điểm > game dừng

while max(player_scrores) < max_scrore :
    try:
        should_roll = input("Bạn muốn roll Dice không (c - để roll ; x - để dừng game)")
        if should_roll.upper() == "C": player_scrores[0]+= roll()
        if should_roll.upper() == "X": raise Exception("Cảm ơn bạn đã tham gia trò chơi!")
        for x in range(1,len(player_scrores)):
            value = roll()
            player_scrores[x]+= value
            print("Player ",x+1," đã roll được ",value)
        print("Player Scroll = ",player_scrores)
        if max(player_scrores) >= max_scrore:
            print("\------------Game Over------------/\n")
            print("Đã có người chiến thắng\n")
            print("Người thắng là player số : ----", player_scrores.index(max(player_scrores))+1,"\n")
            break
    except Exception as e:
        print(str(e))
        break