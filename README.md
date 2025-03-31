### README（中文版）

#### 基隆氣象站 山海好厝邊 🌧️🏞️

##### 概述
「基隆氣象站 山海好厝邊」是一個專注於基隆北海岸海氣象資訊的網站，旨在提供簡易清晰、便民實用的氣象與海洋資訊，供機關與民眾參考。本站整合中央氣象署及其他單位的氣象產品，設計簡潔直觀，確保在手機與電腦等不同載具上均能順暢閱覽，目標成為基隆北海岸最值得信賴的氣象資訊平台。

##### 功能
- **氣象圖表**：展示雷達回波、累積雨量、衛星雲圖等 8 項氣象資訊（2*4 佈局）。
- **海象圖表**：提供潮浪柱狀圖、潮高預報、浪高預報等海洋相關數據。
- **天氣預報**：嵌入中央氣象署基隆地區天氣預報。
- **鄉鎮沿海預報**：顯示基隆沿海鄉鎮的詳細預報。
- **雲寶問天氣**：整合中央氣象署的雲寶問天氣服務。
- **觀測時序圖**：提供溫度、濕度、風速及雨量分布的動態圖表，含互動地圖。
- **關於本站**：介紹網站目標與作者資訊。
- **Google Analytics**：追蹤訪客統計數據。

##### 使用說明
1. 開啟網站後，點擊頂部分頁切換不同資訊頁面。
2. 在「觀測時序圖」頁面，點擊地圖上的站點可切換顯示的測站數據。
3. 網站支援響應式設計，可在手機與電腦上正常瀏覽。

##### 安裝與運行
1. **下載檔案**：
   - 從 GitHub 倉庫下載所有檔案（`keelungcwa.html` 及 `data/keelung_data.json`）。
2. **本地運行**：
   - 將檔案放在同一目錄下（例如 `keelungcwa` 文件夾）。
   - 安裝 Node.js，並使用以下命令啟動本地伺服器：
     ```
     npm install -g http-server
     cd keelungcwa
     http-server
     ```
   - 在瀏覽器中訪問 `http://127.0.0.1:8080/keelungcwa.html`。
3. **數據來源**：
   - 需自行更新 `data/keelung_data.json`，格式參考中央氣象署開放數據。

##### 注意事項
- 部分圖表（如浪高預報）依賴外部連結，可能因來源更新而變動。
- 使用非中央氣象署產品時，請以官方預報為準。

##### 聯絡資訊
- 作者：基隆氣象站 鄧乃誠
- 電子郵件：keelung@cwa.gov.tw
- 電話：(02)2422-4240
- 地址：200基隆市仁愛區港西街6號6樓

---

### README（English Version）

#### Keelung Weather Station: Mountain and Sea Companion 🌧️🏞️

##### Overview
"Keelung Weather Station: Mountain and Sea Companion" is a website dedicated to providing meteorological and marine information for the Keelung North Coast. It aims to deliver simple, clear, and practical content for both government agencies and the public. The site integrates key weather products from the Central Weather Administration (CWA) and other sources, featuring an intuitive design optimized for seamless viewing on mobile devices and computers. Our goal is to become the most trusted weather resource for the Keelung North Coast community.

##### Features
- **Weather Charts**: Displays 8 weather-related visuals (2*4 layout), including radar echoes, rainfall accumulation, satellite imagery, and more.
- **Marine Charts**: Offers tide and wave bar charts, tide height forecasts, wave height forecasts, and other ocean data.
- **Weather Forecast**: Embeds the CWA's weather forecast for the Keelung area.
- **Coastal Town Forecast**: Provides detailed forecasts for Keelung's coastal towns.
- **Yunbao Weather Chatbot**: Integrates the CWA's Yunbao weather service.
- **Observation Time Series**: Features dynamic charts for temperature, humidity, wind speed, and rainfall distribution, with an interactive map.
- **About This Site**: Introduces the website's purpose and author information.
- **Google Analytics**: Tracks visitor statistics.

##### Usage Instructions
1. Open the website and click the tabs at the top to switch between information pages.
2. On the "Observation Time Series" page, click stations on the map to toggle displayed data.
3. The site supports responsive design, ensuring compatibility with both mobile and desktop devices.

##### Installation and Running
1. **Download Files**:
   - Download all files from the GitHub repository (`keelungcwa.html` and `data/keelung_data.json`).
2. **Run Locally**:
   - Place the files in the same directory (e.g., `keelungcwa` folder).
   - Install Node.js and start a local server with the following commands:
     ```
     npm install -g http-server
     cd keelungcwa
     http-server
     ```
   - Open a browser and visit `http://127.0.0.1:8080/keelungcwa.html`.
3. **Data Source**:
   - Update `data/keelung_data.json` manually, following the format of CWA's open data.

##### Notes
- Some charts (e.g., wave height forecasts) rely on external links and may change based on source updates.
- When using non-CWA products, please refer to official forecasts for accuracy.

##### Contact Information
- Author: Nai-Cheng Teng, Keelung Weather Station
- Email: keelung@cwa.gov.tw
- Phone: (02)2422-4240
- Address: 6F, No. 6, Gangxi St., Ren’ai District, Keelung City, 200, Taiwan
