import os

assets_dir = r"C:\Users\samik\.gemini\antigravity\scratch\codsoft-level-1\task-1-portfolio\assets"
projects_dir = os.path.join(assets_dir, "projects")
os.makedirs(projects_dir, exist_ok=True)

# 1. Avatar SVG
avatar_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5" />
      <stop offset="100%" stop-color="#06b6d4" />
    </linearGradient>
    <linearGradient id="skinGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fcd34d" />
      <stop offset="100%" stop-color="#f59e0b" />
    </linearGradient>
    <linearGradient id="hairGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <linearGradient id="hoodieGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#4f46e5" flood-opacity="0.35"/>
    </filter>
  </defs>
  <!-- Background Circle with glow -->
  <circle cx="120" cy="120" r="105" fill="url(#bgGrad)" filter="url(#glow)"/>
  
  <!-- Outer Tech Ring -->
  <circle cx="120" cy="120" r="114" fill="none" stroke="#60a5fa" stroke-width="2.5" stroke-dasharray="8 6" opacity="0.6"/>
  
  <!-- Hoodie / Shoulders -->
  <path d="M 45 220 Q 120 160 195 220 Z" fill="url(#hoodieGrad)"/>
  <path d="M 98 175 L 120 220 L 142 175 Z" fill="#1e40af" opacity="0.6"/>
  
  <!-- Neck -->
  <rect x="106" y="140" width="28" height="25" rx="5" fill="#f59e0b"/>
  
  <!-- Face -->
  <rect x="80" y="75" width="80" height="85" rx="40" fill="url(#skinGrad)"/>
  
  <!-- Hair -->
  <path d="M 75 90 C 70 50 170 50 165 90 C 155 65 85 65 75 90 Z" fill="url(#hairGrad)"/>
  <path d="M 72 90 C 65 105 70 120 75 125 C 75 105 78 95 82 90 Z" fill="url(#hairGrad)"/>
  <path d="M 168 90 C 175 105 170 120 165 125 C 165 105 162 95 158 90 Z" fill="url(#hairGrad)"/>
  
  <!-- Modern Glasses -->
  <rect x="82" y="98" width="32" height="22" rx="6" fill="#0f172a" fill-opacity="0.8" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="126" y="98" width="32" height="22" rx="6" fill="#0f172a" fill-opacity="0.8" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="114" y1="108" x2="126" y2="108" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="72" y1="105" x2="82" y2="108" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="158" y1="108" x2="168" y2="105" stroke="#38bdf8" stroke-width="2.5"/>
  
  <!-- Smiling Mouth -->
  <path d="M 106 138 Q 120 148 134 138" fill="none" stroke="#b45309" stroke-width="3" stroke-linecap="round"/>
  
  <!-- Floating Code Badges -->
  <g transform="translate(18, 55)">
    <rect width="48" height="22" rx="11" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="24" y="15" font-family="sans-serif" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">&lt;dev/&gt;</text>
  </g>
  <g transform="translate(175, 145)">
    <rect width="46" height="22" rx="11" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="23" y="15" font-family="sans-serif" font-size="10" font-weight="bold" fill="#c084fc" text-anchor="middle">JS/TS</text>
  </g>
</svg>"""

with open(os.path.join(assets_dir, "avatar.svg"), "w", encoding="utf-8") as f:
    f.write(avatar_svg)

# 2. Project 1: Portfolio Showcase
proj1_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
  <defs>
    <linearGradient id="p1bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b" />
      <stop offset="100%" stop-color="#312e81" />
    </linearGradient>
  </defs>
  <rect width="600" height="360" rx="16" fill="url(#p1bg)"/>
  <!-- Browser window mockup -->
  <rect x="40" y="30" width="520" height="300" rx="12" fill="#0f172a" stroke="#4338ca" stroke-width="2"/>
  <circle cx="65" cy="50" r="5" fill="#ef4444"/>
  <circle cx="82" cy="50" r="5" fill="#f59e0b"/>
  <circle cx="99" cy="50" r="5" fill="#10b981"/>
  <rect x="120" y="42" width="280" height="16" rx="8" fill="#1e293b"/>
  <!-- Content inside window -->
  <rect x="70" y="80" width="180" height="20" rx="6" fill="#818cf8"/>
  <rect x="70" y="110" width="240" height="12" rx="4" fill="#94a3b8" opacity="0.6"/>
  <rect x="70" y="130" width="190" height="12" rx="4" fill="#94a3b8" opacity="0.4"/>
  <!-- Avatar mock -->
  <circle cx="430" cy="140" r="55" fill="#4f46e5" stroke="#818cf8" stroke-width="3"/>
  <circle cx="430" cy="125" r="22" fill="#e0e7ff"/>
  <path d="M 395 175 Q 430 150 465 175" fill="#c7d2fe"/>
  <!-- Cards row -->
  <rect x="70" y="180" width="130" height="110" rx="8" fill="#1e293b" stroke="#334155"/>
  <rect x="220" y="180" width="130" height="110" rx="8" fill="#1e293b" stroke="#334155"/>
  <rect x="370" y="215" width="150" height="75" rx="8" fill="#4338ca" fill-opacity="0.3" stroke="#6366f1"/>
  <text x="300" y="320" font-family="sans-serif" font-size="14" font-weight="bold" fill="#a5b4fc" text-anchor="middle">Personal Portfolio Website</text>
</svg>"""

