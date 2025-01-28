
import logging
from .configuration import config
# Configure logger
log_level = config.get("logger","level",fallback='INFO')
print(log_level)

logging.basicConfig(level=log_level, filemode='a', 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("wag.main")