import os
import glob
from datetime import date

BASE_URL = "https://bakulemas.com"
BLOG_DIR = "./blog"  # sesuaikan dengan lokasi folder blog di komputer kamu

# Halaman utama (non-blog)
static_pages = [
    {"loc": "/", "priority": "1.0"},
    {"loc": "/blog/", "priority": "0.8"},
]

# Auto-detect semua artikel blog
blog_files = sorted(glob.glob(os.path.join(BLOG_DIR, "*.html")))
blog_pages = []
for f in blog_files:
    filename = os.path.basename(f)
    if filename == "index.html":
        continue  # sudah dihandle di static_pages
    slug = filename.replace(".html", "")
    blog_pages.append({
        "loc": f"/blog/{slug}.html",
        "priority": "0.7"
    })

# Gabungkan semua halaman
all_pages = static_pages + blog_pages
today = date.today().isoformat()

# Generate XML
lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for page in all_pages:
    lines.append("  <url>")
    lines.append(f"    <loc>{BASE_URL}{page['loc']}</loc>")
    lines.append(f"    <lastmod>{today}</lastmod>")
    lines.append(f"    <priority>{page['priority']}</priority>")
    lines.append("  </url>")

lines.append("</urlset>")

sitemap_content = "\n".join(lines)

# Simpan ke sitemap.xml
output_path = "./sitemap.xml"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"✅ sitemap.xml berhasil dibuat! ({len(all_pages)} URL)")
print(f"📄 Isi sitemap:")
print(sitemap_content)
