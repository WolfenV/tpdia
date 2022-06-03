from KernelFeaturesGenerator import KernelFeaturesGenerator
from Troodon import Troodon

def main():
    generator = KernelFeaturesGenerator()
    samples = generator.generate_samples(5)
    for sample in samples:
        sample.print()
    troodon = Troodon(samples)
    troodon.run_algorithm()

if __name__ == "__main__":
    main()
