from KernelFeaturesGenerator import KernelFeaturesGenerator


def main():
    generator = KernelFeaturesGenerator()
    samples = generator.generate_samples(5)
    for sample in samples:
        sample.print()


if __name__ == "__main__":
    main()
