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
            p["reward_text"] = "达标" if p["total"] >= avg / 2 else "未达标"
            p["reward_class"] = "reward-pass" if p["total"] >= avg / 2 else "reward-fail"
        elif rank == 2:  # 第二名组别
            p["reward_status"] = "✅" if p["total"] >= avg else "❌"
            p["reward_text"] = "达标" if p["total"] >= avg else "未达标"
            p["reward_class"] = "reward-pass" if p["total"] >= avg else "reward-fail"
        else:  # 第三名组别
            # 找出组内前三名
            top3 = sorted(group_data[g], key=lambda x: x["total"], reverse=True)[:3]
            top3_names = [t["name_cn"] for t in top3]
            if p["name_cn"] in top3_names:
                p["reward_status"] = "✅"
                p["reward_text"] = "达标"
                p["reward_class"] = "reward-pass"
            else:
                p["reward_status"] = "❌"
                p["reward_text"] = "未达标"
                p["reward_class"] = "reward-fail"

# 组别颜色配置
group_colors = {
    "星穹组": {"primary": "#fbbf24", "light": "#fef3c7", "border": "#f59e0b"},
    "夜曜组": {"primary": "#a78bfa", "light": "#ede9fe", "border": "#8b5cf6"},
    "沧澜组": {"primary": "#60a5fa", "light": "#dbeafe", "border": "#3b82f6"}
}

