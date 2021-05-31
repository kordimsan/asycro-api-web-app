import time
from datetime import datetime

class Worker:
    """
    Результаты задач воркера складываются в список (список из целых чисел).
    Задачи воркера состоят из двух параметров: 	
        num: int - целое число, которое будет добавлено в список
        timeout: int - время ожидания работы (в сек)
    """
    _list = []
    _queue = []
    
    def add_task(self, num: int, timeout: int):
        self._queue.append({
            'num': num,
            'timeout': timeout,
            'addtime': datetime.now()
        })
    
    def del_task(self, _task):
        for q in self._queue:
            if _task['addtime'] == q['addtime']:
                self._queue.remove(_task)

    def resolve_task(self, _task):
        time.sleep(_task['timeout'])
        self._list.append(_task['num'])
        self.del_task(_task)

    def run_worker(self):
        while True:
            time.sleep(0.1)
            if self._queue:
                _task = self._queue[0]
                self.resolve_task(_task)

    def get_queue(self):
        return self._queue
    
    def get_list(self):
        return self._list