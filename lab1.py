import random
class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.location = random.choice(list(environment.keys()))
    def sense(self):
        return self.environment[self.location]
    def act(self, action):
        if action == "left":
            self.location = "A"
        elif action == "right":
            self.location = "B"
        elif action == "clean":
            self.environment[self.location] = 0
def simulate_environment():
    return {"A": random.randint(0, 1), "B": random.randint(0, 1)}
def main():
    environment = simulate_environment()
    agent = VacuumCleanerAgent(environment)
    for _ in range(10):  # Simulate 10 steps
        print(f"Current State: {environment}")
        print(f"Agent Location: {agent.location}")
        dirt_status = agent.sense()
        if dirt_status == 1:
            print("Agent cleaning...")
            agent.act("clean")
        else:
            action = random.choice(["left", "right"])
            print(f"Agent moving {action}...")
            agent.act(action)
        print("---------")
if __name__ == "__main__":
    main()
