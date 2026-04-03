import pandas as pd
from datetime import datetime
import json

# ===== 你要修改的地方 =====
SHEET_ID = "1YVa3nLUBW80j2nA4mudEqLH91RJ0FSRytmoDqmbyUJk"
SHEET_NAME = "Sheet3"
LANGUAGES_JSON_PATH = "languages.json"
# ========================

# ===== 2026年联课活动数据 =====
cca_data = [
    {"date": "2026-02-24", "activity": "活动顾问+总学长+副总学长", "uniform": "校服"},
    {"date": "2026-02-26", "activity": "操步", "uniform": "体育衣"},
    {"date": "2026-03-03", "activity": "操步", "uniform": "体育衣"},
    {"date": "2026-03-05", "activity": "活动（文书+财政+查账）", "uniform": "校服"},
    {"date": "2026-03-10", "activity": "操步", "uniform": "体育衣"},
    {"date": "2026-03-12", "activity": "活动（行动组）", "uniform": "校服"},
    {"date": "2026-03-17", "activity": "操步", "uniform": "体育衣"},
    {"date": "2026-03-31", "activity": "操步", "uniform": "体育衣"},
    {"date": "2026-04-02", "activity": "活动（值岗组）", "uniform": "校服"},
    {"date": "2026-04-07", "activity": "操步", "uniform": "体育衣"},
    {"date": "2026-04-09", "activity": "活动（督察组）", "uniform": "校服"},
    {"date": "2026-04-14", "activity": "操步", "uniform": "体育衣"},
    {"date": "2026-04-16", "activity": "活动（星穹组）", "uniform": "校服"},
    {"date": "2026-04-21", "activity": "操步", "uniform": "体育衣"},
    {"date": "2026-04-23", "activity": "活动（夜曜组）", "uniform": "校服"},
    {"date": "2026-04-28", "activity": "操步", "uniform": "体育衣"},
    {"date": "2026-04-30", "activity": "活动（沧澜组）", "uniform": "校服"},
    {"date": "2026-05-05", "activity": "第一学期检讨", "uniform": "校服"},
    {"date": "2026-05-07", "activity": "操步", "uniform": "体育衣"}
]

# ===== 成员名单 =====
members_list = [
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

# 读取 Google Sheets
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
print("正在从 Google Sheets 读取数据...")
df = pd.read_csv(url, header=None, encoding='utf-8-sig')
print(f"读取到 {len(df)} 行数据")

# 获取日期
dates = []
if len(df) > 0:
    first_row = df.iloc[0].tolist()
    for j in range(7, len(first_row)):
        if pd.notna(first_row[j]):
            date_str = str(first_row[j])
            if "00:00" in date_str:
                date_str = date_str[5:10]
            dates.append(date_str)
        else:
            dates.append("")
print(f"找到 {len(dates)} 个日期")

# 匹配成员
people = []
group_totals = {"星穹组": 0, "夜曜组": 0, "沧澜组": 0}
group_members_count = {"星穹组": 0, "夜曜组": 0, "沧澜组": 0}

print("\n开始匹配成员...")
for idx, member in enumerate(members_list):
    found = False
    for i in range(len(df)):
        row = df.iloc[i].tolist()
        if len(row) > 4:
            row_name_cn = str(row[3]) if len(row) > 3 and pd.notna(row[3]) else ""
            row_name_en = str(row[4]) if len(row) > 4 and pd.notna(row[4]) else ""
            if member["name_cn"] in row_name_cn or member["name_en"][:20] in row_name_en[:20]:
                total = 0
                score_dict = {}
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
                            except:
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
                    "people_idx": idx
                })
                print(f"✓ 找到 {member['name_cn']} (总分: {total})")
                found = True
                break
    if not found:
        print(f"✗ 找不到 {member['name_cn']}")

print(f"\n总共找到 {len(people)} 人")

# 按组别整理
group_data = {"星穹组": [], "夜曜组": [], "沧澜组": []}
for p in people:
    group_data[p["group"]].append(p)
    group_totals[p["group"]] += p["total"]
    group_members_count[p["group"]] += 1

# 排序
for g in group_data:
    group_data[g].sort(key=lambda x: x["order"])

# 组排名
sorted_groups = sorted(group_totals.items(), key=lambda x: x[1], reverse=True)
group_rank = {}
for i, (g, _) in enumerate(sorted_groups, 1):
    group_rank[g] = i

