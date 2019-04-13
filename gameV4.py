import pygame, sys #import module pygame untuk membuat GUI game
from pygame.locals import * #Kata tutorialnya karena pygame.locals sering dipake
import random #Buat ngerandom jalannya computer
import tkinter #Buat inisialisasi window di exception
from tkinter.messagebox import showinfo #Buat bikin showinfo di exception

class NimGame:
    '''Kelas untuk membuat Nim Game. Bismillah insyaAllah bisa!!! AAMIINN!!!'''
    def __init__(self, display):
        '''Inisisalisasi Kelas'''
        self.display = display

        self.x = 300
        self.y = 530
        self.x2 = 400
        self.y2 = 530
        self.x3 = 500
        self.y3 = 530
        self.x4 = 600
        self.y4 = 530

        self.__init_start()
        self.__init_text()

    def __init_start(self):
        '''Membuat inisialisasi jumlah Quanta di awal sekaligus menggambar Quanta untuk memulai permainan'''
        self.quanta = pygame.image.load('aset/quanta.png')
        self.pile1 = 0
        self.pile2 = 0
        self.pile3 = 0
        self.pile4 = 0

        for i in range(3):
            self.y -= 5
            self.display.blit(self.quanta, (self.x, self.y))
            self.y -= 50
            pygame.display.update()
            self.pile1 += 1

        for i in range(5):
            self.y2 -= 5
            self.display.blit(self.quanta, (self.x2, self.y2))
            self.y2 -= 50
            pygame.display.update()
            self.pile2 += 1

        for i in range(5):
            self.y3 -= 5
            self.display.blit(self.quanta, (self.x3,self.y3))
            self.y3 -= 50
            pygame.display.update()
            self.pile3 += 1

        for i in range(7):
            self.y4 -= 5
            self.display.blit(self.quanta, (self.x4, self.y4))
            self.y4 -= 50
            pygame.display.update()
            self.pile4 += 1

    def __init_text(self):
        '''Inisialisasi tulisan yang berupa jumlah Quanta yang tersisa di setiap tumpukan'''
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS',20,'bold')

        text1 = myfont.render("PileA:", True, (255,0,0))
        sum1 = myfont.render(str(self.pile1),True, (255,0,0))
        pygame.draw.rect(self.display, (255,255,255), (280, 70, 65, 55))
        self.display.blit(text1, (280, 70))
        self.display.blit(sum1, (300, 90))

        text2 = myfont.render("PileB:", True, (255,0,0))
        sum2 = myfont.render(str(self.pile2),True, (255,0,0))
        pygame.draw.rect(self.display, (255, 255, 255), (380, 70, 65, 55))
        self.display.blit(text2, (380, 70))
        self.display.blit(sum2, (400, 90))

        text3 = myfont.render("PileC:", True, (255,0,0))
        sum3 = myfont.render(str(self.pile3),True, (255,0,0))
        pygame.draw.rect(self.display, (255, 255, 255), (480, 70, 65, 55))
        self.display.blit(text3, (480, 70))
        self.display.blit(sum3, (500, 90))

        text4 = myfont.render("PileD:", True, (255,0,0))
        sum4 = myfont.render(str(self.pile4),True, (255,0,0))
        pygame.draw.rect(self.display, (255, 255, 255), (580, 70, 65, 55))
        self.display.blit(text4, (580, 70))
        self.display.blit(sum4, (600, 90))

        pygame.display.update()

    def key1(self):
        '''Menghapus satu Quanta di tumpukan pertama setiap user menekan tombol Space'''
        self.pile1 -= 1
        self.__init_text()
        self.y += 50
        pygame.draw.rect(self.display, (255,255,255),(self.x,self.y,48,48))
        self.y += 5
        pygame.display.update()

    def key2(self):
        '''Menghapus satu Quanta di tumpukan kedua setiap user menekan tombol Space'''
        self.pile2 -= 1
        self.__init_text()
        self.y2 += 50
        pygame.draw.rect(self.display, (255,255,255),(self.x2,self.y2,48,48))
        self.y2 += 5
        pygame.display.update()

    def key3(self):
        '''Menghapus satu Quanta di tumpukan ketiga setiap user menekan tombol Space'''
        self.pile3 -= 1
        self.__init_text()
        self.y3 += 50
        pygame.draw.rect(self.display, (255,255,255),(self.x3,self.y3,48,48))
        self.y3 += 5
        pygame.display.update()

    def key4(self):
        '''Menghapus satu Quanta di tumpukan keempat setiap user menekan tombol Space'''
        self.pile4 -= 1
        self.__init_text()
        self.y4 += 50
        pygame.draw.rect(self.display, (255,255,255),(self.x4,self.y4,48,48))
        self.y4 += 5
        pygame.display.update()

    def checkCode(self, code):
        '''Untuk memeriksa apakah masih ada Quanta pada tumpukan yang dipilih'''
        if code == 1:
            return self.pile1 > 0
        if code == 2:
            return self.pile2 > 0
        if code == 3:
            return self.pile3 > 0
        return self.pile4 > 0

    def checkEnd(self, turn):
        '''Untuk memeriksa apakah masih ada Quanta di dalam Game'''
        self.turn = turn
        if self.pile1 <= 0 and self.pile2 <= 0 and self.pile3 <= 0 and self.pile4 <= 0:
            self.endGame()
            return True
        return False

    def endGame(self):
        '''Untuk menyelesaikan game'''
        root = tkinter.Tk()
        root.withdraw()
        if self.turn % 2 == 0:
            showinfo(message="Player Win!!!")
        else:
            showinfo(message="Computer Win!!!")
        root.destroy()
    def checkSum(self, num, code):
        '''Untuk memeriksa apakah Quanta masih bisa diambil dari tumpukkan'''
        if code == 1:
            return self.pile1 - num >= 0
        if code == 2:
            return self.pile2 - num >= 0
        if code == 3:
            return self.pile3 - num >= 0
        if code == 4:
            return self.pile4 - num >= 0