# 生成HTML
html = f"""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>训育处 - 学长团分数板 · 奖励机制</title>
    <style>
        * {{
            -webkit-tap-highlight-color: rgba(0,0,0,0);
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Microsoft YaHei', sans-serif;
            background: #f5f7fa;
            padding: 16px;
            color: #1e293b;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        /* 头部 - 简洁干净 */
        .header {{
            background: white;
            border-radius: 24px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            border: 1px solid #edf2f7;
        }}
        
        h1 {{
            font-size: 1.5rem;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 4px;
        }}
        
        .subtitle {{
            display: flex;
            justify-content: space-between;
            color: #64748b;
            font-size: 0.85rem;
        }}
        
        .search-box {{
            margin-top: 16px;
        }}
        
        #search {{
            width: 100%;
            padding: 14px 18px;
            border: 1px solid #e2e8f0;
            border-radius: 40px;
            font-size: 1rem;
            background: #f8fafc;
            transition: all 0.2s;
        }}
        
        #search:focus {{
            outline: none;
            border-color: #94a3b8;
            background: white;
        }}
        
        /* 组排名卡片 */
        .rank-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-bottom: 24px;
        }}
        
        .rank-card {{
            background: white;
            border-radius: 18px;
            padding: 14px 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
            border: 1px solid #edf2f7;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            border-left: 4px solid;
            transition: all 0.2s;
        }}
        
        .rank-card:active {{
            transform: scale(0.97);
        }}
        
        .rank-card[data-group="星穹组"] {{
            border-left-color: #fbbf24;
            background: linear-gradient(to right, #fef9e7, white);
        }}
        .rank-card[data-group="夜曜组"] {{
            border-left-color: #a78bfa;
            background: linear-gradient(to right, #f5f0ff, white);
        }}
        .rank-card[data-group="沧澜组"] {{
            border-left-color: #60a5fa;
            background: linear-gradient(to right, #f0f7ff, white);
        }}
        
        .rank-icon {{
            font-size: 1.8rem;
        }}
        
        .rank-info {{
            flex: 1;
        }}
        
        .rank-name {{
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 2px;
        }}
        
        .rank-score {{
            font-weight: 700;
            font-size: 1.2rem;
            color: #0f172a;
        }}
        
        .rank-score small {{
            font-size: 0.7rem;
            font-weight: 400;
            color: #64748b;
        }}
        
        /* 组卡片 */
        .groups {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        
        .group-card {{
            background: white;
            border-radius: 24px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            border: 1px solid #edf2f7;
            scroll-margin-top: 10px;
            border-top: 4px solid;
        }}
        
        .group-card[data-group="星穹组"] {{
            border-top-color: #fbbf24;
        }}
        .group-card[data-group="夜曜组"] {{
            border-top-color: #a78bfa;
        }}
        .group-card[data-group="沧澜组"] {{
            border-top-color: #60a5fa;
        }}
        
        .group-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 2px solid #f1f5f9;
        }}
        
        .group-title {{
            font-size: 1.3rem;
            font-weight: 600;
        }}
        
        .group-badge {{
            padding: 6px 14px;
            border-radius: 40px;
            font-size: 0.85rem;
            font-weight: 500;
            color: white;
        }}
        
        .group-card[data-group="星穹组"] .group-badge {{
            background: #fbbf24;
            color: #1e293b;
        }}
        .group-card[data-group="夜曜组"] .group-badge {{
            background: #a78bfa;
        }}
        .group-card[data-group="沧澜组"] .group-badge {{
            background: #60a5fa;
        }}
        
        /* 表格 - 手机优化 */
        .table-container {{
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }}
        
        .member-table {{
            width: 100%;
            border-collapse: collapse;
            min-width: 600px;
            font-size: 0.9rem;
        }}
        
        .member-table th {{
            text-align: left;
            padding: 10px 6px;
            font-size: 0.7rem;
            font-weight: 600;
            color: #64748b;
            text-transform: uppercase;
            border-bottom: 2px solid #f1f5f9;
        }}
        
        .member-table td {{
            padding: 12px 6px;
            border-bottom: 1px solid #f1f5f9;
        }}
        
        .member-table tr:last-child td {{
            border-bottom: none;
        }}
        
        .rank-number {{
            font-weight: 500;
            color: #94a3b8;
            width: 40px;
        }}
        
        .name-cell {{
            min-width: 120px;
        }}
        
        .name-cn {{
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 2px;
        }}
        
        .name-en {{
            font-size: 0.65rem;
            color: #64748b;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 110px;
        }}
        
        .info-cell {{
            font-size: 0.85rem;
            color: #475569;
        }}
        
        .scores-cell {{
            max-width: 180px;
        }}
        
        .score-tags {{
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
        }}
        
        .score-item {{
            padding: 3px 8px;
            border-radius: 20px;
            font-size: 0.65rem;
            font-weight: 500;
            background: #f1f5f9;
            color: #334155;
        }}
        
        .score-item.has-score {{
            background: #e0f2fe;
            color: #0369a1;
        }}
        
        .score-date {{
            opacity: 0.7;
        }}
        
        .score-value {{
            font-weight: 700;
        }}
        
        .total-cell {{
            font-weight: 700;
            font-size: 1rem;
            color: #0f172a;
            text-align: right;
            width: 50px;
        }}
        
        /* 奖励状态 */
        .reward-cell {{
            text-align: center;
            width: 50px;
        }}
        
        .reward-pass {{
            background: #dcfce7;
            color: #166534;
            padding: 4px 8px;
            border-radius: 30px;
            font-size: 0.7rem;
            font-weight: 600;
            display: inline-block;
        }}
        
        .reward-fail {{
            background: #fee2e2;
            color: #991b1b;
            padding: 4px 8px;
            border-radius: 30px;
            font-size: 0.7rem;
            font-weight: 600;
            display: inline-block;
        }}
        
        /* 奖励规则卡片 - 移到最下方 */
        .reward-card {{
            background: white;
            border-radius: 24px;
            padding: 20px;
            margin-top: 30px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            border: 1px solid #edf2f7;
            border-left: 4px solid #fbbf24;
        }}
        
        .reward-title {{
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .reward-grid {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        
        .reward-item {{
            background: #f8fafc;
            border-radius: 16px;
            padding: 14px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        
        .reward-rank-icon {{
            font-size: 1.8rem;
            min-width: 40px;
            text-align: center;
        }}
        
        .reward-content {{
            flex: 1;
        }}
        
        .reward-rank-text {{
            font-weight: 700;
            font-size: 1rem;
            margin-bottom: 2px;
        }}
        
        .reward-desc {{
            font-size: 0.85rem;
            color: #64748b;
            margin-bottom: 2px;
        }}
        
        .reward-highlight {{
            font-size: 0.85rem;
            font-weight: 600;
            color: #0f172a;
        }}
        
        .reward-note {{
            margin-top: 16px;
            padding: 12px;
            background: #f8fafc;
            border-radius: 16px;
            font-size: 0.85rem;
            color: #475569;
            text-align: center;
            border: 1px dashed #e2e8f0;
        }}
        
        .footer {{
            margin-top: 20px;
            text-align: center;
            color: #94a3b8;
            font-size: 0.75rem;
            padding: 16px;
        }}
        
        /* 手机端优化 */
        @media (max-width: 640px) {{
            body {{ padding: 12px; }}
            
            .rank-grid {{
                gap: 8px;
            }}
            
            .rank-card {{
                padding: 12px 8px;
            }}
            
            .rank-icon {{
                font-size: 1.5rem;
            }}
            
            .rank-name {{
                font-size: 0.85rem;
            }}
            
            .rank-score {{
                font-size: 1rem;
            }}
            
            .group-card {{
                padding: 16px;
            }}
            
            .group-title {{
                font-size: 1.1rem;
            }}
            
            .group-badge {{
                padding: 4px 10px;
                font-size: 0.75rem;
            }}
            
            .member-table th {{
                font-size: 0.65rem;
                padding: 8px 4px;
            }}
            
            .member-table td {{
                padding: 10px 4px;
                font-size: 0.8rem;
            }}
            
            .reward-item {{
                padding: 12px;
            }}
            
            .reward-rank-icon {{
                font-size: 1.5rem;
                min-width: 35px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏫 学长团分数板</h1>
            <div class="subtitle">
                <span>Prefects' Scoreboard</span>
                <span>{datetime.now().strftime('%Y.%m.%d %H:%M')}</span>
            </div>
            <div class="search-box">
                <input type="text" id="search" placeholder="🔍 搜索姓名、英文名、班级或学号...">
            </div>
        </div>

        <!-- 组排名卡片 -->
        <div class="rank-grid">
"""