with open(os.path.join(projects_dir, "project1.svg"), "w", encoding="utf-8") as f:
    f.write(proj1_svg)

# 3. Project 2: Landing Page Showcase
proj2_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
  <defs>
    <linearGradient id="p2bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
  </defs>
  <rect width="600" height="360" rx="16" fill="url(#p2bg)"/>
  <!-- Browser window mockup -->
  <rect x="40" y="30" width="520" height="300" rx="12" fill="#0b132b" stroke="#0ea5e9" stroke-width="2"/>
  <circle cx="65" cy="50" r="5" fill="#ef4444"/>
  <circle cx="82" cy="50" r="5" fill="#f59e0b"/>
  <circle cx="99" cy="50" r="5" fill="#10b981"/>
  <!-- Nav header -->
  <rect x="65" y="70" width="80" height="18" rx="4" fill="#38bdf8"/>
  <rect x="360" y="72" width="40" height="12" rx="3" fill="#94a3b8"/>
  <rect x="415" y="72" width="40" height="12" rx="3" fill="#94a3b8"/>
  <rect x="470" y="68" width="70" height="22" rx="11" fill="#0284c7"/>
  <!-- Hero banner -->
  <rect x="65" y="115" width="260" height="28" rx="6" fill="#ffffff"/>
  <rect x="65" y="155" width="220" height="12" rx="4" fill="#7dd3fc"/>
  <rect x="65" y="175" width="180" height="12" rx="4" fill="#7dd3fc" opacity="0.7"/>
  <rect x="65" y="205" width="110" height="32" rx="6" fill="#0ea5e9"/>
  <!-- Hero graphic -->
  <circle cx="430" cy="165" r="50" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="430,130 460,185 400,185" fill="#38bdf8" opacity="0.8"/>
  <!-- Pricing columns -->
  <rect x="65" y="255" width="145" height="60" rx="6" fill="#1e293b"/>
  <rect x="225" y="255" width="145" height="60" rx="6" fill="#0284c7" stroke="#38bdf8"/>
  <rect x="385" y="255" width="145" height="60" rx="6" fill="#1e293b"/>
  <text x="300" y="340" font-family="sans-serif" font-size="14" font-weight="bold" fill="#bae6fd" text-anchor="middle">NovaCloud SaaS Landing Page</text>
