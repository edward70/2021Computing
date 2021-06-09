import time
import heapq

def curr_time():
    return round(time.time() * 1000)

class GameEventPQueue:
    ''' singleton event queue for the game, event listeners handle different game event types
        game events are scheduled in a pqueue for certain events can be handled before others
        uses minpqueue since events can be scheduled by time in ms to occur in future
        events that are scheduled earlier will run earlier. when proceeding through the queue, hitting an event
        that isn't scheduled to run yet will cancel the procession. '''

    def __init__(self):
        self.listeners = {}
        self.tick = 0
        self.timepqueue = []
        self.tickpqueue = []

    def add_listener(self, event_name, listener):
        if not self.listeners.get(event_name, None):
            self.listeners[event_name] = {listener}
        else:
            self.listeners[event_name].add(listener)

    def remove_listener(self, event_name, listener):
        self.listeners[event_name].remove(listener)
        if len(self.listeners[event_name]) == 0:
            del self.listeners[event_name]

    def tick_enq(self, event_name, event, priority):
        # don't initialize priority since time_enq is preferrable for immediate events since it respects enqueuing order
        # event execution timing and order is based on game ticks
        priority = self.tick + priority
        heapq.heappush(self.tickpqueue, (priority, event_name, event))
        
    def time_enq(self, event_name, event, priority=0):
        # enqueue events with priority based on time in ms
        priority = curr_time() + priority
        heapq.heappush(self.timepqueue, (priority, event_name, event))

    def _proceed(pqueue, moment):
        while pqueue != []:
            peek = pqueue[0]
            event_time = peek[0]
            event_name = peek[1]
            event = peek[2]

            if event_time <= moment:
                heapq.heappop(pqueue)

                listeners = self.listeners.get(event_name, [])
                for listener in listeners:
                    listener(event)
            else:
                break

    def tick(self):
        self._proceed(self.timepqueue, curr_time()) # timepqueue is processed first since immediate tasks run on it
        self._proceed(self.tickpqueue, self.tick)
        self.tick += 1 # increment game ticks

    #def clear(maxt=0, event_name):
    #    if maxt == 0:
    #        # clear all events in event_name
    #    else:
    #        # clear events before or equal to maxt relating to event

# instantiate global event prioq
eventQ = GameEventPQueue()

# test code

#def test(event):
#    print("hello", event)
#
#def test2(event):
#    print("test2", event)
#
#gameQueue = GameEventPQueue()
#gameQueue.add_listener("test", test)
#gameQueue.add_listener("test2", test)
#gameQueue.enqueue("test", "world")
#gameQueue.enqueue("test2", "here")
#gameQueue.enqueue("test", "test")
#gameQueue.enqueue("test2", "again", 1000)
#gameQueue.dequeue()
#gameQueue.dequeue(3)
#time.sleep(1)
#gameQueue.dequeue()