# 组平均分
group_averages = {}
for g in ["星穹组", "夜曜组", "沧澜组"]:
    group_averages[g] = group_totals[g] / len(group_data[g]) if group_data[g] else 0

# 达标状态
for g in group_data:
    for p in group_data[g]:
        rank = group_rank[g]
        avg = group_averages[g]
        if rank == 1:
            p["reward_status"] = "✅" if p["total"] >= avg / 2 else "❌"
            p["reward_class"] = "reward-pass" if p["total"] >= avg / 2 else "reward-fail"
        elif rank == 2:
            p["reward_status"] = "✅" if p["total"] >= avg else "❌"
            p["reward_class"] = "reward-pass" if p["total"] >= avg else "reward-fail"
        else:
            top3 = sorted(group_data[g], key=lambda x: x["total"], reverse=True)[:3]
            top3_names = [t["name_cn"] for t in top3]
            if p["name_cn"] in top3_names:
                p["reward_status"] = "✅"
                p["reward_class"] = "reward-pass"
            else:
                p["reward_status"] = "❌"
                p["reward_class"] = "reward-fail"

# 组内排名
for g in group_data:
    sorted_members = sorted(group_data[g], key=lambda x: x["total"], reverse=True)
    rank = 1
    for i, member in enumerate(sorted_members):
        if i > 0 and member["total"] < sorted_members[i-1]["total"]:
            rank = i + 1
        member["group_rank"] = rank
        if rank == 1:
            member["medal"] = "🥇"
        elif rank == 2:
            member["medal"] = "🥈"
        elif rank == 3:
            member["medal"] = "🥉"
        else:
            member["medal"] = f"#{rank}"

# 最高最低分
group_max_scores = {}
group_min_scores = {}
for g in group_data:
    if group_data[g]:
        group_max_scores[g] = max(m["total"] for m in group_data[g])
        group_min_scores[g] = min(m["total"] for m in group_data[g])
    else:
        group_max_scores[g] = 0
        group_min_scores[g] = 0

# 准备注入的数据
people_json = json.dumps(people, ensure_ascii=False)
group_averages_json = json.dumps(group_averages, ensure_ascii=False)
cca_data_json = json.dumps(cca_data, ensure_ascii=False)

