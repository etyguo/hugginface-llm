# LLM Course - Chapter 1

Following the Hugging Face LLM Course: https://huggingface.co/learn/llm-course/en/chapter1/3

## Usage

### Local Development

This project uses `uv` for dependency management.

1.  **Install uv:**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  **Install dependencies:**
    ```bash
    uv sync
    ```

3.  **Run the script:**
    ```bash
    uv run chapter1_3.py
    ```

### Docker (with GPU Support)

1.  **Build the image:**
    ```bash
    docker build -t llm-course .
    ```

2.  **Run with NVIDIA GPU:**
    (Requires [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) installed on the host)
    ```bash
    docker run --gpus all -it --rm llm-course
    ```

    *To mount your local files (e.g., to access downloaded audio):*
    ```bash
    docker run --gpus all -it --rm -v $(pwd):/app -v /home/et/Downloads:/home/et/Downloads llm-course
    ```

