import numpy as np

from Job import CpuJob, Job
from KernelFeaturesSample import KernelFeaturesSample


class DeviceSuitabilityClassifier:
    def __init__(self):
        self._cpu_job_pool = []
        self._gpu_job_pool = []

    def classify(self, samples: list[KernelFeaturesSample]):
        """
        Input: samples
        Function assign samples to CPU or GPU based on classification result
        """

        scaled_sample = []

        for sample in samples:
            # conversion to list
            sample = list(sample.__dict__.values())

            for feature in sample:
                # normalization of features
                scaled_feature = (feature - np.min(sample)) / (np.max(sample) - np.min(sample))
                scaled_sample.append(scaled_feature)

            # if mean value of features is less then 0.5 sample goes to CPU, otherwise to GPU
            classification_result = float(np.array(scaled_sample).mean())
            job = Job(classification_result).get_suitable_job_type()
            if type(job) == type(CpuJob):
                self._cpu_job_pool.append(job)
            else:
                self._gpu_job_pool.append(job)

    def get_cpu_job_pool(self) -> list[Job]:
        return self._cpu_job_pool

    def get_gpu_job_pool(self) -> list[Job]:
        return self._gpu_job_pool
