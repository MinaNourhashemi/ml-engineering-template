import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def train_model() -> None:
    logger.info("event=training_started model=dummy_model")
    logger.info("event=training_finished status=success")
