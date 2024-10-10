import logging
from time import time
import os
import hydra
import logging
import pickle
import struct
from omegaconf import OmegaConf,open_dict
from function import output




LOG = logging.getLogger(__name__)

@hydra.main(config_path='config', config_name='config')
def run(config):

    LOG.info(f'os.getcwd(): {os.getcwd()}')
    LOG.info(f'hydra.utils.get_original_cwd(): {hydra.utils.get_original_cwd()}')

    LOG.info(f'[-alg CONFIG-] : {config.alg.version}')
    LOG.info(f'[-alg CONFIG-] : 123')
    output('Hello Hydra')

    with open(f'log.pkl', 'wb') as f:
        pickle.dump(
            {'all_UP': 1}, f)

if __name__ == '__main__':
    run()