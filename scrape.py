import json
from bs4 import BeautifulSoup
import csv

html_file = "leetcode_page.html"  # path to your saved HTML file

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Extract embedded JSON
data_tag = soup.find("script", {"id": "__NEXT_DATA__"})
data = json.loads(data_tag.string)

# Navigate to study plan data
plan_data = data["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["studyPlanV2Detail"]
groups = plan_data["planSubGroups"]

problems = []

for group in groups:
    group_name = group["name"]
    for q in group["questions"]:
        qid = q.get("id")
        frontend_id = q.get("questionFrontendId")

        # Warn if mismatch
        if str(qid) != str(frontend_id):
            print(f"⚠️ ID mismatch in group '{group_name}': id={qid}, questionFrontendId={frontend_id}, title={q.get('title')}")

        problems.append({
            "group": group_name,
            "frontend_id": frontend_id,
            "title_cn": q.get("translatedTitle"),
            "title_en": q.get("title"),
            "difficulty": q.get("difficulty"),
        })

# Print preview
for p in problems[:10]:
    print(f"[{p['group']}] {p['frontend_id']} - {p['title_cn']} ({p['title_en']}) [{p['difficulty']}]")

print(f"\nTotal problems parsed: {len(problems)}")

# Save to CSV
with open("leetcode_top150.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["group", "frontend_id", "title_cn", "title_en", "difficulty"])
    writer.writeheader()
    writer.writerows(problems)
