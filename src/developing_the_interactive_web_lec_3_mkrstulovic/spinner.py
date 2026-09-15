from halo import Halo
import time

spinner = Halo(text='I am spinninggggggg!!!!!',
               text_color='cyan',
               color='magenta',
               spinner='star')

spinner.start()
time.sleep(60)
spinner.stop()