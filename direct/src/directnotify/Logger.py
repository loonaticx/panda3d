"""Logger module: contains the logger class which creates and writes
   data to log files on disk"""

import time
import math


class Logger:
    def __init__(self, fileName="log"):
        """
        Logger constructor
        """
        self.__timeStamp = 1
        self.__startTime = 0.0
        self.__logFile = None
        self.__logFileName = fileName

    def setTimeStamp(self, enable):
        """
        Toggle time stamp printing with log entries on and off.
        """
        self.__timeStamp = enable

    def getTimeStamp(self):
        """
        Return whether or not we are printing time stamps with log entries.
        """
        return self.__timeStamp

    # logging control

    def resetStartTime(self):
        """
        Reset the start time of the log file for time stamps.
        """
        self.__startTime = time.time()

    def log(self, entryString):
        """log(self, string)
        Print the given string to the log file."""
        if self.__logFile is None:
            self.__openLogFile()
        if self.__timeStamp:
            self.__logFile.write(self.__getTimeStamp())
        self.__logFile.write(entryString + '\n')

    # logging functions

    def __openLogFile(self):
        """
        Open a file for logging error/warning messages.
        """
        self.resetStartTime()
        t = time.localtime(self.__startTime)
        st = time.strftime("%m-%d-%Y-%H-%M-%S", t)
        logFileName = self.__logFileName + "." + st
        self.__logFile = open(logFileName, "w")

    def __closeLogFile(self):
        """
        Close the error/warning output file.
        """
        if self.__logFile is not None:
            self.__logFile.close()

    def __getTimeStamp(self):
        """
        Return the offset between current time and log file startTime.
        """
        t = time.time()
        dt = t - self.__startTime
        days, dt = divmod(dt, 86400)
        hours, dt = divmod(dt, 3600)
        minutes, dt = divmod(dt, 60)
        seconds = int(math.ceil(dt))
        return "%02d:%02d:%02d:%02d: " % (days, hours, minutes, seconds)
