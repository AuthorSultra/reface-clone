app_title = "ReActor"
version_flag = "v0.3.0"

from scripts.logger import logger, get_Run, set_Run

is_run = get_Run()

if not is_run:
    logger.info(f"Running {version_flag}")
    set_Run(True)
