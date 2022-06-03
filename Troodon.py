from DeviceSuitabilityClassifier import DeviceSuitabilityClassifier
from KernelFeaturesSample import KernelFeaturesSample
from SpeedupPredictor import SpeedupPredictor


class Troodon:
    def __init__(self, samples: list[KernelFeaturesSample]):
        self._samples = samples
        self._device_suitability_classifier = DeviceSuitabilityClassifier()
        self._speedup_predictor = SpeedupPredictor()
        self._cpu_job_pool = []
        self._gpu_job_pool = []
        self._job_pool = []

    def run_algorithm(self):
        self._device_suitability_classifier.classify(self._samples)
        self._cpu_job_pool = self._device_suitability_classifier.get_cpu_job_pool()
        self._gpu_job_pool = self._device_suitability_classifier.get_gpu_job_pool()
        self._cpu_job_pool = self._speedup_predictor.predict(self._cpu_job_pool)
        self._gpu_job_pool = self._speedup_predictor.predict(self._gpu_job_pool)
        self._job_pool = self._get_job_pool()
        return self._job_pool

    def _get_job_pool(self):
        return self._cpu_job_pool + self._gpu_job_pool
