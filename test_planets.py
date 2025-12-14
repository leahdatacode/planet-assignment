import unittest
from Planets import Planet, find_planet_in_question

class TestPlanets(unittest.TestCase):
    """Test plan for the Planets program."""

    def test_create_planet(self):
        """Test that a Planet is created with correct characteristics."""
        earth = Planet("Earth", 1.0, 1.0, ["Moon"])
        self.assertEqual(earth.name, "Earth")
        self.assertEqual(earth.mass, 1.0)
        self.assertEqual(earth.distance, 1.0)
        self.assertEqual(earth.moons, ["Moon"])

    def test_find_planet_by_name(self):
        """Test that the program can find Earth from a user question."""
        question = "Tell me about Earth"
        planet = find_planet_in_question(question)
        self.assertIsNotNone(planet)
        self.assertEqual(planet.name, "Earth")

if __name__ == "__main__":
    unittest.main()

