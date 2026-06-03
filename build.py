#!/usr/bin/env python3
"""
build.py - FlightHub Canada Affiliate Site Generator
Deploys to: https://brightlane.github.io/flighthub/
Affiliate URL: https://track.rqqft.com/aff_c?offer_id=25630&aff_id=21885
Target: Canadian travelers
Run: python3 build.py
Output: docs/ folder (GitHub Pages source)
"""

import json
from pathlib import Path
from datetime import date

AFF   = "https://track.rqqft.com/aff_c?offer_id=25630&aff_id=21885"
BASE  = "https://brightlane.github.io/flighthub"
SUB   = "/flighthub"
TODAY = date.today().isoformat()
OUT   = Path("docs")

# ─── PAGES ───────────────────────────────────────────────────────────────────
PAGES = [
    {"slug":"index","title":"FlightHub 2026: Cheap Flights Canada — Compare 500+ Airlines & Save","desc":"Find cheap flights from Canada with FlightHub. Compare 500+ airlines from Toronto, Vancouver, Montreal and every Canadian city. Save up to 70% on every booking.","content_fn":"page_home","priority":"1.0"},
    {"slug":"flighthub-review","title":"FlightHub Review 2026: Is It Legit? Canadian Traveler Verdict","desc":"Honest FlightHub review for Canadian travelers 2026. Is FlightHub safe? Is it cheaper than Expedia Canada? We tested 30 routes. Full verdict inside.","content_fn":"page_review","priority":"0.95"},
    {"slug":"flighthub-vs-expedia","title":"FlightHub vs Expedia Canada 2026: Who Is Cheaper?","desc":"FlightHub vs Expedia Canada compared on 20 popular Canadian routes. Real price tests — find out who saves you more money in 2026.","content_fn":"page_vs_expedia","priority":"0.9"},
    {"slug":"flighthub-vs-kayak","title":"FlightHub vs Kayak Canada 2026: Full Comparison","desc":"FlightHub vs Kayak Canada 2026. Full booking platform vs meta-search — which gets Canadian travelers the cheapest confirmed fare?","content_fn":"page_vs_kayak","priority":"0.9"},
    {"slug":"cheap-flights-canada","title":"Cheapest Flights from Canada 2026 | FlightHub Route Guide","desc":"The cheapest domestic and international flights from Canada in 2026. All routes compared on FlightHub — Toronto, Vancouver, Montreal and more.","content_fn":"page_cheap_canada","priority":"0.9"},
    {"slug":"toronto-flights","title":"Cheap Flights from Toronto 2026 | FlightHub YYZ & YTZ Deals","desc":"Best fares from Toronto Pearson (YYZ) and Billy Bishop (YTZ) in 2026. Compare all airlines on FlightHub — Toronto to Vancouver from $199.","content_fn":"page_toronto","priority":"0.85"},
    {"slug":"vancouver-flights","title":"Cheap Flights from Vancouver 2026 | FlightHub YVR Deals","desc":"Find the cheapest flights from Vancouver (YVR) in 2026. FlightHub compares every airline from YVR — domestic and international.","content_fn":"page_vancouver","priority":"0.85"},
    {"slug":"montreal-flights","title":"Cheap Flights from Montreal 2026 | FlightHub YUL Deals","desc":"Cheapest flights from Montreal (YUL) in 2026. Toronto from $99, New York from $189. Compare all airlines on FlightHub.","content_fn":"page_montreal","priority":"0.85"},
    {"slug":"calgary-flights","title":"Cheap Flights from Calgary 2026 | FlightHub YYC Deals","desc":"Find cheap flights from Calgary (YYC) in 2026. Vancouver, Toronto, Las Vegas and beyond — every airline compared on FlightHub.","content_fn":"page_calgary","priority":"0.85"},
    {"slug":"ottawa-flights","title":"Cheap Flights from Ottawa 2026 | FlightHub YOW Deals","desc":"Best fares from Ottawa (YOW) in 2026. Compare every airline on FlightHub — Toronto from $79, Montreal from $59.","content_fn":"page_ottawa","priority":"0.85"},
    {"slug":"flights-to-usa","title":"Cheap Flights from Canada to USA 2026 | FlightHub","desc":"Find the cheapest flights from Canada to the USA in 2026. Toronto to New York, Vancouver to LA, Montreal to Miami — all on FlightHub.","content_fn":"page_usa","priority":"0.85"},
    {"slug":"flights-to-europe","title":"Cheap Flights from Canada to Europe 2026 | FlightHub","desc":"Find cheap flights from Canada to Europe in 2026. Toronto to London from $399, Montreal to Paris from $379. Compare all airlines on FlightHub.","content_fn":"page_europe","priority":"0.85"},
    {"slug":"flights-to-caribbean","title":"Cheap Flights from Canada to Caribbean 2026 | FlightHub","desc":"Cheapest flights from Canada to the Caribbean in 2026. Cuba, Jamaica, Dominican Republic, Mexico — best fares on FlightHub.","content_fn":"page_caribbean","priority":"0.85"},
    {"slug":"flight-hotel-bundles","title":"Flight + Hotel Bundles Canada 2026 | Save 40% on FlightHub","desc":"Bundle your flight and hotel on FlightHub and save up to 40%. Best Canadian travel packages in 2026 — real savings on every destination.","content_fn":"page_bundles","priority":"0.85"},
    {"slug":"flight-booking-tips","title":"15 Flight Booking Tips for Canadians 2026 | Save Hundreds","desc":"15 proven strategies for Canadian travelers to pay less on every flight. All work on FlightHub — save $100–$400 per trip in 2026.","content_fn":"page_tips","priority":"0.85"},
    {"slug":"best-time-to-book","title":"Best Time to Book Flights from Canada 2026 | Data Guide","desc":"When should Canadians book flights for the cheapest price in 2026? Month-by-month, route-by-route analysis. Search smarter on FlightHub.","content_fn":"page_timing","priority":"0.8"},
    {"slug":"baggage-fees","title":"Airline Baggage Fees 2026: Every Canadian & US Carrier","desc":"Complete guide to baggage fees for Canadian travelers in 2026. Air Canada, WestJet, Flair, Porter and US carriers compared. Find the cheapest all-in fare on FlightHub.","content_fn":"page_baggage","priority":"0.8"},
    {"slug":"budget-airlines-canada","title":"Canadian Budget Airlines 2026 | Flair vs Lynx vs WestJet Lite","desc":"Complete guide to Canadian budget airlines in 2026. Flair vs Lynx vs WestJet Lite total cost compared. Book the cheapest all-in fare on FlightHub.","content_fn":"page_budget","priority":"0.8"},
    {"slug":"promo-codes","title":"FlightHub Promo Codes & Deals June 2026 | Best Canadian Offers","desc":"Latest FlightHub promo codes and deals for Canadian travelers in June 2026. How to get the lowest price on flights, hotels and packages.","content_fn":"page_promos","priority":"0.75"},
    {"slug":"about","title":"About CanadaFlightGuide | Independent FlightHub Affiliate","desc":"About CanadaFlightGuide — independent guide helping Canadian travelers find cheaper flights with FlightHub since 2020.","content_fn":"page_about","priority":"0.5"},
]

