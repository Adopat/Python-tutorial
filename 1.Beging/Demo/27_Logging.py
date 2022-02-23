# # Python 日志记录
# print("=====日志示例=====")
# import logging
# logging.warning("This is a warning!")
print("=====日志严重程度=====")
import logging

logging.basicConfig(filename='program.log', level=logging.DEBUG)
logging.warning('An example message.')
logging.warning('Another message')
print("=====记录时间=====")
# import logging
#
# logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
# logging.info('Logging app started')
# logging.warning('An example logging message.')
# logging.warning('Another log message')

logging.basicConfig(filename='program1.log', format='%(asctime)s %(message)s', level=logging.INFO)
logging.info('Logging app started')
logging.warning('An example logging message.')
logging.warning('Another log message')
