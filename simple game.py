global gold
gold=100
global apples
def start():
    print "hello and welcome"
    name=raw_input ("what is your name:")
    print "welcome,"+name+"!"
    print "the objective of this game is to collect apples"
    print "after collecting them you sell them"
    choice=raw_input ("do you want to play y/n?")
    if choice=="y":
        begin()
        if choice=="n":
            print "ok bye..."
    def begin():
        print("lets get started!")
        pick=raw_input("do you want to pick an apples y/n")
        if pick =="y":
            time.sleep(1)
        print "you picked an apple"
        apples=apple+1
        print "you currently ahce"+apples+" apples"
        begin()
        if pick =="n":
            sell=raw_input("do you want to sell your apple y/n")
            if sell =="y":
             global gold
          
             print "you currently have",+apples ,"apples"
             print "you have not sold your apples"
             gold=apples*10
             apples=0
             print "your gold is now:",gold