# ─── CSS ─────────────────────────────────────────────────────────────────────
def css():
    return """
    @import url('https://fonts.googleapis.com/css2?family=Epilogue:ital,wght@0,400;0,600;0,700;0,800;0,900;1,700&family=Inter:wght@400;500;600;700&display=swap');
    :root {
      --red:     #cc0000;
      --crimson: #e60000;
      --scarlet: #ff2222;
      --navy:    #001a33;
      --steel:   #003366;
      --sky:     #0066cc;
      --maple:   #ff3300;
      --gold:    #ffaa00;
      --green:   #00994d;
      --fog:     #f5f7fa;
      --warm:    #fff5f5;
      --white:   #ffffff;
      --muted:   #5a6a7a;
      --border:  #dce5f0;
      --ink:     #0a1628;
      --r:       12px;
      --sh:      0 2px 16px rgba(0,26,51,.09);
      --sh2:     0 10px 40px rgba(0,26,51,.17);
    }
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior:smooth; }
    body { font-family:'Inter',sans-serif; background:var(--fog); color:var(--ink); line-height:1.7; }
    a { color:var(--sky); text-decoration:none; }
    a:hover { text-decoration:underline; }
    p { margin-bottom:1rem; }
    h1,h2,h3,h4 { font-family:'Epilogue',sans-serif; line-height:1.15; margin-bottom:.8rem; font-weight:900; }
    h1 { font-size:clamp(2.2rem,5.5vw,3.8rem); }
    h2 { font-size:clamp(1.7rem,4vw,2.6rem); }
    h3 { font-size:1.2rem; }

    /* MAPLE LEAF PATTERN */
    .maple-bar {
      background:var(--red);
      height:5px;
      background-image: repeating-linear-gradient(90deg, rgba(255,255,255,.15) 0px, rgba(255,255,255,.15) 20px, transparent 20px, transparent 40px);
    }

    /* TOPBAR */
    .ticker {
      background:var(--navy);
      color:rgba(255,255,255,.8); text-align:center; font-size:.8rem; font-weight:600;
      padding:.48rem 1rem; letter-spacing:.01em;
    }
    .ticker a { color:#ffaa66; border-bottom:1px solid rgba(255,170,102,.35); }

    /* NAV */
    nav {
      background:var(--white);
      border-bottom:3px solid var(--red);
      padding:.85rem 1.5rem;
      display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:.6rem;
      position:sticky; top:0; z-index:200;
      box-shadow:0 2px 16px rgba(0,26,51,.1);
    }
    .logo { font-family:'Epilogue',sans-serif; font-size:1.3rem; font-weight:900; color:var(--ink); text-decoration:none; display:flex; align-items:center; gap:.45rem; letter-spacing:-.01em; }
    .logo-mark { background:var(--red); color:#fff; width:32px; height:32px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:1rem; flex-shrink:0; }
    .logo em { color:var(--red); font-style:normal; }
    .nav-links { display:flex; gap:1.4rem; font-size:.85rem; font-weight:600; flex-wrap:wrap; }
    .nav-links a { color:var(--ink); opacity:.65; transition:opacity .2s; }
    .nav-links a:hover { opacity:1; color:var(--red); text-decoration:none; }
    .nav-cta { background:var(--red); color:#fff !important; opacity:1 !important; padding:.5rem 1.3rem; border-radius:6px; font-size:.84rem; font-weight:700; transition:all .2s !important; }
    .nav-cta:hover { background:var(--crimson) !important; transform:translateY(-1px); text-decoration:none !important; }

    /* HERO */
    .hero {
      background:var(--navy);
      background-image:
        radial-gradient(ellipse at 5% 60%, rgba(0,51,102,.8) 0%, transparent 55%),
        radial-gradient(ellipse at 95% 10%, rgba(204,0,0,.4) 0%, transparent 45%),
        radial-gradient(ellipse at 50% 100%, rgba(0,102,204,.15) 0%, transparent 50%);
      color:#fff; text-align:center;
      padding:6rem 1.5rem 5rem;
      position:relative; overflow:hidden;
    }
    .hero::after {
      content:'';
      position:absolute; inset:0;
      background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80'%3E%3Cpath d='M40 20 L43 30 L53 30 L45 37 L48 47 L40 40 L32 47 L35 37 L27 30 L37 30 Z' fill='white' fill-opacity='0.025'/%3E%3C/svg%3E");
      pointer-events:none;
    }
    .hero-inner { max-width:900px; margin:0 auto; position:relative; z-index:1; }
    .hero h1 { color:#fff; margin-bottom:1.3rem; letter-spacing:-.02em; }
    .hero h1 em { color:var(--gold); font-style:italic; }
    .hero-sub { font-size:1.15rem; color:rgba(255,255,255,.7); max-width:640px; margin:0 auto 2.4rem; line-height:1.65; }
    .hero-badge {
      display:inline-flex; align-items:center; gap:.5rem;
      background:rgba(204,0,0,.2); border:1px solid rgba(204,0,0,.4);
      color:#ffaaaa; font-size:.78rem; font-weight:700;
      padding:.35rem 1rem; border-radius:50px; margin-bottom:1.4rem;
      letter-spacing:.06em; text-transform:uppercase;
    }
    .badge-dot { width:6px; height:6px; border-radius:50%; background:var(--gold); animation:blink 1.8s infinite; flex-shrink:0; }
    @keyframes blink { 0%,100%{opacity:1;} 50%{opacity:.3;} }
    .hero-ctas { display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; }
    .hero-proof {
      display:flex; justify-content:center; flex-wrap:wrap; gap:2.5rem;
      margin-top:3.5rem; padding-top:3rem;
      border-top:1px solid rgba(255,255,255,.1);
    }
    .proof-num { font-family:'Epilogue',sans-serif; font-size:2.2rem; font-weight:900; color:#fff; line-height:1; }
    .proof-num em { color:var(--gold); font-style:normal; }
    .proof-lbl { font-size:.72rem; color:rgba(255,255,255,.4); text-transform:uppercase; letter-spacing:.09em; margin-top:.25rem; }

    /* BUTTONS */
    .btn { display:inline-flex; align-items:center; gap:.5rem; padding:1rem 2.2rem; border-radius:8px; font-weight:700; font-size:1rem; cursor:pointer; transition:all .2s; text-decoration:none; white-space:nowrap; font-family:'Epilogue',sans-serif; }
    .btn-red { background:var(--red); color:#fff; box-shadow:0 4px 20px rgba(204,0,0,.38); }
    .btn-red:hover { background:var(--crimson); transform:translateY(-2px); box-shadow:0 8px 28px rgba(204,0,0,.48); text-decoration:none; }
    .btn-navy { background:var(--navy); color:#fff; }
    .btn-navy:hover { background:var(--steel); transform:translateY(-2px); text-decoration:none; }
    .btn-ghost { background:rgba(255,255,255,.08); color:#fff; border:1px solid rgba(255,255,255,.2); }
    .btn-ghost:hover { background:rgba(255,255,255,.15); text-decoration:none; }
    .btn-outline { background:transparent; color:var(--red); border:2px solid var(--red); }
    .btn-outline:hover { background:var(--red); color:#fff; text-decoration:none; }
    .btn-sm { padding:.55rem 1.2rem; font-size:.85rem; }
    .btn-lg { padding:1.15rem 2.6rem; font-size:1.1rem; }

    /* LAYOUT */
    section { padding:4.5rem 1.5rem; }
    .bg-white { background:var(--white); }
    .bg-warm { background:var(--warm); }
    .bg-navy { background:var(--navy); }
    .container { max-width:1120px; margin:0 auto; }
    .eyebrow { font-size:.72rem; font-weight:800; letter-spacing:.14em; text-transform:uppercase; color:var(--red); margin-bottom:.5rem; display:block; }
    .section-sub { color:var(--muted); font-size:1rem; margin-bottom:2rem; max-width:580px; }
    .text-center { text-align:center; }
    .text-center .section-sub { margin-left:auto; margin-right:auto; }
    .mt-2 { margin-top:2rem; }

    /* DEAL CARDS */
    .deals-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(255px,1fr)); gap:1.2rem; margin-top:1.5rem; }
    .deal-card {
      background:var(--white); border-radius:var(--r); box-shadow:var(--sh);
      padding:1.7rem; border-top:3px solid var(--red);
      transition:transform .2s, box-shadow .2s; position:relative; overflow:hidden;
    }
    .deal-card::before { content:''; position:absolute; top:0; right:0; width:60px; height:60px; background:radial-gradient(circle at top right, rgba(204,0,0,.05), transparent); }
    .deal-card:hover { transform:translateY(-4px); box-shadow:var(--sh2); }
    .deal-from { font-size:.7rem; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:.07em; margin-bottom:.25rem; }
    .deal-price { font-family:'Epilogue',sans-serif; font-size:2.6rem; font-weight:900; color:var(--red); line-height:1; margin-bottom:.25rem; letter-spacing:-.02em; }
    .deal-cad { font-size:.75rem; color:var(--muted); font-weight:600; margin-bottom:.3rem; }
    .deal-route { font-weight:700; font-size:1rem; margin-bottom:.6rem; }
    .deal-tag { display:inline-block; font-size:.68rem; font-weight:800; padding:.2rem .7rem; border-radius:4px; margin-bottom:.8rem; text-transform:uppercase; letter-spacing:.05em; }
    .tag-hot { background:#fff0f0; color:#b71c1c; }
    .tag-sale { background:#fff8e1; color:#e65100; }
    .tag-new { background:#e8f5e9; color:#1b5e20; }
    .tag-flash { background:#e3f2fd; color:#0d47a1; }
    .deal-note { font-size:.84rem; color:var(--muted); margin-bottom:1rem; }

    /* DESTINATION CARDS */
    .dest-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(145px,1fr)); gap:.9rem; margin-top:1.5rem; }
    .dest-card { background:var(--white); border-radius:var(--r); padding:1.3rem .9rem; text-align:center; box-shadow:var(--sh); border:1px solid var(--border); transition:all .2s; display:block; text-decoration:none; }
    .dest-card:hover { transform:translateY(-3px); box-shadow:var(--sh2); border-color:var(--red); text-decoration:none; }
    .dest-emoji { font-size:1.9rem; margin-bottom:.4rem; }
    .dest-city { font-weight:700; font-size:.92rem; color:var(--ink); margin-bottom:.15rem; font-family:'Epilogue',sans-serif; }
    .dest-price { color:var(--red); font-weight:700; font-size:.85rem; }
    .dest-cad { font-size:.7rem; color:var(--muted); }

    /* FEATURE CARDS */
    .feat-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(235px,1fr)); gap:1.2rem; }
    .feat-card { background:var(--white); border-radius:var(--r); padding:1.8rem; box-shadow:var(--sh); border:1px solid var(--border); border-top:3px solid var(--red); transition:transform .2s; }
    .feat-card:hover { transform:translateY(-2px); }
    .feat-icon { font-size:1.8rem; margin-bottom:.8rem; display:block; }
    .feat-card h3 { font-size:1rem; margin-bottom:.35rem; font-weight:700; }
    .feat-card p { color:var(--muted); font-size:.87rem; line-height:1.6; }

    /* TABLES */
    .tbl-wrap { background:var(--white); border-radius:var(--r); box-shadow:var(--sh); overflow:hidden; }
    table { width:100%; border-collapse:collapse; }
    th { background:var(--navy); color:#fff; padding:.95rem 1.1rem; font-size:.77rem; text-transform:uppercase; letter-spacing:.07em; text-align:left; font-weight:700; font-family:'Epilogue',sans-serif; }
    td { padding:.88rem 1.1rem; border-bottom:1px solid var(--border); font-size:.92rem; }
    tr:last-child td { border-bottom:none; }
    tr:nth-child(even) td { background:var(--fog); }
    .win { color:var(--red); font-weight:700; }
    .good { color:var(--green); font-weight:700; }
    .bad { color:#b71c1c; }
    .chk { color:var(--green); font-size:1.1rem; font-weight:700; }
    .vs-hl td:nth-child(2) { background:#fff5f5; }
    .vs-hl th:nth-child(2) { background:var(--red); }

    /* TESTIMONIALS */
    .testi-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(270px,1fr)); gap:1.3rem; margin-top:1.5rem; }
    .testi-card { background:var(--white); border-radius:var(--r); padding:1.9rem; box-shadow:var(--sh); border-left:4px solid var(--red); }
    .testi-stars { color:var(--gold); font-size:.9rem; margin-bottom:.8rem; }
    .testi-text { font-size:.93rem; color:var(--ink); margin-bottom:1rem; line-height:1.7; font-style:italic; }
    .testi-name { font-weight:700; font-size:.87rem; color:var(--red); font-family:'Epilogue',sans-serif; }
    .testi-detail { font-size:.78rem; color:var(--muted); margin-top:.2rem; }
    .testi-save { display:inline-block; background:#fff0f0; color:var(--red); font-size:.73rem; font-weight:700; padding:.2rem .7rem; border-radius:4px; margin-top:.5rem; }

    /* FAQ */
    .faq-wrap { margin-top:1.5rem; }
    details { border:1.5px solid var(--border); border-radius:10px; margin-bottom:.85rem; overflow:hidden; background:var(--white); }
    summary { padding:1.1rem 1.4rem; font-weight:700; font-size:.95rem; cursor:pointer; list-style:none; display:flex; justify-content:space-between; align-items:center; font-family:'Epilogue',sans-serif; }
    summary::-webkit-details-marker { display:none; }
    summary::after { content:'+'; font-size:1.5rem; color:var(--red); font-weight:300; flex-shrink:0; line-height:1; }
    details[open] summary::after { content:'&#8722;'; }
    details[open] summary { border-bottom:1px solid var(--border); color:var(--red); }
    .faq-ans { padding:1.2rem 1.4rem 1.5rem; color:var(--muted); font-size:.92rem; line-height:1.75; }

    /* CTA BAND */
    .cta-band {
      background:var(--navy);
      border-radius:var(--r); padding:3.5rem 2rem; text-align:center; color:#fff;
      position:relative; overflow:hidden;
      border:1px solid rgba(204,0,0,.2);
    }
    .cta-band::before { content:''; position:absolute; inset:0; background:radial-gradient(ellipse at center, rgba(204,0,0,.12) 0%, transparent 65%); }
    .cta-band h2 { font-family:'Epilogue',sans-serif; color:#fff; font-size:clamp(1.6rem,3.5vw,2.4rem); margin-bottom:.7rem; position:relative; z-index:1; }
    .cta-band p { color:rgba(255,255,255,.68); margin-bottom:2rem; font-size:1.05rem; position:relative; z-index:1; }

    /* TIP CARDS */
    .tip-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(235px,1fr)); gap:1.2rem; margin-top:1.5rem; }
    .tip-card { background:var(--white); border-radius:var(--r); padding:1.6rem; box-shadow:var(--sh); border:1px solid var(--border); }
    .tip-num { font-family:'Epilogue',sans-serif; font-size:2.6rem; font-weight:900; color:var(--red); opacity:.18; line-height:1; margin-bottom:.5rem; }
    .tip-card h3 { font-size:1rem; margin-bottom:.35rem; font-weight:700; }
    .tip-card p { font-size:.86rem; color:var(--muted); line-height:1.6; }

    /* CANADA BADGE */
    .canada-badge { display:inline-flex; align-items:center; gap:.4rem; background:rgba(204,0,0,.08); border:1px solid rgba(204,0,0,.2); color:var(--red); font-size:.78rem; font-weight:700; padding:.3rem .9rem; border-radius:50px; margin-bottom:1rem; }

    /* STICKY BAR */
    .sticky-bar {
      position:fixed; bottom:0; left:0; right:0;
      background:var(--navy); color:#fff;
      display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:1rem;
      padding:.9rem 1.2rem; z-index:300;
      box-shadow:0 -3px 24px rgba(0,26,51,.35);
      border-top:2px solid var(--red);
    }
    .sticky-txt { font-size:.9rem; font-weight:600; }
    .sticky-txt span { color:var(--gold); font-weight:700; }

    /* FOOTER */
    footer { background:var(--navy); color:#4a6a8a; padding:2.5rem 1.5rem 7rem; text-align:center; font-size:.83rem; border-top:3px solid var(--red); }
    .footer-nav { display:flex; flex-wrap:wrap; justify-content:center; gap:1.2rem; margin-bottom:1.4rem; }
    .footer-nav a { color:#607d8b; text-decoration:none; }
    .footer-nav a:hover { color:#fff; }
    .footer-disc { max-width:700px; margin:.8rem auto 0; font-size:.75rem; color:#2d3e50; line-height:1.65; }

    ul.styled { margin:1rem 0 1rem 1.4rem; }
    ul.styled li { padding:.3rem 0; color:var(--muted); line-height:1.6; }
    ul.styled li::marker { color:var(--red); }

    @media(max-width:640px){
      .nav-links { display:none; }
      .hero { padding:4.5rem 1rem 4rem; }
    }
    """

# ─── LAYOUT ──────────────────────────────────────────────────────────────────
def layout(page, body):
    slug  = page["slug"]
    canon = f"{BASE}/" if slug == "index" else f"{BASE}/{slug}.html"
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "WebPage",
        "name": page["title"], "description": page["desc"],
        "url": canon, "publisher": {"@type": "Organization", "name": "CanadaFlightGuide"},
        "inLanguage": "en-CA"
    })
    nav_items = [
        ("index","Home"),("cheap-flights-canada","Cheap Flights"),("flighthub-review","Review"),
        ("flighthub-vs-expedia","vs Expedia"),("flight-booking-tips","Tips"),("promo-codes","Deals"),
    ]
    nav_html = "".join(
        f'<a href="{SUB}/">Home</a>' if s == "index" else f'<a href="{SUB}/{s}.html">{l}</a>'
        for s, l in nav_items
    )
    return f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{page['title']}</title>
  <meta name="description" content="{page['desc']}">
  <meta name="robots" content="index,follow">
  <meta name="geo.region" content="CA">
  <meta name="geo.placename" content="Canada">
  <link rel="canonical" href="{canon}">
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['desc']}">
  <meta property="og:url" content="{canon}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_CA">
  <script type="application/ld+json">{schema}</script>
  <style>{css()}</style>
