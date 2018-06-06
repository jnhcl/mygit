#!usr/bin/env python3
# _*_ coding: utf-8 _*_

__author__ = 'zxy'

import logging 
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler('log.txt')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info('----------------im the line---------------------');
logger.info('start printing');
