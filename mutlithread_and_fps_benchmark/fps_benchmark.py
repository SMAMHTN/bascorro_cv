import  datetime

class FPS:
    def __init__(self):
        self._start = None
        self._end = None
        self._numFrames = None

    def start(self):
        self._start = datetime.datetime.now()
        return self

    def stop(self):
        self.__end = datetime.datetime.now()

    def update(self):
        self.__numFrames += 1

    def elapsed(self):
        return (self._end - self._start).total_seconds()

    def fps(self):
        return self._numFrames / self.elapsed()