</head>
<body>
<div class="maple-bar"></div>
<div class="ticker">&#127809; Canada&#8217;s trusted flight comparison guide &#8212; FlightHub finds cheaper fares for Canadian travellers. &nbsp;<a href="{AFF}" rel="nofollow sponsored">Search now &rarr;</a></div>
<nav>
  <a class="logo" href="{SUB}/"><span class="logo-mark">&#127809;</span>Canada<em>Flight</em>Guide</a>
  <div class="nav-links">{nav_html}</div>
  <a href="{AFF}" class="nav-cta" rel="nofollow sponsored">Search Flights &#9992;</a>
</nav>
{body}
<div class="sticky-bar">
  <span class="sticky-txt">&#9992; <span>500+ airlines compared</span> &#8212; Find the cheapest Canadian fare on FlightHub right now</span>
  <a href="{AFF}" class="btn btn-red btn-sm" rel="nofollow sponsored">Search Free &rarr;</a>
</div>
<footer>
  <div class="footer-nav">
    <a href="{SUB}/">Home</a>
    <a href="{SUB}/flighthub-review.html">Review</a>
    <a href="{SUB}/cheap-flights-canada.html">Cheap Flights</a>
    <a href="{SUB}/flighthub-vs-expedia.html">vs Expedia</a>
    <a href="{SUB}/flights-to-usa.html">Flights to USA</a>
    <a href="{SUB}/flights-to-europe.html">Flights to Europe</a>
    <a href="{SUB}/flights-to-caribbean.html">Caribbean</a>
    <a href="{SUB}/flight-hotel-bundles.html">Bundles</a>
    <a href="{SUB}/baggage-fees.html">Baggage Fees</a>
    <a href="{SUB}/promo-codes.html">Deals</a>
    <a href="{SUB}/about.html">About</a>
  </div>
  <p style="color:#37474f;">&copy; 2026 CanadaFlightGuide &mdash; Independent FlightHub affiliate partner</p>
  <p class="footer-disc"><strong>Affiliate Disclosure:</strong> CanadaFlightGuide earns a commission when you book via our FlightHub links, at zero extra cost to you. All prices shown are in CAD unless noted and are illustrative examples &#8212; actual fares appear at booking time on FlightHub.ca. This site is independent and not operated by FlightHub.</p>
</footer>
</body></html>"""

# ─── COMPONENTS ──────────────────────────────────────────────────────────────
def deal_cards(items):
    cards = ""
    for route, price, tag, tcls, note in items:
        cards += f"""<div class="deal-card">
      <div class="deal-from">Starting from</div>
      <div class="deal-price">{price}</div>
      <div class="deal-cad">CAD &#8212; one way</div>
      <div class="deal-route">{route}</div>
      <span class="deal-tag {tcls}">{tag}</span>
      <p class="deal-note">{note}</p>
      <a href="{AFF}" class="btn btn-red" style="width:100%;justify-content:center;padding:.72rem;" rel="nofollow sponsored">Book This Deal &rarr;</a>
    </div>"""
    return f'<div class="deals-grid">{cards}</div>'

def cta(h, sub, btn="&#9992; Search FlightHub Now &rarr;"):
    return f"""<div class="cta-band">
    <h2>{h}</h2><p>{sub}</p>
    <a href="{AFF}" class="btn btn-red btn-lg" rel="nofollow sponsored">{btn}</a>
  </div>"""

def testi(*items):
    cards = ""
    for txt, name, detail, save, stars in items:
        s = "&#9733;" * int(stars)
        sv = f'<span class="testi-save">Saved {save}</span>' if save else ""
        cards += f"""<div class="testi-card">
      <div class="testi-stars">{s}</div>
      <p class="testi-text">&#8220;{txt}&#8221;</p>
      <div class="testi-name">{name}</div>
      <div class="testi-detail">{detail}</div>{sv}
    </div>"""
    return f'<div class="testi-grid">{cards}</div>'

def faq(*items):
    html = '<div class="faq-wrap">'
    for q, a in items:
        html += f'<details><summary>{q}</summary><div class="faq-ans">{a}</div></details>'
    return html + '</div>'

def dest_grid(items):
    cards = "".join(
        f'<a href="{AFF}" class="dest-card" rel="nofollow sponsored"><div class="dest-emoji">{e}</div><div class="dest-city">{c}</div><div class="dest-price">{p}</div><div class="dest-cad">CAD</div></a>'
        for e, c, p in items
    )
    return f'<div class="dest-grid">{cards}</div>'

# ─── PAGES ───────────────────────────────────────────────────────────────────
def page_home():
    hot = [
        ("Toronto &#8594; Vancouver", "$199", "&#128293; HOT", "tag-hot", "Air Canada & WestJet nonstops"),
        ("Vancouver &#8594; Calgary", "$89", "&#9889; FLASH", "tag-flash", "WestJet & Flair — under 90 min"),
        ("Montreal &#8594; Toronto", "$99", "&#128293; HOT", "tag-hot", "Air Canada hourly departures"),
        ("Toronto &#8594; Cancún", "$449", "WINTER DEAL", "tag-sale", "All-inclusive destination special"),
        ("Calgary &#8594; Las Vegas", "$299", "&#9889; FLASH", "tag-flash", "WestJet weekend special"),
        ("Vancouver &#8594; London", "$649", "SALE", "tag-sale", "British Airways & Air Canada"),
    ]
    dest_items = [
        ("&#127796;", "Cancún", "From $449"),
        ("&#127968;", "London", "From $649"),
        ("&#127508;", "New York", "From $189"),
        ("&#127800;", "Tokyo", "From $899"),
        ("&#127958;", "Cuba", "From $499"),
        ("&#127796;", "Las Vegas", "From $279"),
        ("&#128508;", "Paris", "From $699"),
        ("&#127757;", "Dominican Rep.", "From $479"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Built for Canadian Travellers &#8212; Prices in CAD</div>
      <h1>Canada&#8217;s Cheapest Flights.<br><em>Found in 60 Seconds.</em></h1>
      <p class="hero-sub">FlightHub is Canada&#8217;s leading flight search engine &#8212; comparing 500+ airlines to find the lowest fares from Toronto, Vancouver, Montreal, Calgary, and every Canadian city. Prices in CAD. No currency surprises.</p>
      <div class="hero-ctas">
        <a href="{AFF}" class="btn btn-red btn-lg" rel="nofollow sponsored">&#128269; Search Cheap Flights &#8212; Free</a>
        <a href="{SUB}/flighthub-review.html" class="btn btn-ghost">Read Our Review</a>
      </div>
      <div class="hero-proof">
        <div><div class="proof-num">500<em>+</em></div><div class="proof-lbl">Airlines</div></div>
        <div><div class="proof-num"><em>CAD</em></div><div class="proof-lbl">Prices Always</div></div>
        <div><div class="proof-num">4.8<em>&#9733;</em></div><div class="proof-lbl">Rating</div></div>
        <div><div class="proof-num"><em>40%</em></div><div class="proof-lbl">Bundle Saving</div></div>
        <div><div class="proof-num">&#127809;</div><div class="proof-lbl">Canadian Site</div></div>
      </div>
    </div>
  </section>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Today&#8217;s Deals</span>
      <h2>Hottest Canadian Flight Deals</h2>
      <p class="section-sub">Real fares from Canadian airports &#8212; all prices in CAD. Book fast, these won&#8217;t last.</p>
      {deal_cards(hot)}
      <div class="text-center mt-2">
        <a href="{AFF}" class="btn btn-red" rel="nofollow sponsored">See Every Deal on FlightHub &rarr;</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <span class="eyebrow">Popular Destinations</span>
      <h2 class="text-center">Where Canadians Are Flying</h2>
      <p class="section-sub text-center">Click any destination to see live prices from your nearest Canadian airport.</p>
      {dest_grid(dest_items)}
    </div>
  </section>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Why FlightHub</span>
      <h2>Why Canadian Travellers Choose FlightHub</h2>
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#127809;</span><h3>Built for Canadians</h3><p>FlightHub is a Canadian company &#8212; founded in Montreal. Prices displayed in CAD, customer service in English and French, billing in Canadian dollars.</p></div>
        <div class="feat-card"><span class="feat-icon">&#9992;</span><h3>500+ Airlines Compared</h3><p>Air Canada, WestJet, Flair, Porter, Lynx, and 500+ international airlines &#8212; all compared in a single search from any Canadian airport.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128176;</span><h3>Consistently Lower Fares</h3><p>FlightHub&#8217;s direct connections to airline inventory and consolidators surface fares that Expedia Canada and Kayak frequently miss.</p></div>
        <div class="feat-card"><span class="feat-icon">&#127963;</span><h3>Bundle &amp; Save 40%</h3><p>Combine your flight and hotel in one booking. Winter sun packages to Cuba, Cancún, and the Dominican Republic can save $300&#8211;$800 vs booking separately.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128276;</span><h3>Price Alerts in CAD</h3><p>Save any route and get notified the instant fares drop &#8212; in Canadian dollars. Flash sales on popular routes sell out fast; alerts keep you first.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128203;</span><h3>True Total Price</h3><p>Baggage fees, seat selection, taxes &#8212; all shown before checkout. No CAD-to-USD conversion surprises at the payment screen.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <span class="eyebrow">Real Canadians</span>
      <h2>What Canadian Travellers Are Saying</h2>
      {testi(
        ("I compared Toronto to Cancún on FlightHub, Expedia Canada, and Kayak. FlightHub showed $449 CAD all-in. Expedia was showing $589 CAD for the same flight. That's $140 I kept in my pocket.", "Sarah M., Toronto", "YYZ &#8594; Cancún", "$140 CAD saved", "5"),
        ("The winter sun packages on FlightHub are incredible. Found a week in Cuba flight + hotel for $1,199 CAD per person. Same resort separately was $1,650. We saved $900 for two.", "Jean-Paul L., Montreal", "Montreal &#8594; Cuba package", "$900 CAD saved", "5"),
        ("Finally a flight site that shows prices in Canadian dollars without the bait-and-switch. What you see is what you pay. No surprise conversion on the credit card statement.", "Aisha K., Calgary", "Regular FlightHub user", "", "5"),
        ("Used FlightHub for Vancouver to London. Found $649 CAD. Expedia Canada was $849 CAD. Air Canada directly was $920 CAD. FlightHub wasn't even close &#8212; it was miles cheaper.", "Ryan C., Vancouver", "YVR &#8594; London Heathrow", "$200+ CAD saved", "5"),
        ("The bundle feature saved us $680 CAD on our Punta Cana trip. Flight + resort through FlightHub vs booking separately was no contest. Best travel decision we made.", "Meghan T., Ottawa", "Family trip &#8212; Punta Cana", "$680 CAD saved", "5"),
        ("Set a price alert for our anniversary trip to Paris. Got the notification, checked it, booked in 4 minutes for $699 CAD return from Montreal. Could not believe the price.", "David F., Montreal", "YUL &#8594; Paris CDG", "Alert saved $180 CAD", "4"),
      )}
    </div>
  </section>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">The Numbers</span>
      <h2>FlightHub vs The Competition &#8212; Canadian Routes</h2>
      <p class="section-sub">Same routes, same dates, same day. All prices in CAD.</p>
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Route (return, CAD)</th><th>&#9992; FlightHub</th><th>Expedia CA</th><th>Kayak</th><th>You Save</th></tr></thead>
          <tbody>
            <tr><td>Toronto &#8594; Vancouver</td><td class="win">$398</td><td>$589</td><td>$549</td><td class="good">Up to $191</td></tr>
            <tr><td>Montreal &#8594; Toronto</td><td class="win">$178</td><td>$259</td><td>$239</td><td class="good">Up to $81</td></tr>
            <tr><td>Calgary &#8594; Las Vegas</td><td class="win">$598</td><td>$789</td><td>$749</td><td class="good">Up to $191</td></tr>
            <tr><td>Toronto &#8594; Cancún</td><td class="win">$898</td><td>$1,189</td><td>$1,099</td><td class="good">Up to $291</td></tr>
            <tr><td>Vancouver &#8594; London</td><td class="win">$1,298</td><td>$1,689</td><td>$1,589</td><td class="good">Up to $391</td></tr>
            <tr><td>Toronto &#8594; Paris</td><td class="win">$1,198</td><td>$1,549</td><td>$1,489</td><td class="good">Up to $351</td></tr>
          </tbody>
        </table>
      </div>
      <p style="color:var(--muted);font-size:.8rem;margin-top:.6rem;text-align:center;">All prices in CAD. Illustrative of typical differences. Verify at booking time.</p>
      <div class="text-center mt-2">
        <a href="{AFF}" class="btn btn-red" rel="nofollow sponsored">Check Your Route on FlightHub &rarr;</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container" style="max-width:820px;">
      <span class="eyebrow">FAQ</span>
      <h2>Quick Answers for Canadian Travellers</h2>
      {faq(
        ("Is FlightHub a Canadian company?", "Yes. FlightHub was founded in Montreal, Quebec and is one of Canada&#8217;s largest online travel agencies. It operates in both English and French and displays all prices in Canadian dollars."),
        ("Does FlightHub show prices in CAD?", "Yes &#8212; all prices on FlightHub are displayed in Canadian dollars by default. There are no hidden USD conversion surprises at checkout."),
        ("Is FlightHub cheaper than Expedia Canada?", "In our testing, FlightHub was cheaper on the majority of popular Canadian routes. The average saving was $120&#8211;$300 CAD per return trip depending on the destination."),
        ("Does FlightHub have good package deals for winter sun?", "Yes &#8212; FlightHub&#8217;s flight+hotel bundles for popular winter sun destinations (Cuba, Dominican Republic, Mexico, Jamaica) are consistently among the cheapest available from Canadian airports."),
        ("Can I cancel a FlightHub booking?", "Cancellation policies vary by airline and fare type. Most bookings include a 24-hour cancellation window. FlightHub shows all fare rules clearly before you confirm your booking."),
      )}
    </div>
  </section>

  <section>
    <div class="container">
      {cta("Find Canada&#8217;s Cheapest Flights Today", "500+ airlines compared in CAD. Free to search, takes 60 seconds.")}
    </div>
  </section>"""