# 生成 HTML
html = f'''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>学长团分数板</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: system-ui, sans-serif;
            background: #f5f7fc;
            padding: 16px;
            transition: background 0.2s;
        }}
        body.dark {{
            background: #1a1a2e;
            color: #eee;
        }}
        .header {{
            background: white;
            border-radius: 20px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
        body.dark .header,
        body.dark .rank-card,
        body.dark .group-card {{
            background: #16213e;
            color: #eee;
        }}
        h1 {{ font-size: 1.4rem; margin-bottom: 8px; }}
        .search-box {{
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 30px;
            font-size: 14px;
        }}
        body.dark .search-box {{
            background: #0f0f23;
            color: #eee;
            border-color: #333;
        }}
        .rank-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-bottom: 20px;
        }}
        .rank-card {{
            background: white;
            border-radius: 16px;
            padding: 12px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            cursor: pointer;
            transition: transform 0.1s;
        }}
        .rank-card:active {{ transform: scale(0.97); }}
        .group-card {{
            background: white;
            border-radius: 20px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
        .group-title {{
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 2px solid #eee;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }}
        th, td {{
            padding: 8px 4px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }}
        th {{
            color: #666;
            font-weight: 600;
        }}
        body.dark th {{ color: #aaa; }}
        body.dark td {{ border-color: #2a2a4a; }}
        .clickable-name {{
            cursor: pointer;
            transition: opacity 0.2s;
        }}
        .clickable-name:active {{ opacity: 0.6; }}
        .total-heat {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            color: white;
            font-weight: bold;
        }}
        .reward-pass {{
            background: #dcfce7;
            color: #166534;
            padding: 2px 6px;
            border-radius: 12px;
        }}
        .reward-fail {{
            background: #fee2e2;
            color: #991b1b;
            padding: 2px 6px;
            border-radius: 12px;
        }}
        body.dark .reward-pass {{
            background: #1a4a3a;
            color: #bbf7d0;
        }}
        body.dark .reward-fail {{
            background: #5a2a2a;
            color: #fecaca;
        }}
        .rank-cell {{
            text-align: center;
            font-weight: bold;
        }}
        .footer {{
            text-align: center;
            font-size: 11px;
            color: #999;
            margin-top: 20px;
        }}
        /* 弹窗样式 */
        .modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.6);
            z-index: 10000;
            justify-content: center;
            align-items: center;
        }}
        .modal.show {{ display: flex; }}
        .modal-content {{
            background: white;
            border-radius: 24px;
            max-width: 450px;
            width: 90%;
            max-height: 80vh;
            overflow-y: auto;
            padding: 20px;
        }}
        body.dark .modal-content {{
            background: #1e2a3a;
            color: #eee;
        }}
        .modal-header {{
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid #ddd;
        }}
        .modal-close {{
            float: right;
            font-size: 24px;
            cursor: pointer;
        }}
        .modal-name {{ font-size: 1.4rem; font-weight: bold; }}
        .modal-stats {{
            display: flex;
            gap: 12px;
            margin: 16px 0;
        }}
        .stat-card {{
            flex: 1;
            background: #f0f0f0;
            border-radius: 12px;
            padding: 10px;
            text-align: center;
        }}
        body.dark .stat-card {{ background: #2a3a4a; }}
        .stat-label {{ font-size: 11px; color: #888; }}
        .stat-value {{ font-size: 20px; font-weight: bold; }}
        .score-detail-item {{
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #ddd;
        }}
        .chart-wrapper {{ margin-top: 16px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🏫 学长团分数板</h1>
        <input type="text" class="search-box" id="search" placeholder="🔍 搜姓名/班级/学号...">
    </div>

    <div class="rank-grid" id="rankGrid"></div>
    <div id="groups"></div>
    <div class="footer">👆 点击姓名查看详情 · 双击屏幕切换深色模式</div>

    <!-- 弹窗 -->
    <div id="memberModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <span class="modal-close">&times;</span>
                <div class="modal-name" id="modalName"></div>
                <div class="modal-info" id="modalInfo"></div>
            </div>
            <div class="modal-stats">
                <div class="stat-card"><div class="stat-label">总分</div><div class="stat-value" id="modalTotal"></div></div>
                <div class="stat-card"><div class="stat-label">组内排名</div><div class="stat-value" id="modalRank"></div></div>
                <div class="stat-card"><div class="stat-label">vs组平均</div><div class="stat-value" id="modalVsAvg"></div></div>
            </div>
            <h3>📅 得分明细</h3>
            <div id="modalScores"></div>
            <div class="chart-wrapper">
                <canvas id="modalChart" width="400" height="150"></canvas>
            </div>
        </div>
    </div>

    <script>
        // 数据注入
        const membersData = {people_json};
        const groupAverages = {group_averages_json};
        const ccaData = {cca_data_json};

        // 搜索功能
        document.getElementById('search').addEventListener('input', function(e) {{
            const term = e.target.value.toLowerCase();
            document.querySelectorAll('tbody tr').forEach(row => {{
                const text = row.getAttribute('data-search') || '';
                row.style.display = text.includes(term) ? '' : 'none';
            }});
        }});

        // 深色模式
        let darkMode = false;
        function toggleDarkMode() {{
            darkMode = !darkMode;
            document.body.classList.toggle('dark', darkMode);
        }}
        document.addEventListener('dblclick', toggleDarkMode);

        // 弹窗功能
        let trendChart = null;
        
        function showMemberModal(member) {{
            const modal = document.getElementById('memberModal');
            document.getElementById('modalName').textContent = member.name_cn;
            document.getElementById('modalInfo').textContent = `${{member.class}}班 · 学号:${{member.student_id}} · ${{member.group}}`;
            document.getElementById('modalTotal').textContent = Math.floor(member.total);
            document.getElementById('modalRank').innerHTML = member.medal;
            
            const avg = groupAverages[member.group] || 0;
            const vsAvg = member.total - avg;
            document.getElementById('modalVsAvg').innerHTML = vsAvg >= 0 ? `+${{Math.floor(vsAvg)}}` : `${{Math.floor(vsAvg)}}`;
            
            // 得分明细
            const sortedDates = Object.entries(member.score_dict).sort((a,b) => a[0].localeCompare(b[0]));
            let scoresHtml = '';
            for (const [date, score] of sortedDates) {{
                scoresHtml += `<div class="score-detail-item"><span>📅 ${{date.slice(5)}}</span><span>+${{Math.floor(score)}}分</span></div>`;
            }}
            document.getElementById('modalScores').innerHTML = scoresHtml || '<div>暂无得分记录</div>';
            
            // 趋势图
            const canvas = document.getElementById('modalChart');
            if (trendChart) trendChart.destroy();
            const ctx = canvas.getContext('2d');
            const labels = sortedDates.map(d => d[0].slice(5));
            const data = sortedDates.map(d => d[1]);
            trendChart = new Chart(ctx, {{
                type: 'line',
                data: {{ labels, datasets: [{{
                    label: '得分', data, borderColor: '#eab308', backgroundColor: '#eab30820', fill: true, tension: 0.3
                }}] }},
                options: {{ responsive: true, maintainAspectRatio: true, plugins: {{ legend: {{ display: false }} }} }}
            }});
            
            modal.classList.add('show');
        }}
        
        document.querySelector('.modal-close')?.addEventListener('click', () => {{
            document.getElementById('memberModal').classList.remove('show');
        }});
        document.getElementById('memberModal')?.addEventListener('click', (e) => {{
            if (e.target === document.getElementById('memberModal')) e.target.classList.remove('show');
        }});
        
        function bindNameClick() {{
            document.querySelectorAll('.clickable-name').forEach(el => {{
                el.addEventListener('click', (e) => {{
                    e.stopPropagation();
                    const idx = parseInt(el.getAttribute('data-idx'));
                    if (!isNaN(idx) && membersData[idx]) showMemberModal(membersData[idx]);
                }});
            }});
        }}
    </script>
</body>
</html>'''

