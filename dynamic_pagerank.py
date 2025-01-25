import random
import numpy as np
import logging

class DynamicPageRank:
    """
    An advanced web crawler that dynamically optimizes page ranking using Q-learning.
    It applies deep reinforcement learning principles to adjust the page rankings based on web exploration.
    Emphasizes best practices for code maintainability, efficiency, and readability.
    
    Developed by: Gazi P0ll0B Hussain (G|I|X)
    """

    def __init__(self, pages=None, links=None, alpha=0.1, gamma=0.9, epsilon=0.1, decay_rate=0.995):
        """
        Initializes the DynamicPageRank class with pages and links to simulate dynamic crawling and ranking.

        :param pages: List of page URLs (default: empty list)
        :param links: Dictionary of links between pages (default: empty dict)
        :param alpha: Learning rate (default 0.1)
        :param gamma: Discount factor (default 0.9)
        :param epsilon: Exploration rate (default 0.1)
        :param decay_rate: Rate at which epsilon (exploration) decays over time (default 0.995)
        """
        self.pages = pages or []  # List of pages to crawl
        self.links = links or {}  # Links between pages
        self.q_values = {page: 0 for page in self.pages}  # Initialize Q-values to 0 for all pages

        # Q-learning hyperparameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.decay_rate = decay_rate  # Decay for exploration rate

        # Logging setup
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

    def add_page(self, page, links=None):
        """
        Adds a new page and its associated links to the crawling process.

        :param page: The page to add (string URL or identifier)
        :param links: List of pages that the new page links to
        """
        if links is None:
            links = []
        self.pages.append(page)
        self.links[page] = links
        if page not in self.q_values:
            self.q_values[page] = 0  # Initialize Q-value for the new page
        logging.info(f"New page added: {page} with links: {links}")

    def update_q_value(self, current_page, next_page, reward):
        """
        Updates the Q-value of the current page based on moving to the next page.
        This follows the Q-learning formula for updates: 
        Q(s, a) = Q(s, a) + alpha * (reward + gamma * max(Q(s', a')) - Q(s, a))

        :param current_page: Current page that is being evaluated
        :param next_page: Next page that the crawler visits
        :param reward: The reward from moving to the next page (0 to 1)
        """
        current_q = self.q_values.get(current_page, 0)
        next_max_q = max(self.q_values.get(next_page, 0), 0)  # Max Q-value for the next page

        # Q-learning update rule
        new_q_value = current_q + self.alpha * (reward + self.gamma * next_max_q - current_q)
        self.q_values[current_page] = new_q_value
        logging.debug(f"Q-value updated for {current_page}: {current_q} -> {new_q_value}")

    def get_next_page(self, current_page):
        """
        Decides the next page to visit based on the current page's Q-values and the links available.
        Implements both exploration and exploitation strategies.

        :param current_page: Current page to evaluate for next move
        :return: The next page to visit
        """
        possible_links = self.links.get(current_page, [])
        if not possible_links:
            logging.warning(f"No further links from {current_page}, staying put.")
            return current_page

        # Exploration vs Exploitation tradeoff using epsilon-greedy strategy
        if random.uniform(0, 1) < self.epsilon:  # Exploration: pick a random page
            next_page = random.choice(possible_links)
            logging.info(f"Exploration: Moving from {current_page} to {next_page}")
        else:  # Exploitation: pick the page with the highest Q-value
            next_page = max(possible_links, key=lambda page: self.q_values.get(page, 0))
            logging.info(f"Exploitation: Moving from {current_page} to {next_page}")

        # Decay the epsilon value to shift from exploration to exploitation over time
        self.epsilon *= self.decay_rate
        logging.debug(f"Epsilon decayed to: {self.epsilon}")

        return next_page

    def crawl(self, start_page, num_steps=10):
        """
        Simulates the crawling process over multiple steps, starting from the given page.
        The crawling dynamically updates Q-values based on the visited pages.

        :param start_page: The starting page to begin crawling
        :param num_steps: Number of crawling steps to perform
        """
        current_page = start_page
        for step in range(num_steps):
            logging.info(f"Step {step + 1}: Currently on {current_page}")
            next_page = self.get_next_page(current_page)

            # Simulate a reward for visiting the next page (this can be adjusted)
            reward = random.uniform(0, 1)  # A random reward (between 0 and 1)
            self.update_q_value(current_page, next_page, reward)

            # Move to the next page
            current_page = next_page

    def print_q_values(self):
        """
        Prints the current Q-values for all pages, helping track the learning progress.
        """
        logging.info("Current Q-values:")
        for page, q_value in self.q_values.items():
            logging.info(f"Page: {page}, Q-value: {q_value:.4f}")

    def print_links(self):
        """
        Prints the links available for each page in the crawling process.
        """
        logging.info("Page Links:")
        for page, links in self.links.items():
            logging.info(f"Page: {page}, Links: {links}")


# Example Usage:

# Define the pages and links
pages = ['https://gpollob.blogspot.com/', 'https://aikoinfinity.blogspot.com', 'P3']
links = {
    'https://aikoinfinity.blogspot.com': ['P2', 'P3'],
    'https://gpollob.blogspot.com/': ['P1'],
    'https://gixsync.blogspot.com/': ['P2']
}

# Create the DynamicPageRank object
crawler = DynamicPageRank(pages, links)

# Print the initial links and Q-values
crawler.print_links()

# Start the crawling process with detailed logging
crawler.crawl('https://aikoinfinity.blogspot.com', num_steps=5)

# Print the updated Q-values after crawling
crawler.print_q_values()
