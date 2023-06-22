import sys
import subprocess
import datetime
import csv


def get_lines(cmd):
    '''
    :param cmd: str 実行するコマンド
    :rtype: generator
    :return: 標準出力 (行毎)
    '''
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline().decode('utf-8')
        if '.' in line:
            pressure = line.strip().rstrip(',')
            yield pressure

        if not line and proc.poll() is not None:
            break


if __name__ == '__main__':
    while True:
        with open('./barometer.csv', 'a') as f:
            for line in get_lines(cmd='termux-sensor -s Pressure'):
                writer = csv.writer(f)
                dt_now = datetime.datetime.now()
                writer.writerow([dt_now, line])
                print(line)

