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

# 生成HTML - 优化排版
html = '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>训育处 · 学长团分数板 · 奖励机制</title>
    <style>
        * {
            -webkit-tap-highlight-color: rgba(0,0,0,0);
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        :root {
            --bg-body: #f8fafc;
            --bg-card: #ffffff;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --text-tertiary: #94a3b8;
            --border-light: #f1f5f9;
            --border-color: #e2e8f0;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1);
            
            /* 组颜色 - 柔和版 */
            --star-primary: #fbbf24;
            --star-light: #fef3c7;
            --star-bg: #fffbeb;
            --night-primary: #a78bfa;
            --night-light: #ede9fe;
            --night-bg: #f5f3ff;
            --ocean-primary: #60a5fa;
            --ocean-light: #dbeafe;
            --ocean-bg: #eff6ff;
            
            --score-bg: #f1f5f9;
            --score-text: #475569;
            --score-positive-bg: #dbeafe;
            --score-positive-text: #1e40af;
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
            --text-tertiary: #64748b;
            --border-light: #334155;
            --border-color: #475569;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.5);
            --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.5);
            
            --star-light: #422f1a;
            --star-bg: #2a2a1a;
            --night-light: #2a1f3a;
            --night-bg: #1e1a2a;
            --ocean-light: #1a2a45;
            --ocean-bg: #1a1f2a;
            
            --score-bg: #2d3748;
            --score-text: #9ca3af;
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
            padding: 20px;
            color: var(--text-primary);
            transition: background-color 0.3s, color 0.3s;
            line-height: 1.5;
        }
        
        .container {
            max-width: 1280px;
            margin: 0 auto;
        }
        
        /* 头部 - 优化间距 */
        .header {
            background: var(--bg-card);
            border-radius: 24px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-light);
        }
        
        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            flex-wrap: wrap;
            gap: 16px;
        }
        
        .title-section {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .title-icon {
            font-size: 2rem;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
        }
        
        h1 {
            font-size: 1.6rem;
            font-weight: 600;
            color: var(--text-primary);
            letter-spacing: -0.02em;
        }
        
        .theme-toggle {
            background: var(--bg-body);
            border: 1px solid var(--border-color);
            border-radius: 40px;
            padding: 8px 20px;
            cursor: pointer;
            color: var(--text-primary);
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }
        
        .theme-toggle:hover {
            background: var(--border-light);
        }
        
        .subtitle {
            display: flex;
            justify-content: space-between;
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 1px dashed var(--border-light);
        }
        
        .search-box {
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
            padding: 14px 20px 14px 48px;
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
            box-shadow: 0 0 0 3px rgba(100,116,139,0.1);
        }
        
        #search::placeholder {
            color: var(--text-tertiary);
        }
        
        /* 组排名卡片 - 更精致 */
        .rank-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 32px;
        }
        
        .rank-card {
            background: var(--bg-card);
            border-radius: 20px;
            padding: 18px 16px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--border-light);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 12px;
            border-left: 4px solid;
            transition: all 0.2s;
            position: relative;
            overflow: hidden;
        }
        
        .rank-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }
        
        .rank-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.8), transparent 70%);
            opacity: 0;
            transition: opacity 0.3s;
            pointer-events: none;
        }
        
        .rank-card:hover::before {
            opacity: 0.3;
        }
        
        .rank-card.rank-up {
            animation: rankUp 0.5s ease;
        }
        
        .rank-card.rank-down {
            animation: rankDown 0.5s ease;
        }
        
        @keyframes rankUp {
            0%, 100% { transform: translateY(0); }
            30% { transform: translateY(-4px); }
            60% { transform: translateY(2px); }
        }
        
        @keyframes rankDown {
            0%, 100% { transform: translateY(0); }
            30% { transform: translateY(4px); }
            60% { transform: translateY(-2px); }
        }
        
        .rank-card[data-group="星穹组"] {
            border-left-color: var(--star-primary);
            background: linear-gradient(135deg, var(--star-bg), var(--bg-card));
        }
        .rank-card[data-group="夜曜组"] {
            border-left-color: var(--night-primary);
            background: linear-gradient(135deg, var(--night-bg), var(--bg-card));
        }
        .rank-card[data-group="沧澜组"] {
            border-left-color: var(--ocean-primary);
            background: linear-gradient(135deg, var(--ocean-bg), var(--bg-card));
        }
        
        .rank-icon {
            font-size: 2rem;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
        }
        
        .rank-info {
            flex: 1;
        }
        
        .rank-name {
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 4px;
            color: var(--text-primary);
        }
        
        .rank-score {
            font-weight: 700;
            font-size: 1.3rem;
            color: var(--text-primary);
            line-height: 1.2;
        }
        
        .rank-score small {
            font-size: 0.75rem;
            font-weight: 400;
            color: var(--text-secondary);
            margin-left: 4px;
        }
        
        .rank-change {
            font-size: 0.75rem;
            margin-top: 4px;
            font-weight: 500;
        }
        
        .change-up { color: var(--change-up); }
        .change-down { color: var(--change-down); }
        .change-steady { color: var(--change-steady); }
        
        /* 组卡片 - 优化间距 */
        .groups {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }
        
        .group-card {
            background: var(--bg-card);
            border-radius: 28px;
            padding: 24px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-light);
            scroll-margin-top: 20px;
            border-top: 4px solid;
            transition: box-shadow 0.3s;
        }
        
        .group-card:hover {
            box-shadow: var(--shadow-lg);
        }
        
        .group-card[data-group="星穹组"] {
            border-top-color: var(--star-primary);
        }
        .group-card[data-group="夜曜组"] {
            border-top-color: var(--night-primary);
        }
        .group-card[data-group="沧澜组"] {
            border-top-color: var(--ocean-primary);
        }
        
        .group-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 16px;
            border-bottom: 2px solid var(--border-light);
            flex-wrap: wrap;
            gap: 12px;
        }
        
        .group-title-section {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .group-emoji {
            font-size: 1.6rem;
        }
        
        .group-title {
            font-size: 1.4rem;
            font-weight: 600;
            color: var(--text-primary);
        }
        
        .group-stats {
            display: flex;
            gap: 12px;
            align-items: center;
        }
        
        .group-badge {
            padding: 6px 16px;
            border-radius: 40px;
            font-size: 0.9rem;
            font-weight: 500;
            color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .group-card[data-group="星穹组"] .group-badge {
            background: var(--star-primary);
            color: #1e293b;
        }
        .group-card[data-group="夜曜组"] .group-badge {
            background: var(--night-primary);
        }
        .group-card[data-group="沧澜组"] .group-badge {
            background: var(--ocean-primary);
        }
        
        .group-avg {
            background: var(--bg-body);
            padding: 4px 12px;
            border-radius: 30px;
            font-size: 0.85rem;
            color: var(--text-secondary);
            border: 1px solid var(--border-light);
        }
        
        /* 表格 - 优化对齐 */
        .table-container {
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            border-radius: 16px;
            margin-top: 8px;
        }
        
        .member-table {
            width: 100%;
            border-collapse: collapse;
            min-width: 750px;
            font-size: 0.9rem;
        }
        
        .member-table th {
            text-align: left;
            padding: 14px 8px;
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            background: var(--bg-body);
            border-bottom: 2px solid var(--border-light);
        }
        
        .member-table td {
            padding: 14px 8px;
            border-bottom: 1px solid var(--border-light);
            vertical-align: middle;
        }
        
        .member-table tr:last-child td {
            border-bottom: none;
        }
        
        .member-table tr:hover {
            background: var(--bg-body);
        }
        
        /* 列宽定义 */
        .member-table th:nth-child(1) { width: 50px; text-align: center; }
        .member-table th:nth-child(2) { width: 140px; }
        .member-table th:nth-child(3) { width: 70px; }
        .member-table th:nth-child(4) { width: 90px; }
        .member-table th:nth-child(5) { width: auto; }
        .member-table th:nth-child(6) { width: 70px; text-align: right; padding-right: 16px; }
        .member-table th:nth-child(7) { width: 60px; text-align: center; }
        
        .member-table td:nth-child(1) { text-align: center; color: var(--text-tertiary); font-weight: 500; }
        .member-table td:nth-child(6) { text-align: right; padding-right: 16px; font-weight: 600; }
        .member-table td:nth-child(7) { text-align: center; }
        
        .rank-number {
            font-weight: 500;
            color: var(--text-tertiary);
        }
        
        .name-cell {
            min-width: 140px;
        }
        
        .name-cn {
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 2px;
            color: var(--text-primary);
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
            font-weight: 500;
        }
        
        .scores-cell {
            max-width: 220px;
        }
        
        .score-tags {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }
        
        .score-item {
            padding: 4px 10px;
            border-radius: 30px;
            font-size: 0.7rem;
            font-weight: 500;
            background: var(--score-bg);
            color: var(--score-text);
            border: 1px solid var(--border-light);
            transition: all 0.2s;
        }
        
        .score-item:hover {
            transform: translateY(-1px);
            box-shadow: var(--shadow-sm);
        }
        
        .score-item.has-score {
            background: var(--score-positive-bg);
            color: var(--score-positive-text);
            border-color: transparent;
        }
        
        .score-date {
            opacity: 0.7;
            margin-right: 2px;
        }
        
        .score-value {
            font-weight: 700;
        }
        
        .total-cell {
            font-weight: 700;
            font-size: 1rem;
            color: var(--text-primary);
        }
        
        .reward-cell {
            font-weight: 500;
        }
        
        .reward-pass, .reward-fail {
            padding: 4px 8px;
            border-radius: 30px;
            font-size: 0.7rem;
            font-weight: 600;
            display: inline-block;
            min-width: 45px;
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
        
        /* 奖励卡片 - 优化样式 */
        .reward-card {
            background: var(--bg-card);
            border-radius: 28px;
            padding: 24px;
            margin-top: 32px;
            margin-bottom: 20px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-light);
            border-left: 4px solid #fbbf24;
        }
        
        .reward-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--text-primary);
        }
        
        .reward-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 16px;
        }
        
        .reward-item {
            background: var(--bg-body);
            border-radius: 20px;
            padding: 16px;
            display: flex;
            gap: 12px;
            border: 1px solid var(--border-light);
            transition: transform 0.2s;
        }
        
        .reward-item:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        .reward-rank-icon {
            font-size: 2rem;
            min-width: 48px;
            text-align: center;
        }
        
        .reward-content {
            flex: 1;
        }
        
        .reward-rank-text {
            font-weight: 700;
            font-size: 1rem;
            margin-bottom: 4px;
            color: var(--text-primary);
        }
        
        .reward-desc {
            font-size: 0.8rem;
            color: var(--text-secondary);
            margin-bottom: 4px;
        }
        
        .reward-highlight {
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--text-primary);
        }
        
        .reward-note {
            margin-top: 16px;
            padding: 16px;
            background: var(--bg-body);
            border-radius: 16px;
            font-size: 0.85rem;
            color: var(--text-secondary);
            text-align: center;
            border: 1px dashed var(--border-light);
        }
        
        .footer {
            margin-top: 24px;
            text-align: center;
            color: var(--text-tertiary);
            font-size: 0.75rem;
            padding: 16px;
            border-top: 1px solid var(--border-light);
        }
        
        /* 移动端优化 */
        @media (max-width: 768px) {
            body { padding: 16px; }
            
            .rank-grid {
                gap: 12px;
            }
            
            .rank-card {
                padding: 14px 10px;
            }
            
            .rank-icon {
                font-size: 1.6rem;
            }
            
            .rank-score {
                font-size: 1.1rem;
            }
            
            .reward-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            
            .group-header {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .group-stats {
                width: 100%;
                justify-content: space-between;
            }
        }
        
        @media (max-width: 640px) {
            .rank-grid {
                gap: 8px;
            }
            
            .rank-card {
                padding: 12px 8px;
            }
            
            .rank-name {
                font-size: 0.85rem;
            }
            
            .rank-score {
                font-size: 1rem;
            }
            
            .rank-score small {
                font-size: 0.65rem;
            }
            
            .group-card {
                padding: 20px;
            }
            
            .group-title {
                font-size: 1.2rem;
            }
            
            .group-badge {
                padding: 4px 12px;
                font-size: 0.8rem;
            }
            
            .member-table th {
                padding: 10px 6px;
                font-size: 0.65rem;
            }
            
            .member-table td {
                padding: 10px 6px;
                font-size: 0.8rem;
            }
            
            .member-table th:nth-child(6),
            .member-table td:nth-child(6) {
                padding-right: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-top">
                <div class="title-section">
                    <span class="title-icon">🏫</span>
                    <h1>学长团分数板</h1>
                </div>
                <div class="theme-toggle" onclick="document.body.classList.toggle('night-mode')">
                    <span>🌓</span>
                    <span>夜间模式</span>
                </div>
            </div>
            <div class="subtitle">
                <span>Prefects' Scoreboard · 奖励机制</span>
                <span>''' + datetime.now().strftime('%Y.%m.%d %H:%M') + '''</span>
            </div>
            <div class="search-box">
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

        <!-- 三组 -->
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
                    <div class="group-title-section">
                        <span class="group-emoji">''' + group_emojis[group_name] + '''</span>
                        <span class="group-title">''' + group_name + '''</span>
                    </div>
                    <div class="group-stats">
                        <span class="group-avg">平均 ''' + str(int(avg_score)) + '''</span>
                        <span class="group-badge">第''' + str(rank) + '''名 · ''' + str(int(group_totals[group_name])) + '''分</span>
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

        <!-- 奖励规则卡片 -->
        <div class="reward-card">
            <div class="reward-title">
                <span>🎁</span>
                <span>本轮奖励机制</span>
            </div>
            <div class="reward-grid">
                <div class="reward-item">
                    <div class="reward-rank-icon">🥇</div>
                    <div class="reward-content">
                        <div class="reward-rank-text">第一名组别</div>
                        <div class="reward-desc">个人分数 ≥ 组平均分一半</div>
                        <div class="reward-highlight">✅ 免搬椅子 + 减免操步</div>
                    </div>
                </div>
                <div class="reward-item">
                    <div class="reward-rank-icon">🥈</div>
                    <div class="reward-content">
                        <div class="reward-rank-text">第二名组别</div>
                        <div class="reward-desc">个人分数 ≥ 组平均分</div>
                        <div class="reward-highlight">✅ 免搬椅子 + 减免操步</div>
                    </div>
                </div>
                <div class="reward-item">
                    <div class="reward-rank-icon">🥉</div>
                    <div class="reward-content">
                        <div class="reward-rank-text">第三名组别</div>
                        <div class="reward-desc">个人分数 组内前三名</div>
                        <div class="reward-highlight">✅ 免搬椅子 + 减免操步</div>
                    </div>
                </div>
            </div>
            <div class="reward-note">
                ⚡ 第一名组别达标者额外获得一份奖励 · 公平原则，不负每一位付出的学长
            </div>
        </div>

        <div class="footer">
            👆 点击组排名卡片快速跳转 · 点击🌓切换夜间模式 · 显示较昨日变化 · 最近5次得分
        </div>
    </div>

    <script>
        // 检查系统主题偏好
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.body.classList.add('night-mode');
        }
        
        const searchInput = document.getElementById('search');
        const allRows = document.querySelectorAll('tbody tr');
        
        searchInput.addEventListener('input', (e) => {
            const searchTerm = e.target.value.toLowerCase().trim();
            
            if (searchTerm === '') {
                allRows.forEach(row => row.style.display = '');
                return;
            }
            
            allRows.forEach(row => {
                const searchText = row.getAttribute('data-search').toLowerCase();
                row.style.display = searchText.includes(searchTerm) ? '' : 'none';
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
print("✨ 优化：精致排版 + 对齐优化 + 响应式设计")
