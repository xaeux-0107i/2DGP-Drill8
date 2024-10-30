from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_a

#이벤트 체크 함수를 정의
# 상태 이벤트 # e = ( 종류, 실제 값) 튜플로 정의
def start_event(e):
    return e[0] == 'START'

def space_down(e): #e가 space down 인지 판단
    return e[0] =='INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def time_out(e): #e가 time out 인지 판단
    return e[0] == 'TIME_OUT'

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

class StateMachine:
    def __init__(self, obj):
        self.obj = obj # 어떤 객체를 위한 상태머신인지 알려줌
        self.event_q = []   #어떤 객체를 위한 상태머신인지
        #상태 이벤트를 보고할 이벤트
        pass
    def start(self, state):
        self.cur_state = state # 시작 상태를 받아서, 그걸로 현재 상태를 정의
        self.cur_state.enter(self.obj, ('START' , 0))
        print(f'Enter int0 {state}')
        pass
    def update(self):
        self.cur_state.do(self.obj) #Idle.do()
        #혹시 이벤트가 있나?
        if self.event_q:        #List 는 맴버가 있으면 True, 비어있으면 False
            e = self.event_q.pop(0)     #맨 앞에 있는 것을 꺼낸다 (pop(0))
            #이시점에서 우리한테 주어진 정보?
            #e
            #cur_state
            #
            # 현재 상태와 현재 발생한 이벤트에 따라서
            #다음 상태를 결정하는 방법은??
            #
            #상태변환 테이블을 이용 (Dictionary 이용)
            for check_event, next_state in self.set_transitions[self.cur_state].items():
                if check_event(e):    #중요!
                    print(f'Exit from {self.cur_state}')
                    self.cur_state.exit(self.obj, e)
                    self.cur_state = next_state
                    print(f'Enter into {next_state}')
                    self.cur_state.enter(self.obj, e) # 상태 변환의 이유를 명확히 알려준다. e
                    return      #return : 이벤트에 따른 상태 변환이 끝남
            #이 시점으로 왔다는 것은, event 에 따른 전환 못함.
            print(f'        WARING: {e} not hadnled at state {self.cur_state}')


    def draw(self):
        self.cur_state.draw(self.obj)
        pass

    def add_event(self, e):
        print(f'    DEBUG: add event {e}')
        self.event_q.append(e)
        pass

    def set_transitions(self, transitions):
        self.set_transitions = transitions
        pass