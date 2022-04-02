import boto3
import time
class DatabaseHandler:

    #TODO: #1 gestire quando il db è spento
    def __init__(self, database: str) -> None:
        self.__rdsData = boto3.client('rds-data')
        self.__cluster_arn = 'arn:aws:rds:eu-central-1:123446374287:cluster:sweeat'
        self.__secret_arn = 'arn:aws:secretsmanager:eu-central-1:123446374287:secret:rds-db-credentials/cluster-AQLMTHUP2LEAFVXYXDMZFEHDR4/admin-5WXjei'
        self.__database = database
        self.__wait_for_db_on()

    #chehck if db is turned on
    def __is_db_on (self):
        response = self.__rdsData.execute_statement(resourceArn = self.__cluster_arn,
                                      secretArn = self.__secret_arn,
                                      database = self.__database,
                                      sql = 'SELECT 1',
                                      parameters = [],
                                      includeResultMetadata = True)
        return response



    #for two minutes check if db is on
    def __wait_for_db_on (self):
        ok = False
        for i in range (20):
            response = self.__is_db_on()
            if response['records'] != []:
                print('db is on')
                ok = True
                break
            else:
                print('db is off, i will try again in 20 seconds...')
                time.sleep(20)
        if ok is False: print('cannot connect to db, exiting...')
        




    def __parse_result (self, results):
        columns = [column['name'] for column in results['columnMetadata']]
        parsed_records = []
        for record in results['records']:
            parsed_record = {}
            for i, cell in enumerate(record):
                key = columns[i]
                value = list(cell.values())[0]
                parsed_record[key] = value
            parsed_records.append(parsed_record)
        return parsed_records

    #param_set format: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.execute_statement
    def do_write_query (self, query: str, param_set = []):
        response = self.__rdsData.execute_statement(resourceArn = self.__cluster_arn,
                                      secretArn = self.__secret_arn,
                                      database = self.__database,
                                      sql = query,
                                      parameters = param_set)
        return response

    #param_set format: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.execute_statement
    def do_read_query (self, query:str, param_set = []):
        response = self.__rdsData.execute_statement(resourceArn = self.__cluster_arn,
                                      secretArn = self.__secret_arn,
                                      database = self.__database,
                                      sql = query,
                                      parameters = param_set,
                                      includeResultMetadata = True)
        return self.__parse_result (response)

