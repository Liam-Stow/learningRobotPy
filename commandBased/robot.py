#!/usr/bin/env python3

import wpilib
import commands2
from robotcontainer import RobotContainer

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.container = RobotContainer()

    def robotPeriodic(self) -> None:
        """
        Periodic code for all modes should go here.

        This function is called each time a new packet is received from the driver
        station.
        """
        commands2.CommandScheduler.getInstance().run()
        
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        pass

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)