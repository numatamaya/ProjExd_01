import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
   
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    
    kk_imgs =[kk_img, pg.transform.rotozoom(kk_img,10,1.0)]
    bg_imgs = [bg_img,pg.transform.flip(bg_img,True,False)]*2
    x = 0
    fs = 300
    tmr = 0
    kkmv = 0
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        if tmr%(fs//5) >= fs//10:
           kkmv = 0
        else:
           kkmv = 1       # screen.blit(bg_img, [-x, 0])
       # screen.blit(bg_img, [1600-x, 0])
    
        tmr += 1        
        x = tmr % 3200 
        for i in range(4):
            screen.blit(bg_imgs[i],[-x+1600*i, 0])
        screen.blit(kk_imgs[kkmv],[300,200])
        pg.display.update()   
        clock.tick(fs)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()