import logging
from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded, MaxRetriesExceededError

logger = logging.getLogger(__name__)


@shared_task(
    name="T1: Git repository url changed",
    max_retries=1,
    soft_time_limit=8,
    time_limit=10,
    # rate_limit='12/h',
    ignore_result=True
)
def bot_msg_receive(folder_id: int):
    """ After changing git url -> Update folder files from git repository folder """
    try:
        pass
    except SoftTimeLimitExceeded:
        logger.warning(f'Deleting ')
