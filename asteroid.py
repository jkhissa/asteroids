from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):

        """
        Initializes an Asteroid instance.

        The constructor calls the parent CircleShape constructor to set up
        the fundamental properties of a circular object.

        Args:
            x (float): The initial x-coordinate of the asteroid's center.
            y (float): The initial y-coordinate of the asteroid's center.
            radius (float): The radius of the asteroid's circular boundary.
        """
        # Call the parent class (CircleShape) constructor to handle the
        # initialization of position and radius. This is essential for
        # any methods inherited from CircleShape to work correctly.
        super().__init__(x, y, radius)

    

    def draw(self, screen):
        """
        Draws the asteroid on the screen as a white circle.

        This method overrides the default draw behavior and uses pygame's
        circle drawing function to render the asteroid.

        Args:
            screen (pygame.Surface): The surface on which to draw the asteroid.
        """
        # Draw a circle on the provided screen surface.
        # - "white": The color of the circle's outline.
        # - self.position: The center coordinates (a pygame.Vector2).
        # - self.radius: The radius of the circle.
        # - 2: The thickness of the circle's outline in pixels.
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """
        Updates the asteroid's position based on its velocity.

        This method moves the asteroid in a straight line at a constant speed.
        The velocity is inherited from the CircleShape parent class.

        Args:
            dt (float): The delta time, or time elapsed since the last frame.
                        Used to ensure frame-rate independent movement.
        """
        # Update the position by adding the velocity vector scaled by delta time.
        # This makes the movement smooth and consistent across different frame rates.
        self.position += self.velocity * dt