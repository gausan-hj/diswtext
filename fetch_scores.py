import pandas as pd
from datetime import datetime

# ===== 你要修改的地方 =====
SHEET_ID = "1YVa3nLUBW80j2nA4mudEqLH91RJ0FSRytmoDqmbyUJk"
SHEET_NAME = "Sheet3"
# ========================

# 生成Google Sheets的CSV导出链接
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# 读取数据
print("正在从 Google Sheets 读取数据...")
try:
    df = pd.read_csv(url, header=None, encoding='utf-8-sig')
except:
    try:
        df = pd.read_csv(url, header=None, encoding='latin1')
    except:
        df = pd.read_csv(url, header=None, encoding='cp1252')

print(f"读取到 {len(df)} 行数据")

# 获取日期（第一行）
dates = []
date_objects = []
if len(df) > 0:
    first_row = df.iloc[0].tolist()
    for j in range(7, len(first_row)):
        if pd.notna(first_row[j]):
            date_str = str(first_row[j])
            try:
                if "00:00" in date_str:
                    date_str = date_str[5:10]
                dates.append(date_str)
                try:
                    date_objects.append(datetime.strptime(first_row[j][:10], '%Y-%m-%d'))
                except:
                    date_objects.append(None)
            except:
                dates.append("")
                date_objects.append(None)
        else:
            dates.append("")
            date_objects.append(None)

print(f"找到 {len(dates)} 个日期")

# ===== 成员名单 =====
members_list = [
    # 星穹组 (10人)
    {"group": "星穹组", "name_cn": "陈展艺", "name_en": "IVAN TAN ZHAN YI", "class": "S2FA", "student_id": "22038", "order": 1},
    {"group": "星穹组", "name_cn": "侯展扬", "name_en": "HOW ZHAN YANG", "class": "S2Y", "student_id": "22100", "order": 2},
    {"group": "星穹组", "name_cn": "邱嘉瑞", "name_en": "KATHERINE KHOO JAI RUI", "class": "J3T", "student_id": "24076", "order": 3},
    {"group": "星穹组", "name_cn": "莎哈娜", "name_en": "SADHANA A/P SASU BAKIAN", "class": "J3T", "student_id": "24078", "order": 4},
    {"group": "星穹组", "name_cn": "李韡翰", "name_en": "LEE WEI HANN", "class": "J3K", "student_id": "24068", "order": 5},
    {"group": "星穹组", "name_cn": "彭绍洋", "name_en": "PEH SHAO YANG", "class": "J3T", "student_id": "24088", "order": 6},
    {"group": "星穹组", "name_cn": "梁纹璇", "name_en": "LEONG WEN XUAN", "class": "J2Y", "student_id": "25035", "order": 7},
    {"group": "星穹组", "name_cn": "尤嘉乐", "name_en": "JUSTIN YEW JIA LE", "class": "J2Y", "student_id": "25046", "order": 8},
    {"group": "星穹组", "name_cn": "许艳棋", "name_en": "KHOR YAN QI", "class": "J1Y", "student_id": "26018", "order": 9},
    {"group": "星穹组", "name_cn": "林隽毓", "name_en": "LIM JOON YI", "class": "J1Y", "student_id": "26032", "order": 10},
    
    # 夜曜组 (11人)
    {"group": "夜曜组", "name_cn": "李竑证", "name_en": "LEE HOONG ZHENG", "class": "S2FA", "student_id": "22040", "order": 1},
    {"group": "夜曜组", "name_cn": "廖若含", "name_en": "LIEW XIN YU", "class": "S2Y", "student_id": "22029", "order": 2},
    {"group": "夜曜组", "name_cn": "林芷嫣", "name_en": "LIM ZHI YAN", "class": "S2Y", "student_id": "22083", "order": 3},
    {"group": "夜曜组", "name_cn": "周柔慈", "name_en": "CHEO ROU ZHI", "class": "S2K", "student_id": "22051", "order": 4},
    {"group": "夜曜组", "name_cn": "林骏喨", "name_en": "LIM TEIK LIANG", "class": "J3T", "student_id": "24083", "order": 5},
    {"group": "夜曜组", "name_cn": "林宜彤", "name_en": "LIM YEE TONG", "class": "J2Y", "student_id": "25036", "order": 6},
    {"group": "夜曜组", "name_cn": "潘宛瑜", "name_en": "TRACY PHUAH WANYU", "class": "J2Y", "student_id": "25071", "order": 7},
    {"group": "夜曜组", "name_cn": "符传吉", "name_en": "FOO CHUAN JI", "class": "J2Y", "student_id": "25044", "order": 8},
    {"group": "夜曜组", "name_cn": "陈欣怡", "name_en": "CINDY TAN XIN YI", "class": "J2F", "student_id": "25058", "order": 9},
    {"group": "夜曜组", "name_cn": "丽亚", "name_en": "DHIYA ZULAIKHA DARWISYAH BINTI YUSNIZAN", "class": "J2F", "student_id": "25059", "order": 10},
    {"group": "夜曜组", "name_cn": "郑宜桐", "name_en": "TEH YEE THONG", "class": "J1Y", "student_id": "26024", "order": 11},
    
    # 沧澜组 (10人)
    {"group": "沧澜组", "name_cn": "浦源政", "name_en": "POH YUAN ZHENG", "class": "S2Y", "student_id": "22044", "order": 1},
    {"group": "沧澜组", "name_cn": "吴贝优", "name_en": "GOH BEI YO", "class": "S2Y", "student_id": "22021", "order": 2},
    {"group": "沧澜组", "name_cn": "林沛筠", "name_en": "LIM PEI JUN", "class": "S2Y", "student_id": "22030", "order": 3},
    {"group": "沧澜组", "name_cn": "陈诗惠", "name_en": "CHAN SHI HUI", "class": "S2FA", "student_id": "22017", "order": 4},
    {"group": "沧澜组", "name_cn": "郑憶欣", "name_en": "TEE YEE XIN", "class": "S1Y", "student_id": "23065", "order": 5},
    {"group": "沧澜组", "name_cn": "谢楷棋", "name_en": "CHEAH KHAI QI", "class": "S1T", "student_id": "23013", "order": 6},
    {"group": "沧澜组", "name_cn": "蔡善恩", "name_en": "CHUAH SHAN EN", "class": "J3F", "student_id": "24039", "order": 7},
    {"group": "沧澜组", "name_cn": "许家绮", "name_en": "KOO JIA QI", "class": "J2Y", "student_id": "25031", "order": 8},
    {"group": "沧澜组", "name_cn": "张子欣", "name_en": "TEON ZI XIN", "class": "J2F", "student_id": "25070", "order": 9},
    {"group": "沧澜组", "name_cn": "施锦轩", "name_en": "SEE JIN XUAN", "class": "J1T", "student_id": "26092", "order": 10}
]

