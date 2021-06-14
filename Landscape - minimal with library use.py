# *****************************************************************************
# * | This version:   V1.0
# * | Date        :   2021-06-14
# # | Info        :   Landscape demo
# -----------------------------------------------------------------------------
# Autrhor:  Arnoud van Leijden
# Function: Same as other landscape example, but minimal coding by using the EPB0-library
#           see the examples below.
import EPB0

if __name__=='__main__':
    epd = EPB0.EPD_2in13()
    epd.Clear(0xff)

 
    EPB0.LineHor(10, 10, 30)
    EPB0.LineHor(10, 20, 40)
    EPB0.LineHor(10, 30, 80)
    EPB0.LineHor(10, 40, 200)
    
    EPB0.LineVer(10, 10, 30)
    EPB0.LineVer(20, 10, 30)
    EPB0.LineVer(30, 10, 30)
    EPB0.LineVer(200, 10, 40)
    
    EPB0.Rect(50,50,50,50)
    EPB0.Rect(55,55,40,40)
    EPB0.Rect(47,47,6,6)
    
    EPB0.DLineH(40, 10, 200)
    EPB0.DLineV(35, 10, 60)
    
    EPB0.DRect(150, 25, 50, 50)
    

    EPB0.PrtStxt("Ola Arnie", 11, 1, 0)
    EPB0.PrtStxt("Arnie !", 11, 2, 1)
    EPB0.PrtLtxt("Ola Arnie", 100, 10, 0)
    EPB0.PrtLtxt("Arnie!", 100, 7, 1)
    
    epd.display(EPB0.Beeld)

    epd.delay_ms(20000)
    epd.Clear(0xff)
    epd.delay_ms(2000)
    epd.sleep()
    
