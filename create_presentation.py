import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation(output_path):
    prs = Presentation()
    # 16:9 widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette - Professional Corporate Navy & Amber Accents (Zero Emojis)
    BG_DARK = RGBColor(12, 20, 36)        # Deep Slate Navy
    BG_CARD = RGBColor(20, 32, 54)        # Card Slate
    TEXT_LIGHT = RGBColor(241, 245, 249)  # Off-white / light slate
    TEXT_MUTED = RGBColor(148, 163, 184)  # Cool grey
    ACCENT_AMBER = RGBColor(245, 158, 11) # Warm Amber / Gold
    ACCENT_BLUE = RGBColor(56, 189, 248)  # Sky blue
    ACCENT_RED = RGBColor(239, 68, 68)    # Crimson red
    BORDER_COLOR = RGBColor(39, 55, 85)   # Border subtle

    def set_slide_background(slide, color=BG_DARK):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="EUROPEAN BANKING ANALYTICS"):
        # Header container
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(1.0))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0)
        tf.margin_top = Inches(0)
        
        # Category / Kicker
        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_AMBER
        p_cat.font.name = "Calibri"

        # Main Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_LIGHT
        p_title.font.name = "Calibri"
        p_title.space_before = Pt(4)

        # Subtle divider
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.02))
        div.fill.solid()
        div.fill.fore_color.rgb = BORDER_COLOR
        div.line.fill.background()

    def add_card(slide, left, top, width, height, bg_color=BG_CARD):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1)
        return card

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # Topic Name & Presenter: Panchaksharayya
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1, RGBColor(8, 14, 26))

    # Center card / frame
    add_card(slide1, Inches(1.0), Inches(1.0), Inches(11.333), Inches(5.5), bg_color=RGBColor(15, 24, 42))

    tbox1 = slide1.shapes.add_textbox(Inches(1.5), Inches(1.4), Inches(10.333), Inches(4.7))
    tf1 = tbox1.text_frame
    tf1.word_wrap = True
    tf1.vertical_anchor = MSO_ANCHOR.MIDDLE

    p = tf1.paragraphs[0]
    p.text = "EXECUTIVE RESEARCH REPORT & QUANTITATIVE ANALYTICS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.font.name = "Calibri"
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "Customer Segmentation and Churn Pattern Analytics in European Banking"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.font.name = "Calibri"
    p.space_after = Pt(12)

    p = tf1.add_paragraph()
    p.text = "Empirical Analysis of Depositor Attrition, Demographic Vulnerabilities, and Capital Balance Flight Across 10,000 European Retail Accounts"
    p.font.size = Pt(15)
    p.font.color.rgb = TEXT_MUTED
    p.font.name = "Calibri"
    p.space_after = Pt(28)

    # Author Metadata
    p = tf1.add_paragraph()
    p.text = "Author / Lead Analyst: Panchaksharayya"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.font.name = "Calibri"
    p.space_after = Pt(4)

    p = tf1.add_paragraph()
    p.text = "Institutional Affiliation: Quantitative Banking Analytics and Financial Risk Advisory | September 2026"
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_MUTED
    p.font.name = "Calibri"

    # ==========================================
    # SLIDE 2: EXECUTIVE SUMMARY & OBJECTIVES
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "Executive Summary and Project Objectives")

    # Card 1: Context & Problem
    add_card(slide2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    tb2a = slide2.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.5))
    tf2a = tb2a.text_frame
    tf2a.word_wrap = True
    p = tf2a.paragraphs[0]
    p.text = "Industry Context and Strategic Challenge"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(12)

    points2a = [
        ("Rising Attrition in European Retail Banking", "Open Banking regulations (PSD2/PSD3) and aggressive fintech challenger banks have lowered account migration friction across the Eurozone."),
        ("The Limitations of Aggregate Metrics", "Standard enterprise reporting tracks aggregate churn (~20%), obscuring catastrophic flight within ultra-profitable micro-segments."),
        ("Balance Sheet and Liquidity Impact", "Customer attrition destroys Customer Lifetime Value (CLV), inflates replacement customer acquisition costs by 5x to 7x, and drains core deposit stability under Basel III Liquidity Coverage Ratio (LCR) guidelines.")
    ]
    for title, desc in points2a:
        p = tf2a.add_paragraph()
        p.text = f"- {title}: "
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(8)

    # Card 2: Research Objectives
    add_card(slide2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb2b = slide2.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf2b = tb2b.text_frame
    tf2b.word_wrap = True
    p = tf2b.paragraphs[0]
    p.text = "Primary Research and Analytical Scope"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(12)

    points2b = [
        ("Empirical Baseline Quantification", "Conduct an exhaustive audit of 10,000 retail banking accounts across France, Germany, and Spain to establish empirical churn baselines."),
        ("Multi-Dimensional Segmentation", "Evaluate intersecting customer profiles spanning Geography, Age, Gender, Balance Tiers, Digital Engagement, and Product Breadth."),
        ("Capital Exposure Modeling", "Quantify exact Euro-denominated liquidity flight across high-balance account tiers rather than relying strictly on account counts."),
        ("Operational Deployment", "Formulate a concrete 4-Pillar Strategic Retention Playbook and deploy an interactive production scoring engine.")
    ]
    for title, desc in points2b:
        p = tf2b.add_paragraph()
        p.text = f"- {title}: "
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(8)

    # ==========================================
    # SLIDE 3: DATASET ARCHITECTURE & OVERVIEW
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "Dataset Architecture and Exploratory Portfolio Overview")

    # 4 Top KPI Cards
    kpis = [
        ("Total Depositor Records", "10,000", "Audited retail accounts", ACCENT_BLUE),
        ("Overall Churn Rate", "20.37%", "2,037 exited depositors", ACCENT_RED),
        ("Total Retained Cohort", "79.63%", "7,963 active depositors", ACCENT_AMBER),
        ("Portfolio Balance Audited", "EUR 764.86M", "Mean: EUR 76,486", TEXT_LIGHT)
    ]
    for i, (title, val, sub, col) in enumerate(kpis):
        left = Inches(0.8 + i * 2.95)
        add_card(slide3, left, Inches(1.8), Inches(2.8), Inches(1.5))
        tb = slide3.shapes.add_textbox(left + Inches(0.15), Inches(1.9), Inches(2.5), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title.upper()
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = TEXT_MUTED
        p = tf.add_paragraph()
        p.text = val
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = col
        p = tf.add_paragraph()
        p.text = sub
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED

    # Bottom Split Cards
    add_card(slide3, Inches(0.8), Inches(3.6), Inches(5.6), Inches(3.2))
    tb3a = slide3.shapes.add_textbox(Inches(1.1), Inches(3.8), Inches(5.0), Inches(2.8))
    tf3a = tb3a.text_frame
    tf3a.word_wrap = True
    p = tf3a.paragraphs[0]
    p.text = "Key Feature Dimensions Evaluated"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(8)

    features = [
        "Demographic Attributes: Age (18 to 92), Gender (54.6% Male, 45.4% Female).",
        "Geographic Jurisdictions: France (5,014), Germany (2,509), Spain (2,477).",
        "Credit Risk Profile: Credit Score ranging from 350 to 850 (Mean: 650.5).",
        "Relationship Tenure: Customer tenure spans from 0 to 10 years (Mean: 5.0).",
        "Banking Product Density: Holding between 1 and 4 institutional products."
    ]
    for feat in features:
        p = tf3a.add_paragraph()
        p.text = f"- {feat}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(4)

    add_card(slide3, Inches(6.8), Inches(3.6), Inches(5.7), Inches(3.2))
    tb3b = slide3.shapes.add_textbox(Inches(7.1), Inches(3.8), Inches(5.1), Inches(2.8))
    tf3b = tb3b.text_frame
    tf3b.word_wrap = True
    p = tf3b.paragraphs[0]
    p.text = "Exploratory Data Integrity & Validation"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(8)

    validations = [
        "Zero Missing Values: Full completeness across all 10,000 rows and 14 raw variables.",
        "Zero-Balance Depositor Cohort: 36.17% (3,617 accounts) maintain 0.00 EUR balance (predominantly in France and Spain).",
        "Identity Sanitization: CustomerId and Surname decoupled from analytical modeling to maintain GDPR compliance.",
        "Target Balance: 20.37% exit proportion provides robust minority class representation without requiring artificial oversampling."
    ]
    for val in validations:
        p = tf3b.add_paragraph()
        p.text = f"- {val}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(4)

    # ==========================================
    # SLIDE 4: GEOGRAPHIC DISPARITIES - GERMAN ANOMALY
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "Geographic Variance and the German Attrition Anomaly")

    # 3 Country Comparison Columns
    countries = [
        ("FRANCE", "5,014 Accounts", "16.15%", "810 Exits", "0.79x", "Baseline Market", BG_CARD, TEXT_LIGHT),
        ("SPAIN", "2,477 Accounts", "16.67%", "413 Exits", "0.82x", "Stable Cohort", BG_CARD, TEXT_LIGHT),
        ("GERMANY", "2,509 Accounts", "32.44%", "814 Exits", "1.59x", "Critical Risk Zone", RGBColor(38, 20, 28), ACCENT_RED)
    ]
    for i, (name, base, rate, exits, gri, status, card_bg, stat_col) in enumerate(countries):
        left = Inches(0.8 + i * 3.95)
        add_card(slide4, left, Inches(1.8), Inches(3.8), Inches(2.5), bg_color=card_bg)
        tb = slide4.shapes.add_textbox(left + Inches(0.2), Inches(2.0), Inches(3.4), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = stat_col
        
        p = tf.add_paragraph()
        p.text = f"{base} | {status}"
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(8)

        p = tf.add_paragraph()
        p.text = f"Churn Rate: {rate}"
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = stat_col

        p = tf.add_paragraph()
        p.text = f"Total Attrition: {exits} | GRI: {gri}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED

    # Bottom Deep-Dive Card
    add_card(slide4, Inches(0.8), Inches(4.5), Inches(11.7), Inches(2.3))
    tb4 = slide4.shapes.add_textbox(Inches(1.1), Inches(4.65), Inches(11.1), Inches(2.0))
    tf4 = tb4.text_frame
    tf4.word_wrap = True
    p = tf4.paragraphs[0]
    p.text = "Root Drivers of the German Banking Disparity (GRI = 1.59x)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(6)

    german_drivers = [
        ("Volume Disproportion", "Germany contains only 25.09% of the customer base but accounts for 39.96% of all European churned depositors."),
        ("Interest Rate & Yield Sensitivity", "German retail depositors demonstrate rapid deposit reallocation toward high-yield digital neobanks (such as N26, Trade Republic, and ING DiBa)."),
        ("Compounded Demographic Risk", "German depositors aged 46 to 60 experience a staggering 67.33% churn rate, representing the single highest risk intersection in the entire dataset."),
        ("Operational Implication", "A uniform European retention strategy is inherently flawed. Germany requires a dedicated regional retention desk and tailored yield preservation offerings.")
    ]
    for title, desc in german_drivers:
        p = tf4.add_paragraph()
        p.text = f"- {title}: "
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(3)

    # ==========================================
    # SLIDE 5: DEMOGRAPHIC VULNERABILITIES (AGE 46-60)
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "Demographic Vulnerability and the Pre-Retirement Crisis")

    # Left: Age Breakdown Cards
    add_card(slide5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    tb5a = slide5.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.5))
    tf5a = tb5a.text_frame
    tf5a.word_wrap = True
    p = tf5a.paragraphs[0]
    p.text = "Churn Rate Distribution by Age Cohort"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(10)

    age_data = [
        ("Age 18 to 30 (Young Professionals)", "1,968 accounts", "7.52%", TEXT_LIGHT),
        ("Age 31 to 45 (Career Accumulators)", "6,032 accounts", "14.78%", TEXT_LIGHT),
        ("Age 46 to 60 (Pre-Retirement Decumulation)", "1,586 accounts", "51.12%", ACCENT_RED),
        ("Age 61 and Above (Retirees / Pensioners)", "414 accounts", "27.29%", ACCENT_AMBER)
    ]
    for cohort, vol, rate, col in age_data:
        p = tf5a.add_paragraph()
        p.text = f"{cohort}"
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = col
        p = tf5a.add_paragraph()
        p.text = f"Volume: {vol}  |  Observed Churn: {rate}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(6)

    # Right: Analytical Diagnosis
    add_card(slide5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb5b = slide5.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf5b = tb5b.text_frame
    tf5b.word_wrap = True
    p = tf5b.paragraphs[0]
    p.text = "Behavioral & Financial Drivers (Age 46-60)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(10)

    age_insights = [
        ("Peak Net Worth Phase", "Depositors aged 46 to 60 control peak career earnings, substantial mortgage equity, and major investment portfolios."),
        ("Pension & Decumulation Planning", "Approaching retirement creates demand for consolidated wealth advisory, private banking services, and estate planning—services retail branches fail to provide."),
        ("Heightened Fee Sensitivity", "Unlike younger digital customers who tolerate account maintenance fees, pre-retirees actively switch institutions to eliminate custodial drag."),
        ("Gender Disparity Finding", "Female depositors in this bracket churn at 56.4% compared to 45.8% for males, indicating unmet needs in advisory engagement.")
    ]
    for title, desc in age_insights:
        p = tf5b.add_paragraph()
        p.text = f"- {title}: "
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(6)

    # ==========================================
    # SLIDE 6: WEALTH TIER & CAPITAL FLIGHT
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "Wealth Tier Dynamics and Capital Exposure Analysis")

    # 3 Balance Tier Cards
    tiers = [
        ("ZERO-BALANCE COHORT", "EUR 0.00", "3,617 Accounts", "13.82%", "500 Exits", "EUR 0.00 Exposed", BG_CARD),
        ("MODERATE BALANCE", "EUR 1 - 119.8k", "3,883 Accounts", "23.87%", "927 Exits", "EUR 74.92M Exposed", BG_CARD),
        ("PREMIER CAPITAL TIER", ">= EUR 119.8k", "2,500 Accounts", "24.16%", "610 Exits", "EUR 110.85M Exposed", RGBColor(38, 20, 28))
    ]
    for i, (name, range_val, accs, rate, exits, exposed, bg) in enumerate(tiers):
        left = Inches(0.8 + i * 3.95)
        add_card(slide6, left, Inches(1.8), Inches(3.8), Inches(2.6), bg_color=bg)
        tb = slide6.shapes.add_textbox(left + Inches(0.2), Inches(1.95), Inches(3.4), Inches(2.3))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = ACCENT_AMBER
        
        p = tf.add_paragraph()
        p.text = f"Balance Range: {range_val}"
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(6)

        p = tf.add_paragraph()
        p.text = f"Capital Exposed: {exposed}"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = ACCENT_RED if i == 2 else TEXT_LIGHT

        p = tf.add_paragraph()
        p.text = f"Churn Rate: {rate} ({exits} departures)"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED

    # Bottom Analysis Card
    add_card(slide6, Inches(0.8), Inches(4.6), Inches(11.7), Inches(2.2))
    tb6 = slide6.shapes.add_textbox(Inches(1.1), Inches(4.75), Inches(11.1), Inches(1.9))
    tf6 = tb6.text_frame
    tf6.word_wrap = True
    p = tf6.paragraphs[0]
    p.text = "Systemic Liquidity and Balance Sheet Vulnerability"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(6)

    liquidity_points = [
        ("The Fallacy of Unweighted Churn", "Traditional head-count metrics treat a 0.00 EUR balance account departure identically to a 200,000 EUR wealth exit."),
        ("EUR 110.85M Flight in Top Quartile", "610 churned depositors held balances exceeding 119.8k EUR, pulling over 110.85 Million EUR in liquid deposits out of the institution."),
        ("LCR and Funding Stability Risk", "Under Basel III and ECB guidelines, rapid run-off of retail operational deposits strains short-term liquidity buffers and raises wholesale borrowing costs.")
    ]
    for title, desc in liquidity_points:
        p = tf6.add_paragraph()
        p.text = f"- {title}: "
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(3)

    # ==========================================
    # SLIDE 7: PRODUCT BUNDLING PARADOX & ENGAGEMENT
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "Digital Engagement and the Product Bundling Paradox")

    # Left: Product Breakdown
    add_card(slide7, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    tb7a = slide7.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.5))
    tf7a = tb7a.text_frame
    tf7a.word_wrap = True
    p = tf7a.paragraphs[0]
    p.text = "The Multi-Product Bundling Paradox"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(8)

    prod_data = [
        ("1 Product (Single Relationship)", "5,084 accounts", "27.71% Churn", TEXT_LIGHT),
        ("2 Products (Optimal Relationship)", "4,590 accounts", "7.58% Churn (Retained)", ACCENT_BLUE),
        ("3 Products (Severe Attrition)", "266 accounts", "82.71% Churn (Exited)", ACCENT_RED),
        ("4 Products (Complete Catastrophe)", "60 accounts", "100.00% Churn (60/60 Exited)", ACCENT_RED)
    ]
    for title, vol, churn, col in prod_data:
        p = tf7a.add_paragraph()
        p.text = f"{title}"
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = col
        p = tf7a.add_paragraph()
        p.text = f"Volume: {vol}  |  Performance: {churn}"
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(4)

    # Right: Engagement & Operational Drivers
    add_card(slide7, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb7b = slide7.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf7b = tb7b.text_frame
    tf7b.word_wrap = True
    p = tf7b.paragraphs[0]
    p.text = "Operational Explanation & Engagement Gap"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(8)

    bundle_drivers = [
        ("Why 3 & 4 Products Collapse", "Aggressive promotional cross-selling packages teaser-rate cards, credit lines, and insurance. When introductory discounts expire, accumulated multi-product fees trigger abrupt relationship cancellations."),
        ("Customer Fatigue & Administrative Friction", "Managing disparate statements, regulatory disclaimers, and conflicting account minimums generates negative customer sentiment."),
        ("Digital Engagement Dividend", "Active members (IsActiveMember=1) churn at 14.27% compared to 26.85% for inactive members—a 1.88x relative risk reduction."),
        ("Strategic Sweet Spot", "Maintaining 2 deeply integrated core products maximizes switching barriers without inducing fee fatigue.")
    ]
    for title, desc in bundle_drivers:
        p = tf7b.add_paragraph()
        p.text = f"- {title}: "
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(5)

    # ==========================================
    # SLIDE 8: MACHINE LEARNING & PREDICTIVE MODELING
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "Predictive Modeling and Machine Learning Benchmarks")

    # Top Table: Model Comparison
    add_card(slide8, Inches(0.8), Inches(1.8), Inches(11.7), Inches(2.4))
    tb8a = slide8.shapes.add_textbox(Inches(1.1), Inches(1.95), Inches(11.1), Inches(2.1))
    tf8a = tb8a.text_frame
    tf8a.word_wrap = True
    p = tf8a.paragraphs[0]
    p.text = "Model Evaluation on 80/20 Stratified Validation Split"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(6)

    models_data = [
        "Logistic Regression (Baseline): Accuracy 81.1%, ROC-AUC 0.768, Recall (Churn) 34.2%",
        "Random Forest Classifier: Accuracy 86.4%, ROC-AUC 0.852, Recall (Churn) 51.8%",
        "LightGBM Gradient Booster: Accuracy 86.9%, ROC-AUC 0.865, Recall (Churn) 54.6%",
        "XGBoost Classifier (Production): Accuracy 87.2%, ROC-AUC 0.871, Recall (Churn) 56.4%, F1-Score 0.638"
    ]
    for m in models_data:
        p = tf8a.add_paragraph()
        p.text = f"- {m}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(2)

    # Bottom 2 Cards: Feature Importance & Operational Triage
    add_card(slide8, Inches(0.8), Inches(4.4), Inches(5.6), Inches(2.4))
    tb8b = slide8.shapes.add_textbox(Inches(1.1), Inches(4.55), Inches(5.0), Inches(2.1))
    tf8b = tb8b.text_frame
    tf8b.word_wrap = True
    p = tf8b.paragraphs[0]
    p.text = "Top Model Feature Importance (SHAP / Gini)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(6)

    shap_features = [
        "1. Age (Weight: 0.28): Non-linear escalation between ages 45 and 60.",
        "2. Geography Germany (Weight: 0.21): Primary geographical exit predictor.",
        "3. Number of Products (Weight: 0.19): Severe cliff at 3+ products.",
        "4. Account Balance (Weight: 0.17): Flight concentration in top quartile.",
        "5. Active Membership Status (Weight: 0.15): Strong retention shield."
    ]
    for s in shap_features:
        p = tf8b.add_paragraph()
        p.text = f"- {s}"
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(2)

    add_card(slide8, Inches(6.8), Inches(4.4), Inches(5.7), Inches(2.4))
    tb8c = slide8.shapes.add_textbox(Inches(7.1), Inches(4.55), Inches(5.1), Inches(2.1))
    tf8c = tb8c.text_frame
    tf8c.word_wrap = True
    p = tf8c.paragraphs[0]
    p.text = "Operational Triage Integration"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(6)

    triage_points = [
        "Real-Time Streamlit Scoring: Deployed via Python/Streamlit engine on port 8501.",
        "Risk Stratification: Scores depositors into Low (<20%), Medium (20-50%), and Critical (>50%) flight hazard buckets.",
        "Batch Export: Generates actionable CSV rosters for branch manager interventions.",
        "Intervention Window: Triggers retention actions 60-90 days prior to formal account closure."
    ]
    for t in triage_points:
        p = tf8c.add_paragraph()
        p.text = f"- {t}"
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(2)

    # ==========================================
    # SLIDE 9: 4-PILLAR STRATEGIC RETENTION PLAYBOOK
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9)
    add_header(slide9, "Four-Pillar Strategic Retention Playbook")

    pillars = [
        ("PILLAR 1: PRE-RETIREMENT WEALTH DESK", "Target: Ages 46 to 60 (51.12% Churn)", [
            "Assign dedicated private wealth relationship managers before depositors enter pension decumulation.",
            "Bundle tax optimization, estate structuring, and preferential term deposit yields.",
            "Counteract female pre-retiree attrition (56.4%) with personalized wealth planning seminars."
        ], ACCENT_AMBER),
        ("PILLAR 2: GERMAN JURISDICTION TASKFORCE", "Target: German Depositors (32.44% Churn)", [
            "Audit secondary account maintenance fees and debit card surcharges.",
            "Introduce competitive rate tiers on core liquid savings to defend against neobanks.",
            "Establish localized Berlin/Munich customer retention desks with fast-track escalation."
        ], ACCENT_RED),
        ("PILLAR 3: DIGITAL ACTIVITY INCENTIVIZATION", "Target: Inactive Accounts (26.85% Churn)", [
            "Deploy automated 45-day inactivity alerts across mobile app and debit transactions.",
            "Offer direct deposit cashback incentives and recurring bill pay setup rewards.",
            "Transition passive single-product depositors into daily operational bank users."
        ], ACCENT_BLUE),
        ("PILLAR 4: PRODUCT BUNDLING RATIONALIZATION", "Target: 3+ Product Holders (82.7%+ Churn)", [
            "Eliminate punitive post-promotional fee cliffs on bundled credit and insurance lines.",
            "Consolidate account statements into unified digital relationship overviews.",
            "Focus relationship growth on the 2-product sweet spot (7.58% churn) rather than forced cross-selling."
        ], TEXT_LIGHT)
    ]
    for i, (title, target, items, col) in enumerate(pillars):
        row = i // 2
        col_idx = i % 2
        left = Inches(0.8 + col_idx * 5.95)
        top = Inches(1.8 + row * 2.65)
        add_card(slide9, left, top, Inches(5.75), Inches(2.45))
        tb = slide9.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), Inches(5.35), Inches(2.15))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = col

        p = tf.add_paragraph()
        p.text = target
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(4)

        for item in items:
            p = tf.add_paragraph()
            p.text = f"- {item}"
            p.font.size = Pt(10)
            p.font.color.rgb = TEXT_LIGHT
            p.space_after = Pt(2)

    # ==========================================
    # SLIDE 10: REGULATORY GOVERNANCE & CONCLUSIONS
    # ==========================================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10)
    add_header(slide10, "Regulatory Governance, Economic Impact and Conclusions")

    # Left: Regulatory Alignment
    add_card(slide10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    tb10a = slide10.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.5))
    tf10a = tb10a.text_frame
    tf10a.word_wrap = True
    p = tf10a.paragraphs[0]
    p.text = "Regulatory & Supervisory Alignment"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(10)

    reg_points = [
        ("ECB SREP & ICAAP Integration", "European Central Bank supervisors evaluate operational deposit stability under Pillar 2 capital guidelines. Segment-specific depositor flight must be integrated into liquidity stress testing."),
        ("Basel III Liquidity Standards (LCR & NSFR)", "Mitigating the EUR 110.85M flight among high-balance retail depositors directly strengthens the 30-day Liquidity Coverage Ratio buffer."),
        ("Consumer Protection & TCF Compliance", "Eliminating deceptive teaser rates and multi-product fee cliffs ensures strict compliance with European Banking Authority (EBA) Treating Customers Fairly principles."),
        ("GDPR Compliant Architecture", "Predictive modeling and scoring are conducted on pseudonymized data pipelines without PII exposure.")
    ]
    for title, desc in reg_points:
        p = tf10a.add_paragraph()
        p.text = f"- {title}: "
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(6)

    # Right: ROI & Project Conclusions
    add_card(slide10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb10b = slide10.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf10b = tb10b.text_frame
    tf10b.word_wrap = True
    p = tf10b.paragraphs[0]
    p.text = "Project Conclusions & Direct Resources"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(10)

    concl_points = [
        ("Projected Economic Return", "A 15% reduction in high-balance attrition preserves an estimated EUR 16.6 Million in core liquidity and EUR 1.8 Million in annual net interest income."),
        ("Executive Transformation", "Shifts banking management from passive reactive attrition reporting to proactive, algorithmic depositor relationship preservation."),
        ("Repository Artifacts", "Complete audited codebase, interactive Helix web portal, Streamlit analytical app, research papers, and technical reports available in the repository."),
        ("Project Lead", "Prepared by Panchaksharayya | Quantitative Banking Analytics & Financial Risk Advisory | September 2026")
    ]
    for title, desc in concl_points:
        p = tf10b.add_paragraph()
        p.text = f"- {title}: "
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(6)

    prs.save(output_path)
    print(f"Presentation generated successfully: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\panch\Downloads\Bankchurn"
    out_file = os.path.join(out_dir, "Presentation_Customer_Segmentation_and_Churn.pptx")
    build_presentation(out_file)
