import random
import logging
import numpy as np
from datetime import datetime

# Logging configuration for dynamic KPI and learning simulation
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("KPI_Monitoring")

class KPI_Monitor:
    """
    AikoInfinity 2.0 - Founded by Gazi P0ll0B Hussain (G|I|X)
    The KPI_Monitor class tracks and optimizes multiple Key Performance Indicators (KPIs)
    for the system, enabling real-time, adaptive decision-making.
    """

    def __init__(self):
        self.metrics = {
            "crawl_efficiency": [],
            "user_engagement": [],
            "resource_utilization": []
        }

    def update_metrics(self, crawl_time, user_interaction, resource_usage):
        efficiency = max(100 - crawl_time, 0)  # Higher efficiency for faster crawls
        self.metrics["crawl_efficiency"].append(efficiency)
        self.metrics["user_engagement"].append(user_interaction)
        self.metrics["resource_utilization"].append(resource_usage)
        logger.info(f"Updated Metrics: Efficiency={efficiency}, Engagement={user_interaction}, Resource Usage={resource_usage}")

    def get_current_metrics(self):
        return {
            "crawl_efficiency": self.metrics["crawl_efficiency"][-1] if self.metrics["crawl_efficiency"] else None,
            "user_engagement": self.metrics["user_engagement"][-1] if self.metrics["user_engagement"] else None,
            "resource_utilization": self.metrics["resource_utilization"][-1] if self.metrics["resource_utilization"] else None,
        }

    def log_metrics(self):
        logger.info(f"Current Metrics: {self.get_current_metrics()}")

class QLearningAgent:
    """
    Q-Learning Agent for adaptive web crawling and decision-making with multi-metric optimization.
    """

    def __init__(self, pages, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, decay_rate=0.995):
        self.pages = pages
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.decay_rate = decay_rate
        self.q_values = {page: 0.0 for page in pages}
        self.external_factors = {page: random.uniform(0.8, 1.2) for page in pages}

    def dynamic_reward(self, page):
        base_rewards = {
            "home": 10,
            "about": 5,
            "contact": 2,
            "blog": 7,
            "services": 8,
            "portfolio": 9,
        }
        reward = base_rewards.get(page, 0) * self.external_factors[page]
        logger.info(f"Reward for {page}: {reward:.2f} (External Factor: {self.external_factors[page]:.2f})")
        return reward

    def epsilon_greedy_strategy(self):
        if random.random() < self.exploration_rate:
            page = random.choice(self.pages)
            logger.info(f"Exploration: Visiting {page}")
        else:
            page = max(self.q_values, key=self.q_values.get)
            logger.info(f"Exploitation: Prioritizing {page}")
        return page

    def update_q_value(self, current_page, next_page, reward):
        current_q = self.q_values[current_page]
        next_q = self.q_values[next_page]
        self.q_values[current_page] = current_q + self.learning_rate * (reward + self.discount_factor * next_q - current_q)
        logger.info(f"Updated Q-value for {current_page}: {self.q_values[current_page]:.2f}")

    def decay_exploration_rate(self):
        self.exploration_rate *= self.decay_rate
        logger.info(f"Decayed Exploration Rate: {self.exploration_rate:.3f}")

# Simulated Environment Integration
class Simulation:
    def __init__(self):
        self.kpi_monitor = KPI_Monitor()
        self.pages = ["home", "about", "contact", "blog", "services", "portfolio"]
        self.agent = QLearningAgent(self.pages)

    def run(self, steps=10):
        for step in range(steps):
            logger.info(f"\n--- Simulation Step {step + 1} ---")

            current_page = self.agent.epsilon_greedy_strategy()
            reward = self.agent.dynamic_reward(current_page)
            next_page = random.choice(self.pages)

            self.agent.update_q_value(current_page, next_page, reward)

            crawl_time = random.randint(5, 15)
            user_engagement = random.randint(50, 100)
            resource_usage = random.randint(30, 70)

            self.kpi_monitor.update_metrics(crawl_time, user_engagement, resource_usage)
            self.kpi_monitor.log_metrics()

            self.agent.decay_exploration_rate()

        logger.info("\nFinal Q-Values:")
        for page, q_value in self.agent.q_values.items():
            logger.info(f"Page: {page}, Q-Value: {q_value:.2f}")

# Execute the simulation
if __name__ == "__main__":
    simulation = Simulation()
    simulation.run(steps=20)