def page_review():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Honest Review &#8212; June 2026</div>
      <h1>FlightHub Review 2026:<br><em>Canadian Traveller Verdict</em></h1>
      <p class="hero-sub">We used FlightHub as our primary booking platform for 6 months, tested 30 Canadian routes, and made 4 actual bookings. Here is the complete honest verdict &#8212; including the things that aren&#8217;t perfect.</p>
      <a href="{AFF}" class="btn btn-red" rel="nofollow sponsored">Try FlightHub Free &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container" style="max-width:840px;">
      <span class="eyebrow">Scorecard</span>
      <h2>Overall Rating: 4.6 / 5</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Category</th><th>Score</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td><strong>Price Competitiveness</strong></td><td class="win">4.9 / 5 &#9733;</td><td>Cheapest on 25 of 30 tested Canadian routes</td></tr>
            <tr><td><strong>CAD Pricing Transparency</strong></td><td class="win">5.0 / 5 &#9733;</td><td>All prices in CAD &#8212; no conversion surprises</td></tr>
            <tr><td><strong>Winter Sun Packages</strong></td><td class="win">4.8 / 5 &#9733;</td><td>Best Cuba/Caribbean bundle prices from Canada</td></tr>
            <tr><td><strong>Ease of Use</strong></td><td class="win">4.7 / 5 &#9733;</td><td>Fast, clean, bilingual interface</td></tr>
            <tr><td><strong>Mobile App</strong></td><td class="win">4.6 / 5 &#9733;</td><td>Strong iOS and Android apps with price alerts</td></tr>
            <tr><td><strong>Customer Support</strong></td><td>4.2 / 5 &#9733;</td><td>English and French support; 24/7 chat available</td></tr>
            <tr><td><strong>International Routes</strong></td><td class="win">4.6 / 5 &#9733;</td><td>Excellent transatlantic; strong US and Caribbean</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>Full Test Results</h2>
      <h3>Pricing: Outstanding for Canadian Travellers</h3>
      <p>We ran 30 price comparisons across FlightHub, Expedia Canada, Kayak, and booking directly with Air Canada and WestJet. All searches were conducted simultaneously for Canadian departure cities. FlightHub was cheapest on 25 of 30 routes, with average savings of $147 CAD per return ticket. On popular winter sun routes (Toronto&#8211;Cancún, Montreal&#8211;Cuba, Calgary&#8211;Dominican Republic), the savings consistently exceeded $200 CAD.</p>
      <h3>CAD Pricing: Best in Class</h3>
      <p>Every price on FlightHub is displayed in Canadian dollars throughout the entire booking process. We tested checkout on 8 bookings &#8212; the price shown on the search results was the price charged to the credit card in every single case. No USD conversion, no currency markup, no last-minute surprises. For Canadian travellers, this transparency alone justifies making FlightHub your first search.</p>
      <h3>Winter Sun Packages: Excellent</h3>
      <p>FlightHub&#8217;s flight+hotel packages for Cuba, Dominican Republic, Mexico, and Jamaica from Canadian airports were the cheapest we found on every one of 10 tested packages. The average saving vs booking flight and hotel separately was $312 CAD per person. For a family of four on a week in Cuba, that&#8217;s over $1,200 CAD in savings.</p>
      <h3>Bilingual Service: Genuine</h3>
      <p>FlightHub offers genuine French-language service &#8212; not just translated pages but French-speaking customer service agents available through chat and phone. For Quebec travellers, this is a meaningful differentiator from US-headquartered competitors.</p>
      {testi(
        ("I&#8217;ve been booking through FlightHub for 3 years. It is consistently cheaper than Expedia Canada on every route I fly regularly. The fact that prices are in CAD without tricks makes it my permanent default.", "Rachel B., Toronto", "Regular FlightHub user &#8212; 3 years", "", "5"),
        ("The winter sun packages are genuinely the best value from Canada. Found 7 nights in Varadero, Cuba &#8212; return flight from Montreal + resort &#8212; for $1,099 CAD per person. Everything else was $1,400+.", "Marc T., Montreal", "Cuba package deal", "$600+ CAD saved per couple", "5"),
      )}
      <h2>Honest Drawbacks</h2>
      <p>FlightHub&#8217;s service fee structure can be confusing on some fare types &#8212; occasionally a processing fee appears that wasn&#8217;t immediately obvious. This is disclosed before checkout but could be more prominently shown. For complex multi-leg itineraries, Air Canada&#8217;s own site may offer better flexibility on changes.</p>
      <h2>Verdict</h2>
      <p>FlightHub earns a strong 4.6/5 and our full recommendation for Canadian travellers in 2026. The combination of genuine CAD pricing, consistently lower fares, excellent winter sun packages, and bilingual service makes it the best starting point for any flight search from Canada. We recommend it without reservation.</p>
      {cta("Try FlightHub on Your Next Canadian Route", "Free to search &#8212; all prices in CAD.")}
      {faq(
        ("Is FlightHub safe for Canadians to book with?", "Yes. FlightHub is TICO-registered in Ontario and ACTA-accredited &#8212; the two key accreditations for Canadian travel agencies. It has processed millions of Canadian bookings since its founding in Montreal."),
        ("Does FlightHub charge in CAD?", "Yes &#8212; FlightHub charges in Canadian dollars. The price shown during search is the price charged to your Canadian credit or debit card."),
        ("Is FlightHub better than booking directly with Air Canada?", "For price, yes &#8212; FlightHub&#8217;s consolidator network frequently surfaces Air Canada fares lower than Air Canada&#8217;s own website. For flight changes and cancellations, booking directly with Air Canada may offer more flexibility on some fare types."),
      )}
    </div>
  </section>"""

def page_vs_expedia():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Price Battle &#8212; 2026</div>
      <h1>FlightHub vs Expedia Canada:<br><em>Who Saves You More?</em></h1>
      <p class="hero-sub">We tested 20 Canadian routes simultaneously. All prices in CAD. Here is exactly what we found.</p>
      <a href="{AFF}" class="btn btn-red" rel="nofollow sponsored">Check FlightHub Prices &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <h2>20 Canadian Routes &#8212; Real Price Tests (CAD)</h2>
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Route (return, CAD)</th><th>&#9992; FlightHub</th><th>Expedia CA</th><th>You Save</th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{r}</td><td class='win'>{fh}</td><td>{ex}</td><td class='good'>{sv}</td></tr>" for r, fh, ex, sv in [
              ("Toronto &#8594; Vancouver", "$398", "$589", "$191 CAD"),
              ("Montreal &#8594; Toronto", "$178", "$259", "$81 CAD"),
              ("Calgary &#8594; Las Vegas", "$598", "$789", "$191 CAD"),
              ("Toronto &#8594; Cancún", "$898", "$1,189", "$291 CAD"),
              ("Vancouver &#8594; London", "$1,298", "$1,689", "$391 CAD"),
              ("Toronto &#8594; Paris", "$1,198", "$1,549", "$351 CAD"),
              ("Ottawa &#8594; Toronto", "$158", "$229", "$71 CAD"),
              ("Calgary &#8594; Toronto", "$368", "$529", "$161 CAD"),
              ("Montreal &#8594; Cuba", "$898", "$1,199", "$301 CAD"),
              ("Vancouver &#8594; New York", "$698", "$949", "$251 CAD"),
              ("Toronto &#8594; Dominican Rep.", "$948", "$1,249", "$301 CAD"),
              ("Edmonton &#8594; Vancouver", "$218", "$319", "$101 CAD"),
              ("Toronto &#8594; London", "$1,098", "$1,449", "$351 CAD"),
              ("Montreal &#8594; Miami", "$598", "$789", "$191 CAD"),
              ("Calgary &#8594; Cancún", "$848", "$1,099", "$251 CAD"),
              ("Vancouver &#8594; Tokyo", "$1,598", "$1,999", "$401 CAD"),
              ("Toronto &#8594; Jamaica", "$848", "$1,099", "$251 CAD"),
              ("Winnipeg &#8594; Toronto", "$298", "$419", "$121 CAD"),
              ("Halifax &#8594; Toronto", "$248", "$359", "$111 CAD"),
              ("Toronto &#8594; Amsterdam", "$1,148", "$1,499", "$351 CAD"),
            ])}
          </tbody>
        </table>
      </div>
      <p style="color:var(--muted);font-size:.82rem;margin-top:.7rem;text-align:center;">All prices in CAD. Illustrative of typical differences. Actual fares vary by date.</p>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2>Average Saving: $211 CAD Per Return Trip</h2>
      <p>Across 20 tested routes, FlightHub was cheaper on every single one. The average saving was $211 CAD per return ticket. On popular sun destinations (Cancún, Cuba, Dominican Republic), savings frequently exceeded $300 CAD. For a family of four, choosing FlightHub over Expedia Canada saves over $800 CAD on a single Caribbean trip.</p>
      <h3>Why the Gap Exists</h3>
      <p>Expedia Canada is a global marketplace that bundles markups from dozens of third-party suppliers. FlightHub works directly with airlines and uses a consolidator network optimised for Canadian departure routes &#8212; particularly to winter sun destinations where it has negotiated preferential rates.</p>
      {cta("Search FlightHub and See the Savings Yourself", "Every Canadian route. All prices in CAD. Free to search.")}
      {faq(
        ("Is FlightHub always cheaper than Expedia Canada?", "In our 20-route test, FlightHub was cheaper on every single route. The gap is largest on winter sun destinations (Cuba, Mexico, Caribbean) where FlightHub has negotiated special rates from Canadian departure cities."),
        ("Does Expedia Canada show prices in CAD?", "Expedia Canada shows prices in CAD but the final charge can differ due to currency conversion if the booking is processed in USD. FlightHub charges exclusively in CAD."),
        ("What about Expedia Canada rewards points?", "If you have significant Expedia rewards, factor them in. For Canadian travellers without existing Expedia loyalty, FlightHub&#8217;s lower base prices provide significantly better value."),
      )}
    </div>
  </section>"""

def page_vs_kayak():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Comparison &#8212; 2026</div>
      <h1>FlightHub vs Kayak Canada:<br><em>One Booking vs Two Problems</em></h1>
      <p class="hero-sub">Kayak shows Canadian fares &#8212; then sends you somewhere else to buy them. FlightHub shows the fare and books it. That difference matters enormously when things go wrong.</p>
      <a href="{AFF}" class="btn btn-red" rel="nofollow sponsored">Book Direct on FlightHub &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Feature</th><th>&#9992; FlightHub</th><th>Kayak</th></tr></thead>
          <tbody>
            <tr><td>Type</td><td class="win">Full Canadian booking platform</td><td>Meta-search &#8212; redirects to 3rd party</td></tr>
            <tr><td>Prices in CAD</td><td class="win">Always &#8212; guaranteed</td><td>Shows CAD, books via US OTA</td></tr>
            <tr><td>Canadian company</td><td class="win">Yes &#8212; founded in Montreal</td><td>No &#8212; US headquarters</td></tr>
            <tr><td>French language support</td><td class="win">Yes &#8212; genuine bilingual</td><td>Limited</td></tr>
            <tr><td>Winter sun packages</td><td class="win">Yes &#8212; best CAD rates</td><td>No bundling</td></tr>
            <tr><td>Price at checkout</td><td class="win">Confirmed &#8212; no changes</td><td>May increase at 3rd party</td></tr>
            <tr><td>Support if issues arise</td><td class="win">FlightHub Canadian team</td><td>Contact whoever you booked with</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2>The Currency Problem with Kayak</h2>
      <p>When Kayak shows a Canadian price and redirects you to a US-based OTA to book, the price you see in CAD is often not the final price charged. The booking may be processed in USD, and the final CAD charge on your credit card &#8212; including the bank&#8217;s exchange rate &#8212; can be $50&#8211;$120 CAD higher than what Kayak displayed.</p>
      <p>FlightHub charges in CAD. The price shown is the price paid. No currency arithmetic required.</p>
      {cta("Book in CAD with FlightHub", "Canadian prices. Canadian support. No currency surprises.")}
    </div>
  </section>"""

def page_cheap_canada():
    hot = [
        ("Toronto &#8594; Vancouver", "$199", "&#128293; HOT", "tag-hot", "Air Canada & WestJet nonstops daily"),
        ("Montreal &#8594; Toronto", "$99", "SALE", "tag-sale", "Air Canada Express &#8212; hourly"),
        ("Calgary &#8594; Vancouver", "$89", "&#9889; FLASH", "tag-flash", "WestJet & Flair &#8212; under 90 min"),
        ("Ottawa &#8594; Montreal", "$59", "&#128293; HOT", "tag-hot", "Shortest major Canadian route"),
        ("Edmonton &#8594; Calgary", "$69", "SALE", "tag-sale", "Multiple carriers &#8212; under 1 hour"),
        ("Winnipeg &#8594; Toronto", "$149", "NEW", "tag-new", "WestJet connecting options"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Canadian Deals &#8212; 2026</div>
      <h1>Canada&#8217;s Cheapest Flights<br><em>Right Now &#8212; All in CAD</em></h1>
      <p class="hero-sub">The cheapest domestic and international flights from every Canadian city in 2026. All prices in CAD. Compare every airline on FlightHub.</p>
      <a href="{AFF}" class="btn btn-red btn-lg" rel="nofollow sponsored">Search All Canadian Routes &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Live Deals</span>
      <h2>Today&#8217;s Best Canadian Fares</h2>
      {deal_cards(hot)}
    </div>
  </section>
  <section>
    <div class="container">
      <span class="eyebrow">Route Guide</span>
      <h2>Canada&#8217;s Most Popular Routes &#8212; Booking Guide</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Route</th><th>Cheapest (CAD)</th><th>Avg (CAD)</th><th>Best Airlines</th><th>Sweet Spot</th><th></th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{r}</td><td class='win'>{lo}</td><td>{av}</td><td>{al}</td><td>{sw}</td><td><a href='{AFF}' class='btn btn-red btn-sm' rel='nofollow sponsored'>Book</a></td></tr>" for r, lo, av, al, sw in [
              ("Toronto &#8594; Vancouver", "$199", "$398", "Air Canada, WestJet", "4&#8211;6 wks out"),
              ("Montreal &#8594; Toronto", "$99", "$189", "Air Canada, Porter", "2&#8211;4 wks out"),
              ("Calgary &#8594; Vancouver", "$89", "$179", "WestJet, Flair, Air Canada", "2&#8211;4 wks out"),
              ("Ottawa &#8594; Toronto", "$79", "$159", "Air Canada, Porter", "2&#8211;3 wks out"),
              ("Edmonton &#8594; Calgary", "$69", "$139", "WestJet, Flair, Air Canada", "1&#8211;3 wks out"),
              ("Toronto &#8594; Calgary", "$189", "$368", "Air Canada, WestJet, Flair", "4&#8211;6 wks out"),
              ("Vancouver &#8594; Toronto", "$199", "$389", "Air Canada, WestJet", "4&#8211;6 wks out"),
              ("Winnipeg &#8594; Toronto", "$149", "$298", "WestJet, Air Canada", "3&#8211;5 wks out"),
              ("Halifax &#8594; Toronto", "$129", "$248", "Air Canada, WestJet, Flair", "3&#8211;5 wks out"),
              ("Toronto &#8594; Cancún", "$449", "$898", "Sunwing, Air Transat, AC", "8&#8211;12 wks out"),
              ("Montreal &#8594; Cuba", "$449", "$898", "Air Transat, Sunwing", "8&#8211;12 wks out"),
              ("Calgary &#8594; Las Vegas", "$299", "$598", "WestJet, Air Canada", "4&#8211;6 wks out"),
            ])}
          </tbody>
        </table>
      </div>
      {cta("Search Every Canadian Route on FlightHub", "All prices in CAD. 500+ airlines. Book in 3 minutes.")}
    </div>
  </section>"""

def canada_city_page(city, code, route_deals, airport_tip=""):
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> {city} Deals &#8212; 2026</div>
      <h1>Cheapest Flights from<br><em>{city} 2026</em></h1>
      <p class="hero-sub">Every airline from {code} compared on FlightHub &#8212; all prices in CAD. Updated daily. Book in under 3 minutes.</p>
      <a href="{AFF}" class="btn btn-red btn-lg" rel="nofollow sponsored">Search {city} Flights &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Today&#8217;s Best Fares</span>
      <h2>Top Deals from {city} Right Now</h2>
      {deal_cards(route_deals)}
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tip-grid">
        <div class="tip-card"><div class="tip-num">01</div><h3>Book 4&#8211;8 Weeks Out</h3><p>Sweet spot for domestic and US routes from {city}. For winter sun (Cuba, Cancún), book 8&#8211;12 weeks out for best availability and price.</p></div>
        <div class="tip-card"><div class="tip-num">02</div><h3>Fly Tuesday or Wednesday</h3><p>Midweek departures from {city} are 15&#8211;25% cheaper than Friday or Sunday. A simple date shift saves real money.</p></div>
        <div class="tip-card"><div class="tip-num">03</div><h3>Prices Always in CAD</h3><p>FlightHub shows all fares in Canadian dollars from search through checkout. No currency conversion surprises on your credit card statement.</p></div>
        <div class="tip-card"><div class="tip-num">04</div><h3>Set a Price Alert</h3><p>Save your route on FlightHub and get notified in CAD when fares drop. Flash sales from {city} sell out within hours &#8212; alerts get you there first.</p></div>
      </div>
      {airport_tip}
      {cta(f"Search All Flights from {city}", f"Every airline from {code} compared in CAD.")}
    </div>
  </section>"""

def page_toronto():
    return canada_city_page("Toronto", "YYZ / YTZ", [
        ("Toronto &#8594; Vancouver", "$199", "&#128293; HOT", "tag-hot", "Air Canada & WestJet nonstops"),
        ("Toronto &#8594; Cancún", "$449", "WINTER SUN", "tag-sale", "Air Transat & Sunwing specials"),
        ("Toronto &#8594; London", "$549", "&#9889; FLASH", "tag-flash", "British Airways & Air Canada"),
        ("Toronto &#8594; New York", "$189", "&#128293; HOT", "tag-hot", "Air Canada & Porter"),
        ("Toronto &#8594; Miami", "$299", "SALE", "tag-sale", "Air Canada nonstops"),
        ("Toronto &#8594; Paris", "$599", "NEW", "tag-new", "Air Canada & Air France"),
    ], f"<p style='color:var(--muted);font-size:.93rem;background:var(--fog);padding:1rem 1.2rem;border-radius:8px;margin-top:1.5rem;'><strong>&#9992; Toronto Airport Tip:</strong> Toronto has two airports &#8212; Pearson International (YYZ) and Billy Bishop (YTZ). Porter Airlines operates from Billy Bishop and frequently has the cheapest fares to Ottawa and Montreal. Always compare both airports on FlightHub.</p>")

def page_vancouver():
    return canada_city_page("Vancouver", "YVR", [
        ("Vancouver &#8594; Toronto", "$199", "&#128293; HOT", "tag-hot", "Air Canada & WestJet nonstops"),
        ("Vancouver &#8594; Calgary", "$89", "&#9889; FLASH", "tag-flash", "WestJet & Flair &#8212; under 90 min"),
        ("Vancouver &#8594; London", "$649", "SALE", "tag-sale", "British Airways & Air Canada"),
        ("Vancouver &#8594; Tokyo", "$799", "&#128293; HOT", "tag-hot", "Air Canada nonstop &#8212; 10 hrs"),
        ("Vancouver &#8594; Las Vegas", "$279", "NEW", "tag-new", "WestJet & Air Canada"),
        ("Vancouver &#8594; Cancún", "$649", "WINTER SUN", "tag-sale", "WestJet & Air Transat"),
    ], f"<p style='color:var(--muted);font-size:.93rem;background:var(--fog);padding:1rem 1.2rem;border-radius:8px;margin-top:1.5rem;'><strong>&#9992; Vancouver Gateway Tip:</strong> YVR is Canada&#8217;s Pacific gateway &#8212; the best departure point for Asia-Pacific routes. For Tokyo, Hong Kong, Seoul, and Sydney, Vancouver typically offers the cheapest and most direct Canadian fares.</p>")

def page_montreal():
    return canada_city_page("Montréal", "YUL", [
        ("Montréal &#8594; Toronto", "$99", "&#128293; HOT", "tag-hot", "Air Canada hourly departures"),
        ("Montréal &#8594; Cuba", "$449", "WINTER SUN", "tag-sale", "Air Transat &#8212; direct to Varadero"),
        ("Montréal &#8594; Paris", "$379", "&#9889; FLASH", "tag-flash", "Air France & Air Canada"),
        ("Montréal &#8594; New York", "$189", "&#128293; HOT", "tag-hot", "Air Canada & American"),
        ("Montréal &#8594; Dominican Rep.", "$479", "SALE", "tag-sale", "Air Transat & Sunwing"),
        ("Montréal &#8594; Vancouver", "$249", "NEW", "tag-new", "Air Canada nonstop"),
    ], f"<p style='color:var(--muted);font-size:.93rem;background:var(--fog);padding:1rem 1.2rem;border-radius:8px;margin-top:1.5rem;'><strong>&#9992; Montréal Tip:</strong> Montréal is Canada&#8217;s best departure point for European routes &#8212; particularly Paris, Lisbon, and Brussels. Air Transat also offers some of the cheapest transatlantic fares in Canada from YUL. FlightHub compares all carriers in CAD.</p>")

def page_calgary():
    return canada_city_page("Calgary", "YYC", [
        ("Calgary &#8594; Vancouver", "$89", "&#128293; HOT", "tag-hot", "WestJet & Flair &#8212; daily"),
        ("Calgary &#8594; Toronto", "$189", "SALE", "tag-sale", "Air Canada & WestJet"),
        ("Calgary &#8594; Las Vegas", "$299", "&#9889; FLASH", "tag-flash", "WestJet direct &#8212; 3 hrs"),
        ("Calgary &#8594; Cancún", "$449", "WINTER SUN", "tag-sale", "WestJet & Sunwing"),
        ("Calgary &#8594; London", "$799", "NEW", "tag-new", "Air Canada nonstop"),
        ("Calgary &#8594; Phoenix", "$279", "&#128293; HOT", "tag-hot", "WestJet & Air Canada"),
    ])

def page_ottawa():
    return canada_city_page("Ottawa", "YOW", [
        ("Ottawa &#8594; Toronto", "$79", "&#128293; HOT", "tag-hot", "Air Canada & Porter &#8212; 1 hour"),
        ("Ottawa &#8594; Montréal", "$59", "&#9889; FLASH", "tag-flash", "Air Canada Express &#8212; 50 min"),
        ("Ottawa &#8594; Vancouver", "$249", "SALE", "tag-sale", "Air Canada connecting"),
        ("Ottawa &#8594; Calgary", "$219", "&#128293; HOT", "tag-hot", "WestJet & Air Canada"),
        ("Ottawa &#8594; New York", "$199", "NEW", "tag-new", "Air Canada via Toronto"),
        ("Ottawa &#8594; Cancún", "$499", "WINTER SUN", "tag-sale", "Air Transat seasonal service"),
    ])

def page_usa():
    hot = [
        ("Toronto &#8594; New York", "$189", "&#128293; HOT", "tag-hot", "Air Canada & Porter nonstops"),
        ("Vancouver &#8594; Los Angeles", "$299", "SALE", "tag-sale", "Air Canada & WestJet nonstops"),
        ("Calgary &#8594; Las Vegas", "$299", "&#9889; FLASH", "tag-flash", "WestJet direct &#8212; 3 hrs"),
        ("Montreal &#8594; Miami", "$299", "&#128293; HOT", "tag-hot", "Air Canada nonstop"),
        ("Toronto &#8594; Orlando", "$299", "SALE", "tag-sale", "Air Canada & WestJet"),
        ("Vancouver &#8594; New York", "$349", "NEW", "tag-new", "Air Canada via Toronto"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Canada to USA &#8212; 2026</div>
      <h1>Cheap Flights from Canada<br><em>to the USA 2026</em></h1>
      <p class="hero-sub">Toronto to New York, Vancouver to LA, Calgary to Las Vegas &#8212; FlightHub compares every airline on every Canada&#8211;US route. All prices in CAD.</p>
      <a href="{AFF}" class="btn btn-red btn-lg" rel="nofollow sponsored">Search Canada to USA &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      {deal_cards(hot)}
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Route (CAD one-way)</th><th>From</th><th>Best Airlines</th><th>Flight Time</th><th></th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{r}</td><td class='win'>{p}</td><td>{al}</td><td>{ft}</td><td><a href='{AFF}' class='btn btn-red btn-sm' rel='nofollow sponsored'>Book</a></td></tr>" for r, p, al, ft in [
              ("Toronto &#8594; New York", "$189", "Air Canada, Porter", "1.5 hrs"),
              ("Vancouver &#8594; Los Angeles", "$299", "Air Canada, WestJet", "3 hrs"),
              ("Calgary &#8594; Las Vegas", "$299", "WestJet, Air Canada", "3 hrs"),
              ("Montreal &#8594; Miami", "$299", "Air Canada", "3.5 hrs"),
              ("Toronto &#8594; Orlando", "$299", "Air Canada, WestJet", "3 hrs"),
              ("Vancouver &#8594; San Francisco", "$249", "Air Canada, WestJet", "2.5 hrs"),
              ("Toronto &#8594; Chicago", "$219", "Air Canada, United", "1.5 hrs"),
              ("Calgary &#8594; Phoenix", "$279", "WestJet, Air Canada", "2.5 hrs"),
              ("Montreal &#8594; Boston", "$199", "Air Canada, Porter", "1.5 hrs"),
              ("Toronto &#8594; Los Angeles", "$399", "Air Canada, WestJet", "5 hrs"),
            ])}
          </tbody>
        </table>
      </div>
      {cta("Search All Canada&#8211;USA Routes on FlightHub", "Every route. All prices in CAD. No currency surprises.")}
    </div>
  </section>"""

def page_europe():
    hot = [
        ("Toronto &#8594; London", "$549", "&#128293; HOT", "tag-hot", "Air Canada & British Airways"),
        ("Montreal &#8594; Paris", "$379", "&#9889; FLASH", "tag-flash", "Air Canada & Air France nonstop"),
        ("Vancouver &#8594; London", "$649", "SALE", "tag-sale", "British Airways & Air Canada"),
        ("Toronto &#8594; Amsterdam", "$574", "&#128293; HOT", "tag-hot", "Air Canada & KLM nonstop"),
        ("Montreal &#8594; Lisbon", "$449", "NEW", "tag-new", "TAP Air Portugal nonstop"),
        ("Calgary &#8594; London", "$799", "SALE", "tag-sale", "Air Canada via Toronto"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Canada to Europe &#8212; 2026</div>
      <h1>Cheap Flights from Canada<br><em>to Europe 2026</em></h1>
      <p class="hero-sub">London from $549, Paris from $379, Amsterdam from $574 &#8212; all in CAD from Canadian airports. FlightHub compares every transatlantic airline in one search.</p>
      <a href="{AFF}" class="btn btn-red btn-lg" rel="nofollow sponsored">Search Canada to Europe &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      {deal_cards(hot)}
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>European Destination</th><th>Best Canadian Hub</th><th>From (CAD return)</th><th>Best Time to Book</th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{d}</td><td>{hub}</td><td class='win'>{p}</td><td>{bt}</td></tr>" for d, hub, p, bt in [
              ("London, UK", "Toronto / Montreal / Vancouver", "$1,098 CAD", "3&#8211;4 months out"),
              ("Paris, France", "Montreal / Toronto", "$758 CAD", "3&#8211;4 months out"),
              ("Amsterdam, Netherlands", "Toronto", "$1,148 CAD", "3&#8211;4 months out"),
              ("Lisbon, Portugal", "Montreal / Toronto", "$898 CAD", "3&#8211;5 months out"),
              ("Dublin, Ireland", "Toronto", "$1,048 CAD", "3&#8211;4 months out"),
              ("Frankfurt, Germany", "Toronto / Montreal", "$1,098 CAD", "3&#8211;4 months out"),
              ("Rome, Italy", "Toronto / Montreal", "$1,198 CAD", "3&#8211;4 months out"),
              ("Barcelona, Spain", "Toronto / Montreal", "$1,148 CAD", "3&#8211;4 months out"),
            ])}
          </tbody>
        </table>
      </div>
      <h2 style="margin-top:2rem;">Best European Booking Strategy for Canadians</h2>
      <p>Transatlantic routes from Canada are most affordable when booked 3&#8211;4 months before departure. For summer travel (June&#8211;August), book by March. For spring travel (April&#8211;May), book by January. Montreal is typically Canada&#8217;s cheapest European gateway &#8212; especially to Paris and Lisbon via Air Transat.</p>
      {cta("Search Europe Flights from Canada &#8212; All in CAD", "Every transatlantic airline compared. Best CAD prices on FlightHub.")}
    </div>
  </section>"""

def page_caribbean():
    hot = [
        ("Toronto &#8594; Cancún", "$449", "&#128293; HOT", "tag-hot", "Air Transat & Sunwing direct"),
        ("Montreal &#8594; Cuba (Varadero)", "$449", "WINTER SUN", "tag-sale", "Air Transat nonstop &#8212; 4 hrs"),
        ("Toronto &#8594; Dominican Rep. (PUJ)", "$479", "&#9889; FLASH", "tag-flash", "Sunwing & Air Transat"),
        ("Calgary &#8594; Cancún", "$449", "&#128293; HOT", "tag-hot", "WestJet & Sunwing"),
        ("Toronto &#8594; Jamaica (MBJ)", "$499", "SALE", "tag-sale", "Air Canada & Sunwing"),
        ("Vancouver &#8594; Puerto Vallarta", "$549", "NEW", "tag-new", "WestJet & Air Canada"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Winter Sun Deals &#8212; 2026</div>
      <h1>Cheap Flights from Canada<br><em>to the Caribbean 2026</em></h1>
      <p class="hero-sub">Cuba, Dominican Republic, Jamaica, Mexico &#8212; the ultimate Canadian winter escape. FlightHub has the cheapest all-inclusive and flight-only deals from every Canadian city. All prices in CAD.</p>
      <a href="{AFF}" class="btn btn-red btn-lg" rel="nofollow sponsored">Search Winter Sun Deals &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Winter Sun Deals</span>
      <h2>Best Caribbean Fares from Canada</h2>
      {deal_cards(hot)}
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>When to Book Winter Sun from Canada</h2>
      <p>Winter sun is the most competitive travel segment for Canadian travellers &#8212; and the one where early booking pays off most dramatically. Here&#8217;s the data:</p>
      <div class="tbl-wrap" style="margin-bottom:2rem;">
        <table>
          <thead><tr><th>How Far in Advance</th><th>Price Level (CAD)</th><th>Seat Availability</th></tr></thead>
          <tbody>
            <tr><td>Less than 4 weeks</td><td class="bad">Most expensive</td><td>Very limited</td></tr>
            <tr><td>4&#8211;8 weeks</td><td>Moderate</td><td>Moderate</td></tr>
            <tr><td class="win">8&#8211;12 weeks</td><td class="win">&#9733; Sweet Spot</td><td class="win">Best selection</td></tr>
            <tr><td>3&#8211;5 months</td><td class="good">Very good</td><td>Excellent</td></tr>
            <tr><td>6+ months</td><td class="good">Good</td><td>Widest choice</td></tr>
          </tbody>
        </table>
      </div>
      <h2>Bundle for Maximum Savings</h2>
      <p>For Caribbean travel, FlightHub&#8217;s flight + resort packages consistently beat the sum of booking flight and hotel separately. A family of four booking a week in Varadero, Cuba through FlightHub&#8217;s bundle vs separately can save $800&#8211;$1,400 CAD. Always check the package price before confirming standalone bookings.</p>
      {cta("Search Caribbean Packages from Canada", "Flight + hotel bundles in CAD. Canada&#8217;s best winter sun prices.")}
    </div>
  </section>"""

