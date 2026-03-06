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
if len(df) > 0:
    first_row = df.iloc[0].tolist()
    for j in range(7, len(first_row)):
        if pd.notna(first_row[j]):
            date_str = str(first_row[j])
            try:
                if "00:00" in date_str:
                    date_str = date_str[5:10]
                dates.append(date_str)
            except:
                dates.append(f"D{j-6}")
        else:
            dates.append(f"D{j-6}")

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

print("\n开始匹配成员...")

for member in members_list:
    found = False
    
    for i in range(len(df)):
        row = df.iloc[i].tolist()
        
        if len(row) > 4:
            row_name_cn = str(row[3]) if len(row) > 3 and pd.notna(row[3]) else ""
            row_name_en = str(row[4]) if len(row) > 4 and pd.notna(row[4]) else ""
            
            if (member["name_cn"] in row_name_cn or 
                member["name_en"][:20] in row_name_en[:20]):
                
                # 提取分数
                scores = []
                total = 0
                score_dict = {}
                for j in range(7, len(row)):
                    if j-7 < len(dates):
                        date = dates[j-7]
                        val = row[j]
                        if pd.notna(val):
                            try:
                                num = float(val)
                                scores.append(num)
                                total += num
                                if num > 0:
                                    score_dict[date] = num
                            except (ValueError, TypeError):
                                scores.append(0)
                        else:
                            scores.append(0)
                
                people.append({
                    "group": member["group"],
                    "order": member["order"],
                    "name_cn": member["name_cn"],
                    "name_en": member["name_en"],
                    "class": member["class"],
                    "student_id": member["student_id"],
                    "scores": scores,
                    "score_dict": score_dict,
                    "total": total
                })
                print(f"✓ 找到 {member['name_cn']} (总分: {total})")
                found = True
                break
    
    if not found:
        print(f"✗ 找不到 {member['name_cn']}")

print(f"\n总共找到 {len(people)} 人")

# 按组别整理
group_data = {g: [] for g in ["星穹组", "夜曜组", "沧澜组"]}
group_totals = {g: 0 for g in ["星穹组", "夜曜组", "沧澜组"]}

for p in people:
    group_data[p["group"]].append(p)
    group_totals[p["group"]] += p["total"]

# 每个组内按order排序
for g in group_data:
    group_data[g].sort(key=lambda x: x["order"])

# 计算组排名
sorted_groups = sorted(group_totals.items(), key=lambda x: x[1], reverse=True)
group_rank = {}
for i, (g, _) in enumerate(sorted_groups, 1):
    group_rank[g] = i

