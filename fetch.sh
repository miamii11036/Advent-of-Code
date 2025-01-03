#fetch.sh
#會自動在當前目錄中建立名為 某年/某題 的資料夾樹狀結構
#目標：用來儲存Advent of Code中指定年份的所有題目，每個題目都有自己的資料夾，用來儲存題目與自己的答案
#(不包含網頁提供的個人參數)


YEAR=2024
mkdir -p "$YEAR"
cd "$YEAR"


for day in $(seq 1 25); do #題目每年只有25題
    mkdir "Day$day"

    # 確保目錄存在後再切換
    if [ -d "Day$day" ]; then
        cd "Day$day" && touch "solution.py" && touch "puzzle.md"
        cd ..
    else
        echo "目錄 $YEAR/Day$day 不存在，無法切換。"
        exit 1
    fi

    sleep 1 #等待1秒，避免過多請求
done