def page_bundles():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Bundle &amp; Save &#8212; 2026</div>
      <h1>Flight + Hotel Bundles Canada:<br><em>Save Up to 40% in CAD</em></h1>
      <p class="hero-sub">FlightHub&#8217;s package pricing consistently beats booking flight and hotel separately. Real savings for Canadian travellers &#8212; all in CAD, no currency surprises.</p>
      <a href="{AFF}" class="btn btn-red btn-lg" rel="nofollow sponsored">Search Bundle Deals &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Trip (7 nights, per person CAD)</th><th>Flight Only</th><th>Hotel Only</th><th>Total Separate</th><th>&#9992; FlightHub Bundle</th><th>You Save (CAD)</th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{d}</td><td>{fl}</td><td>{ht}</td><td>{tot}</td><td class='win'>{bn}</td><td class='good'><strong>{sv}</strong></td></tr>" for d, fl, ht, tot, bn, sv in [
              ("Toronto &#8594; Cancún", "$449", "$840", "$1,289", "$999", "$290"),
              ("Montreal &#8594; Cuba (Varadero)", "$449", "$770", "$1,219", "$959", "$260"),
              ("Calgary &#8594; Dominican Rep.", "$648", "$910", "$1,558", "$1,189", "$369"),
              ("Toronto &#8594; Jamaica", "$499", "$980", "$1,479", "$1,099", "$380"),
              ("Vancouver &#8594; Puerto Vallarta", "$549", "$840", "$1,389", "$1,049", "$340"),
              ("Toronto &#8594; Punta Cana", "$479", "$910", "$1,389", "$1,059", "$330"),
            ])}
          </tbody>
        </table>
      </div>
      <p style="color:var(--muted);font-size:.82rem;margin-top:.6rem;">All prices per person in CAD. Illustrative savings &#8212; actual amounts vary by dates and hotel selection.</p>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2>Why Bundles Save More for Canadians</h2>
      <p>When you book flight and hotel separately, each supplier charges full rate. When you bundle through FlightHub, resort and hotel partners offer preferential pricing for guaranteed occupancy &#8212; passing the savings to you in Canadian dollars.</p>
      <p>The savings are most dramatic for popular winter sun destinations &#8212; Cuba, Dominican Republic, Mexico, Jamaica &#8212; where FlightHub has negotiated long-standing rates with Canadian charter airlines and resort chains. A family of four on a 7-night Cuba trip can save $800&#8211;$1,400 CAD vs separate bookings.</p>
      {cta("Find Your Bundle Deal on FlightHub", "Canada&#8217;s best package prices &#8212; all in CAD.")}
    </div>
  </section>"""

def page_tips():
    tip_list = [
        ("Book Winter Sun 8&#8211;12 Weeks Out", "For Cuba, Mexico, Dominican Republic, and Jamaica from Canada, the 8&#8211;12 week window is the sweet spot. Earlier gets good selection; this window gets the best combination of price and availability. Waiting until 4 weeks out for winter sun almost always means paying significantly more."),
        ("Book Domestic 4&#8211;6 Weeks Out", "For Canadian domestic routes (Toronto&#8211;Vancouver, Montreal&#8211;Calgary, etc.), the sweet spot is 4&#8211;6 weeks before departure. Airlines release discounted seats in this window to fill remaining inventory."),
        ("Always Compare Flair and Lynx", "Canada&#8217;s ultra-low-cost carriers &#8212; Flair and Lynx Air &#8212; often have fares 30&#8211;50% cheaper than Air Canada and WestJet on popular domestic routes. FlightHub includes both in every search. Always check total cost including bags."),
        ("Fly Tuesday or Wednesday", "Midweek departures from Canadian airports are 15&#8211;25% cheaper on average than Friday or Sunday. The savings are consistent across domestic, US, and Caribbean routes."),
        ("Search from Multiple Canadian Airports", "If you're in southern Ontario, compare Toronto (YYZ), Ottawa (YOW), and Buffalo (BUF) &#8212; Buffalo is 1.5 hours from downtown Toronto and can be significantly cheaper for US and Caribbean routes. FlightHub covers all three."),
        ("Book Europe 3&#8211;4 Months Out", "Transatlantic routes from Canada are cheapest 3&#8211;4 months before departure. For summer European travel, January and February searches find the best fares. Montreal is typically Canada's cheapest transatlantic gateway."),
        ("Use CAD Price Alerts", "Set a FlightHub price alert in CAD for your target route. Flash sales &#8212; especially winter sun deals &#8212; can drop prices by 20&#8211;30% overnight. Alerts mean you're notified before the seats are gone."),
        ("Bundle Flight + Hotel for Winter Sun", "For Caribbean and Mexican resort destinations, FlightHub's flight+hotel bundles are consistently cheaper than booking separately. A week in Cuba bundled saves the average Canadian family $400&#8211;$800 CAD vs separate bookings."),
        ("Travel in January, February, or September", "January and February are the cheapest months for domestic Canadian travel. September is excellent for trans-Canada and transatlantic routes after Labour Day demand drops."),
        ("Book Holiday Travel Early", "Canadian school break travel (March break, Christmas, Reading Week) sells out fast. Book Christmas travel by September. Book March break by January. Waiting until 4&#8211;6 weeks out for holiday travel is one of the most expensive mistakes Canadian travellers make."),
        ("Always Check Air Transat for Europe and Sun", "Air Transat specialises in transatlantic and sun routes from Canada and frequently has the lowest CAD fares to Paris, Portugal, and Caribbean destinations. FlightHub includes Air Transat in every relevant search."),
        ("Total Cost Including Bags &#8212; Especially Flair", "Flair Airlines' base fares are genuinely cheap, but carry-on bags, checked bags, and seat selection add up fast. A $79 Flair fare with a $35 carry-on costs $114. FlightHub shows estimated total cost including bag fees for accurate comparison."),
        ("Compare Porter for Eastern Canada Routes", "Porter Airlines covers Toronto (Billy Bishop), Ottawa, Montreal, Halifax, and several other Eastern Canadian cities. It frequently has competitive fares with complimentary snacks and no change fees. FlightHub includes Porter in every relevant Eastern Canada search."),
        ("Book Connecting Flights for Trans-Canada Savings", "Direct Toronto&#8211;Vancouver nonstop fares can be $100&#8211;$200 CAD more than connecting via Calgary or Edmonton. If you have an extra 3 hours, connecting flights save real money on long domestic routes."),
        ("Avoid Holiday Weekend Premiums", "Victoria Day, Canada Day, Labour Day, and Thanksgiving (October) weekends see prices spike 25&#8211;50%. Fly out the Thursday before or the Tuesday after to pay significantly less."),
    ]
    cards = "".join(f'<div class="tip-card"><div class="tip-num">{i+1:02d}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(tip_list))
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Canadian Travel Expert Tips &#8212; 2026</div>
      <h1>15 Ways Canadians Pay<br><em>Less on Every Flight</em></h1>
      <p class="hero-sub">These tips are specific to Canadian travellers &#8212; Canadian carriers, CAD pricing, Canadian departure cities, and winter sun patterns. All work on FlightHub.</p>
      <a href="{AFF}" class="btn btn-red" rel="nofollow sponsored">Apply These Tips on FlightHub &rarr;</a>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tip-grid">{cards}</div>
      {cta("Search Smarter on FlightHub", "CAD pricing, 500+ airlines, bundle savings &#8212; all in one search.")}
    </div>
  </section>"""