# 自动匹配每一行
people = []
group_totals = {g: 0 for g in ["星穹组", "夜曜组", "沧澜组"]}
group_yesterday_totals = {g: 0 for g in ["星穹组", "夜曜组", "沧澜组"]}
group_today_totals = {g: 0 for g in ["星穹组", "夜曜组", "沧澜组"]}
previous_rank = {g: 0 for g in ["星穹组", "夜曜组", "沧澜组"]}

print("\n开始匹配成员...")

today_idx = len(dates) - 1
yesterday_idx = max(0, len(dates) - 2)

for member in members_list:
    found = False
    
    for i in range(len(df)):
        row = df.iloc[i].tolist()
        
        if len(row) > 4:
            row_name_cn = str(row[3]) if len(row) > 3 and pd.notna(row[3]) else ""
            row_name_en = str(row[4]) if len(row) > 4 and pd.notna(row[4]) else ""
            
            if (member["name_cn"] in row_name_cn or 
                member["name_en"][:20] in row_name_en[:20]):
                
                total = 0
                score_dict = {}
                today_score = 0
                yesterday_score = 0
                
                for j in range(7, len(row)):
                    if j-7 < len(dates):
                        date = dates[j-7]
                        val = row[j]
                        if pd.notna(val):
                            try:
                                num = float(val)
                                total += num
                                if num > 0:
                                    score_dict[date] = num
                                if j-7 == today_idx:
                                    today_score = num
                                elif j-7 == yesterday_idx:
                                    yesterday_score = num
                            except (ValueError, TypeError):
                                pass
                
                people.append({
                    "group": member["group"],
                    "order": member["order"],
                    "name_cn": member["name_cn"],
                    "name_en": member["name_en"],
                    "class": member["class"],
                    "student_id": member["student_id"],
                    "score_dict": score_dict,
                    "total": total,
                    "today": today_score,
                    "yesterday": yesterday_score
                })
                print(f"✓ 找到 {member['name_cn']} (总分: {total})")
                found = True
                break
    
    if not found:
        print(f"✗ 找不到 {member['name_cn']}")

print(f"\n总共找到 {len(people)} 人")

if len(people) == 0:
    print("❌ 没有找到任何人！请检查：")
    print("1. Google Sheets 权限是否设置为 '任何知道链接的人可查看'")
    print("2. Sheet 名字是否正确（当前是 Sheet3）")
    print("3. 数据格式是否和 Excel 一致")
    exit(1)

# 按组别整理
group_data = {g: [] for g in ["星穹组", "夜曜组", "沧澜组"]}
for p in people:
    group_data[p["group"]].append(p)
    group_totals[p["group"]] += p["total"]
    group_today_totals[p["group"]] += p["today"]
    group_yesterday_totals[p["group"]] += p["yesterday"]

# 计算变化
group_changes = {}
for g in ["星穹组", "夜曜组", "沧澜组"]:
    change = group_today_totals[g] - group_yesterday_totals[g]
    group_changes[g] = change

# 每个组内按order排序
for g in group_data:
    group_data[g].sort(key=lambda x: x["order"])

# 计算当前排名
sorted_groups = sorted(group_totals.items(), key=lambda x: x[1], reverse=True)
group_rank = {}
for i, (g, _) in enumerate(sorted_groups, 1):
    group_rank[g] = i

