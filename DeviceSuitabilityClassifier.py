from Job import Job
from KernelFeaturesSample import KernelFeaturesSample


class DeviceSuitabilityClassifier:
    def __init__(self):
        self._cpu_job_pool = []
        self._gpu_job_pool = []

    def classify(self, samples: KernelFeaturesSample):
        pass

    def get_cpu_job_pool(self) -> list[Job]:
        pass

    def get_gpu_job_pool(self) -> list[Job]:
        pass
