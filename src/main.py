from src.pipelines.selic_meta import run_selic_meta
from src.pipelines.selic_over import run_selic_over


def main():
    run_selic_over()
    run_selic_meta()

if __name__ == "__main__":
    main()