# 模拟上次排名
previous_rank["星穹组"] = max(1, group_rank["星穹组"] - 1) if group_rank["星穹组"] > 1 else 2
previous_rank["夜曜组"] = max(1, group_rank["夜曜组"] - 1) if group_rank["夜曜组"] > 1 else 2
previous_rank["沧澜组"] = max(1, group_rank["沧澜组"] - 1) if group_rank["沧澜组"] > 1 else 2

# 计算每组平均分
group_averages = {}
for g in ["星穹组", "夜曜组", "沧澜组"]:
    if group_data[g]:
        group_averages[g] = group_totals[g] / len(group_data[g])
    else:
        group_averages[g] = 0

# 计算每个人的达标状态
for g in group_data:
    for p in group_data[g]:
        rank = group_rank[g]
        avg = group_averages[g]
        
        if rank == 1:  # 第一名组别
            p["reward_status"] = "✅" if p["total"] >= avg / 2 else "❌"
            p["reward_class"] = "reward-pass" if p["total"] >= avg / 2 else "reward-fail"
        elif rank == 2:  # 第二名组别
            p["reward_status"] = "✅" if p["total"] >= avg else "❌"
            p["reward_class"] = "reward-pass" if p["total"] >= avg else "reward-fail"
        else:  # 第三名组别
            # 找出组内前三名
            top3 = sorted(group_data[g], key=lambda x: x["total"], reverse=True)[:3]
            top3_names = [t["name_cn"] for t in top3]
            if p["name_cn"] in top3_names:
                p["reward_status"] = "✅"
                p["reward_class"] = "reward-pass"
            else:
                p["reward_status"] = "❌"
                p["reward_class"] = "reward-fail"

