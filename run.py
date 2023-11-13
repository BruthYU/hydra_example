import logging
from time import time
import os
import hydra
import logging
import pickle
import struct
from omegaconf import OmegaConf,open_dict
from function import output

# hydra config uuid

logging.basicConfig(format='%(asctime)s - %(levelname)s [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
LOG = logging.getLogger(__name__)

@hydra.main(config_path='config', config_name='config')
def run(config):
    alg_CONFIG = dict(config.alg)
    collge_CONFIG = config.college

    LOG.info(f'[-alg CONFIG-] : {config.alg.version}')
    LOG.info(f'[-alg CONFIG-] : 123')
    output('Hello Hydra')

    with open(f'log.pkl', 'wb') as f:
        pickle.dump(
            {'all_UP': 1}, f)

if __name__ == '__main__':
    run()