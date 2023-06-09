import commands2.cmd
import commands2.button

class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        self.controller = commands2.button.CommandXboxController(0)

        # The robot's subsystems

        # Configure the button bindings
        self.configureButtonBindings()

        # Configure default commands


    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :GenericHID or one of its subclasses (Joystick or XboxController),
        and then passing it to a JoystickButton.
        """
        self.controller.A().onTrue(commands2.cmd.print("button a pressed"))

    def getAutonomousCommand(self) -> commands2.Command:
        return commands2.cmd.nothing