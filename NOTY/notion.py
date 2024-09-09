import json
import requests
from datetime import datetime

class NotionClient:

    def create_note(self, token, database_id, description, status):
        create_url = 'https://api.notion.com/v1/pages'

        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

        data = {
        "parent": { "database_id": database_id },
        "properties": {
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                            "start": datetime.now().astimezone().isoformat(), # getting the current time and date
                            "end": None
                        }
            },
            "Status": {
                "rich_text": [
                    {
                        "text": {
                            "content": status
                        }
                    }
                ]
            }
        }}

        data = json.dumps(data)
        res = requests.post(create_url, headers=headers, data=data)
        print(res.status_code)
        return res
