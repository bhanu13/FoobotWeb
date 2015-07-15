from foobot import *



magnetobot = FoobotWeb("magnetog@gmail.com")

# magnetobot.GetDatapointLast()

# magnetobot.GetDatapointLast(3600, 0)
starttime = datetime(year=2015, month=1, day=1, hour=0, minute=0, second=0)
# endtime = datetime(year=2015, month=7, day=15, hour=0, minute=0, second=0)
magnetobot.GetDataInterval(starttime = starttime, save = True)	# endtime defaulting to now

# magnetobot.GetLastHour(save = True)

# magnetobot.GetLastDay(save = True)