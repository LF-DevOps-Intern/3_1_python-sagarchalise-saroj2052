import argparse
import requests
from pywebcopy import save_webpage

def reqUrl(address):
        response = requests.get(address, timeout=7) 


parser = argparse.ArgumentParser()

parser.add_argument('--url', type=str, required=True)
parser.add_argument('--http_server', action='store_true')
args = parser.parse_args()


if args.http_server:
  print(args.url)
  url = args.url
  reqUrl(url)
  download_folder = './' # download on the same folder of the project    

  kwargs = {'bypass_robots': True, 'project_name': 'saroj'}

  save_webpage(url, download_folder, **kwargs)

print(args.url)
