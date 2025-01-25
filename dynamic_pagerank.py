import random
import logging
import numpy as np

# Logging configuration for dynamic PageRank simulation
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Parameters for PageRank and Q-learning dynamics
LEARNING_RATE = 0.1  # Learning rate for Q-value updates
DISCOUNT_FACTOR = 0.9  # Discount factor for future rewards
EXPLORATION_RATE = 1.0  # Initial exploration rate (100% exploration)
DECAY_RATE = 0.995  # Decay rate for exploration over time
META_LEARNING_RATE = 0.01  # Learning rate for meta-learning process

# Pages to crawl in the simulation (states)
pages = ["home", "about", "contact", "blog", "services", "portfolio"]

# Initialize Q-values for each page representing initial knowledge
Q_VALUES = {page: 0 for page in pages}

# External factors influencing the reward (e.g., user engagement)
external_factors = {
    "home": 1.0,  # Stable engagement factor for home page
    "about": 0.8,
    "contact": 0.5,
    "blog": 0.9,
    "services": 1.2,
    "portfolio": 1.1,
}

# Dynamic reward based on both immediate importance and external factors
def dynamic_reward(page):
    """
    Dynamically calculate the reward based on immediate importance and external user engagement factors.
    The agent finds fun and quirky ways to reward certain pages.
    """
    base_rewards = {
        "home": 10,
        "about": 5,
        "contact": 2,
        "blog": 7,
        "services": 8,
        "portfolio": 9,
    }
    # Playfully adjust the reward based on external factors and a "fun" mood factor
    fun_mood_factor = random.uniform(0.9, 1.1)  # Introducing fun factor into the reward
    logger.info(f"🌈 Fun mood factor applied: {fun_mood_factor:.2f}")
    return base_rewards.get(page, 0) * external_factors.get(page, 1.0) * fun_mood_factor

# Exploration vs. Exploitation Strategy (epsilon-greedy with reasoning and fun)
def epsilon_greedy_strategy():
    """
    The strategy considers exploration and exploitation but also factors in a fun, unpredictable AI that 
    takes curious, whimsical decisions along the way.
    """
    global EXPLORATION_RATE
    if random.random() < EXPLORATION_RATE:
        # Exploration: The agent feels playful, just wants to roam around!
        page = random.choice(pages)
        logger.info(f"🎉 Exploration: Let's try something new! Visiting {page}.")
    else:
        # Exploitation: The agent is feeling confident and applies its learned knowledge
        weighted_q_values = {page: Q_VALUES[page] * external_factors.get(page, 1.0) for page in pages}
        page = max(weighted_q_values, key=weighted_q_values.get)
        logger.info(f"🚀 Exploitation: Confidently heading to {page} based on what I know!")
    
    return page

# Meta-learning: Adjusting the exploration rate based on long-term optimization goals
def meta_learning_adjustment():
    """
    The agent knows it has to grow, so it adjusts its exploration rate to balance out curiosity and smart decision-making.
    """
    global EXPLORATION_RATE
    exploration_change = META_LEARNING_RATE * (1 - EXPLORATION_RATE)
    EXPLORATION_RATE += exploration_change  # The agent is getting wiser
    logger.info(f"🔄 Meta-learning adjustment: Exploration rate updated to {EXPLORATION_RATE}.")

# Update Q-value with reasoning, considering both immediate reward and future outcomes
def update_q_value(current_page, next_page, reward):
    """
    Update Q-values with deeper reasoning, considering fun dynamics and long-term implications.
    The agent is evolving and improving its strategies based on long-term rewards.
    """
    current_q = Q_VALUES.get(current_page, 0)
    next_q = Q_VALUES.get(next_page, 0)

    # The agent learns to reason about rewards and incorporate its own fun logic
    Q_VALUES[current_page] = current_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * next_q - current_q)
    logger.info(f"✨ Updated Q-value for {current_page}: {Q_VALUES[current_page]}.")

# Decay the exploration rate over time to shift focus towards optimal strategies
def decay_exploration_rate():
    """
    The exploration rate is decayed as the agent matures, but it still keeps a bit of curiosity.
    """
    global EXPLORATION_RATE
    EXPLORATION_RATE *= DECAY_RATE
    logger.info(f"🔄 Exploration rate decayed to: {EXPLORATION_RATE}.")

# Main simulation loop: learning from the web's digital landscape with a dash of fun!
def crawl_website():
    """
    Simulate the website crawling process, incorporating deep reasoning, fun, and curiosity at each step to 
    improve the agent's decision-making. The agent learns, adjusts, and refines its strategy based on immediate 
    and long-term goals while having fun in the process!
    """
    for step in range(10):  # Simulate 10 steps of exploration and learning
        logger.info(f"\nStep {step + 1}:")
        current_page = epsilon_greedy_strategy()  # Choose next page with fun reasoning
        reward = dynamic_reward(current_page)  # Calculate dynamic reward considering external factors and fun
        logger.info(f"🎯 Crawled {current_page}, received reward: {reward}")
        
        # Simulate moving to the next page (could be influenced by reasoning or randomness)
        next_page = random.choice(pages)
        update_q_value(current_page, next_page, reward)  # Update Q-values based on reasoning

        meta_learning_adjustment()  # Adjust exploration rate based on reasoning and fun

        decay_exploration_rate()  # Decay the exploration rate as learning progresses

    # Final summary: Reflect on what the agent has learned with a fun, whimsical touch
    logger.info("\n✨ Final Q-values after deep reasoning process with fun:")
    for page, q_value in Q_VALUES.items():
        logger.info(f"🔑 Page: {page}, Final Q-value: {q_value}.")

# Execute the enhanced crawling process
if __name__ == "__main__":
    crawl_website()
