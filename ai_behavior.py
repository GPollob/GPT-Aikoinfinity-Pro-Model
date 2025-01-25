from ai_integration.reinforcement_learning import QLearningAgent

def test_qlearning_agent():
    agent = QLearningAgent(action_space=3, state_space=5)
    initial_state = 0
    action = agent.choose_action(initial_state)
    assert action in range(3)
