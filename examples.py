import aws_lambda_logging
import logging

logger = logging.getLogger()
loglevel = "DEBUG"
botologlevel = "CRITICAL"


# Example 1 - Basic log entry
def handler_example1(event, context):
 aws_lambda_logging.setup(level='INFO')
 
 logger.info('This is an example message')
 
 
 # Example 2 - Basic log entry with Lambda context Objects
def handler_example2(event, context):
 aws_lambda_logging.setup(level='INFO', aws_function_id=context.function_name, aws_request_id=context.aws_request_id, aws_identity=context.identity.cognito_identity_id)
 
 logger.info('This is example number 2')


# Example 3 - Basic log entry with custom key
def handler_example3(event, context):
 aws_lambda_logging.setup(level='INFO', This_Is_A_Custom_Key="This is the custom keys value")
 
 logger.info('This is example number 3')
 
 
 # Example 4 - Basic log entry with varying log levels
 def handler_example4(event, context):
 aws_lambda_logging.setup(level='INFO')
 
 logger.info('This is example number 4 - INFO level')
 logger.warning('This is example number 4 - WARNING level')
 logger.error('This is example number 4 - ERROR level')
 logger.debug("This is example number 4 - DEBUG level which you won't see in the output")
 
 
 # Example 5 - JSON String log entry
 def handler_example5(event, context):
 aws_lambda_logging.setup(level='INFO')
 
 logger.info('{"Example 5": [1,2,3]}')


 # Example 6 - Variant boto logging level
def handler_example6(event, context):
 aws_lambda_logging.setup(level=loglevel, boto_level=botologlevel)