# 生成HTML
html = f"""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>训育处 · 学长团分数板</title>
    <style>
        * {{
            -webkit-tap-highlight-color: rgba(0,0,0,0);
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        
        /* 日夜间模式变量 */
        :root {{
            --bg-body: #f5f7fa;
            --bg-card: #ffffff;
            --bg-input: #f8fafc;
            --text-primary: #2c3e50;
            --text-secondary: #64748b;
            --border-color: #edf2f7;
            --border-input: #e2e8f0;
            --shadow: 0 4px 12px rgba(0,0,0,0.03);
            --star-light: #fffbf0;
            --night-light: #f8f3ff;
            --ocean-light: #f0f7ff;
            
            /* 组颜色 */
            --star-primary: #fbbf24;
            --night-primary: #a78bfa;
            --ocean-primary: #60a5fa;
        }}
        
        body.night-mode {{
            --bg-body: #0f1319;
            --bg-card: #1e242b;
            --bg-input: #1e242b;
            --text-primary: #e5e7eb;
            --text-secondary: #9ca3af;
            --border-color: #2d343e;
            --border-input: #2d343e;
            --shadow: 0 4px 12px rgba(0,0,0,0.3);
            --star-light: #332e1f;
            --night-light: #241f33;
            --ocean-light: #1a2533;
            
            /* 夜间模式组颜色 - 加强漫透感 */
            --star-primary: #fbbf24;
            --night-primary: #c4b5fd;
            --ocean-primary: #7ab2ff;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Microsoft YaHei', sans-serif;
            background: var(--bg-body);
            padding: 20px;
            color: var(--text-primary);
            transition: background 0.3s, color 0.3s;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        /* 头部 */
        .header {{
            background: var(--bg-card);
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
        }}
        
        .header-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }}
        
        h1 {{
            font-size: 1.8rem;
            font-weight: 600;
            color: var(--text-primary);
        }}
        
        .theme-toggle {{
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
        }}
        
        .theme-toggle:hover {{
            background: var(--border-color);
        }}
        
        .subtitle {{
            display: flex;
            justify-content: space-between;
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-bottom: 16px;
        }}
        
        #search {{
            width: 100%;
            padding: 14px 20px;
            border: 1px solid var(--border-input);
            border-radius: 40px;
            font-size: 1rem;
            background: var(--bg-input);
            color: var(--text-primary);
            transition: all 0.2s;
        }}
        
        #search:focus {{
            outline: none;
            border-color: var(--text-secondary);
            background: var(--bg-card);
        }}
        
        /* 组排名卡片 - 加强漫透效果 */
        .rank-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 24px;
        }}
        
        .rank-card {{
            background: var(--bg-card);
            border-radius: 16px;
            padding: 16px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 12px;
            border-left: 4px solid;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }}
        
        /* 漫透光效果 */
        .rank-card::after {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.3s;
        }}
        
        .rank-card:hover::after {{
            opacity: 0.6;
        }}
        
        .rank-card[data-group="星穹组"]::after {{
            background: radial-gradient(circle at 30% 30%, rgba(251, 191, 36, 0.2), transparent 70%);
        }}
        
        .rank-card[data-group="夜曜组"]::after {{
            background: radial-gradient(circle at 30% 30%, rgba(167, 139, 250, 0.2), transparent 70%);
        }}
        
        .rank-card[data-group="沧澜组"]::after {{
            background: radial-gradient(circle at 30% 30%, rgba(96, 165, 250, 0.25), transparent 70%);
        }}
        
        body.night-mode .rank-card[data-group="沧澜组"]::after {{
            background: radial-gradient(circle at 30% 30%, rgba(96, 165, 250, 0.35), transparent 75%);
        }}
        
        .rank-card[data-group="星穹组"] {{
            border-left-color: var(--star-primary);
            background: linear-gradient(to right, var(--star-light), var(--bg-card));
        }}
        .rank-card[data-group="夜曜组"] {{
            border-left-color: var(--night-primary);
            background: linear-gradient(to right, var(--night-light), var(--bg-card));
        }}
        .rank-card[data-group="沧澜组"] {{
            border-left-color: var(--ocean-primary);
            background: linear-gradient(to right, var(--ocean-light), var(--bg-card));
        }}
        
        .rank-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        }}
        
        .rank-icon {{
            font-size: 2.2rem;
            position: relative;
            z-index: 1;
        }}
        
        .rank-info {{
            flex: 1;
            position: relative;
            z-index: 1;
        }}
        
        .rank-name {{
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 4px;
        }}
        
        .rank-score {{
            font-weight: 700;
            font-size: 1.4rem;
        }}
        
        .rank-score small {{
            font-size: 0.8rem;
            font-weight: 400;
            color: var(--text-secondary);
            margin-left: 4px;
        }}
        
        /* 组卡片 - 加强漫透效果 */
        .groups {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        
        .group-card {{
            background: var(--bg-card);
            border-radius: 20px;
            padding: 24px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
            scroll-margin-top: 20px;
            border-top: 4px solid;
            position: relative;
            overflow: hidden;
        }}
        
        .group-card::after {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 100px;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.3s;
        }}
        
        .group-card:hover::after {{
            opacity: 0.5;
        }}
        
        .group-card[data-group="星穹组"]::after {{
            background: radial-gradient(circle at 20% 20%, rgba(251, 191, 36, 0.15), transparent 70%);
        }}
        
        .group-card[data-group="夜曜组"]::after {{
            background: radial-gradient(circle at 20% 20%, rgba(167, 139, 250, 0.15), transparent 70%);
        }}
        
        .group-card[data-group="沧澜组"]::after {{
            background: radial-gradient(circle at 20% 20%, rgba(96, 165, 250, 0.2), transparent 70%);
        }}
        
        body.night-mode .group-card[data-group="沧澜组"]::after {{
            background: radial-gradient(circle at 20% 20%, rgba(96, 165, 250, 0.3), transparent 75%);
        }}
        
        .group-card[data-group="星穹组"] {{ border-top-color: var(--star-primary); }}
        .group-card[data-group="夜曜组"] {{ border-top-color: var(--night-primary); }}
        .group-card[data-group="沧澜组"] {{ border-top-color: var(--ocean-primary); }}
        
        .group-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 2px solid var(--border-color);
            position: relative;
            z-index: 1;
        }}
        
        .group-title {{
            font-size: 1.4rem;
            font-weight: 600;
        }}
        
        .group-badge {{
            padding: 6px 16px;
            border-radius: 30px;
            font-size: 0.9rem;
            font-weight: 500;
            color: white;
            position: relative;
            z-index: 1;
        }}
        
        .group-card[data-group="星穹组"] .group-badge {{ background: var(--star-primary); color: #1e293b; }}
        .group-card[data-group="夜曜组"] .group-badge {{ background: var(--night-primary); }}
        .group-card[data-group="沧澜组"] .group-badge {{ background: var(--ocean-primary); }}
        
        /* 表格 */
        .member-table {{
            width: 100%;
            border-collapse: collapse;
            position: relative;
            z-index: 1;
        }}
        
        .member-table th {{
            text-align: left;
            padding: 12px 8px;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--text-secondary);
            text-transform: uppercase;
            border-bottom: 2px solid var(--border-color);
        }}
        
        .member-table td {{
            padding: 14px 8px;
            border-bottom: 1px solid var(--border-color);
        }}
        
        .member-table tr:hover {{
            background: var(--bg-body);
        }}
        
        .rank-number {{
            font-weight: 500;
            color: var(--text-secondary);
            width: 45px;
        }}
        
        .name-cell {{
            min-width: 130px;
        }}
        
        .name-cn {{
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 2px;
        }}
        
        .name-en {{
            font-size: 0.7rem;
            color: var(--text-secondary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 130px;
        }}
        
        .info-cell {{
            font-size: 0.9rem;
            color: var(--text-secondary);
            font-weight: 500;
        }}
        
        /* 分数标签 */
        .scores-cell {{
            max-width: 220px;
        }}
        
        .score-tags {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        
        .score-item {{
            padding: 4px 10px;
            border-radius: 30px;
            font-size: 0.75rem;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            background: var(--bg-body);
            color: var(--text-secondary);
            border: 1px solid var(--border-color);
            transition: all 0.2s;
        }}
        
        .score-item:hover {{
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        .score-item.has-score {{
            background: #dbeafe;
            color: #1e40af;
            border: 1px solid #bfdbfe;
        }}
        
        body.night-mode .score-item.has-score {{
            background: #1a2a45;
            color: #93c5fd;
            border: 1px solid #3b5b9b;
        }}
        
        .score-date {{
            opacity: 0.7;
        }}
        
        .score-value {{
            font-weight: 700;
        }}
        
        .total-cell {{
            font-weight: 700;
            font-size: 1.1rem;
            text-align: right;
            width: 60px;
        }}
        
        /* 搜索高亮 */
        .group-card[data-group="星穹组"] tr.search-match {{ background: var(--star-light) !important; }}
        .group-card[data-group="夜曜组"] tr.search-match {{ background: var(--night-light) !important; }}
        .group-card[data-group="沧澜组"] tr.search-match {{ background: var(--ocean-light) !important; }}
        
        .footer {{
            margin-top: 40px;
            text-align: center;
            color: var(--text-secondary);
            font-size: 0.8rem;
            padding: 20px;
            border-top: 1px solid var(--border-color);
        }}
        
        @media (max-width: 640px) {{
            body {{ padding: 16px; }}
            .rank-grid {{ gap: 12px; }}
            .rank-card {{ padding: 14px 10px; }}
            .rank-icon {{ font-size: 1.8rem; }}
            .member-table th {{ font-size: 0.7rem; padding: 8px 4px; }}
            .member-table td {{ padding: 10px 4px; font-size: 0.85rem; }}
            .scores-cell {{ max-width: 140px; }}
            .header-top {{ flex-direction: column; gap: 12px; align-items: flex-start; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-top">
                <h1>🏫 学长团分数板</h1>
                <div class="theme-toggle" onclick="document.body.classList.toggle('night-mode')">
                    <span>🌓</span>
                    <span>切换模式</span>
                </div>
            </div>
            <div class="subtitle">
                <span>Prefects' Scoreboard</span>
                <span>{datetime.now().strftime('%Y.%m.%d')}</span>
            </div>
            <input type="text" id="search" placeholder="搜索姓名、英文名、班级或学号...">
        </div>

        <!-- 组排名卡片 -->
        <div class="rank-grid">
"""

