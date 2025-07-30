def lambda_handler(event, context):
    a = 10
    b = 15
    result = a + b
    
    return {
        'statusCode': 200,
        'body': f'The sum of {a} and {b} is {result}'
    }
