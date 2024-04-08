import sys
import i3ipc

i3 = i3ipc.Connection()

def dothing(i3, e):
    print("Window Opened :)")
    e.container.command('floating toggle')
    sys.exit(0)

i3.on('window::new', dothing)

i3.main()