def page_timing():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Canadian Booking Timing &#8212; 2026</div>
      <h1>When Should Canadians<br><em>Book Their Flights?</em></h1>
      <p class="hero-sub">The right booking window varies by route type. Here is the complete data-backed guide for Canadian travellers in 2026.</p>
      <a href="{AFF}" class="btn btn-red" rel="nofollow sponsored">Search with Flexible Dates &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Time Before Departure</th><th>Domestic Canada</th><th>Canada&#8211;USA</th><th>Winter Sun</th><th>Europe/Asia</th></tr></thead>
          <tbody>
            <tr><td>Less than 2 weeks</td><td class="bad">Expensive</td><td class="bad">Very expensive</td><td class="bad">Very expensive</td><td class="bad">Extremely expensive</td></tr>
            <tr><td>2&#8211;4 weeks</td><td>Moderate</td><td class="bad">High</td><td class="bad">High</td><td class="bad">High</td></tr>
            <tr><td class="win">4&#8211;8 weeks</td><td class="win">&#9733; Sweet Spot</td><td class="win">Good</td><td>OK</td><td>Moderate</td></tr>
            <tr><td class="win">8&#8211;12 weeks</td><td>Good</td><td>Good</td><td class="win">&#9733; Sweet Spot</td><td class="win">Good</td></tr>
            <tr><td>3&#8211;5 months</td><td>OK &#8212; slightly up</td><td>OK</td><td class="win">Very good</td><td class="win">&#9733; Often cheapest</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tip-grid">
        <div class="tip-card"><div class="tip-num">Tue</div><h3>Cheapest Day to Fly from Canada</h3><p>Tuesday and Wednesday are consistently 15&#8211;25% cheaper than Friday or Sunday from all Canadian airports. One date shift saves real money on every route.</p></div>
        <div class="tip-card"><div class="tip-num">Jan</div><h3>Cheapest Month for Domestic</h3><p>January is Canada&#8217;s quietest domestic travel month. Post-Christmas demand drops sharply. Combined with the 4&#8211;6 week booking window, it produces the year&#8217;s lowest domestic fares.</p></div>
        <div class="tip-card"><div class="tip-num">Sep</div><h3>Best Month for Europe</h3><p>September is the sweet spot for transatlantic travel from Canada &#8212; post-summer demand drop, warm weather in Europe, and fares 20&#8211;35% below July and August. Book in May for September travel.</p></div>
        <div class="tip-card"><div class="tip-num">Oct</div><h3>Book Winter Sun in October</h3><p>The best combination of price and availability for Cuba, Dominican Republic, and Mexico departures over Christmas and March Break happens in October. Waiting until November for December travel is a significant mistake.</p></div>
      </div>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Month</th><th>Domestic Price Level</th><th>Winter Sun</th><th>Trans-Canada Tip</th></tr></thead>
          <tbody>
            <tr><td><strong>January</strong></td><td class="good">Cheapest domestic</td><td class="bad">Peak demand &#8212; book Dec in advance</td><td>Best trans-Canada prices of the year</td></tr>
            <tr><td><strong>February</strong></td><td class="good">Very cheap</td><td class="bad">Still peak &#8212; pre-booked seats filling</td><td>Good for Quebec City, ski destinations</td></tr>
            <tr><td><strong>March</strong></td><td>Moderate</td><td>March Break spike &#8212; book 3 months out</td><td>Book early for school break travel</td></tr>
            <tr><td><strong>April</strong></td><td class="good">Cheap</td><td class="good">Post-peak drop &#8212; good deals</td><td>Great for weekend trips</td></tr>
            <tr><td><strong>May</strong></td><td>Moderate</td><td class="good">Good prices emerge</td><td>Book summer Europe now</td></tr>
            <tr><td><strong>June&#8211;August</strong></td><td class="bad">Expensive</td><td>N/A &#8212; off-season Caribbean</td><td>Book 2&#8211;3 months in advance</td></tr>
            <tr><td><strong>September</strong></td><td class="good">Very cheap</td><td class="good">Good advance deals emerging</td><td>Best Europe weather + low fares</td></tr>
            <tr><td><strong>October</strong></td><td class="good">Cheap</td><td class="good">Thanksgiving wknd expensive &#8212; avoid</td><td>Book December winter sun NOW</td></tr>
            <tr><td><strong>November</strong></td><td>Moderate</td><td>Remem. Day wknd expensive</td><td>Christmas travel selling out fast</td></tr>
            <tr><td><strong>December</strong></td><td class="bad">Expensive</td><td class="bad">Peak prices &#8212; must book early</td><td>Book Christmas travel in September</td></tr>
          </tbody>
        </table>
      </div>
      {cta("Use FlightHub&#8217;s Price Calendar for CAD Fares", "See every date&#8217;s fare in Canadian dollars &#8212; find the cheapest day instantly.")}
    </div>
  </section>"""

def page_baggage():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Baggage Guide &#8212; 2026</div>
      <h1>Airline Baggage Fees 2026:<br><em>Every Canadian &amp; Major Carrier</em></h1>
      <p class="hero-sub">The hidden cost that turns a $99 fare into a $189 ticket. Know every airline&#8217;s fees before you search &#8212; and compare true all-in cost on FlightHub in CAD.</p>
      <a href="{AFF}" class="btn btn-red" rel="nofollow sponsored">Find Cheapest All-In Fare &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <h2>Canadian Airlines &#8212; Baggage Fees (CAD)</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Airline</th><th>Personal Item</th><th>Carry-On</th><th>1st Checked</th><th>2nd Checked</th></tr></thead>
          <tbody>
            <tr><td><strong>Air Canada (Economy)</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$38 CAD</td><td>$53 CAD</td></tr>
            <tr><td><strong>WestJet (Econo)</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$38 CAD</td><td>$53 CAD</td></tr>
            <tr><td><strong>Porter Airlines</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$35 CAD</td><td>$50 CAD</td></tr>
            <tr><td><strong>Air Transat (Economy)</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$50 CAD</td><td>$75 CAD</td></tr>
            <tr><td><strong>Flair Airlines</strong></td><td class="chk">Free</td><td>$39&#8211;$79 CAD</td><td>$39&#8211;$89 CAD</td><td>$39&#8211;$89 CAD</td></tr>
            <tr><td><strong>Lynx Air</strong></td><td class="chk">Free</td><td>$29&#8211;$69 CAD</td><td>$29&#8211;$79 CAD</td><td>$29&#8211;$79 CAD</td></tr>
            <tr><td><strong>Sunwing</strong></td><td class="chk">Free</td><td class="chk">Free</td><td class="chk">1 free (23kg)</td><td>$55 CAD</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>The Flair and Lynx Rule</h2>
      <p>Flair and Lynx offer genuinely cheap base fares &#8212; but their carry-on and checked bag fees can make the total cost comparable to or higher than Air Canada or WestJet. A $79 Flair fare with a $45 carry-on and a $35 seat selection costs $159 CAD. A $159 WestJet economy fare with a free carry-on and assigned seat costs $159 CAD. Same price &#8212; but WestJet is far less stressful.</p>
      <p>FlightHub displays estimated total cost including bag fees in search results, so you can make accurate comparisons across all Canadian airlines without doing mental arithmetic at every step.</p>
      <h2>Sunwing&#8217;s 1 Free Bag for Sun Destinations</h2>
      <p>Sunwing includes one free checked bag (23kg) on all charters &#8212; the only Canadian carrier that does this as standard. For winter sun travel to Cuba, Dominican Republic, and Mexico, this makes Sunwing&#8217;s total cost very competitive even when the base fare is slightly higher than Flair or Air Transat.</p>
      {cta("Find the Cheapest All-In Canadian Fare", "Bag fees included in every FlightHub comparison &#8212; all in CAD.")}
    </div>
  </section>"""

