import time


def Clamp(value, min_value=0, max_value=1):
    """
    Clamp returns the number provided within the bounds provided
    :param value: The number to be kept in the range
    :param min_value: The minimum number the value can reach
    :param max_value: The maximum value the value can reach
    :return: The value within the bounds
    """
    return min(max_value, max(min_value, value))


class Vector2:
    """
    Acts as a simple Vector2, for use in interpreting sense hat joystick Values
    """

    def __init__(self, args_):
        self.movementDict = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0], "middle": [0, 0]}

        if isinstance(args_, str):
            if args_ in self.movementDict:
                direction = self.movementDict[args_]
                self.x = direction[0]
                self.y = direction[1]
                self.value = direction

        if isinstance(args_, list):
            self.x = args_[0]
            self.y = args_[1]
            self.value = args_

    def X(self):
        return self.x

    def Y(self):
        return self.y

    def Set(self, args_):
        if isinstance(args_, str):
            if args_ in self.movementDict:
                direction = self.movementDict.get(args_)
                self.x = direction[0]
                self.y = direction[1]
                self.value = direction

        if isinstance(args_, list):
            self.x = args_[0]
            self.y = args_[1]
            self.value = args_

    def Get(self):
        return self.value


class AdTime:
    """
    Includes more advanced time operators not included by default
    """

    def __init__(self, waitTime_=1):
        """
        Setup time system
        :param waitTime_: How many seconds until delta time passes (can be set later in DeltaTime)
        """
        self.lastFrameTime = time.time()
        self.accumulator = 0
        self.waitTime = waitTime_

    def DeltaTime(self, waitTime_=None):
        """
        Checks if the time that has passed has reached the desired length
        :param waitTime_: How many seconds until delta time passes
        :return: If the time in seconds specified on Adtime innit, in the method or the default value has been reached
        """
        timeChunk = waitTime_

        if timeChunk is None:
            timeChunk = self.waitTime

        currentTime = time.time()
        dt = currentTime - self.lastFrameTime
        self.lastFrameTime = currentTime

        self.accumulator += dt
        if self.accumulator >= timeChunk:
            self.accumulator = 0
            return True
        else:
            return False

    def WaitUntil(self, time_):
        """
        Waits via delta time until the desired time (CHANGES WAIT TIME)
        :param time_: new wait time
        :return: where it stops
        """
        while not self.DeltaTime(time_):
            pass
        return
