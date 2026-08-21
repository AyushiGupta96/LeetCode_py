import random
#from turtledemo.penrose import start
import matplotlib.pyplot as p
import numpy

class T_T_T:
    def __init__(self):#initialize
        self.tile = [" "] * 9
        self.curr = "x"
    def reset(self):
        self.tile = [" "] * 9
        self.curr = "x"
        return self.state()#get state of the tile
    def state(self):#join current board as string
        return "".join(self.tile)
    def actions(self):
        action1 = []
        for i in range(9):# there are position in 3 x 3 matrix
            if self.tile[i] == " ":# if position is blank then only it can append value of i
                action1.append(i)
        return action1
    def moves(self,action1,p):#p is player1
        if action1 is None:
            return False
        if self.tile[action1] != " ": # if position is not blank don't take any action
            return False
        self.tile[action1]= p
        return True



    def printing(self):
        print(f"{self.tile[0]} | {self.tile[1]}|{self.tile[2]}")
        print("                                                          ")
        print(f"{self.tile[3]} | {self.tile[4]} |{self.tile[5]}")
        print("                                                           ")
        print(f"{self.tile[6]}|{self.tile[7]}|{self.tile[8]}")
    def win(self):
        conditions = [
            (0,1,2),# same row
            (3,4,5),#same row
            (6,7,8),#same row
            (0,4,8),# diogonal
            (2,4,6),#daigonal
            (0,3,6),# same column
            (2,5,8),#same column
            (1,4,7)#same column

        ]
        for i,j,k in conditions:
            if self.tile[i]  != " " and \
               self.tile[i] == self.tile[j] and \
               self.tile[j] == self.tile[k]:

                    return self.tile[i]
        if " " not in self.tile:# if no position have same, row or column or diogonal
            return "draw"
    def exit1(self):
        exit2 = self.win()
        return exit2
class player1:
    def get_action(self,env):
        action1 = env.actions()
        if len(action1) == 0:
            return None
        return random.choice(action1)


def agent1(agent, start=10):#for 10 games we want to play so start is 10
    player2 = player1()#will cal player 1 for performing action
    totalScore = 0
    oldEpsilon = agent.epsilo
    agent.epsilo = 0
    for _ in range(start):
        start = T_T_T()
        start.reset()
        done = False
        while not done:
            state = start.state()
            action= agent.get_action(state,start.actions())
            if action is None:
                reward = 0.5
                done = True
                break
            start.moves(action,"x")
            target = start.win()
            if target == "x":
                totalScore = totalScore +1
                break
            if target == "draw":
                totalScore = totalScore +0.5
                break
            player2_move = player2.get_action(start)
            if player2_move is None:
                totalScore = totalScore+0.5
                break
            start.moves(player2_move, "o")
            target = start.win()
            if target == "o":
                totalScore = totalScore+0
                break
            if target == "draw":
                totalScore = totalScore +0.5
                break
            if len(start.actions()) == 0:
                totalScore = totalScore+ 0.5

                break

    agent.epsilo = oldEpsilon
    return totalScore




