__author__ = 'marion'

from consider import Consider
import threading
import arduino.arduino_controls as arduino
import time
import sound

def stream():
    con = Consider()
    meditation_threshold = 55
    attention_threshold = 35
    print "waiting for BCI headset signal ..."
    turn = False
    for p in con.packet_generator():
        if p.poor_signal == 0:
            print "meditation: %s / 100 | attention : %s / 100" % (p.meditation, p.attention)
            if p.meditation > meditation_threshold:
                t1 = threading.Thread(target=sound.play_meditation_sound)
                t1.daemon = True
                t1.start()


                if not turn:
                    t2 = threading.Thread(target=arduino.send_turn_left())
                    t2.daemon = True
                    t2.start()
                    turn = True
                else:
                    time.sleep(1)
                    turn = False


            if p.attention > attention_threshold:
                t3 = threading.Thread(target=sound.play_attention_sound)
                t3.daemon = True
                t3.start()


                t4 = threading.Thread(target=arduino.send_go_foreward())
                t4.daemon = True
                t4.start()

        else:
            print "no signal yet"


if __name__ == "__main__":
    stream()