</svg>"""

with open(os.path.join(projects_dir, "project2.svg"), "w", encoding="utf-8") as f:
    f.write(proj2_svg)

# 4. Project 3: Calculator Showcase
proj3_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
  <defs>
    <linearGradient id="p3bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#18181b" />
      <stop offset="100%" stop-color="#27272a" />
    </linearGradient>
  </defs>
  <rect width="600" height="360" rx="16" fill="url(#p3bg)"/>
  <!-- Calculator Device body -->
  <rect x="180" y="30" width="240" height="300" rx="20" fill="#09090b" stroke="#3f3f46" stroke-width="3"/>
  <!-- Screen -->
  <rect x="200" y="55" width="200" height="65" rx="10" fill="#18181b" stroke="#27272a"/>
  <text x="385" y="80" font-family="monospace" font-size="13" fill="#71717a" text-anchor="end">1,240 × 8.5</text>
  <text x="385" y="108" font-family="monospace" font-size="24" font-weight="bold" fill="#10b981" text-anchor="end">10,540</text>
  <!-- Buttons Grid (4 cols, 4 rows) -->
  <!-- Row 1 -->
  <rect x="200" y="135" width="42" height="35" rx="8" fill="#ef4444"/>
  <rect x="252" y="135" width="42" height="35" rx="8" fill="#3f3f46"/>
  <rect x="304" y="135" width="42" height="35" rx="8" fill="#3f3f46"/>
  <rect x="356" y="135" width="42" height="35" rx="8" fill="#f59e0b"/>
  <!-- Row 2 -->
  <rect x="200" y="180" width="42" height="35" rx="8" fill="#27272a"/>
  <rect x="252" y="180" width="42" height="35" rx="8" fill="#27272a"/>
  <rect x="304" y="180" width="42" height="35" rx="8" fill="#27272a"/>
  <rect x="356" y="180" width="42" height="35" rx="8" fill="#f59e0b"/>
  <!-- Row 3 -->
  <rect x="200" y="225" width="42" height="35" rx="8" fill="#27272a"/>
  <rect x="252" y="225" width="42" height="35" rx="8" fill="#27272a"/>
  <rect x="304" y="225" width="42" height="35" rx="8" fill="#27272a"/>
  <rect x="356" y="225" width="42" height="35" rx="8" fill="#f59e0b"/>
  <!-- Row 4 -->
  <rect x="200" y="270" width="42" height="35" rx="8" fill="#27272a"/>
  <rect x="252" y="270" width="42" height="35" rx="8" fill="#27272a"/>
  <rect x="304" y="270" width="94" height="35" rx="8" fill="#10b981"/>
  <text x="300" y="345" font-family="sans-serif" font-size="14" font-weight="bold" fill="#e4e4e7" text-anchor="middle">Interactive CSS Grid Calculator</text>
</svg>"""

with open(os.path.join(projects_dir, "project3.svg"), "w", encoding="utf-8") as f:
    f.write(proj3_svg)

# 5. Project 4: E-Commerce Showcase
proj4_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
  <defs>
    <linearGradient id="p4bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#311042" />
      <stop offset="100%" stop-color="#581c87" />
    </linearGradient>
  </defs>
  <rect width="600" height="360" rx="16" fill="url(#p4bg)"/>
  <!-- Browser window mockup -->
  <rect x="40" y="30" width="520" height="300" rx="12" fill="#1e102d" stroke="#a855f7" stroke-width="2"/>
  <circle cx="65" cy="50" r="5" fill="#ef4444"/>
  <circle cx="82" cy="50" r="5" fill="#f59e0b"/>
  <circle cx="99" cy="50" r="5" fill="#10b981"/>
  <!-- Nav & Cart -->
  <rect x="65" y="70" width="100" height="16" rx="4" fill="#c084fc"/>
  <rect x="480" y="66" width="60" height="24" rx="12" fill="#9333ea"/>
  <!-- Product Cards -->
  <rect x="65" y="105" width="140" height="150" rx="8" fill="#2e1065" stroke="#7e22ce"/>
  <rect x="75" y="115" width="120" height="70" rx="6" fill="#a855f7" opacity="0.3"/>
  <rect x="75" y="195" width="90" height="12" rx="3" fill="#f3e8ff"/>
  <rect x="75" y="215" width="50" height="12" rx="3" fill="#34d399"/>
  <rect x="75" y="235" width="120" height="15" rx="4" fill="#9333ea"/>

  <rect x="225" y="105" width="140" height="150" rx="8" fill="#2e1065" stroke="#7e22ce"/>
  <rect x="235" y="115" width="120" height="70" rx="6" fill="#ec4899" opacity="0.3"/>
  <rect x="235" y="195" width="90" height="12" rx="3" fill="#f3e8ff"/>
  <rect x="235" y="215" width="50" height="12" rx="3" fill="#34d399"/>
  <rect x="235" y="235" width="120" height="15" rx="4" fill="#ec4899"/>

  <rect x="385" y="105" width="140" height="150" rx="8" fill="#2e1065" stroke="#7e22ce"/>
  <rect x="395" y="115" width="120" height="70" rx="6" fill="#6366f1" opacity="0.3"/>
  <rect x="395" y="195" width="90" height="12" rx="3" fill="#f3e8ff"/>
  <rect x="395" y="215" width="50" height="12" rx="3" fill="#34d399"/>
  <rect x="395" y="235" width="120" height="15" rx="4" fill="#6366f1"/>

  <text x="300" y="325" font-family="sans-serif" font-size="14" font-weight="bold" fill="#f3e8ff" text-anchor="middle">ShopSphere Modern E-Commerce</text>
</svg>"""

with open(os.path.join(projects_dir, "project4.svg"), "w", encoding="utf-8") as f:
    f.write(proj4_svg)

print("All SVGs created successfully!")