# 添加组排名卡片
rank_icons = {1: "🥇", 2: "🥈", 3: "🥉"}
group_ids = {"星穹组": "group-xingqiong", "夜曜组": "group-yeyao", "沧澜组": "group-canglan"}
for i, (g, total) in enumerate(sorted_groups, 1):
    group_id = group_ids[g]
    html += f"""
            <div class="rank-card" data-group="{g}" onclick="document.getElementById('{group_id}').scrollIntoView({{behavior: 'smooth'}})">
                <span class="rank-icon">{rank_icons[i]}</span>
                <div class="rank-info">
                    <div class="rank-name">{g}</div>
                    <div class="rank-score">{int(total)}<small>分</small></div>
                </div>
            </div>
"""

html += """
        </div>

        <!-- 三组 -->
        <div class="groups">
"""

# 添加三个组
for group_name in ["星穹组", "夜曜组", "沧澜组"]:
    members = group_data[group_name]
    rank = group_rank[group_name]
    group_id = group_ids[group_name]
    avg_score = group_averages[group_name]
    
    html += f"""
            <div class="group-card" data-group="{group_name}" id="{group_id}">
                <div class="group-header">
                    <div>
                        <span class="group-title">{group_name}</span>
                        <span style="font-size:0.75rem; color:#64748b; margin-left:6px;">平均 {int(avg_score)}</span>
                    </div>
                    <span class="group-badge">第{rank}名 · {int(group_totals[group_name])}分</span>
                </div>
                <div class="table-container">
                    <table class="member-table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>姓名</th>
                                <th>班级</th>
                                <th>学号</th>
                                <th>得分</th>
                                <th>总分</th>
                                <th>奖</th>
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
        name_en_short = member['name_en'][:15] + "…" if len(member['name_en']) > 15 else member['name_en']
        
        html += f"""
                        <tr data-search="{member['name_cn']} {member['name_en']} {member['class']} {member['student_id']}">
                            <td class="rank-number">{member['order']}</td>
                            <td class="name-cell">
                                <div class="name-cn">{member['name_cn']}</div>
                                <div class="name-en">{name_en_short}</div>
                            </td>
                            <td class="info-cell">{member['class']}</td>
                            <td class="info-cell">{member['student_id']}</td>
                            <td class="scores-cell"><div class="score-tags">{score_tags}</div></td>
                            <td class="total-cell">{int(member['total'])}</td>
                            <td class="reward-cell"><span class="{member['reward_class']}">{member['reward_status']}</span></td>
                        </tr>
        """
    
    html += """
                        </tbody>
                    </table>
                </div>
            </div>
    """

html += """
        </div>

        <!-- 奖励规则卡片 - 移到最下方 -->
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
            👆 点击组排名卡片快速跳转 · 显示最近5次得分 · ✅达标可免搬椅子+减免操步
        </div>
    </div>

    <script>
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
    </script>
</body>
</html>
"""

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
    print(f"  总分: {int(group_totals[g])}分, 第{group_rank[g]}名")
print("✨ 奖励卡片已移到最下方 + 手机版美化")
