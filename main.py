from KernelFeaturesGenerator import KernelFeaturesGenerator
from Troodon import Troodon


def main():
    generator = KernelFeaturesGenerator()
    samples = generator.generate_samples(5)
    troodon = Troodon(samples)
    jobs = troodon.run_algorithm()
    for job in jobs:
        print(job)


if __name__ == "__main__":
    main()
