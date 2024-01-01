import csv
import json

import requests

from schema import ExtractedData, Property

data_file_path = "./data.json"
housing_data_path = "./data.csv"

slugs = ["ashanti", "greater-accra"]

Json = list[dict]


def write_to_dump(file_path: str, data: Json):
    with open(file_path, "+a", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def write_to_results(file_path: str, data: Json):
    with open(file_path, "+a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        adverts = [Property(**advert) for advert in data]
        extracted = [
            ExtractedData(
                region_id=ad.region_id,
                region_name=ad.region_name,
                region_parent_name=ad.region_parent_name,
                description=ad.short_description,
                price=ad.price_obj.value,
                message_url=ad.message_url,
            )
            for ad in adverts
        ]

        for ad in extracted:
            row = []
            for _, value in ad:
                row.append(value)
            csv_writer.writerow(row)


def scrape_from_internet(region_slug: str, page_size: int):
    responses: Json = []
    for i in range(1, page_size + 1):
        url = f"https://jiji.com.gh/api_web/v1/listing?slug=real-estate&init_page=true&region_slug={region_slug}&page={i}&webp=true&lsmid=1704112165200"

        data = requests.get(url)
        responses.append(data.json())

    write_to_dump(file_path=data_file_path, data=responses)


def process_data(file_path: str, results_file_path: str):
    with open(file_path, "r") as file:
        data = json.load(file)

        for item in data:
            obj: dict = item["adverts_list"]["adverts"]

            write_to_results(file_path=results_file_path, data=obj)


# this was just for testing purposes
print("Scraping from the internet")
scrape_from_internet(slugs[1], page_size=100)

print("Processing information")
process_data(file_path=data_file_path, results_file_path=housing_data_path)