for i, (g, total) in enumerate(sorted_groups, 1):
    icons = {1: "🥇", 2: "🥈", 3: "🥉"}
    html += f"""
            <div class="rank-card" data-group="{g}" onclick="document.getElementById('group-{g}').scrollIntoView({{behavior: 'smooth'}})">
                <span class="rank-icon">{icons[i]}</span>
                <div class="rank-info">
                    <div class="rank-name">{g}</div>
                    <div class="rank-score">{int(total)} <small>分</small></div>
                </div>
            </div>
"""

html += """
        </div>

        <div class="groups">
"""

# 添加三个组
group_emojis = {"星穹组": "✨", "夜曜组": "🌙", "沧澜组": "🌊"}
for group_name in ["星穹组", "夜曜组", "沧澜组"]:
    members = group_data[group_name]
    rank = group_rank[group_name]
    
    html += f"""
            <div class="group-card" data-group="{group_name}" id="group-{group_name}">
                <div class="group-header">
                    <span class="group-title">{group_emojis[group_name]} {group_name}</span>
                    <span class="group-badge">第{rank}名 · {int(group_totals[group_name])}分</span>
                </div>
                <table class="member-table">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>姓名</th>
                            <th>班级</th>
                            <th>学号</th>
                            <th>每日得分</th>
                            <th>总分</th>
                        </tr>
                    </thead>
                    <tbody>
"""

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
        name_en_short = member['name_en'][:20] + "..." if len(member['name_en']) > 20 else member['name_en']
        
        html += f"""
                        <tr data-search="{member['name_cn']} {member['name_en']} {member['class']} {member['student_id']}">
                            <td class="rank-number">{member['order']:02d}</td>
                            <td class="name-cell">
                                <div class="name-cn">{member['name_cn']}</div>
                                <div class="name-en">{name_en_short}</div>
                            </td>
                            <td class="info-cell">{member['class']}</td>
                            <td class="info-cell">{member['student_id']}</td>
                            <td class="scores-cell"><div class="score-tags">{score_tags}</div></td>
                            <td class="total-cell">{int(member['total'])}</td>
                        </tr>
"""

    html += """
                    </tbody>
                </table>
            </div>
"""

