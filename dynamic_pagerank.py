import random
import logging

# 🌟 Constants: These are the guiding stars, the fixed laws of the universe, setting the course for our adventure! 🌌
# Each constant represents a force, a principle that shapes the journey and leads us toward greater discovery. 🌍✨
const LEARNING_RATE = 0.1  # The cosmic velocity at which we absorb new knowledge! 🚀💡
const DISCOUNT_FACTOR = 0.9  # The gravity of future rewards, guiding our steps toward the ultimate goal. 🌠🔮
const EXPLORATION_RATE = 1.0  # The boundless curiosity that drives us into the unknown, forever seeking new frontiers! 🌌🌍
const DECAY_RATE = 0.995  # The natural evolution from curiosity to mastery, as we refine our journey over time. ⏳✨
const REWARD_RANGE = (0, 1)  # The spectrum of rewards, each one a beacon signaling progress on our path! 🌟🔑

# 🌌 Q-Values: These are the keys to the universe—our guideposts, revealing the value of every decision, every step taken. 🌍💫
const Q_VALUES = {}

# 🔗 Crawled Pages & Links: The cosmic web we weave, every link a star, every page a world awaiting exploration. 🌠✨
const crawled_pages = []
const page_links = {}

# 📖 Logger: Our chronicler, recording every twist and turn of the cosmic journey, capturing the story of our exploration! 🔮✨
const logger = logging.getLogger(__name__)

# 🔍 Function Definitions: These are our navigational tools, each one a step toward mastering the vast universe of knowledge. 🌌💎

def initialize_page(page_url):
    """🌱 Initialization: Every new page is a fresh world, waiting to be explored and understood. A new star is born! 🌠"""
    if page_url not in Q_VALUES:
        Q_VALUES[page_url] = 0.0  # A blank canvas, a new galaxy to explore. 🌍
        crawled_pages.append(page_url)
        logger.info(f"🌱 Initialized Q-value for {page_url}: {Q_VALUES[page_url]}! A new world begins its journey!")

def add_page_links(page_url, links):
    """🔗 Links: Pathways between worlds, stars connecting to form a constellation of knowledge! 🌌✨"""
    if page_url not in page_links:
        page_links[page_url] = []
    page_links[page_url].extend(links)
    for link in links:
        if link not in Q_VALUES:
            Q_VALUES[link] = 0.0  # Another star emerges, a new link in the constellation of knowledge! 🌠
            logger.info(f"💫 New link discovered: {link}. Its Q-value initialized to {Q_VALUES[link]}!")

def epsilon_greedy_strategy():
    """⚖️ Exploration vs. Exploitation: A cosmic dance between the thrill of discovery and the wisdom of the known. 🌠💃"""
    if random.random() < EXPLORATION_RATE:
        # Exploration: A leap into the unknown, driven by the eternal curiosity of the explorer. 🌍🚀
        page = random.choice(crawled_pages) if crawled_pages else None
        logger.info(f"🔍 Exploration: A bold venture into uncharted territory. The universe is endless!")
    else:
        # Exploitation: Using our accumulated wisdom to make the best possible choice. 🌌💡
        page = max(Q_VALUES, key=Q_VALUES.get)
        logger.info(f"💎 Exploitation: Armed with knowledge, we choose the page with the highest Q-value!")
    return page

def update_q_value(current_page, next_page, reward):
    """🎨 Updating Q-values: Each stroke of the brush refines our understanding, shaping the grand masterpiece of learning. 🌌🎨"""
    if next_page is None:
        logger.warning("❗ No valid next page. A brief pause before the next wave of discovery!")
        return

    current_q = Q_VALUES.get(current_page, 0)
    next_q = Q_VALUES.get(next_page, 0)
    Q_VALUES[current_page] = current_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * next_q - current_q)
    logger.info(f"✨ Q-value for {current_page} updated to {Q_VALUES[current_page]}! Each step adds another layer to the cosmic canvas of knowledge.")

def decay_exploration_rate():
    """🌿 Decay of Exploration: The refinement of our journey, a shift from endless curiosity to deep, purposeful mastery. 🌱➡️🌳"""
    global EXPLORATION_RATE
    EXPLORATION_RATE *= DECAY_RATE
    logger.info(f"🔄 Exploration rate decayed to: {EXPLORATION_RATE}. A more focused path forward, as we evolve into mastery.")

def simulate_crawling():
    """🌌 Simulation: A cosmic saga unfolds with each epoch—a journey where every choice, every decision leads us forward! 🌠🚀"""
    global crawled_pages
    for epoch in range(100):  # Each epoch, a chapter in the epic journey of discovery! 📖✨
        logger.info(f"\n🚀 Epoch {epoch + 1}: The adventure continues. With each step, the web of wisdom grows!")

        # Explore or exploit? The eternal decision, where the unknown meets the known in a cosmic dance! 💃🌌
        current_page = epsilon_greedy_strategy()
        if current_page is None:
            continue  # In moments of stillness, we reflect and prepare for the next phase of the journey! 🌿

        # Reward: A symbol of progress, a token affirming our journey toward enlightenment! 🎁🌠
        reward = random.uniform(*REWARD_RANGE)
        logger.info(f"🎁 Reward for {current_page}: {reward}. A small triumph on the journey to mastery!")

        # The next page, a new world, a new opportunity for growth and learning. 🌍🌠
        links = page_links.get(current_page, [])
        if links:
            next_page = random.choice(links)
            logger.info(f"🌐 Next page chosen: {next_page}. The journey into new dimensions continues!")
        else:
            next_page = current_page  # The inward journey begins—a time to reflect, a time to learn from within. 🌿
            logger.info(f"🌿 No links available. The journey inward starts.")

        # Update Q-value based on the reward and next page—each step is a brushstroke refining our masterpiece. 🎨✨
        update_q_value(current_page, next_page, reward)

        # Decay the exploration rate—mastery is near! 🌱➡️🌳
        decay_exploration_rate()

# 🌍 Initializing pages: Each page, a new universe, a new opportunity to expand the horizon of knowledge! 🌠✨
initialize_page("https://aikoinfinity.blogspot.com")
initialize_page("https://gpollob.blogspot.com")
add_page_links("https://aikoinfinity.blogspot.com", ["https://gpollob.blogspot.com", "https://aikoinfinity2.blogspot.com"])
add_page_links("https://gpollob.blogspot.com", ["https://aikoinfinity.blogspot.com"])

# 🚀 Simulating the crawl: Each epoch a new chapter in the unfolding cosmic journey of learning. 🌌✨
simulate_crawling()

# ✨ Final Q-values: The culmination of this cosmic journey, where each page reflects a milestone in the ever-expanding universe of wisdom. 📖💫
logger.info("\n✨ Final Q-values: The story of the journey, each decision shaping the future!")
for page, q_value in Q_VALUES.items():
    logger.info(f"🔑 Page: {page}, Final Q-value: {q_value}. Every page a part of the grand cosmic adventure!")
