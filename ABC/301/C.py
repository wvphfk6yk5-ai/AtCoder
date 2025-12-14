from collections import Counter

s = input().strip()
t = input().strip()
at = set("atcoder")

#s,tの文字数カウント
cs = Counter(s)
ct = Counter(t)

#@の数を別途保存
ats,att = cs["@"],ct["@"]
#s,tの不足文字リスト
dfs=[]
dft=[]

#@以外の差分を計算
for ch in set(cs.keys()) | set(ct.keys()):
  if ch ==  "@":
    continue
  ds = cs[ch] - ct[ch]
  if ds < 0:
    dfs += [ch]*(-ds)
    
  elif ds>0:
    dft += [ch]*(ds)

#不足文字にatcoder以外があればNo
if any(ch not in at for ch in dfs) or any(ch not in at for ch in dft):
  print("No")
  exit()

#不足文字数が@の数を超えていなければYes
if len(dfs) <= ats and len(dft) <= att:
  print("Yes")
else:
  print("No")
