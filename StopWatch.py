import simplegui

# define global variables
interval = 100
tenth = 0
position = [55, 80]
position_two = [160, 30]
width = 200
height = 120	
count = 0
count_whole = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    ans = str(t // 600) + ":" + str((t % 600) // 100) + str((t % 100) // 10) + "." + str(t % 10)
    return ans

# define event handlers for buttons; "Start", "Stop", "Reset"
def start ():
    timer.start()

def stop():
    global count, count_whole
    if timer.is_running():
        timer.stop()
        count += 1

        if tenth%10 == 0:
            count_whole += 1

def reset():
    global tenth, interval
    tenth = 0
    interval = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenth, interval
    interval += 100
    tenth += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(tenth), position, 36, "Red")
    canvas.draw_text(str(count_whole) + "/" + str(count), position_two, 26, "Yellow")
    
# create frame
frame = simplegui.create_frame("StopWatch", width, height)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, timer_handler)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()
