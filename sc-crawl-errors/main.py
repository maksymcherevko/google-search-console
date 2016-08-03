#!/usr/bin/python

import os
import argparse
import sys
import json
import time
import urllib
import logging
from googleapiclient import sample_tools as api_client

argparser = argparse.ArgumentParser(add_help=False)
required_named = argparser.add_argument_group('required named arguments')

required_named.add_argument('-u', '--url', type=str, required=True, nargs='?', metavar='URL',
    help='The site\'s URL, including protocol. For example: http://www.example.com/')

required_named.add_argument('-c', '--category', type=str, required=True, nargs='?', metavar='category',
    choices=['authPermissions', 'flashContent', 'manyToOneRedirect', 'notFollowed', 'notFound', 'other', 'roboted', 'serverError', 'soft404'],
    help='The crawl error category. For example: notFound')

required_named.add_argument('-p', '--platform', type=str, required=True, nargs='?', metavar='platform',
    choices=['mobile', 'smartphoneOnly', 'web'],
    help='The user agent type (platform) that made the request. For example: web')

def getList(service, flags):

    logger.info('Start getting the list of urls')
    try:
        jsonResponse = service.urlcrawlerrorssamples().list(
            siteUrl=flags.url, category=flags.category, platform=flags.platform).execute()
        logger.info('Finish getting the list of urls. SUCCESS')
    except Exception, e:
        logger.error('Finish getting the list of urls. FAILED. ' + str(e))
        return False

    return jsonResponse

def setMarkAsFixed(service, flags, jsonData, limit=1000):

    successCount = failedCount = 0
    successJsonData = []

    logger.info('Start marking urls as fixed')

    elementsCount = len(jsonData['urlCrawlErrorSample'])

    if elementsCount == 0:
        logger.error('Start marking urls as fixed. FAILED. Elements count == 0')
        return False

    for key, row in enumerate(jsonData['urlCrawlErrorSample']):

        if key >= limit:
            break

        if row['pageUrl']:
            try:
                json_response = service.urlcrawlerrorssamples().markAsFixed(
                    siteUrl=flags.url, url=row['pageUrl'], category=flags.category, platform=flags.platform).execute()

                successJsonData.append(row)
                successCount += 1
            except Exception, e:
                failedCount += 1

    logger.info('Finish marking urls as fixed. COUNT [' + str(elementsCount) + '] - SUCCESS [' + str(successCount) + '] - FAILED [' + str(failedCount) + ']')

    return {'urlCrawlErrorSample' : successJsonData}

def logResponse(jsonData):

    logger.info('Start dumping list of urls')

    try:
        if not os.path.exists('reports'):
            os.makedirs('reports')
        fileName = 'reports/' + str(time.strftime('%Y-%m-%d %H:%M')) + '.log'
        with open(fileName, 'w') as logFile:
            json.dump(jsonData, logFile, indent=4, sort_keys=True)
        logger.info('Finish dumping list of urls. SUCCESS. Filename: ' + str(fileName))
    except Exception, e:
            logger.error('Finish dumping list of urls. FAILED. ' + str(e))
            return False

    return True

def getLogger():

    handler = logging.FileHandler('app.log')
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger

def main(argv):

    logger.info('App START')
    logger.info('Start API service')

    try:
        service, flags = api_client.init(
            argv, 'webmasters', 'v3', __doc__, __file__, scope='https://www.googleapis.com/auth/webmasters', parents=[argparser])
        logger.info('Finish API service. SUCCESS')
    except Exception, e:
        logger.error('Finish API service. FAILED. ' + str(e))
        return False

    jsonResponse = getList(service, flags)

    if not jsonResponse:
        return False

    successJsonData = setMarkAsFixed(service, flags, jsonResponse, 5)

    if not successJsonData:
        return False

    logResponse(successJsonData)

if __name__ == '__main__':

    logger = getLogger()
    main(sys.argv)
    logger.info('App FINISH\n\n\n')