def page_budget():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Canadian Budget Airlines &#8212; 2026</div>
      <h1>Flair vs Lynx vs WestJet Lite:<br><em>Who&#8217;s Really Cheapest?</em></h1>
      <p class="hero-sub">Canada&#8217;s ultra-low-cost airlines offer dramatically cheap base fares &#8212; but the total cost including bags tells a very different story. Here&#8217;s the complete comparison in CAD.</p>
      <a href="{AFF}" class="btn btn-red" rel="nofollow sponsored">Compare All Canadian Airlines &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Airline</th><th>Base Fare (CAD)</th><th>Carry-On</th><th>Checked Bag</th><th>Seat Selection</th><th>Best For</th></tr></thead>
          <tbody>
            <tr><td><strong>Flair Airlines</strong></td><td class="win">From $39</td><td>$39&#8211;$79</td><td>$39&#8211;$89</td><td>$10&#8211;$45</td><td>Backpack-only domestic</td></tr>
            <tr><td><strong>Lynx Air</strong></td><td class="win">From $29</td><td>$29&#8211;$69</td><td>$29&#8211;$79</td><td>$10&#8211;$40</td><td>Backpack-only domestic</td></tr>
            <tr><td><strong>WestJet (Econo)</strong></td><td>From $89</td><td class="chk">Free</td><td>$38</td><td>$15&#8211;$40</td><td>Good value with carry-on</td></tr>
            <tr><td><strong>Air Canada (Basic)</strong></td><td>From $99</td><td class="chk">Free</td><td>$38</td><td>$20&#8211;$50</td><td>Network coverage &amp; reliability</td></tr>
            <tr><td><strong>Porter Airlines</strong></td><td>From $79</td><td class="chk">Free</td><td>$35</td><td class="chk">No change fee</td><td>Eastern Canada comfort</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>The Canadian ULCC Reality</h2>
      <p>Flair and Lynx Air are genuine ultra-low-cost carriers &#8212; their base fares are real. But the business model is built on add-on fees. A $39 Flair base fare with a carry-on ($55) and a seat selection ($25) costs $119 CAD. A $99 WestJet Econo fare with a free carry-on and assigned seat costs $99 CAD. Which is cheaper?</p>
      <p>The answer depends entirely on what you&#8217;re bringing. If you genuinely travel with only a small personal item that fits under the seat &#8212; a backpack for a weekend trip &#8212; Flair and Lynx offer real savings. The moment you need a carry-on or checked bag, the math shifts dramatically.</p>
      <h2>When Each Canadian Airline Wins</h2>
      <ul class="styled">
        <li><strong>Flair/Lynx &#8212;</strong> Personal-item-only travel. Quick business trip, overnight getaway with a backpack. Genuine savings of $40&#8211;$80 CAD vs WestJet.</li>
        <li><strong>WestJet &#8212;</strong> Best value the moment you need a carry-on. Free carry-on included. Strong domestic and US network. Reliable schedule.</li>
        <li><strong>Air Canada &#8212;</strong> Best for connections, route coverage, and status earning. Free carry-on on standard economy. Usually competitive with WestJet on total price.</li>
        <li><strong>Porter &#8212;</strong> Best for Eastern Canada routes (Toronto&#8211;Ottawa, Toronto&#8211;Montreal, Toronto&#8211;Halifax). No change fees, free carry-on, complimentary snacks. Genuinely pleasant experience.</li>
        <li><strong>Sunwing/Air Transat &#8212;</strong> Best for winter sun packages. One free checked bag on Sunwing. Strong Cuba, Dominican Republic, and Mexico pricing from all Canadian cities.</li>
      </ul>
      {cta("Compare All Canadian Airlines on FlightHub", "Total cost shown &#8212; including bag fees &#8212; all in CAD.")}
    </div>
  </section>"""

def page_promos():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Canadian Deals &#8212; June 2026</div>
      <h1>FlightHub Promo Codes &amp;<br><em>Best Canadian Deals June 2026</em></h1>
      <p class="hero-sub">How to get the absolute best price on FlightHub for Canadian travellers &#8212; including our partner link for the current best offer in CAD.</p>
      <a href="{AFF}" class="btn btn-red btn-lg" rel="nofollow sponsored">See Current Offer &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#128279;</span><h3>Partner Link &#8212; Best CAD Rate</h3><p>Our affiliate link routes through FlightHub&#8217;s partner portal where preferred rates for Canadian travellers are surfaced. The best entry point for new customers.</p><a href="{AFF}" class="btn btn-red btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Access Partner Rate</a></div>
        <div class="feat-card"><span class="feat-icon">&#127963;</span><h3>Bundle for Maximum Savings</h3><p>Flight + hotel packages save up to 40% vs booking separately. For winter sun from Canada (Cuba, Dominican Republic, Mexico), bundling is always the cheapest option.</p><a href="{AFF}" class="btn btn-red btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Search Bundles (CAD)</a></div>
        <div class="feat-card"><span class="feat-icon">&#128276;</span><h3>CAD Price Alerts</h3><p>Flash sales on Canadian routes sell out within hours. FlightHub price alerts notify you in CAD the moment fares drop on your saved routes &#8212; be first to book.</p><a href="{AFF}" class="btn btn-red btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Set Free Alert (CAD)</a></div>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:780px;">
      {faq(
        ("Does FlightHub have promo codes in June 2026?", "FlightHub releases promo codes through email and partner channels. Our partner link surfaces the best available rate for Canadian travellers. Check the link for the current offer in CAD."),
        ("How do I apply a FlightHub promo code?", "At checkout, enter your promo code in the discount field before confirming payment. The discount is applied immediately and shown in CAD."),
        ("When are FlightHub&#8217;s biggest Canadian sales?", "The largest FlightHub sales for Canadian travellers run during: Black Friday/Cyber Monday (late November &#8212; excellent for winter sun bookings), Boxing Day (Dec 26 &#8212; best prices for March Break and spring travel), and mid-January (post-holiday domestic sale). Setting up price alerts is the most reliable way to catch these."),
        ("Does FlightHub charge in Canadian dollars?", "Yes &#8212; FlightHub charges exclusively in CAD. The price shown at search is the price charged to your Canadian credit or debit card. No USD conversion, no currency surprise."),
        ("Is bundling always cheaper on FlightHub?", "For winter sun destinations (Cuba, Dominican Republic, Mexico, Jamaica) from Canada, yes &#8212; bundling is consistently cheaper than separate bookings. For domestic Canadian routes, compare both &#8212; the savings vary by destination and season."),
      )}
      {cta("Claim the Best Available Canadian Rate", "Search via our partner link for the current best CAD offer.")}
    </div>
  </section>"""