class QLearning:
    def __init__(self,epsilo=0.1,decreased=0.9,m=0.1):#decreased is discount and m is learing rate
        self.table = {}
        self.m1 = m;
        self.epsilo = epsilo
        self.decreased1=decreased
    def implementQ(self,state):
        if state not in self.table:
            self.table[state] = numpy.zeros(9)
        return self.table[state]
    #e greedy selection
    def get_action(self,state,actions):
        if len(actions)==0:
            return None
        if random.random()<self.epsilo:
            return random.choice(actions)
        qLearning = self.implementQ(state)
        get_action= None
        get_value = -999999
        for i in actions:
            if qLearning[i] > get_value:
                get_value = qLearning[i]
                get_action = i
        return get_action
    def qupdate(self,state,new_state,reward,action,done):# for updating Q
        qLearning = self.implementQ(state)
        curr = qLearning[action]
        if done:
            result = reward
        else:
            new_qLearning = self.implementQ(new_state)
            result = reward + self.decreased1 * max(new_qLearning)
        next_Q = curr + self.m1 *(result - curr)
        self.table[state][action] = next_Q
    def train(self,epochs = 1000,epsilon_d = 0.001,d=50):
        agent = self
        player2 = player1()
        scores = []
        for i in range(epochs):
            start = T_T_T()
            state = start.reset()
            done = False# initialize done as false
            while not done:
               action1 = start.actions()
               if len(action1) ==0:

                   done = True
                   break

               action = agent.get_action(state,action1)
               start.moves(action, "x")
               new_state = start.state()
               target = start.win()

               if target == "x":# in this case agent wins
                   reward = 1
                   agent.qupdate(state,new_state,reward,action,True)
                   done = True
                   break
               if target == "draw":
                   reward = 0.5
                   agent.qupdate(state,new_state,reward,action,True)
                   done = True
                   break
               player2_move = player2.get_action(start)
               if player2_move is None:#this is for human
                   reward = 0.5
                   agent.qupdate(state,new_state,reward, action, True)
                   done = True
                   break
               start.moves(player2_move,"o") # player 2 move , it will be o
               new_state = start.state()
               target = start.win()


               if target == "o":
                   reward = 0
                   agent.qupdate(state,new_state,reward,action,True)
                   done = True
                   break


               if target == "draw":
                   reward = 0.5
                   agent.qupdate(state,new_state,reward,action,True)
                   done = True
                   break

               reward = 0
               agent.qupdate(state,new_state,reward,action,False)
               state = new_state

            scores1 = agent1(agent, start=10)
            scores.append(scores1/10)
            if (i+1) % d == 0:
                agent.epsilo -= epsilon_d
                if agent.epsilo < 0.01:
                    agent.epsilo = 0.01
                if (i+1) % 100 == 0:
                    print("epsilon-",agent.epsilo,"epoches",i+1,"scores",scores[-1])
        return agent,scores

    def opponent_agent(self,agent):
        start = T_T_T()
        start.reset()
        print("\n you are o")
        print("I am x \n")
        print("0|1|2")
        print("3|4|5")
        print("6|7|8")
        while True:
            state1 = start.state()
            action = agent.get_action(state1,start.actions())
            start.moves(action,"x")
            print("\n Agent Move \n")
            start.printing()
            target = start.win()
            if target == "x":
                print("Opponent wins")
                return "x"
            if target == "draw":
                print("draw")
                return "draw"
            while True:
                try:
                    enter = int(input("enter"))#for human to enter
                    if enter in start.actions():
                        break
                    print("invalid")
                except:
                    print("enter valid number")
            start.moves(enter,"o")
            start.printing()
            target = start.win()
            if target == "o":
                print(" you win")
                return "o"
            if target == "draw":
                print("draw")
                return "draw"
    def plot(self,score):
        p.figure(figsize=(10,10))
        p.plot(score,linewidth = 2)
        p.xlabel("epoch")
        p.ylabel("average score / 10")
        p.title("Tic Tac Toe")
        p.grid(True)
        p.ylim(0,1)
        p.show()
def main():
       # print("Training Agent")
        q = QLearning(epsilo=0.1,decreased=0.9,m=0.1)
        agent,score = q.train(epochs = 1000,epsilon_d = 0.001  , d=50)
        q.plot(score)
        win =0
        loss = 0
        draw= 0
        print("play 10 games")
        for i in range(10):
            print("    Game     ",i+1)
            target = q.opponent_agent(agent)
            if target == "o":
                win = win +1
            elif target == "x":
                loss = loss +1
            else:
                draw = draw +1
        print("result")
        print("win",win)
        print("loss",loss)
        print("draw",draw)
if __name__ == "__main__":
        main()












