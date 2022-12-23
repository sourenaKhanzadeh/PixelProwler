# PixelProwler

PixelProwler is a web spider that crawls the internet for images based on user-provided prompts. It uses advanced web crawling and image recognition technology to search for and return relevant results.

## Installation

To install PixelProwler, clone this repository and run the following command:

```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py "cat pictures"
```

## Project Structure
```
.
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── spider.py
│   ├── image_search.py
│   ├── data_store.py
│   └── utils
│       ├── __init__.py
│       ├── image_utils.py
│       ├── web_utils.py
│       └── data_utils.py
├── data
├── tests
│   ├── __init__.py
│   ├── test_spider.py
│   ├── test_image_search.py
│   ├── test_data_store.py
│   └── utils
│       ├── __init__.py
│       ├── test_image_utils.py
│       ├── test_web_utils.py
│       └── test_data_utils.py
├── docs
│   ├── README.md
│   ├── user_manual.md
│   └── developer_guide.md
├── requirements.txt
└── setup.py
```
