import sys
import os
sys.path.append('..')
import argparse
from src import search

def main():
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('prompt', help='the search prompt')
    parser.add_argument('-n', '--num-results', type=int, default=10, help='the number of results to return')
    args = parser.parse_args()

    # Search for images based on the prompt
    image_urls = search(args.prompt, args.num_results)

    # Print the image URLs
    for url in image_urls:
        print(url)

if __name__ == '__main__':
    main()
