def download(url):
  from halo import Halo
  import os
  import requests
  with Halo(text='Downloading', spinner='dots'):
    try:
        fileName = os.path.basename(url)
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(fileName, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    f.write(chunk)
        print(f'\n{fileName}')
        return fileName
    except requests.exceptions.RequestException as e:
        print(f'\n{e}')
