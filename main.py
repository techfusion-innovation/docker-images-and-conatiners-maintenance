import logging

from src.container import clean_old_containers
from src.image import clean_old_images

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("app")

def main():
    """
    Main function to clean up old Docker images and containers.
    """
    logger.info("Starting cleanup of old Docker images and containers.")
    clean_old_images()
    clean_old_containers()


if __name__ == "__main__":
    main()
