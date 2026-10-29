import json
import urllib.request

video_id = "64879338"
api_url = f"https://vimeo.com/api/v2/video/{video_id}.json"

req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())[0]
        print("🎬 Title:", data.get("title"))
        print("👤 Uploader Name:", data.get("user_name"))
        print("🔗 Uploader URL:", data.get("user_url"))
        print("📝 Description:", data.get("description"))
        print("🏷️ Tags:", data.get("tags"))
except Exception as e:
    print("Error fetching Vimeo API:", e)
