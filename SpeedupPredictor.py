from Job import Job, CpuJob


class SpeedupPredictor:
    def __init__(self):
        self._job_pool = []

    def predict(self, job_pool: list[Job]) -> list[Job]:
        self._job_pool = job_pool
        if len(self._job_pool) > 0:
            if type(self._job_pool[0]) == CpuJob:
                self._job_pool = job_pool
                self._job_pool.sort(key=lambda job: job.cpu_suitability)
            else:
                self._job_pool.sort(key=lambda job: job.gpu_suitability, reverse=True)

        return self._job_pool
