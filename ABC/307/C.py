#データ読み込み
def read_data():
  H,W=map(int,input().split())
  grid=[input().strip() for _ in range(H)]
  v = []
  for y in range(H):
    for x in range(W):
      if grid[y][x] == "#":
        v.append([y,x])  #vector(y,x)として保存
  return H,W,v

#(y,x)をbitboardに変換
def position(y,x,W):
  return y*W+x

#A,B<X読み込み
HA,WA,vA = read_data()
HB,WB,vB = read_data()
HX,WX,vX = read_data()

#Xをbitboardに変換
sheet_X=0
for (y,x) in vX:
  sheet_X|=1<<position(y,x,WX)

Ans=False  
#AをXの領域に載せ考えられるすべての平行移動をさせる
for dya in range(-19,20):
  for dxa in range(-19,20):
    sheet_A=0
    jad=True
    for (ya,xa) in vA:
      y=ya+dya
      x=xa+dxa
      #黒点がX領域をはみ出したらやめる
      if not (0<=y<HX and 0<=x<WX):
        jad=False
        break
      sheet_A|=1<<position(y,x,WX)

    # Aの黒点がはみ出さなければBへ
    if not jad:
      continue

    #Bも同様平行移動させる
    for dyb in range(-19,20):
      for dxb in range(-19,20):
        sheet_B=0
        jad=True
        for (yb,xb) in vB:
          y=yb+dyb
          x=xb+dxb
          if not (0<=y<HX and 0<=x<WX):
            jad=False
            break
          sheet_B|=1<<position(y,x,WX)
          
        if not jad:
          continue

        #A,B重ねる
        sheet=sheet_A|sheet_B
        #Xと照合
        if sheet_X == sheet:
          Ans=True

if Ans:
  print("Yes")
else:
  print("No")
          
          
          

    
