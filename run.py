import logging
from time import time
import os
import hydra
import logging
import struct
from omegaconf import OmegaConf,open_dict
from function import output

logging.basicConfig(format='%(asctime)s - %(levelname)s [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
LOG = logging.getLogger(__name__)

@hydra.main(config_path='config', config_name='config')
def run(config):
    alg_CONFIG = dict(config.alg)
    collge_CONFIG = config.college

    LOG.info(f'[-alg CONFIG-] : {config.alg.version}')
    LOG.info(f'[-alg CONFIG-] : 123')
    output('Hello Hydra')

if __name__ == '__main__':
    run()