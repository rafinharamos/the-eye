from celery import shared_task
from celery.utils.log import get_task_logger

from events.api.v1.serializers import EventSerializer
from events.models import EventError

logger = get_task_logger(__name__)


@shared_task()
def create_event(data):
    """
    Validate and create a new event
    """
    logger.info('Validating event data')
    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        logger.info(serializer.data)
        logger.info('Valid event data')
    else:
        EventError.objects.create(message=serializer.errors,
                                  data=serializer.data,
                                  )
        logger.info(serializer.data)
        logger.info('Invalid event data')