#---------------------------------------------------------------------------------------------------------------------#


def gaming():
    '''Fungsi untuk memulai permainan'''
    global code,play,press,play2,turn, smart
    end = game.checkEnd(turn)
    if end:
        play = False
        exit()
    play = True
    press = True
    play2 = False
    endTurn = False
    code = 1
    
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                play = False

        if turn % 2 == 0:
            hard()
        
        else:
            keys = pygame.key.get_pressed()
            pygame.time.delay(100)
            if keys[pygame.K_a] and press:
                code = 1
                test = game.checkCode(code)
                if test:
                    play2 = True
                else:
                    root = tkinter.Tk()
                    root.withdraw()
                    showinfo(message="Batu sudah habis")
                    root.destroy()
                    gaming()
            if keys[pygame.K_b] and press:
                code = 2
                test = game.checkCode(code)
                if test:
                    play2 = True
                else:
                    root = tkinter.Tk()
                    root.withdraw()
                    showinfo(message="Batu sudah habis")
                    root.destroy()
                    gaming()
            if keys[pygame.K_c] and press:
                code = 3
                test = game.checkCode(code)
                if test:
                    play2 = True
                else:
                    root = tkinter.Tk()
                    root.withdraw()
                    showinfo(message="Batu sudah habis")
                    root.destroy()
                    gaming()
            if keys[pygame.K_d] and press:
                code = 4
                test = game.checkCode(code)
                if test:
                    play2 = True
                else:
                    root = tkinter.Tk()
                    root.withdraw()
                    showinfo(message="Batu sudah habis")
                    root.destroy()
                    gaming()
            if keys[pygame.K_SPACE] and play2:
                check = game.checkSum(1,code)
                if check:
                    pile()
                endTurn = True
            if keys[pygame.K_RETURN] and play2 and endTurn:
                turn += 1
                gaming()


def pile():
    '''Untuk mengambil Quanta setelah user menekan tombol Space'''
    global play2, press, code,turn,p1,p2,p3,p4
    press = False
    play2 = True
    while play2:
        pygame.time.delay(100)
        if code == 1:
            game.key1()
            p1-=1
            break
        if code == 2:
            game.key2()
            p2-=1
            break
        if code == 3:
            game.key3()
            p3-=1
            break
        if code == 4:
            game.key4()
            p4-=1
            break


def hard():
    global p1,p2,p3,p4,turn,code
    bit = p1^p2^p3^p4
    print(bit, "Ini Bit")
    print(p1,p2,p3,p4)
    if bit <= p1 and p1 - bit >= 0 and (p1 - bit) ^ p2 ^ p3 ^ p4 == 0 and bit != 0:
        code = 1
    elif bit <= p2 and p2 - bit >= 0 and (p2 - bit) ^ p1 ^ p3 ^ p4 == 0 and bit != 0:
        code = 2
    elif bit<= p3 and p3 - bit >= 0 and (p3 - bit) ^ p2 ^ p1 ^ p4 == 0 and bit != 0:
        code = 3
    elif bit <= p4 and p4 - bit >= 0 and (p4 - bit) ^ p2 ^ p3 ^ p1 == 0 and bit != 0:
        code = 4
    else:
        if bit == 3 or bit == 2 or bit == 7 or bit == 1:
            if p1 > p2 and p1 > p3 and p1 > p4:
                code = 1
            elif p2 > p3 and p2 > p4:
                code = 2
            elif p3 > p4:
                code = 3
            else:
                code = 4
            bit = 1
        elif bit == 6:
            if p1 > p2 and p1 > p3 and p1 > p4:
                code = 1
            elif p2 > p3 and p2 > p4:
                code = 2
            elif p3 > p4:
                code = 3
            else:
                code = 4
            bit = 2
        else:
            check = False
            while not check:
                code = random.randint(1, 4)
                check = game.checkCode(code)
            bit = 1
        
    for i in range(bit):
        pile()
    turn += 1
    print(p1,p2,p3,p4)
    gaming()
    
        
def main():
    '''Fungsi utama untuk menjalankan program'''
    pygame.init()
    global game, turn,p1,p2,p3,p4,smart
    turn = 2
    p1 = 3
    p2 = 5
    p3 = 5
    p4 = 7
    bg = pygame.image.load('aset/bggame.jpg')
    bg = pygame.transform.scale(bg, (1000,700))
    naga = pygame.image.load('aset/naga.gif')

    display = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("NimGame!!!")
    display.blit(bg, (0,0))
    display.blit(naga, (600,300))

    game = NimGame(display)

    gaming()




if __name__ == '__main__':
    main()
