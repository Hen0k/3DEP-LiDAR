from requests_html import AsyncHTMLSession
import datetime
import asyncio
import json
import pandas as pd


def generate_links():
    base_url = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"

    with open("data/filenames.txt", "r") as f:
        urls = [(name.strip(), f"{base_url}{name.strip()}ept.json")
                for name in f.readlines()]
        return urls


async def fetch_json(url, s):
    area_name, uri = url
    for i in range(20):
        response = await s.get(uri)
        if response.status_code == 200:
            try:
                data = response.json()
                return {area_name: data}
            except:
                return fetch_json(url, s)
        print(f" Retrying: {uri}")


def transform(data):
    folder_name = next(iter(data.keys()))
    area_name, year = folder_name[:-6], folder_name[-5:-1]
    data = data.get(folder_name)
    bounds = data.get('bounds', [])
    xmin, ymin, zmin, xmax, ymax, zmax = bounds
    points = data.get('points', None)
    data = {
        "folder_name": folder_name,
        "area_name": area_name,
        "year": year,
        "xmin": xmin,
        "ymin": ymin,
        "zmin": zmin,
        "xmax": xmax,
        "ymax": ymax,
        "zmax": zmax,
        "points": points,
    }
    return data


async def get_ept_md(url):
    s = AsyncHTMLSession()
    data = await fetch_json(url, s)
    data = transform(data)
    return data


async def main(urls):
    tasks = [get_ept_md(url) for url in urls]
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    urls = generate_links()

    results = []
    jump=50
    for slice_idx in range(0, len(urls), jump):
        result = asyncio.run(main(urls[slice_idx:slice_idx+jump]))
        results += result
        if len(results)%jump*5 == 0:
            print(f"Reached at {len(results)}")
    
    results = list(filter(lambda e: e!=None, results))
    print(f"Final list length: {len(results)}")
    output_path = "data/areas_metadata.json"
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=4)
        print("Successfully built a JSON format metadata for the dataset")
    df = pd.read_json("data/areas_metadata.json")
    
    df.to_csv(output_path.replace(".json", ".csv"))
    print("Successfully built a CSV format metadata for the dataset")
    finish_time = datetime.datetime.now() - start_time
    print(f"Took {finish_time}")
