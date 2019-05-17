# -*- coding: utf-8 -*-
# @author : jared
# @date : 2019/5/16 19:33

import os
import sys

from apscheduler.schedulers.background import *


def robot_job(hour):
    scheduler = BlockingScheduler()
    scheduler.add_job(robot, 'cron', hour=hour)
    scheduler.start()


def robot():
    os.system('./start.sh')


# nohup python3 start.py 22 >> /dev/null 2>&1 &
if __name__ == '__main__':
    argv = sys.argv
    robot_job(argv[1])
