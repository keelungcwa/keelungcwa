import requests
import json
from datetime import datetime, timedelta
import os
import pytz

# 讀取 API Key（從環境變數）
API_KEY = os.getenv("CWA_API_KEY")
if not API_KEY:
    raise ValueError("❌ 環境變數 CWA_API_KEY 未設定！請在 CWA 開放資料平台註冊並設定環境變數，例如在終端機輸入 'export CWA_API_KEY=your_key'")

# API 參數
DATA_IDS = ["O-A0003-001", "O-A0001-001"]
FORMAT_TYPE = "JSON"
ELEMENTS = "AirTemperature,RelativeHumidity,WindSpeed,WindDirection,Precipitation,AirPressure,Weather"

# 儲存 JSON 檔案的目錄
OUTPUT_DIR = "data"
JSON_OUTPUT_FILE = os.path.join(OUTPUT_DIR, "keelung_data.json")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 設定時區（台灣）
taiwan_tz = pytz.timezone("Asia/Taipei")

# 載入現有資料（如果存在）
all_data = []
if os.path.exists(JSON_OUTPUT_FILE):
    with open(JSON_OUTPUT_FILE, "r", encoding="utf-8") as f:
        all_data = json.load(f)
    
    # 清理歷史資料中的 -99 或 -99.0
    for entry in all_data:
        for key, value in entry["weather_elements"].items():
            if key != "Weather" and value in [-99, -99.0, "-99"]:
                entry["weather_elements"][key] = None
                print(f"🧹 清理歷史資料: 站點 {entry['station_name']}, 欄位 {key}, 值 {value} 轉為 null")

# 過濾舊資料（保留 72 小時內的資料）
cutoff_time_72h = taiwan_tz.localize(datetime.now()) - timedelta(hours=72)
all_data = [entry for entry in all_data if datetime.strptime(entry["time"], "%Y-%m-%dT%H:%M:%S%z") >= cutoff_time_72h]

# 設定 API 資料時間範圍（最近 24 小時）
cutoff_time = taiwan_tz.localize(datetime.now()) - timedelta(hours=24)

# 定義 safe_get 函數，處理無效值
def safe_get(element, key, nested_key=None):
    if nested_key:
        nested = element.get(nested_key, {})
        value = nested.get(key, -99.0)
    else:
        value = element.get(key, -99.0 if key != "Weather" else None)
    
    if key == "Weather":
        return value if value else None  # Weather 為字串，允許空值設為 None
    
    # 處理多種無效值
    if value in [-99, -99.0, "-99", None] or value == "":
        return None
    try:
        return float(value)  # 嘗試轉換為浮點數
    except (ValueError, TypeError):
        return None  # 如果轉換失敗，返回 None

# 抓取氣象資料
for dataid in DATA_IDS:
    url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/{dataid}?Authorization={API_KEY}&format={FORMAT_TYPE}&elementName={ELEMENTS}"
    response = requests.get(url, headers={"accept": "application/json"})
    print(f"正在處理 {dataid}...")

    if response.status_code == 200:
        data = response.json()
        if "records" in data and "Station" in data["records"]:
            for station in data["records"]["Station"]:
                county_name = station["GeoInfo"]["CountyName"]
                if county_name in ["基隆市", "新北市"]:
                    weather_elements = station["WeatherElement"]
                    obs_time = station["ObsTime"]["DateTime"]
                    entry_time = datetime.strptime(obs_time, "%Y-%m-%dT%H:%M:%S%z")

                    if entry_time >= cutoff_time:
                        new_entry = {
                            "station_name": station["StationName"],
                            "station_id": station["StationId"],
                            "county": county_name,
                            "time": obs_time,
                            "weather_elements": {
                                "AirTemperature": safe_get(weather_elements, "AirTemperature"),
                                "RelativeHumidity": safe_get(weather_elements, "RelativeHumidity"),
                                "WindSpeed": safe_get(weather_elements, "WindSpeed"),
                                "WindDirection": safe_get(weather_elements, "WindDirection"),
                                "Precipitation": safe_get(weather_elements, "Precipitation", "Now"),
                                "AirPressure": safe_get(weather_elements, "AirPressure"),
                                "Weather": safe_get(weather_elements, "Weather")
                            },
                            "source": dataid
                        }
                        # 檢查新資料中的無效值
                        for key, value in weather_elements.items():
                            if key != "Weather" and value in [-99, -99.0, "-99"]:
                                print(f"⚠️ 新資料: 站點 {station['StationName']}, 欄位 {key}, 值 {value} 轉為 null")
                        # 避免重複數據
                        if not any(d["station_id"] == new_entry["station_id"] and d["time"] == new_entry["time"] for d in all_data):
                            all_data.append(new_entry)
            print(f"{dataid} 已抓取 {len(all_data)} 筆資料")
        else:
            print(f"⚠️ {dataid} API 回應格式錯誤")
    else:
        print(f"❌ {dataid} API 請求失敗，狀態碼: {response.status_code}")

# 儲存前最終檢查
for entry in all_data:
    for key, value in entry["weather_elements"].items():
        if key != "Weather" and value in [-99, -99.0, "-99"]:
            print(f"❌ 最終資料中仍包含無效值: 站點 {entry['station_name']}, 欄位 {key}, 值 {value}")

# 儲存 JSON 檔案
with open(JSON_OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)

print(f"✅ 氣象資料已更新：{JSON_OUTPUT_FILE}")
