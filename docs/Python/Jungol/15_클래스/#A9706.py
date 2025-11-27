# 공격 1회 : 상대의 HP - 본인의 ATK
# 몬스터 1, 매 턴마다 서로 한 대씩 공격, HP가 0이 되면 게임 종료
# PYTHON, PYGOON, TIE
# sub 사용

class j:
    def __init__(self, hp, atk):
        self.hp = int(hp)
        self.atk = int(atk)
    
    def __sub__(self, other):
        res = 0
        HP = other.hp

        while HP > 0:
            HP -= self.atk
            res += 1

        return res

t_hp, t_atk = input().split()
g_hp, g_atk= input().split()

ph = j(t_hp, t_atk)
pg = j(g_hp, g_atk)

PH = ph - pg
PG = pg - ph

if PH < PG:
    print('PYTHON')

elif PH > PG:
    print('PYGOON')

elif PH == PG:
    print('TIE')
