import logging
LOG = logging.getLogger(__name__)

def output(info):
    LOG.info(f'[-function Info-] : {info}')