#!/usr/bin/env python3
"""
Obsidian知识库搜索索引生成器
用法: python3 regenerate_index.py
"""

import os
import re
import json
from datetime import datetime

SPACE_DIR = "/Users/steven.sun/Desktop/🧠 史蒂芬的空间站"
OUTPUT_DIR = "/Users/steven.sun/WorkBuddy/2026-05-26-09-53-04"

def generate_index():
    search_index = []
    
    for root, dirs, files in os.walk(SPACE_DIR):
        for f in files:
            if f.endswith('.md'):
                fp = os.path.join(root, f)
                rel_path = os.path.relpath(fp, SPACE_DIR)
                
                try:
                    with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
                        content = file.read()
                        
                        # Extract title
                        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                        title = title_match.group(1).strip() if title_match else f.replace('.md', '')
                        
                        # Extract tags
                        tags = []
                        fm_tags = re.findall(r'^tags:\s*(.+)$', content, re.MULTILINE)
                        for t in fm_tags:
                            tags.extend(re.findall(r'[\w\u4e00-\u9fff]+', t))
                        
                        inline_tags = re.findall(r'#([\w\u4e00-\u9fff]+)', content)
                        tags.extend(inline_tags)
                        tags = list(set(tags))
                        
                        # Extract headings
                        headings = re.findall(r'^#{1,3}\s+(.+)$', content, re.MULTILINE)
                        
                        # Extract summary
                        paragraphs = re.findall(r'\n\n([^#\n].{50,500})', content)
                        summary = paragraphs[0].strip() if paragraphs else ""
                        
                        search_index.append({
                            "path": rel_path,
                            "title": title,
                            "tags": tags,
                            "headings": headings[:10],
                            "summary": summary[:200],
                            "word_count": len(content.split()),
                            "has_frontmatter": content.startswith('---')
                        })
                except:
                    pass
    
    # Save JSON
    output_path = os.path.join(OUTPUT_DIR, "obsidian_search_index.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)
    
    print(f"Index regenerated: {output_path}")
    print(f"Total notes: {len(search_index)}")

if __name__ == "__main__":
    generate_index()
