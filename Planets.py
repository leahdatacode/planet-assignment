import random

class Planet:
    """
    Class representing a planet in the solar system.
    Stores information about mass, distance from the sun, and moons.
    """
    def __init__(self, name, mass, distance, moons):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.moons = moons

# List of planets
planets = [
    Planet("Mercury", 0.055, 0.387, []),
    Planet("Venus", 0.815, 0.723, []),
    Planet("Earth", 1.0, 1.0, ["Moon"]),
    Planet("Mars", 0.107, 1.524, ["Phobos", "Deimos"]),
    Planet("Jupiter", 317.8, 5.203, ["Io", "Europa", "Ganymede", "Callisto",
                                     "Amalthea", "Thebe", "Adrastea", "Metis",
                                     "Himalia", "Elara"]),
    Planet("Saturn", 95.16, 9.572, ["Titan", "Rhea", "Iapetus", "Dione",
                                    "Tethys", "Enceladus", "Mimas", "Hyperion",
                                    "Phoebe", "Janus"]),
    Planet("Uranus", 14.53, 19.194, ["Miranda", "Ariel", "Umbriel", "Titania",
                                     "Oberon", "Puck", "Portia", "Rosalind",
                                     "Cressida", "Cupid"]),
    Planet("Neptune", 17.15, 30.066, ["Triton", "Nereid", "Proteus", "Larissa",
                                      "Galatea", "Despina", "Thalassa", "Halimede",
                                      "Laomedeia", "Psamathe"])
]

# Synonyms to identify what is being asked
moon_synonyms = ["moon", "moons"]
distance_synonyms = ["distance", "far", "close", "near", "from the sun", "away", "where"]
mass_synonyms = ["mass", "weight", "heavy", "big", "size", "large", "huge", "massive"]
everything_synonyms = ["everything", "all"]
question_words = ["what", "how", "where", "when", "tell me"]

def show_menu():
    """Displays the main menu."""
    print("\nPlanets of the Solar System: Menu")
    print("1. Ask a question about a planet")
    print("2. Exit program")

def find_planet_in_question(question):
    """Finds which planet is mentioned in the question."""
    for p in planets:
        if p.name.lower() in question.lower():
            return p
    return None

def answer_question():
    """Handles the question and prints a response."""
    question = input("Enter your question: ").lower()

    # Validate that a question is being asked
    if not any(word in question for word in question_words):
        print("Sorry, I didn’t quite get that. Consider re-phrasing your question.")
        return

    # Pluto response
    if "pluto" in question:
        print("Pluto is a dwarf planet in the Kuiper belt. In 2006, the International Astronomical Union (IAU) formally redefined the term planet to exclude dwarf planets such as Pluto. As such, it is no longer considered a planet of the solar system.")
        return

    # Find the planet being asked about
    planet = find_planet_in_question(question)
    if not planet:
        print("Sorry, I'm not sure which planet you're asking about.")
        return

    # 'Tell me everything' response
    if any(word in question for word in everything_synonyms):
        moons = "no moons" if len(planet.moons) == 0 else ", ".join(planet.moons)
        print(f"{planet.name} info: mass={planet.mass} Earth masses, distance={planet.distance} AU, moons: {moons}")
        return

    # Mass response
    if any(word in question for word in mass_synonyms):
        print(f"{planet.name} has a mass of {planet.mass} Earth masses.")
    
    # Distance response
    elif any(word in question for word in distance_synonyms):
        print(f"{planet.name} is {planet.distance} astronomical units (AU) from the Sun. For reference, 1 AU equals approximately 93 million miles!")
    
    # Moons response
    elif any(word in question for word in moon_synonyms):
        if len(planet.moons) == 0:
            print(f"{planet.name} has no moons.")
        elif len(planet.moons) == 1:
            article = "the " if planet.name.lower() == "earth" else ""
            print(f"{planet.name}'s moon is {article}{planet.moons[0]}.")
        elif len(planet.moons) < 10:
            print(f"{planet.name} has {len(planet.moons)} moons: {', '.join(planet.moons)}")
        else:
            print(f"{planet.name} has many moons. The ten closest are: {', '.join(planet.moons[:10])}")
    else:
        print("Sorry, I didn't quite get that. Consider re-phrasing your question.")
   
    # Another question prompt
    again = input("Would you like to ask another question? Enter yes or no: ").lower()
    if again != 'yes':
        print("OK, goodbye!")
        exit()

def main():
    """Main program loop."""
    while True:
        show_menu()
        choice = input("Please enter 1 or 2: ")

        if choice == "1":
            answer_question()
        elif choice == "2":
            print("OK, goodbye!")
            break
        else:
            print("Invalid entry, try again.")

if __name__ == "__main__":
    main()
