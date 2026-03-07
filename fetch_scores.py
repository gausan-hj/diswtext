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
                date_objects.append(datetime.strptime(first_row[j][:10], '%Y-%m-%d'))
            except:
                dates.append(f"D{j-6}")
                date_objects.append(None)
        else:
            dates.append(f"D{j-6}")
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

# 生成HTML - 使用普通三重引号，不使用f-string
html = '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>训育处 - 学长团分数板 · 奖励机制</title>
    <style>
        * {
            -webkit-tap-highlight-color: rgba(0,0,0,0);
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        :root {
            --bg-body: #f5f7fa;
            --bg-card: #ffffff;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --border-light: #f1f5f9;
            --border-color: #eef2f6;
            --shadow: 0 2px 8px rgba(0,0,0,0.03);
            --star-light: #fef9e7;
            --night-light: #f5f0ff;
            --ocean-light: #f0f7ff;
            --score-bg: #f1f5f9;
            --score-text: #334155;
            --score-positive-bg: #e0f2fe;
            --score-positive-text: #0369a1;
            --change-up: #10b981;
            --change-down: #ef4444;
            --change-steady: #f59e0b;
            --reward-pass: #dcfce7;
            --reward-pass-text: #166534;
            --reward-fail: #fee2e2;
            --reward-fail-text: #991b1b;
        }
        
        body.night-mode {
            --bg-body: #0f172a;
            --bg-card: #1e293b;
            --text-primary: #f1f5f9;
            --text-secondary: #94a3b8;
            --border-light: #334155;
            --border-color: #334155;
            --shadow: 0 4px 12px rgba(0,0,0,0.3);
            --star-light: #2a2a1a;
            --night-light: #1e1a2a;
            --ocean-light: #1a1f2a;
            --score-bg: #2d3748;
            --score-text: #cbd5e1;
            --score-positive-bg: #1e3a5f;
            --score-positive-text: #93c5fd;
            --change-up: #34d399;
            --change-down: #f87171;
            --change-steady: #fbbf24;
            --reward-pass: #14532d;
            --reward-pass-text: #bbf7d0;
            --reward-fail: #7f1d1d;
            --reward-fail-text: #fecaca;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Microsoft YaHei', sans-serif;
            background: var(--bg-body);
            padding: 16px;
            color: var(--text-primary);
            transition: background-color 0.3s, color 0.3s;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .header {
            background: var(--bg-card);
            border-radius: 24px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
        }
        
        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }
        
        h1 {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--text-primary);
        }
        
        .theme-toggle {
            background: var(--bg-body);
            border: 1px solid var(--border-color);
            border-radius: 30px;
            padding: 8px 16px;
            cursor: pointer;
            color: var(--text-primary);
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }
        
        .theme-toggle:hover {
            background: var(--border-color);
        }
        
        .subtitle {
            display: flex;
            justify-content: space-between;
            color: var(--text-secondary);
            font-size: 0.85rem;
        }
        
        .search-box {
            margin-top: 16px;
        }
        
        #search {
            width: 100%;
            padding: 14px 18px;
            border: 1px solid var(--border-color);
            border-radius: 40px;
            font-size: 1rem;
            background: var(--bg-card);
            color: var(--text-primary);
            transition: all 0.2s;
        }
        
        #search:focus {
            outline: none;
            border-color: var(--text-secondary);
        }
        
        .rank-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-bottom: 24px;
        }
        
        .rank-card {
            background: var(--bg-card);
            border-radius: 18px;
            padding: 14px 10px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            border-left: 4px solid;
            transition: all 0.2s;
            animation: cardAppear 0.5s ease-out;
        }
        
        @keyframes cardAppear {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        
        .rank-card.rank-up {
            animation: rankUp 0.8s ease;
        }
        
        .rank-card.rank-down {
            animation: rankDown 0.8s ease;
        }
        
        @keyframes rankUp {
            0% { transform: translateY(0); }
            30% { transform: translateY(-5px); }
            60% { transform: translateY(2px); }
            100% { transform: translateY(0); }
        }
        
        @keyframes rankDown {
            0% { transform: translateY(0); }
            30% { transform: translateY(5px); }
            60% { transform: translateY(-2px); }
            100% { transform: translateY(0); }
        }
        
        .rank-card[data-group="星穹组"] {
            border-left-color: #fbbf24;
            background: linear-gradient(to right, var(--star-light), var(--bg-card));
        }
        .rank-card[data-group="夜曜组"] {
            border-left-color: #a78bfa;
            background: linear-gradient(to right, var(--night-light), var(--bg-card));
        }
        .rank-card[data-group="沧澜组"] {
            border-left-color: #60a5fa;
            background: linear-gradient(to right, var(--ocean-light), var(--bg-card));
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
            margin-bottom: 2px;
        }
        
        .rank-score {
            font-weight: 700;
            font-size: 1.2rem;
            color: var(--text-primary);
        }
        
        .rank-score small {
            font-size: 0.7rem;
            font-weight: 400;
            color: var(--text-secondary);
        }
        
        .rank-change {
            font-size: 0.7rem;
            margin-top: 2px;
            font-weight: 500;
        }
        
        .change-up { color: var(--change-up); }
        .change-down { color: var(--change-down); }
        .change-steady { color: var(--change-steady); }
        
        .groups {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .group-card {
            background: var(--bg-card);
            border-radius: 24px;
            padding: 20px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
            scroll-margin-top: 10px;
            border-top: 4px solid;
        }
        
        .group-card[data-group="星穹组"] {
            border-top-color: #fbbf24;
        }
        .group-card[data-group="夜曜组"] {
            border-top-color: #a78bfa;
        }
        .group-card[data-group="沧澜组"] {
            border-top-color: #60a5fa;
        }
        
        .group-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 2px solid var(--border-light);
        }
        
        .group-title {
            font-size: 1.3rem;
            font-weight: 600;
        }
        
        .group-badge {
            padding: 6px 14px;
            border-radius: 40px;
            font-size: 0.85rem;
            font-weight: 500;
            color: white;
        }
        
        .group-card[data-group="星穹组"] .group-badge {
            background: #fbbf24;
            color: #1e293b;
        }
        .group-card[data-group="夜曜组"] .group-badge {
            background: #a78bfa;
        }
        .group-card[data-group="沧澜组"] .group-badge {
            background: #60a5fa;
        }
        
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
            padding: 10px 6px;
            font-size: 0.7rem;
            font-weight: 600;
            color: var(--text-secondary);
            text-transform: uppercase;
            border-bottom: 2px solid var(--border-light);
        }
        
        .member-table td {
            padding: 12px 6px;
            border-bottom: 1px solid var(--border-light);
        }
        
        .member-table tr:last-child td {
            border-bottom: none;
        }
        
        .rank-number {
            font-weight: 500;
            color: var(--text-secondary);
            width: 40px;
        }
        
        .name-cell {
            min-width: 120px;
        }
        
        .name-cn {
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 2px;
        }
        
        .name-en {
            font-size: 0.65rem;
            color: var(--text-secondary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 110px;
        }
        
        .info-cell {
            font-size: 0.85rem;
            color: var(--text-secondary);
        }
        
        .scores-cell {
            max-width: 180px;
        }
        
        .score-tags {
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
        }
        
        .score-item {
            padding: 3px 8px;
            border-radius: 20px;
            font-size: 0.65rem;
            font-weight: 500;
            background: var(--score-bg);
            color: var(--score-text);
        }
        
        .score-item.has-score {
            background: var(--score-positive-bg);
            color: var(--score-positive-text);
        }
        
        .score-date {
            opacity: 0.7;
        }
        
        .score-value {
            font-weight: 700;
        }
        
        .total-cell {
            font-weight: 700;
            font-size: 1rem;
            color: var(--text-primary);
            text-align: right;
            width: 60px;
        }
        
        .reward-cell {
            text-align: center;
            width: 50px;
        }
        
        .reward-pass {
            background: var(--reward-pass);
            color: var(--reward-pass-text);
            padding: 4px 8px;
            border-radius: 30px;
            font-size: 0.7rem;
            font-weight: 600;
            display: inline-block;
            min-width: 40px;
        }
        
        .reward-fail {
            background: var(--reward-fail);
            color: var(--reward-fail-text);
            padding: 4px 8px;
            border-radius: 30px;
            font-size: 0.7rem;
            font-weight: 600;
            display: inline-block;
            min-width: 40px;
        }
        
        .reward-card {
            background: var(--bg-card);
            border-radius: 24px;
            padding: 20px;
            margin-top: 30px;
            margin-bottom: 20px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
            border-left: 4px solid #fbbf24;
        }
        
        .reward-title {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .reward-grid {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .reward-item {
            background: var(--bg-body);
            border-radius: 16px;
            padding: 14px;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .reward-rank-icon {
            font-size: 1.8rem;
            min-width: 40px;
            text-align: center;
        }
        
        .reward-content {
            flex: 1;
        }
        
        .reward-rank-text {
            font-weight: 700;
            font-size: 1rem;
            margin-bottom: 2px;
        }
        
        .reward-desc {
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin-bottom: 2px;
        }
        
        .reward-highlight {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-primary);
        }
        
        .reward-note {
            margin-top: 16px;
            padding: 12px;
            background: var(--bg-body);
            border-radius: 16px;
            font-size: 0.85rem;
            color: var(--text-secondary);
            text-align: center;
            border: 1px dashed var(--border-color);
        }
        
        .footer {
            margin-top: 20px;
            text-align: center;
            color: var(--text-secondary);
            font-size: 0.75rem;
            padding: 16px;
        }
        
        @media (max-width: 640px) {
            body { padding: 12px; }
            .rank-grid { gap: 8px; }
            .rank-card { padding: 12px 8px; }
            .rank-icon { font-size: 1.5rem; }
            .rank-name { font-size: 0.85rem; }
            .rank-score { font-size: 1rem; }
            .group-card { padding: 16px; }
            .group-title { font-size: 1.1rem; }
            .group-badge { padding: 4px 10px; font-size: 0.75rem; }
            .member-table th { font-size: 0.65rem; padding: 8px 4px; }
            .member-table td { padding: 10px 4px; font-size: 0.8rem; }
            .reward-item { padding: 12px; }
            .reward-rank-icon { font-size: 1.5rem; min-width: 35px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-top">
                <h1>🏫 学长团分数板</h1>
                <div class="theme-toggle" onclick="document.body.classList.toggle('night-mode')">
                    <span>🌓</span>
                    <span>夜间</span>
                </div>
            </div>
            <div class="subtitle">
                <span>Prefects' Scoreboard</span>
                <span>''' + datetime.now().strftime('%Y.%m.%d %H:%M') + '''</span>
            </div>
            <div class="search-box">
                <input type="text" id="search" placeholder="🔍 搜索姓名、英文名、班级或学号...">
            </div>
        </div>

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
        change_text = f'<span class="change-up">▲ +{int(change)}</span>'
    elif change < 0:
        change_text = f'<span class="change-down">▼ {int(change)}</span>'
    else:
        change_text = '<span class="change-steady">◆ 0</span>'
    
    html += '''
            <div class="rank-card ''' + rank_animation + '''" data-group="''' + g + '''" data-rank="''' + str(current_rank) + '''" data-prev-rank="''' + str(prev_rank) + '''" onclick="document.getElementById(\'''' + group_id + '''\').scrollIntoView({behavior: \'smooth\'})">
                <span class="rank-icon">''' + rank_icons[i] + '''</span>
                <div class="rank-info">
                    <div class="rank-name">''' + g + '''</div>
                    <div class="rank-score">''' + str(int(total)) + '''<small>分</small></div>
                    <div class="rank-change">较昨日 ''' + change_text + '''</div>
                </div>
            </div>
'''

html += '''
        </div>

        <div class="groups">
'''

# 添加三个组
for group_name in ["星穹组", "夜曜组", "沧澜组"]:
    members = group_data[group_name]
    rank = group_rank[group_name]
    group_id = group_ids[group_name]
    avg_score = group_averages[group_name]
    
    html += '''
            <div class="group-card" data-group="''' + group_name + '''" id="''' + group_id + '''">
                <div class="group-header">
                    <div>
                        <span class="group-title">''' + group_name + '''</span>
                        <span style="font-size:0.75rem; color:var(--text-secondary); margin-left:6px;">平均 ''' + str(int(avg_score)) + '''</span>
                    </div>
                    <span class="group-badge">第''' + str(rank) + '''名 · ''' + str(int(group_totals[group_name])) + '''分</span>
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
            score = member["score_dict"][date]
            score_tags += f'<span class="score-item has-score"><span class="score-date">{date}</span><span class="score-value">{int(score)}</span></span>'
        
        if not score_tags:
            score_tags = '<span class="score-item">-</span>'
        
        # 截断英文名
        name_en_short = member['name_en'][:15] + "…" if len(member['name_en']) > 15 else member['name_en']
        
        html += '''
                        <tr data-search="''' + member['name_cn'] + ' ' + member['name_en'] + ' ' + member['class'] + ' ' + member['student_id'] + '''">
                            <td class="rank-number">''' + str(member['order']) + '''</td>
                            <td class="name-cell">
                                <div class="name-cn">''' + member['name_cn'] + '''</div>
                                <div class="name-en">''' + name_en_short + '''</div>
                            </td>
                            <td class="info-cell">''' + member['class'] + '''</td>
                            <td class="info-cell">''' + member['student_id'] + '''</td>
                            <td class="scores-cell"><div class="score-tags">''' + score_tags + '''</div></td>
                            <td class="total-cell">''' + str(int(member['total'])) + '''</td>
                            <td class="reward-cell"><span class="''' + member['reward_class'] + '''">''' + member['reward_status'] + '''</span></td>
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

        <div class="reward-card">
            <di
