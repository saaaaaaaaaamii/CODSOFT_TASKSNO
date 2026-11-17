import os

# We can generate a clean, valid standard PDF file directly
def create_pdf(filename):
    # Minimal standard PDF 1.4 generator with text content
    content_stream = b"""BT
/F1 22 Tf
50 780 Td
(SAMIK - FULL STACK WEB DEVELOPER) Tj
/F2 11 Tf
0 -22 Td
(Email: contact@codsoft.in | GitHub: github.com/samik | LinkedIn: linkedin.com/in/samik) Tj
0 -15 Td
(--------------------------------------------------------------------------------------------------------------------) Tj
/F1 14 Tf
0 -25 Td
(PROFILE SUMMARY) Tj
/F2 10 Tf
0 -18 Td
(Passionate and detail-oriented Web Developer with solid expertise in modern HTML5, CSS3, JavaScript,) Tj
0 -14 Td
(Responsive Design, UI/UX engineering, and Full-Stack foundations. Proven track record of building robust,) Tj
0 -14 Td
(accessible, and high-performance web applications during the CodSoft Web Development Internship.) Tj
/F1 14 Tf
0 -25 Td
(TECHNICAL SKILLS) Tj
/F2 10 Tf
0 -18 Td
(- Frontend: HTML5, CSS3 (Grid & Flexbox), JavaScript (ES6+), React.js, Tailwind CSS, Bootstrap) Tj
0 -14 Td
(- Backend & APIs: Node.js, Express.js, RESTful API Design, MongoDB, PostgreSQL) Tj
0 -14 Td
(- Tools & Practices: Git, GitHub, VS Code, Responsive Web Design, Web Performance Optimization) Tj
/F1 14 Tf
0 -25 Td
(INTERNSHIP & PROJECTS) Tj
/F1 11 Tf
0 -18 Td
(CodSoft Web Development Internship | Level 1 Web Projects) Tj
/F2 10 Tf
0 -15 Td
(* Task 1 - Personal Portfolio: Fully responsive developer showcase with Dark/Light mode & resume preview.) Tj
0 -14 Td
(* Task 2 - SaaS Landing Page: Modern responsive product page featuring pricing switch, FAQ, and grid layout.) Tj
0 -14 Td
(* Task 3 - Interactive Calculator: High-precision calculator built with CSS Grid and event-driven JS engine.) Tj
/F1 14 Tf
0 -25 Td
(EDUCATION) Tj
/F1 11 Tf
0 -18 Td
(Bachelor of Technology in Computer Science & Engineering) Tj
/F2 10 Tf
0 -14 Td
(Expected Graduation: 2026 | Relevant Coursework: Web Technologies, DBMS, Software Engineering) Tj
/F1 14 Tf
0 -25 Td
(CERTIFICATIONS & ACHIEVEMENTS) Tj
/F2 10 Tf
0 -18 Td
(- CodSoft Web Development Virtual Internship Certificate) Tj
0 -14 Td
(- Modern Web Development & Responsive Design Specialist) Tj
ET"""

    stream_len = len(content_stream)
    
    pdf_bytes = bytearray()
    pdf_bytes.extend(b"%PDF-1.4\n")
    
    offsets = []
    
    def add_object(obj_num, data):
        offsets.append(len(pdf_bytes))
        pdf_bytes.extend(f"{obj_num} 0 obj\n".encode('ascii'))
        pdf_bytes.extend(data)
        pdf_bytes.extend(b"\nendobj\n")

    # Obj 1: Catalog
    add_object(1, b"<< /Type /Catalog /Pages 2 0 R >>")
    # Obj 2: Pages
    add_object(2, b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    # Obj 3: Page
    add_object(3, b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 842] /Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>")
    # Obj 4: Contents
    add_object(4, f"<< /Length {stream_len} >>\nstream\n".encode('ascii') + content_stream + b"\nendstream")
    # Obj 5: Font Helvetica-Bold
    add_object(5, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
    # Obj 6: Font Helvetica
    add_object(6, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

    xref_pos = len(pdf_bytes)
    pdf_bytes.extend(f"xref\n0 7\n0000000000 65535 f \n".encode('ascii'))
    for off in offsets:
        pdf_bytes.extend(f"{off:010d} 00000 n \n".encode('ascii'))
    
    pdf_bytes.extend(f"trailer\n<< /Size 7 /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode('ascii'))

    with open(filename, 'wb') as f:
        f.write(pdf_bytes)
    print(f"Generated {filename} successfully ({len(pdf_bytes)} bytes)")

if __name__ == '__main__':
    target = r"C:\Users\samik\.gemini\antigravity\scratch\codsoft-level-1\task-1-portfolio\assets\resume.pdf"
    create_pdf(target)
