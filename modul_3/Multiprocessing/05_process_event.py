import sys
from multiprocessing import Process, Event
from time import sleep


def example_work(event: Event):
    print('run event work')
    event.wait()
    print('flag event is true')
    sys.exit(0)


def example_work_timeout(event: Event, time: float):
    while not event.is_set():
        print('wait until the event flag is set')
        event_wait = event.wait(time)
        print('Has our flag been set?')
        if event_wait:
            print('We start working on a signal')
        else:
            print('We still waiting until tje event flag is set')
        sys.exit(0)  # processes should always finish with sys.exit()


if __name__ == '__main__':
    event = Event()
    pr = Process(target=example_work, args=(event,))
    pr.start()

    pr_timeout = Process(target=example_work_timeout, args=(event, 1))
    pr_timeout.start()

    sleep(5)
    event.set()

    print('End program')