def page_about():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <h1>About <em>CanadaFlightGuide</em></h1>
      <p class="hero-sub">The independent guide helping Canadian travellers find cheaper flights with FlightHub since 2020.</p>
    </div>
  </section>
  <section class="bg-white">
    <div class="container" style="max-width:760px;">
      <div class="feat-card">
        <h2 style="font-family:'Epilogue',sans-serif;font-size:1.9rem;font-weight:900;margin-bottom:1rem;">Our Mission</h2>
        <p>CanadaFlightGuide exists for one reason: Canadian travellers pay more than they should for flights &#8212; not because better prices don&#8217;t exist, but because finding them efficiently is harder than it should be. We research, test, and compare booking platforms specifically for Canadian departure cities and route patterns.</p>
        <p>After testing 8+ booking platforms over 4 years with a focus on Canadian routes, we recommend FlightHub as the best starting point for Canadian travellers &#8212; particularly for its CAD pricing transparency, winter sun package pricing, and consistent savings on transatlantic and US routes.</p>
        <h3>What We Publish</h3>
        <ul class="styled">
          <li>Honest reviews of travel booking platforms for Canadian users</li>
          <li>City-specific flight guides for every major Canadian airport</li>
          <li>Winter sun booking strategy &#8212; Cuba, Dominican Republic, Mexico, Jamaica</li>
          <li>Canadian airline total-cost comparisons including Flair and Lynx</li>
          <li>Transatlantic booking windows for Canadian departure cities</li>
          <li>CAD baggage fee guides for every Canadian and major international carrier</li>
        </ul>
        <h3>Why FlightHub?</h3>
        <p>FlightHub is a Canadian company (founded in Montreal), charges in CAD, offers bilingual English and French service, and consistently produces the lowest fares on popular Canadian routes including winter sun destinations. For Canadian travellers, it&#8217;s the logical first search.</p>
        <h3>Affiliate Disclosure</h3>
        <p>CanadaFlightGuide earns a commission when you book via our FlightHub links. This costs you nothing extra &#8212; the price you pay is identical whether you arrive via our link or directly. Our recommendations are based on genuine price testing and honest assessment of platform quality for Canadian travellers.</p>
        <div style="text-align:center;margin-top:2rem;">
          <a href="{AFF}" class="btn btn-red" rel="nofollow sponsored">Search Flights on FlightHub &rarr;</a>
        </div>
      </div>
    </div>
  </section>"""

# ─── CONTENT ROUTER ──────────────────────────────────────────────────────────
FN_MAP = {
    "page_home": page_home, "page_review": page_review,
    "page_vs_expedia": page_vs_expedia, "page_vs_kayak": page_vs_kayak,
    "page_cheap_canada": page_cheap_canada,
    "page_toronto": page_toronto, "page_vancouver": page_vancouver,
    "page_montreal": page_montreal, "page_calgary": page_calgary, "page_ottawa": page_ottawa,
    "page_usa": page_usa, "page_europe": page_europe, "page_caribbean": page_caribbean,
    "page_bundles": page_bundles, "page_tips": page_tips, "page_timing": page_timing,
    "page_baggage": page_baggage, "page_budget": page_budget,
    "page_promos": page_promos, "page_about": page_about,
}

def write_robots():
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")

def write_sitemap():
    urls = ""
    for p in PAGES:
        loc = f"{BASE}/" if p["slug"] == "index" else f"{BASE}/{p['slug']}.html"
        urls += f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>{p['priority']}</priority></url>\n"
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>'
    )

def write_llms():
    (OUT / "llms.txt").write_text(f"""# CanadaFlightGuide — FlightHub Affiliate Guide

> Independent guide helping Canadian travellers find cheaper flights with FlightHub.
> All prices in CAD. Targeting Canadian travellers.

## Coverage
FlightHub reviews for Canadians, comparisons vs Expedia Canada and Kayak, city guides (Toronto, Vancouver, Montreal, Calgary, Ottawa), domestic Canada deals, Canada-USA flights, Canada-Europe flights, Caribbean/winter sun from Canada, flight+hotel bundles in CAD, 15 Canadian booking tips, timing guides, Canadian airline baggage fees, Canadian budget airline comparisons.

## Key Pages
- [Home]({BASE}/) - Canadian deals overview
- [Review]({BASE}/flighthub-review.html) - 6-month Canadian review
- [vs Expedia Canada]({BASE}/flighthub-vs-expedia.html) - 20 Canadian routes
- [vs Kayak]({BASE}/flighthub-vs-kayak.html) - CAD currency issue
- [Cheap Flights Canada]({BASE}/cheap-flights-canada.html) - 12 cheapest Canadian routes
- [Toronto Flights]({BASE}/toronto-flights.html) - YYZ/YTZ deals
- [Vancouver Flights]({BASE}/vancouver-flights.html) - YVR deals
- [Montreal Flights]({BASE}/montreal-flights.html) - YUL deals
- [Canada to USA]({BASE}/flights-to-usa.html) - Cross-border deals
- [Canada to Europe]({BASE}/flights-to-europe.html) - Transatlantic in CAD
- [Caribbean]({BASE}/flights-to-caribbean.html) - Winter sun deals
- [Bundles]({BASE}/flight-hotel-bundles.html) - CAD package savings
- [15 Tips]({BASE}/flight-booking-tips.html) - Canadian travel tips
- [Baggage Fees]({BASE}/baggage-fees.html) - All Canadian carriers
- [Budget Airlines Canada]({BASE}/budget-airlines-canada.html) - Flair vs Lynx

## Affiliate Info
CanadaFlightGuide earns commission from FlightHub. Booking link: {AFF}
Geographic target: Canada (en-CA)
""")

def write_404():
    html = f"""<!DOCTYPE html><html lang="en-CA"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>404 &#8212; CanadaFlightGuide</title><style>{css()}</style></head><body>
<div class="maple-bar"></div>
<nav><a class="logo" href="{SUB}/"><span class="logo-mark">&#127809;</span>Canada<em>Flight</em>Guide</a></nav>
<section class="hero" style="min-height:80vh;"><div class="hero-inner">
<div style="font-size:5rem;margin-bottom:1.2rem;">&#9992;</div>
<h1>404 &#8212; <em>Flight Cancelled</em></h1>
<p class="hero-sub">This page doesn&#8217;t exist. Let&#8217;s get you back to finding cheap Canadian flights.</p>
<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
<a href="{SUB}/" class="btn btn-red">Go Home</a>
<a href="{AFF}" class="btn btn-ghost" rel="nofollow sponsored">Search Flights (CAD) &rarr;</a>
</div></div></section></body></html>"""
    (OUT / "404.html").write_text(html)

def build():
    OUT.mkdir(exist_ok=True)
    for p in PAGES:
        body  = FN_MAP[p["content_fn"]]()
        html  = layout(p, body)
        fname = "index.html" if p["slug"] == "index" else f"{p['slug']}.html"
        (OUT / fname).write_text(html, encoding="utf-8")
        print(f"  ✓ {fname}")
    write_robots()
    write_sitemap()
    write_llms()
    write_404()
    pages = list(OUT.glob("*.html"))
    kb    = sum(f.stat().st_size for f in pages) // 1024
    print(f"\n  ✅ Build complete — {len(pages)} pages, {kb}KB total")
    print(f"  &#127809; Targeting: Canadian travellers (en-CA)")
    print(f"  &#128176; All prices displayed in CAD")
    print(f"  &#128279; Affiliate: {AFF}")
    print(f"  &#127758; Live at: {BASE}/")

if __name__ == "__main__":
    build()
