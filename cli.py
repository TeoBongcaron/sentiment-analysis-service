import argparse
import requests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str)
    parser.add_argument("--url", default="http://localhost:5000/predict")
    args = parser.parse_args()

    resp = requests.post(args.url, json={"text": args.text})
    print(resp.json())

if __name__ == "__main__":
    main()