# 添加组排名卡片
rank_cards_html = ""
for i, (g, total) in enumerate(sorted_groups, 1):
    icons = {1: "🥇", 2: "🥈", 3: "🥉"}
    rank_cards_html += f'''
    <div class="rank-card" onclick="document.getElementById('group-{g}').scrollIntoView({{behavior:'smooth'}})">
        <div style="font-size: 24px;">{icons[i]}</div>
        <div><strong>{g}</strong></div>
        <div style="font-size: 20px; font-weight: bold;">{int(total)}</div>
        <div style="font-size: 12px; color: #888;">第{i}名</div>
    </div>'''

# 添加组别详情
groups_html = ""
for group_name in ["星穹组", "夜曜组", "沧澜组"]:
    members = group_data[group_name]
    rank = group_rank[group_name]
    avg_score = group_averages[group_name]
    group_max = group_max_scores[group_name]
    group_min = group_min_scores[group_name]
    
    group_html = f'''
    <div class="group-card" id="group-{group_name}">
        <div class="group-title">{group_name} · 平均 {int(avg_score)}分 · 第{rank}名</div>
        <table>
            <thead>
                <tr><th>#</th><th>姓名</th><th>班</th><th>学号</th><th>总分</th><th>🏆</th><th>奖</th></tr>
            </thead>
            <tbody>'''
    
    for member in members:
        total_score = member['total']
        if group_max > group_min:
            heat_level = min(9, max(1, int((total_score - group_min) / (group_max - group_min) * 9) + 1))
        else:
            heat_level = 5
        colors = ['#083344', '#164e63', '#155e75', '#0369a1', '#0284c7', '#38bdf8', '#7dd3fc', '#bae6fd', '#e0f2fe']
        bg_color = colors[heat_level - 1]
        
        group_html += f'''
                <tr data-search="{member['name_cn']} {member['class']} {member['student_id']}">
                    <td>{member['order']}</td>
                    <td><span class="clickable-name" data-idx="{member['people_idx']}"><strong>{member['name_cn']}</strong></span><br><small>{member['name_en'][:20]}</small></td>
                    <td>{member['class']}</td>
                    <td>{member['student_id']}</td>
                    <td><span class="total-heat" style="background:{bg_color};">{int(total_score)}</span></td>
                    <td class="rank-cell">{member['medal']}</td>
                    <td><span class="{member['reward_class']}">{member['reward_status']}</span></td>
                </tr>'''
    
    group_html += '''
            </tbody>
        </table>
    </div>'''
    groups_html += group_html

# 替换
html = html.replace('<div class="rank-grid" id="rankGrid"></div>', f'<div class="rank-grid">{rank_cards_html}</div>')
html = html.replace('<div id="groups"></div>', groups_html)

# 在最后加上 bindNameClick 调用
html = html.replace('</body>', '<script>bindNameClick();</script></body>')

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n✅ 生成成功！共 {len(people)} 人")
print("\n📊 奖励统计:")
for g in ["星穹组", "夜曜组", "沧澜组"]:
    if g in group_data:
        members = group_data[g]
        pass_count = sum(1 for m in members if m["reward_status"] == "✅")
        print(f"  {g}: {pass_count}/{len(members)} 人达标")