html += """
        </div>
        
        <div class="footer">
            ｜ 训育处 ｜ 数据每日更新 ｜ 点击组排名跳转 ｜ 点击🌓切换夜间模式 ｜
        </div>
    </div>

    <script>
        // 检查系统主题偏好
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.body.classList.add('night-mode');
        }
        
        // 搜索功能
        const searchInput = document.getElementById('search');
        const allRows = document.querySelectorAll('tbody tr');
        
        searchInput.addEventListener('input', (e) => {
            const searchTerm = e.target.value.toLowerCase().trim();
            
            if (searchTerm === '') {
                allRows.forEach(row => {
                    row.style.display = '';
                    row.classList.remove('search-match');
                });
                return;
            }
            
            allRows.forEach(row => {
                const searchText = row.getAttribute('data-search').toLowerCase();
                if (searchText.includes(searchTerm)) {
                    row.style.display = '';
                    row.classList.add('search-match');
                } else {
                    row.style.display = 'none';
                    row.classList.remove('search-match');
                }
            });
        });
    </script>
</body>
</html>
"""

# 保存HTML文件
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n✅ 生成成功！共 {len(people)} 人")
for g in ["星穹组", "夜曜组", "沧澜组"]:
    print(f"  {g}: {len(group_data[g])}人, {int(group_totals[g])}分, 第{group_rank[g]}名")
