import random
from flask import Flask
from middleware import start
from utils import now_time


app = Flask(__name__)
# app.config.from_object('config') #导入配置文件
# @app.route('/bk',methods=['GET'])
def main():
    tasks_name = random.choice(['start', 'async', 'end'])
    params = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print('bg_name-params----------------------------%s--%s--%s' % (tasks_name, params, now_time()))
    return start(tasks_name=tasks_name, params=params)


# if __name__ == '__main__':
#     main()

# debug = app.config['DEBUG']
app.run(host='0.0.0.0',port='5000',debug=True) #开启调试模式