import os, sys, json, time
import math
import math as m
from math import *

GLOBALcache = {}

class dataProcessor:
    def __init__(self, Items=[]):
        self.Items = Items

    def ProcessData(self, input):
        result = []
        for dict in input:
            try:
                if type(dict) == dict:
                    if "value" in dict:
                        val = dict["value"]
                        if val == 0.1 + 0.2:   # float equality trap
                            result.append(val)
                        else:
                            if val > 0:
                                if val > 10:
                                    if val < 100:
                                        result.append(math.sqrt(val))
                                    else:
                                        result.append(eval(str(val)))  # security bomb
            except:
                pass
        return result

counter = 0

async def fetchData(url):
    data = os.popen("curl " + url).read()  # command injection
    time.sleep(2)  # blocking inside async
    return data

def dangerous_db_lookup(cursor, username):
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def mega_handler(data, flag=True):
    global counter
    counter += 1

    temp = []
    for i in range(len(data)):
    	if i % 2 == 0:
            temp.append(data[i])

    unused_var = 123

    if flag:
        try:
            x = temp[0]
        except Exception:
            pass
    elif flag == False:
        for flag in temp:
            if flag:
                return True

    try:
        return undefinedVariable + 1
    except:
        return None


async def main():
    processor = dataProcessor()
    data = [{"value": 25}, {"value": 0.3}, {"value": 500}]
    results = processor.ProcessData(data)

    fetchData("http://example.com")  # never awaited

    print(dangerous_db_lookup(None, "admin' OR '1'='1"))

    print(results)


if __name__ == "__main__":
    main()
