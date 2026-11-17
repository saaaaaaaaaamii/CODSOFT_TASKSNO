# CodSoft Web Development Internship — Level 1 Project Suite

Welcome to the **CodSoft Web Development Virtual Internship (Level 1)** project repository. This repository contains the complete source code, responsive designs, and interactive implementations for all three Level 1 tasks.

---

## 🚀 Projects Overview

| Task # | Project Name | Technologies | Key Features |
| :--- | :--- | :--- | :--- |
| **Task 1** | [Personal Developer Portfolio](./task-1-portfolio/) | HTML5, CSS3, JS (ES6+) | Dark/Light Mode, Skill Meters, Category Filters, PDF Resume Download, Contact Form Validation |
| **Task 2** | [NovaCloud SaaS Landing Page](./task-2-landing-page/) | HTML5, CSS3 (Grid & Flexbox), JS | Multi-column layouts, Interactive Monthly/Annual Pricing switch, FAQ Accordion, Sticky Navbar |
| **Task 3** | [Interactive CSS Grid Calculator](./task-3-calculator/) | HTML5, CSS3 Grid, JavaScript Engine | CSS Grid layout, Keyboard typing support, Calculation history log, Sound synthesis, Precision math |

---

## 📁 Repository Directory Structure

```text
CODSOFT_TASKSNO/
├── index.html                      # Central Showcase Hub & Live Interactive Previewer
├── README.md                       # Comprehensive Project Documentation (This File)
│
├── task-1-portfolio/               # TASK 1: Personal Portfolio
│   ├── index.html                  # Semantic HTML5 Structure
│   ├── style.css                   # Responsive CSS3 with custom variables & themes
│   ├── script.js                   # Interactive theme toggle, filter, form validation
│   └── assets/
│       ├── avatar.svg              # Developer profile vector illustration
│       ├── resume.pdf              # Verified standard PDF resume
│       └── projects/               # Scalable project thumbnails
│
├── task-2-landing-page/            # TASK 2: Landing Page
│   ├── index.html                  # Multi-column semantic SaaS layout
│   ├── style.css                   # Grid & Flexbox layouts, animations, responsive design
│   ├── script.js                   # Pricing plan calculator & FAQ accordion logic
│   └── assets/
│       └── hero-dashboard.svg      # High-tech vector dashboard preview
│
└── task-3-calculator/              # TASK 3: Interactive Calculator
    ├── index.html                  # Calculator structure & dual display screen
    ├── style.css                   # CSS Grid button arrangement & neumorphic styling
    └── script.js                   # Event listeners, loops, operators, audio feedback
```

---

## 🛠️ Task 1: Personal Portfolio Details
- **Header Section:** Dynamic logo, navigation links (Home, About, Skills, Projects, Resume, Contact), and instant Light/Dark mode switcher.
- **About Section:** Developer profile vector avatar, concise biography, core values, and metric counters.
- **Skills Section:** Technical competencies grouped into Frontend, Frameworks, and Tools with animated proficiency bars.
- **Projects Section:** Card grid showcasing projects with live demo links, source links, and category filter buttons.
- **Resume Section:** Career highlights timeline and 1-click verified PDF download button.
- **Contact Section:** Direct contact information (email, phone, location) alongside a validated client-side contact form.
- **Footer:** Copyright notice, quick links, and floating back-to-top button.

---

## 🌐 Task 2: NovaCloud Landing Page Details
- **Clean Sectional Divisions:** Structured columns, card boxes, and balanced whitespace without overlapping elements.
- **Hero Banner:** Compelling value proposition, email trial signup form, and dashboard illustration.
- **Interactive Pricing Switch:** Toggle between Monthly and Annual billing (with real-time 20% discount calculation).
- **Feature Grid:** 6-card grid with responsive layouts highlighting modern cloud capabilities.
- **Social Proof:** Testimonials with 5-star ratings and enterprise partner trust bar.
- **FAQ Accordion:** Expandable questions and answers with smooth transition animations.

---

## 🧮 Task 3: Interactive CSS Grid Calculator Details
- **CSS Grid Layout:** Perfectly aligned button matrix using `display: grid; grid-template-columns: repeat(4, 1fr)`.
- **Display Screen:** Dual-row screen displaying the active expression, operator indicator, and primary numerical result.
- **Arithmetic Engine:** Addition (`+`), subtraction (`-`), multiplication (`×`), and division (`÷`) with zero-division error handling and floating point rounding.
- **Input Handling:** Both mouse click event listeners (bound via loops) and full keyboard shortcuts (`0-9`, `+`, `-`, `*`, `/`, `Enter`, `Backspace`, `Esc`).
- **History Log:** Dedicated calculation history drawer allowing users to review and restore previous answers.
- **Audio Synthesis:** Optional tactile click sound powered by the Web Audio API.

---

## ⚡ How to Run Locally

You can run this project locally without any dependencies or external servers:

### Option 1: Direct File Opening
Double click `index.html` in your file explorer to open the Master Showcase Hub in any modern web browser (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari).

### Option 2: Local HTTP Server (Python)
If you have Python installed, open your terminal inside the project directory and run:
```bash
python -m http.server 8000
```
Then visit:
```
http://localhost:8000
```

---

## 📝 CodSoft Submission Checklist

- [x] **Repository Naming:** Repo named according to CodSoft guidelines (`CODSOFT_TASKSNO` / `CODSOFT_LEVEL1`).
- [x] **Level 1 Tasks Completed:** All 3 tasks implemented, tested, and fully working.
- [x] **LinkedIn Video Demonstration:**
  - Record a short 1–2 minute screen demo showing the portfolio, landing page, and calculator in action.
  - Tag `@CodSoft` on LinkedIn.
  - Use hashtags: `#codsoft` `#internship` `#webdevelopment`.
- [x] **Submission Form:** Submit the repository URL and LinkedIn post link via the official CodSoft submission form.

---

**Developed with ❤️ by Samik for the CodSoft Web Development Virtual Internship.**
