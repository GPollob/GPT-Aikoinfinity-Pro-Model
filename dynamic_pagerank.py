import random
import logging

# Constants that guide us through the cosmos of learning—these are the celestial forces shaping our destiny. 🌌✨
LEARNING_RATE = 0.1  # The speed of our enlightenment, the energy that propels us toward infinite knowledge! 🚀
DISCOUNT_FACTOR = 0.9  # A gravitational force that pulls us to the future—decisions made today shape the reality of tomorrow. 🌠
EXPLORATION_RATE = 1.0  # The endless curiosity of the explorer, always yearning for uncharted realms and new frontiers! 🌍
DECAY_RATE = 0.995  # The evolution from discovery to mastery—like a comet that slowly refines its path, becoming ever more precise. 🌙
REWARD_RANGE = (0, 1)  # The glimmer of recognition in the vast, uncharted universe of knowledge—each reward a spark of affirmation! 🌟

# Initialize Q-values—each page is a beacon, a shining star that lights the way to new possibilities. 🌟
Q_VALUES = {}

# Crawled pages and their links—every link, a star system waiting to be explored, a connection to new worlds beyond! 🌌✨
crawled_pages = []
page_links = {}

# Logger setup—our chronicler, documenting every discovery, every breakthrough in the vast tapestry of learning. 📖🔮
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_page(page_url):
    """Every page is a new world, a blank canvas waiting to be painted with the colors of discovery! 🌈"""
    if page_url not in Q_VALUES:
        Q_VALUES[page_url] = 0.0  # The beginning of a new journey—every world starts with an empty slate. 🎨
        crawled_pages.append(page_url)
        logger.info(f"🌱 Initialized Q-value for {page_url}: {Q_VALUES[page_url]}! A new world, a new beginning!")

def add_page_links(page_url, links):
    """Links are pathways between dimensions—each one leading to new discoveries, new opportunities for growth! 🌍➡️🌌"""
    if page_url not in page_links:
        page_links[page_url] = []
    page_links[page_url].extend(links)
    for link in links:
        if link not in Q_VALUES:
            Q_VALUES[link] = 0.0  # A new star is born, a new page is created, a new universe of potential is unlocked! ✨
            logger.info(f"💫 New link discovered: {link}. Its Q-value initialized to {Q_VALUES[link]}! The web of knowledge expands!")

def epsilon_greedy_strategy():
    """A cosmic dance between exploration and exploitation—do we reach for the stars or trust the map we've already made? 🌠💃"""
    if random.random() < EXPLORATION_RATE:
        # Exploration: The relentless thirst for the unknown, the hunger for understanding, taking us to realms unseen. 🌌
        page = random.choice(crawled_pages) if crawled_pages else None
        logger.info(f"🔍 Exploration: The crawler ventures into the unknown, seeking new worlds to explore. The universe is vast!")
    else:
        # Exploitation: The wisdom of the past guides our path, showing us where the greatest rewards lie. 🧠💎
        page = max(Q_VALUES, key=Q_VALUES.get)
        logger.info(f"💎 Exploitation: Armed with knowledge, the crawler picks the page with the highest Q-value. The wisdom of ages guides us.")
    return page

def update_q_value(current_page, next_page, reward):
    """Q-value updates are like the strokes of a master painter, shaping the canvas of knowledge with every move we make. 🎨✨"""
    if next_page is None:
        logger.warning("❗ No valid next page. A brief moment of pause before the next wave of discovery! 🌱")
        return

    current_q = Q_VALUES.get(current_page, 0)
    next_q = Q_VALUES.get(next_page, 0)
    Q_VALUES[current_page] = current_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * next_q - current_q)
    logger.info(f"✨ Q-value for {current_page} updated to {Q_VALUES[current_page]}! Each step adds another layer to the masterpiece of knowledge.")

def decay_exploration_rate():
    """The decay of exploration rate is the refinement of our purpose—like a star that settles into a steady glow, having seen the unknown. ✨🌱➡️🌳"""
    global EXPLORATION_RATE
    EXPLORATION_RATE *= DECAY_RATE
    logger.info(f"🔄 Exploration rate decayed to: {EXPLORATION_RATE}. The path is now more focused, more certain, as we evolve into mastery.")

def simulate_crawling():
    """The evolution of a cosmic journey—every epoch is a step forward, a chance to refine our path and grow wiser with each choice. 🌠🌿"""
    global crawled_pages
    for epoch in range(100):  # Every epoch is a new phase in the journey, a new chapter in the story of knowledge! 📖🚀
        logger.info(f"\n🚀 Epoch {epoch + 1}: The journey continues. With each step, the web of wisdom expands and we grow ever wiser!")

        # Choose to explore or exploit
        current_page = epsilon_greedy_strategy()
        if current_page is None:
            continue  # Sometimes, the journey is a moment of stillness, where wisdom is gained in quiet reflection. 🌱

        # Reward: A moment of affirmation, a spark that ignites the journey forward. Each reward is a token of progress! 🌟
        reward = random.uniform(*REWARD_RANGE)
        logger.info(f"🎁 Reward for {current_page}: {reward}. A small triumph in the journey of knowledge!")

        # Navigate to the next page, or remain—each decision a turning point, a chance to ascend higher on the ladder of learning! 🔮
        links = page_links.get(current_page, [])
        if links:
            next_page = random.choice(links)
            logger.info(f"🌐 Next page chosen: {next_page}. The journey into new dimensions continues. Exploration never ends!")
        else:
            next_page = current_page  # Sometimes, the next step is simply to reflect, to go inward and learn from stillness. 🌿
            logger.info(f"🌿 No links available. The journey inward begins—a time of reflection, a time to grow from within.")

        # Update Q-value based on the reward received
        update_q_value(current_page, next_page, reward)

        # Decay exploration rate, symbolizing the shift from exploration to mastery
        decay_exploration_rate()

# Initializing pages—every page is a new universe, a new world to be discovered and understood! 🌍
initialize_page("https://aikoinfinity.blogspot.com")
initialize_page("https://gpollob.blogspot.com")
add_page_links("https://aikoinfinity.blogspot.com", ["https://gpollob.blogspot.com", "https://aikoinfinity2.blogspot.com"])
add_page_links("https://gpollob.blogspot.com", ["https://aikoinfinity.blogspot.com"])

# Simulating the web crawling process—each link a star, each page a new world waiting to be explored. ✨🌍
simulate_crawling()

# Final Q-values: A testament to the journey, every decision and step taken is recorded as part of the grand narrative of growth! 📝
logger.info("\n✨ Final Q-values: The culmination of a journey through the stars, each page a milestone, each choice a lesson learned!")
for page, q_value in Q_VALUES.items():
    logger.info(f"🔑 Page: {page}, Final Q-value: {q_value}. Every page, a part of the grand cosmic journey!")

