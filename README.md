基隆氣象站 山海好厝邊 🌧️🏞️

基隆氣象站 山海好厝邊 是一個專注於基隆北海岸氣象資訊的網站，旨在提供簡單清晰、便民實用的天氣與海象數據，服務機關與民眾。本網站整合中央氣象署及其他單位的氣象產品，透過直觀的圖表、地圖與圖資呈現，支援手機與電腦瀏覽，成為基隆北海岸最值得信賴的氣象好厝邊！
功能特色

即時天氣資訊：展示基隆最新天氣（氣溫、濕度、雨量、風速），支援動態日期顯示與天氣表情符號（☀️ 晴、🌙 晚晴、🌧️ 雨等）。
多樣化圖資：
天氣圖資：雷達回波、累積雨量、真實色衛星雲圖、風速流場等（2x4 佈局）。
海象圖資：潮浪柱狀圖、浪高預報、海溫與海流等（2x3 佈局）。


基隆北海岸專區：
互動式測站地圖，點擊切換站點數據。
溫度、濕度、風速時序圖，支援過去 24 小時數據。
雨量分布圖，視覺化最新降雨量。
觀測排行榜（6 列 x 8 欄），比較「今日」與「現在」最高溫、最低溫、風速、雨量前 5 名，今日與現在欄以排序 1~5 顯示，第 4 欄與第 5 欄間以雙直線分隔。


天氣預報：整合中央氣象署基隆地區與鄉鎮沿海預報。
雲寶問天氣：嵌入中央氣象署雲寶聊天機器人。
氣象站圖卡：展示基隆氣象站特色圖片。
社群分享優化：支援 Open Graph 和 Twitter Card，分享至社群媒體時顯示精美預覽圖（1200x630 像素）。

技術棧

前端：HTML5、CSS3、JavaScript
圖表庫：Chart.js（繪製時序圖與雨量分布圖）
地圖：Leaflet.js（互動式測站地圖）
外部資源：
中央氣象署圖資（雷達、衛星、預報等）
Windy.com（風速流場、海溫預報）
國家災害防救科技中心（浪高動態圖）


部署：GitHub Pages（https://keelungcwa.github.io/）
分析：Google Analytics（追蹤網站使用情況）

安裝與部署
前置條件

瀏覽器：支援現代瀏覽器（Chrome、Firefox、Safari、Edge）
資料檔案：data/keelung_data.json（包含測站天氣數據）
圖片資源：確保 /assets/ 目錄包含 keelung_weather_preview.jpg（社群分享預覽圖）

本地運行

克隆專案：git clone https://github.com/keelungcwa/keelungcwa.git
cd keelungcwa


安裝簡單 HTTP 伺服器（例如 Python 的 http.server）：python3 -m http.server 8000


打開瀏覽器，訪問 http://localhost:8000。
確保 data/keelung_data.json 放置於 data/ 目錄，格式如下：[
    {
        "station_name": "基隆",
        "time": "2025-04-16T12:00:00",
        "weather_elements": {
            "AirTemperature": 25.5,
            "RelativeHumidity": 80,
            "WindSpeed": 5.2,
            "Precipitation": 0,
            "Weather": "晴"
        }
    },
    ...
]



部署到 GitHub Pages

確保專案根目錄包含 index.html 和必要的資料、圖片檔案。
在 GitHub 專案設置中啟用 GitHub Pages，選擇 main 分支的 / (root) 目錄。
部署後，訪問 https://keelungcwa.github.io/。
確認圖片 URL（如 https://keelungcwa.github.io/assets/keelung_weather_preview.jpg）可公開訪問。

使用說明

瀏覽網站：訪問 https://keelungcwa.github.io/，首頁顯示基隆最新天氣資訊。
切換分頁：
天氣圖資 ☁️：查看雷達、雨量、衛星等圖資。
海象圖資 🌊：瀏覽潮浪、浪高、海溫等數據。
基隆北海岸 ❤️：檢視測站地圖、時序圖及排行榜。
天氣預報 ⛅：查詢基隆地區預報。
鄉鎮沿海預報 🛳️：查看沿海鄉鎮天氣。
雲寶問天氣 🤖：與雲寶聊天機器人互動。
氣象站圖卡 🎏：瀏覽特色圖片。


互動功能：
點擊地圖標記切換測站，更新時序圖數據。
在排行榜切換「最高溫」「最低溫」「風速」「雨量」，查看前 5 名。


社群分享：
複製網站 URL，分享至 Facebook、Twitter、LINE 等平台。
預覽圖（keelung_weather_preview.jpg）將自動顯示，包含標題與描述。



測試與驗證

資料載入：確認 keelung_data.json 格式正確，時間可解析，數據完整。
排行榜：檢查「今日」與「現在」欄顯示排序 1~5，雙直線分隔清晰。
天氣表情符號：測試「晴」在 06:0018:00 顯示 ☀️，18:0006:00 顯示 🌙。
手機適配：在手機上測試表格、圖表、地圖的顯示效果。
社群預覽：
使用 Facebook Sharing Debugger 測試 Open Graph。
使用 Twitter Card Validator 驗證 Twitter Card。
確認預覽圖尺寸（1200x630）與內容正確。



注意事項

資料來源：部分圖資來自中央氣象署以外的單位，請以官方預報為準。
圖片資源：確保 /assets/ 目錄的圖片（特別是 keelung_weather_preview.jpg）可公開訪問。
快取問題：社群平台可能快取舊預覽圖，使用 Debugger 工具清除快取。
版權：網站圖片與資料需遵守中央氣象署及其他單位的版權規定，轉載請註明出處。

貢獻指南
歡迎對本專案提出建議或貢獻程式碼！請遵循以下步驟：

Fork 本專案。
創建新分支：git checkout -b feature/你的功能


提交更改：git commit -m "新增/修復：描述你的更改"


推送到遠端：git push origin feature/你的功能


提交 Pull Request，詳細描述你的變更。

聯繫方式

作者：基隆氣象站 鄧乃誠
地址：200 基隆市仁愛區港西街 6 號 6 樓（海港大樓）
電話：(02) 2422-4240
電子郵件：keelung@cwa.gov.tw
服務時間：09:00 至 17:00

版權
中央氣象署基隆氣象站 版權所有，轉載請註明出處。

讓我們一起打造基隆北海岸最實用的氣象資訊平台！ 🌊☁️