# 生成HTML - 华为传输动画版
html = '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>训育处 · 学长团荣耀榜</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }

        :root {
            --bg-primary: #f5f7fc;
            --bg-secondary: #ffffff;
            --card-bg: #ffffff;
            --text-primary: #1a2b3c;
            --text-secondary: #2c3e50;
            --text-tertiary: #5a6b7a;
            --border-light: #e1e8f0;
            --border-subtle: #eef2f6;
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.02);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.04);
            --shadow-lg: 0 8px 24px rgba(0,0,0,0.06);
            
            --star-primary: #eab308;
            --star-light: #fef9c3;
            --star-bg: #fefae8;
            --night-primary: #a855f7;
            --night-light: #f3e8ff;
            --night-bg: #faf5ff;
            --ocean-primary: #3b82f6;
            --ocean-light: #dbeafe;
            --ocean-bg: #f0f7ff;
            
            --score-bg: #f1f5f9;
            --score-text: #475569;
            --score-highlight: #e6f0ff;
            --score-highlight-text: #2563eb;
            --reward-pass: #dcfce7;
            --reward-pass-text: #166534;
            --reward-fail: #fee2e2;
            --reward-fail-text: #991b1b;
            
            --huawei-blue: #0070f0;
            --huawei-light: #e6f0ff;
        }

        body.night-mode {
            --bg-primary: #0f1825;
            --bg-secondary: #1e2a3a;
            --card-bg: #1f2c3d;
            --text-primary: #e6edf5;
            --text-secondary: #cbd5e1;
            --text-tertiary: #94a3b8;
            --border-light: #2d3a4d;
            --border-subtle: #253141;
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.4);
            --shadow-lg: 0 8px 24px rgba(0,0,0,0.5);
            
            --star-light: #423d2a;
            --star-bg: #2f2a1f;
            --night-light: #2f2740;
            --night-bg: #252033;
            --ocean-light: #1f3045;
            --ocean-bg: #1c2638;
            
            --score-bg: #2d3a4f;
            --score-text: #cbd5e1;
            --score-highlight: #1e3a6f;
            --score-highlight-text: #9ac7ff;
            --reward-pass: #1f4a3a;
            --reward-pass-text: #bbf7d0;
            --reward-fail: #562b2b;
            --reward-fail-text: #fecaca;
            
            --huawei-blue: #4098ff;
            --huawei-light: #1e3a6f;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft YaHei', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            padding: 20px;
            min-height: 100vh;
            transition: background 0.3s, color 0.3s;
            line-height: 1.5;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        /* 华为传输按钮 */
        .huawei-transfer-btn {
            position: relative;
            width: 60px;
            height: 60px;
            border-radius: 30px;
            background: var(--huawei-blue);
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(0, 112, 240, 0.3);
            transition: transform 0.2s;
            overflow: hidden;
        }

        .huawei-transfer-btn:hover {
            transform: scale(1.05);
        }

        .huawei-transfer-btn:active {
            transform: scale(0.95);
        }

        .btn-icon {
            color: white;
            font-size: 24px;
            position: relative;
            z-index: 2;
        }

        /* 华为传输圆圈动画 */
        .transfer-circle {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.5);
            opacity: 0;
            pointer-events: none;
        }

        .transfer-circle.active {
            animation: huaweiWave 1.5s ease-out;
        }

        @keyframes huaweiWave {
            0% {
                width: 0;
                height: 0;
                opacity: 0.8;
            }
            100% {
                width: 200px;
                height: 200px;
                opacity: 0;
            }
        }

        /* 数据传输波纹 */
        .data-ripple {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 0;
            height: 0;
            border-radius: 50%;
            background: radial-gradient(circle, var(--huawei-blue) 0%, transparent 70%);
            opacity: 0;
            pointer-events: none;
            z-index: 9999;
        }

        .data-ripple.active {
            animation: dataWave 1s ease-out;
        }

        @keyframes dataWave {
            0% {
                width: 0;
                height: 0;
                opacity: 0.6;
            }
            100% {
                width: 300px;
                height: 300px;
                opacity: 0;
            }
        }

        /* 数据传输粒子 */
        .data-particle {
            position: fixed;
            width: 4px;
            height: 4px;
            background: var(--huawei-blue);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9998;
            opacity: 0;
        }

        .data-particle.active {
            animation: particleFly 1s ease-out;
        }

        @keyframes particleFly {
            0% {
                transform: translate(0, 0) scale(1);
                opacity: 1;
            }
            100% {
                transform: translate(var(--tx), var(--ty)) scale(0);
                opacity: 0;
            }
        }

        /* 头部 */
        .header {
            background: var(--card-bg);
            border-radius: 32px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-subtle);
            position: relative;
        }

        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            flex-wrap: wrap;
            gap: 16px;
        }

        .title-group {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .school-icon {
            font-size: 2rem;
        }

        h1 {
            font-size: 1.6rem;
            font-weight: 600;
            color: var(--text-primary);
        }

        .action-buttons {
            display: flex;
            gap: 12px;
            align-items: center;
        }

        /* 深色模式按钮 */
        .theme-toggle {
            background: var(--bg-primary);
            border: 1px solid var(--border-light);
            border-radius: 40px;
            padding: 8px 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.9rem;
            color: var(--text-primary);
            transition: all 0.2s ease;
        }

        .theme-toggle:hover {
            background: var(--border-light);
            transform: scale(1.02);
        }

        .theme-toggle:active {
            transform: scale(0.98);
        }

        .theme-toggle .toggle-icon {
            display: inline-block;
            transition: transform 0.3s;
        }

        body.night-mode .theme-toggle .toggle-icon {
            transform: rotate(360deg);
        }

        .meta-info {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 2px dashed var(--border-subtle);
            color: var(--text-tertiary);
            font-size: 0.85rem;
        }

        .date-badge {
            background: var(--bg-primary);
            padding: 4px 14px;
            border-radius: 30px;
            font-size: 0.8rem;
            border: 1px solid var(--border-subtle);
        }

        .search-wrapper {
            position: relative;
        }

        .search-icon {
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-tertiary);
            font-size: 1rem;
        }

        #search {
            width: 100%;
            padding: 12px 16px 12px 44px;
            border: 1px solid var(--border-subtle);
            border-radius: 40px;
            font-size: 0.95rem;
            background: var(--bg-primary);
            color: var(--text-primary);
            transition: all 0.2s;
        }

        #search:focus {
            outline: none;
            border-color: var(--text-tertiary);
            box-shadow: 0 0 0 3px rgba(100, 116, 139, 0.1);
        }

        /* 组排名卡片 */
        .rank-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 24px;
        }

        .rank-card {
            background: var(--card-bg);
            border-radius: 24px;
            padding: 18px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-subtle);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 12px;
            border-left: 4px solid;
            transition: transform 0.2s, box-shadow 0.2s;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 0.5s forwards;
        }

        .rank-card:nth-child(1) { animation-delay: 0.1s; }
        .rank-card:nth-child(2) { animation-delay: 0.2s; }
        .rank-card:nth-child(3) { animation-delay: 0.3s; }

        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .rank-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .rank-card:active {
            transform: scale(0.98);
        }

        .rank-card[data-group="星穹组"] {
            border-left-color: var(--star-primary);
            background: linear-gradient(to right, var(--star-bg), var(--card-bg));
        }
        .rank-card[data-group="夜曜组"] {
            border-left-color: var(--night-primary);
            background: linear-gradient(to right, var(--night-bg), var(--card-bg));
        }
        .rank-card[data-group="沧澜组"] {
            border-left-color: var(--ocean-primary);
            background: linear-gradient(to right, var(--ocean-bg), var(--card-bg));
        }

        .rank-card.rank-up {
            animation: rankUp 0.4s ease;
        }

        .rank-card.rank-down {
            animation: rankDown 0.4s ease;
        }

        @keyframes rankUp {
            0% { transform: translateY(0); }
            30% { transform: translateY(-4px); }
            60% { transform: translateY(2px); }
            100% { transform: translateY(0); }
        }

        @keyframes rankDown {
            0% { transform: translateY(0); }
            30% { transform: translateY(4px); }
            60% { transform: translateY(-2px); }
            100% { transform: translateY(0); }
        }

        .rank-icon {
            font-size: 1.8rem;
        }

        .rank-info {
            flex: 1;
        }

        .rank-name {
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 4px;
        }

        .rank-score {
            font-weight: 700;
            font-size: 1.3rem;
            display: flex;
            align-items: baseline;
            gap: 4px;
        }

        .rank-score small {
            font-size: 0.7rem;
            font-weight: 400;
            color: var(--text-tertiary);
        }

        .rank-change {
            font-size: 0.7rem;
            margin-top: 2px;
        }

        /* 组卡片 */
        .groups {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .group-card {
            background: var(--card-bg);
            border-radius: 28px;
            padding: 20px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-subtle);
            scroll-margin-top: 16px;
            border-top: 4px solid;
            opacity: 0;
            transform: translateX(-20px);
            animation: slideIn 0.5s forwards;
        }

        .group-card:nth-child(1) { animation-delay: 0.2s; }
        .group-card:nth-child(2) { animation-delay: 0.3s; }
        .group-card:nth-child(3) { animation-delay: 0.4s; }

        @keyframes slideIn {
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .group-card[data-group="星穹组"] { border-top-color: var(--star-primary); }
        .group-card[data-group="夜曜组"] { border-top-color: var(--night-primary); }
        .group-card[data-group="沧澜组"] { border-top-color: var(--ocean-primary); }

        .group-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--border-subtle);
        }

        .group-title-wrapper {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .group-emoji {
            font-size: 1.4rem;
        }

        .group-title {
            font-size: 1.3rem;
            font-weight: 600;
        }

        .group-stats {
            display: flex;
            gap: 10px;
            align-items: center;
        }

        .group-avg {
            font-size: 0.8rem;
            padding: 4px 12px;
            background: var(--bg-primary);
            border-radius: 30px;
            color: var(--text-secondary);
            border: 1px solid var(--border-subtle);
        }

        .group-badge {
            font-size: 0.8rem;
            padding: 4px 12px;
            border-radius: 30px;
            color: white;
        }

        .group-card[data-group="星穹组"] .group-badge { background: var(--star-primary); }
        .group-card[data-group="夜曜组"] .group-badge { background: var(--night-primary); }
        .group-card[data-group="沧澜组"] .group-badge { background: var(--ocean-primary); }

        /* 表格 */
        .table-container {
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }

        .member-table {
            width: 100%;
            border-collapse: collapse;
            min-width: 700px;
            font-size: 0.9rem;
        }

        .member-table th {
            text-align: left;
            padding: 12px 8px;
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--text-tertiary);
            text-transform: uppercase;
            border-bottom: 1px solid var(--border-subtle);
        }

        .member-table td {
            padding: 12px 8px;
            border-bottom: 1px solid var(--border-subtle);
            transition: background 0.2s;
        }

        .member-table tr:hover td {
            background: var(--bg-primary);
        }

        .member-table tr:last-child td {
            border-bottom: none;
        }

        .member-table th:nth-child(6) { text-align: right; padding-right: 16px; }
        .member-table td:nth-child(6) { text-align: right; padding-right: 16px; font-weight: 600; }
        .member-table td:nth-child(7) { text-align: center; }

        .name-cn {
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 2px;
        }

        .name-en {
            font-size: 0.65rem;
            color: var(--text-tertiary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 130px;
        }

        .info-cell {
            font-size: 0.85rem;
            color: var(--text-secondary);
        }

        /* 分数标签 */
        .score-tags {
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
        }

        .score-item {
            padding: 3px 8px;
            border-radius: 16px;
            font-size: 0.65rem;
            font-weight: 500;
            background: var(--score-bg);
            color: var(--score-text);
            border: 1px solid var(--border-subtle);
        }

        .score-item.has-score {
            background: var(--score-highlight);
            color: var(--score-highlight-text);
        }

        .score-date { opacity: 0.7; margin-right: 2px; }
        .score-value { font-weight: 600; }

        .reward-pass, .reward-fail {
            padding: 3px 8px;
            border-radius: 16px;
            font-size: 0.65rem;
            font-weight: 600;
            display: inline-block;
            min-width: 40px;
            text-align: center;
        }

        .reward-pass {
            background: var(--reward-pass);
            color: var(--reward-pass-text);
        }

        .reward-fail {
            background: var(--reward-fail);
            color: var(--reward-fail-text);
        }

        /* 奖励机制卡片 */
        .reward-section {
            background: linear-gradient(135deg, var(--card-bg) 0%, var(--bg-primary) 100%);
            border-radius: 32px;
            padding: 28px;
            margin-top: 28px;
            margin-bottom: 20px;
            box-shadow: var(--shadow-lg);
            border: 1px solid var(--border-light);
            border-left: 6px solid var(--star-primary);
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 0.6s 0.5s forwards;
        }

        .reward-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }

        .reward-icon {
            font-size: 2.4rem;
        }

        .reward-header h2 {
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .reward-subtitle {
            font-size: 0.95rem;
            color: var(--text-tertiary);
            margin-bottom: 20px;
            padding-left: 12px;
            border-left: 3px solid var(--star-primary);
        }

        .reward-content {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 20px;
        }

        .reward-item {
            background: var(--bg-primary);
            border-radius: 24px;
            padding: 20px;
            border: 1px solid var(--border-subtle);
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .reward-item:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .reward-rank {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 15px;
        }

        .rank-medal {
            font-size: 2rem;
        }

        .rank-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .reward-desc {
            font-size: 0.9rem;
            color: var(--text-tertiary);
            margin-bottom: 12px;
            line-height: 1.5;
        }

        .reward-condition {
            background: var(--card-bg);
            border-radius: 30px;
            padding: 8px 16px;
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--text-primary);
            border: 1px solid var(--border-light);
            margin-bottom: 10px;
        }

        .reward-benefit {
            color: var(--star-primary);
            font-weight: 600;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .reward-note {
            background: var(--bg-primary);
            border-radius: 20px;
            padding: 16px;
            margin-top: 16px;
            border: 2px dashed var(--border-light);
            font-size: 0.9rem;
            color: var(--text-secondary);
            text-align: center;
        }

        .reward-extra {
            color: var(--night-primary);
            font-weight: 600;
        }

        .reward-footer {
            margin-top: 20px;
            text-align: center;
            font-size: 0.9rem;
            color: var(--text-tertiary);
            font-style: italic;
        }

        .footer {
            margin-top: 20px;
            text-align: center;
            color: var(--text-tertiary);
            font-size: 0.75rem;
            padding: 16px;
            border-top: 1px solid var(--border-subtle);
            opacity: 0;
            animation: fadeIn 0.5s 0.9s forwards;
        }

        @keyframes fadeIn {
            to { opacity: 1; }
        }

        /* 数据传输状态提示 */
        .transfer-status {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: var(--card-bg);
            color: var(--text-primary);
            padding: 12px 24px;
            border-radius: 40px;
            box-shadow: var(--shadow-lg);
            border: 1px solid var(--border-light);
            display: flex;
            align-items: center;
            gap: 12px;
            transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            z-index: 10000;
        }

        .transfer-status.show {
            transform: translateX(-50%) translateY(0);
        }

        .status-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--huawei-blue);
            animation: statusPulse 1s infinite;
        }

        @keyframes statusPulse {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.2); opacity: 0.7; }
        }

        .status-text {
            font-size: 0.9rem;
            font-weight: 500;
        }

        .status-progress {
            width: 60px;
            height: 4px;
            background: var(--border-light);
            border-radius: 2px;
            overflow: hidden;
        }

        .progress-bar {
            height: 100%;
            width: 0%;
            background: var(--huawei-blue);
            border-radius: 2px;
            transition: width 0.3s;
        }

        @media (max-width: 768px) {
            body { padding: 16px; }
            h1 { font-size: 1.4rem; }
            .reward-content { grid-template-columns: 1fr; }
            .rank-grid { gap: 10px; }
            .transfer-status { bottom: 10px; padding: 10px 20px; }
        }

        @media (max-width: 640px) {
            .header { padding: 18px; }
            .rank-card { padding: 14px; }
            .rank-icon { font-size: 1.5rem; }
            .rank-score { font-size: 1.1rem; }
            .group-card { padding: 16px; }
            .group-title { font-size: 1.1rem; }
            .huawei-transfer-btn { width: 50px; height: 50px; }
            .btn-icon { font-size: 20px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-top">
                <div class="title-group">
                    <span class="school-icon">🏫</span>
                    <h1>学长团 · 荣耀榜</h1>
                </div>
                <div class="action-buttons">
                    <!-- 华为传输按钮 -->
                    <button class="huawei-transfer-btn" id="transferBtn">
                        <div class="transfer-circle" id="transferCircle"></div>
                        <span class="btn-icon">📲</span>
                    </button>
                    <div class="theme-toggle" onclick="document.body.classList.toggle('night-mode')">
                        <span class="toggle-icon">🌓</span>
                        <span>切换深色</span>
                    </div>
                </div>
            </div>
            <div class="meta-info">
                <span>训育处 · 奖励机制 · 公平公正</span>
                <span class="date-badge">''' + datetime.now().strftime('%Y年%m月%d日 %H:%M') + '''</span>
            </div>
            <div class="search-wrapper">
                <span class="search-icon">🔍</span>
                <input type="text" id="search" placeholder="搜索姓名、英文名、班级或学号...">
            </div>
        </div>

        <!-- 组排名卡片 -->
        <div class="rank-grid">
'''

# 添加组排名卡片
rank_icons = {1: "🥇", 2: "🥈", 3: "🥉"}
group_ids = {"星穹组": "group-xingqiong", "夜曜组": "group-yeyao", "沧澜组": "group-canglan"}
for i, (g, total) in enumerate(sorted_groups, 1):
    group_id = group_ids[g]
    change = group_changes[g]
    prev_rank = previous_rank[g]
    current_rank = group_rank[g]
    
    rank_animation = ""
    if current_rank < prev_rank:
        rank_animation = 'rank-up'
    elif current_rank > prev_rank:
        rank_animation = 'rank-down'
    
    if change > 0:
        change_text = f'<span style="color:#10b981">▲ +{int(change)}</span>'
    elif change < 0:
        change_text = f'<span style="color:#ef4444">▼ {int(change)}</span>'
    else:
        change_text = '<span style="color:#f59e0b">◆ 0</span>'
    
    html += '''
            <div class="rank-card ''' + rank_animation + '''" data-group="''' + g + '''" data-rank="''' + str(current_rank) + '''" data-prev-rank="''' + str(prev_rank) + '''" onclick="document.getElementById(\'''' + group_id + '''\').scrollIntoView({behavior: 'smooth'})">
                <span class="rank-icon">''' + rank_icons[i] + '''</span>
                <div class="rank-info">
                    <div class="rank-name">''' + g + '''</div>
                    <div class="rank-score">''' + str(int(total)) + '''<small>分</small></div>
                    <div class="rank-change">''' + change_text + '''</div>
                </div>
            </div>
'''

html += '''
        </div>

        <!-- 组别详情 -->
        <div class="groups">
'''

# 添加三个组
group_emojis = {"星穹组": "✨", "夜曜组": "🌙", "沧澜组": "🌊"}
for group_name in ["星穹组", "夜曜组", "沧澜组"]:
    members = group_data[group_name]
    rank = group_rank[group_name]
    group_id = group_ids[group_name]
    avg_score = group_averages[group_name]
    
    html += '''
            <div class="group-card" data-group="''' + group_name + '''" id="''' + group_id + '''">
                <div class="group-header">
                    <div class="group-title-wrapper">
                        <span class="group-emoji">''' + group_emojis[group_name] + '''</span>
                        <span class="group-title">''' + group_name + '''</span>
                    </div>
                    <div class="group-stats">
                        <span class="group-avg">平均''' + str(int(avg_score)) + '''</span>
                        <span class="group-badge">第''' + str(rank) + '''名</span>
                    </div>
                </div>
                <div class="table-container">
                    <table class="member-table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>姓名</th>
                                <th>班级</th>
                                <th>学号</th>
                                <th>每日得分</th>
                                <th>总分</th>
                                <th>奖</th>
                            </tr>
                        </thead>
                        <tbody>
'''

    for member in members:
        # 生成每日得分标签
        score_tags = ""
        sorted_dates = sorted(member["score_dict"].keys())
        for date in sorted_dates[-5:]:
            if date:
                score = member["score_dict"][date]
                score_tags += f'<span class="score-item has-score"><span class="score-date">{date}</span><span class="score-value">{int(score)}</span></span>'
        
        if not score_tags:
            score_tags = '<span class="score-item">—</span>'
        
        # 截断英文名
        name_en_short = member['name_en'][:15] + "…" if len(member['name_en']) > 15 else member['name_en']
        
        html += '''
                        <tr data-search="''' + member['name_cn'] + ' ' + member['name_en'] + ' ' + member['class'] + ' ' + member['student_id'] + '''">
                            <td>''' + str(member['order']) + '''</td>
                            <td>
                                <div class="name-cn">''' + member['name_cn'] + '''</div>
                                <div class="name-en">''' + name_en_short + '''</div>
                            </td>
                            <td class="info-cell">''' + member['class'] + '''</td>
                            <td class="info-cell">''' + member['student_id'] + '''</td>
                            <td><div class="score-tags">''' + score_tags + '''</div></td>
                            <td>''' + str(int(member['total'])) + '''</td>
                            <td><span class="''' + member['reward_class'] + '''">''' + member['reward_status'] + '''</span></td>
                        </tr>
'''

    html += '''
                        </tbody>
                    </table>
                </div>
            </div>
'''

html += '''
        </div>

        <!-- 奖励机制卡片 - 移到最下面 -->
        <div class="reward-section">
            <div class="reward-header">
                <span class="reward-icon">🎁</span>
                <h2>本轮奖励机制</h2>
            </div>
            <div class="reward-subtitle">
                基于公平原则及不负任何一位有尽力及付出的学长
            </div>
            <div class="reward-content">
                <!-- 第一名组别 -->
                <div class="reward-item">
                    <div class="reward-rank">
                        <span class="rank-medal">🥇</span>
                        <span class="rank-title">第一名组别</span>
                    </div>
                    <div class="reward-desc">
                        凡个人分数达到该组总平均分一半或以上者
                    </div>
                    <div class="reward-condition">
                        ✅ 达标条件：分数 ≥ 平均分 ÷ 2
                    </div>
                    <div class="reward-benefit">
                        ✨ 免搬椅子 + 减免操步
                    </div>
                </div>
                <!-- 第二名组别 -->
                <div class="reward-item">
                    <div class="reward-rank">
                        <span class="rank-medal">🥈</span>
                        <span class="rank-title">第二名组别</span>
                    </div>
                    <div class="reward-desc">
                        凡个人分数达到该组总平均分或以上者
                    </div>
                    <div class="reward-condition">
                        ✅ 达标条件：分数 ≥ 平均分
                    </div>
                    <div class="reward-benefit">
                        ✨ 免搬椅子 + 减免操步
                    </div>
                </div>
                <!-- 第三名组别 -->
                <div class="reward-item">
                    <div class="reward-rank">
                        <span class="rank-medal">🥉</span>
                        <span class="rank-title">第三名组别</span>
                    </div>
                    <div class="reward-desc">
                        该组个人分数前三名者
                    </div>
                    <div class="reward-condition">
                        ✅ 达标条件：组内排名前三
                    </div>
                    <div class="reward-benefit">
                        ✨ 免搬椅子 + 减免操步
                    </div>
                </div>
            </div>
            <div class="reward-note">
                <span class="reward-extra">🎁 额外奖励：第一名组别达标者额外获得一份奖励</span>
            </div>
            <div class="reward-footer">
                * 未达标者，工作照旧 *
            </div>
        </div>

        <div class="footer">
            👆 点击排名卡片快速跳转 · 点击📲传输数据 · 点击🌓切换深色模式 · 显示较昨日变化 · 最近5次得分
        </div>
    </div>

    <!-- 数据波纹 -->
    <div class="data-ripple" id="dataRipple"></div>
    
    <!-- 传输状态 -->
    <div class="transfer-status" id="transferStatus">
        <div class="status-dot"></div>
        <div class="status-text">正在传输数据...</div>
        <div class="status-progress">
            <div class="progress-bar" id="progressBar"></div>
        </div>
    </div>

    <script>
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.body.classList.add('night-mode');
        }
        
        const searchInput = document.getElementById('search');
        const allRows = document.querySelectorAll('tbody tr');
        const transferBtn = document.getElementById('transferBtn');
        const transferCircle = document.getElementById('transferCircle');
        const dataRipple = document.getElementById('dataRipple');
        const transferStatus = document.getElementById('transferStatus');
        const progressBar = document.getElementById('progressBar');
        
        // 华为传输动画
        function startHuaweiTransfer() {
            // 按钮圆圈动画
            transferCircle.classList.remove('active');
            void transferCircle.offsetWidth;
            transferCircle.classList.add('active');
            
            // 中心波纹动画
            dataRipple.classList.remove('active');
            void dataRipple.offsetWidth;
            dataRipple.classList.add('active');
            
            // 显示传输状态
            transferStatus.classList.add('show');
            
            // 模拟传输进度
            let progress = 0;
            const interval = setInterval(() => {
                progress += Math.random() * 15;
                if (progress >= 100) {
                    progress = 100;
                    clearInterval(interval);
                    
                    // 传输完成，隐藏状态
                    setTimeout(() => {
                        transferStatus.classList.remove('show');
                    }, 1000);
                }
                progressBar.style.width = progress + '%';
            }, 200);
            
            // 创建飞行的粒子
            for (let i = 0; i < 10; i++) {
                setTimeout(() => {
                    createParticle();
                }, i * 50);
            }
            
            // 模拟数据更新动画
            document.querySelectorAll('.rank-card, .group-card').forEach(el => {
                el.style.transform = 'scale(0.98)';
                el.style.transition = 'transform 0.3s';
                setTimeout(() => {
                    el.style.transform = '';
                }, 300);
            });
            
            // 数字翻转效果
            document.querySelectorAll('.member-table td:last-child').forEach(cell => {
                cell.style.transform = 'scale(1.1)';
                cell.style.transition = 'transform 0.3s';
                setTimeout(() => {
                    cell.style.transform = '';
                }, 300);
            });
        }
        
        // 创建飞行粒子
        function createParticle() {
            const particle = document.createElement('div');
            particle.className = 'data-particle';
            
            // 随机起始位置
            const startX = Math.random() * window.innerWidth;
            const startY = Math.random() * window.innerHeight;
            
            // 随机终点偏移
            const tx = (Math.random() - 0.5) * 200;
            const ty = (Math.random() - 0.5) * 200;
            
            particle.style.left = startX + 'px';
            particle.style.top = startY + 'px';
            particle.style.setProperty('--tx', tx + 'px');
            particle.style.setProperty('--ty', ty + 'px');
            
            document.body.appendChild(particle);
            
            // 激活动画
            void particle.offsetWidth;
            particle.classList.add('active');
            
            // 动画结束后移除
            setTimeout(() => {
                particle.remove();
            }, 1000);
        }
        
        transferBtn.addEventListener('click', startHuaweiTransfer);

        // 搜索功能
        searchInput.addEventListener('input', (e) => {
            const searchTerm = e.target.value.toLowerCase().trim();
            
            allRows.forEach(row => {
                const searchText = row.getAttribute('data-search').toLowerCase();
                if (searchText.includes(searchTerm)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });

        // 排名动画
        document.querySelectorAll('.rank-card').forEach(card => {
            const currentRank = parseInt(card.dataset.rank);
            const prevRank = parseInt(card.dataset.prevRank);
            if (currentRank && prevRank) {
                if (currentRank < prevRank) {
                    card.classList.add('rank-up');
                } else if (currentRank > prevRank) {
                    card.classList.add('rank-down');
                }
            }
        });
    </script>
</body>
</html>'''

# 保存HTML文件
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n✅ 生成成功！共 {len(people)} 人")
print("\n📊 奖励统计:")
for g in ["星穹组", "夜曜组", "沧澜组"]:
    if g in group_data:
        members = group_data[g]
        pass_count = sum(1 for m in members if m["reward_status"] == "✅")
        print(f"  {g}: {pass_count}/{len(members)} 人达标 ({int(pass_count/len(members)*100)}%)")
    change = group_changes[g]
    change_symbol = "▲" if change > 0 else "▼" if change < 0 else "◆"
    print(f"  总分: {int(group_totals[g])}分, 第{group_rank[g]}名 {change_symbol} {int(change)}")
print("✨ 华为传输动画：圆圈波纹 + 飞行粒子 + 进度条 + 数字跳动")
