from Job import Job
from KernelFeaturesSample import KernelFeaturesSample
import numpy as np

class DeviceSuitabilityClassifier:
    def __init__(self):
        self._cpu_job_pool = []
        self._gpu_job_pool = []

    def classify(self, samples: KernelFeaturesSample):
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

            #if mean value of features is less then 0.5 sample goes to CPU, otherwise to GPU
            if np.array(scaled_sample).mean() < 0.5:    
                self._cpu_job_pool.append(sample)
            else:
                self._gpu_job_pool.append(sample)


    def get_cpu_job_pool(self):
        return self._cpu_job_pool


    def get_gpu_job_pool(self):
        return self._gpu_job_pool