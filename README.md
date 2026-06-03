# CanadaFlightGuide — FlightHub Affiliate Site

> 20-page static affiliate site promoting FlightHub for Canadian travellers.
> Live at: **https://brightlane.github.io/flighthub/**
> Affiliate URL: `https://track.rqqft.com/aff_c?offer_id=25630&aff_id=21885`
> Target audience: Canadian travellers (en-CA)
> All prices displayed in CAD

---

## Quick Start

```bash
git clone https://github.com/brightlane/flighthub.git
cd flighthub
python3 build.py
```

Push to `main` — GitHub Actions builds and deploys automatically.

---

## Repo Structure

```
flighthub/
├── build.py
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## Pages (20)

| Page | File | Target Keywords |
|------|------|-----------------|
| Homepage | index.html | flighthub canada cheap flights |
| Review | flighthub-review.html | flighthub review canada |
| vs Expedia Canada | flighthub-vs-expedia.html | flighthub vs expedia canada |
| vs Kayak | flighthub-vs-kayak.html | flighthub vs kayak canada |
| Cheap Flights Canada | cheap-flights-canada.html | cheapest flights canada |
| Toronto Flights | toronto-flights.html | cheap flights toronto |
| Vancouver Flights | vancouver-flights.html | cheap flights vancouver |
| Montreal Flights | montreal-flights.html | cheap flights montreal |
| Calgary Flights | calgary-flights.html | cheap flights calgary |
| Ottawa Flights | ottawa-flights.html | cheap flights ottawa |
| Canada to USA | flights-to-usa.html | flights canada to usa |
| Canada to Europe | flights-to-europe.html | cheap flights canada europe |
| Caribbean | flights-to-caribbean.html | cheap flights canada caribbean |
| Bundles | flight-hotel-bundles.html | flight hotel packages canada |
| 15 Tips | flight-booking-tips.html | flight booking tips canada |
| Best Time to Book | best-time-to-book.html | best time book flights canada |
| Baggage Fees | baggage-fees.html | canadian airline baggage fees |
| Budget Airlines | budget-airlines-canada.html | flair lynx westjet canada |
| Promo Codes | promo-codes.html | flighthub promo codes canada |
| About | about.html | about canadaflightguide |

---

## GitHub Pages Setup

1. Create repo `brightlane/flighthub` on GitHub
2. Add `build.py` to the repo root
3. Add `.github/workflows/deploy.yml`
4. Go to **Settings → Pages → Source → GitHub Actions**
5. Push to `main` — builds and deploys automatically
6. Live at `https://brightlane.github.io/flighthub/`

---

## What Makes This Site Canadian-Specific

- `lang="en-CA"` on every page
- `meta name="geo.region" content="CA"` on every page
- All prices displayed and labeled in **CAD**
- Canadian airlines covered: Air Canada, WestJet, Porter, Air Transat, Flair, Lynx, Sunwing
- Canadian city pages: Toronto (YYZ/YTZ), Vancouver (YVR), Montreal (YUL), Calgary (YYC), Ottawa (YOW)
- Winter sun routes targeted: Cuba, Dominican Republic, Mexico, Jamaica from Canadian cities
- Canadian booking windows: winter sun 8–12 weeks, domestic 4–6 weeks, Europe 3–4 months
- Canadian holidays covered: March Break, Victoria Day, Canada Day, Labour Day, Thanksgiving, Christmas
- Bilingual service mentioned throughout (English and French)
- FlightHub's Canadian identity (founded in Montreal) highlighted

---

## Customisation

### Update affiliate URL
```python
AFF = "https://track.rqqft.com/aff_c?offer_id=25630&aff_id=21885"
```

### Update live URL
```python
BASE = "https://brightlane.github.io/flighthub"
SUB  = "/flighthub"
```

### Update deal prices (all in CAD)
Each deal is a 5-tuple:
```python
("Route", "$Price CAD", "Badge", "badge-class", "Note")
```
Badge classes: `tag-hot`, `tag-sale`, `tag-new`, `tag-flash`

### Add a Canadian city page
```python
def page_winnipeg():
    return canada_city_page("Winnipeg", "YWG", [
        ("Winnipeg → Toronto", "$149", "HOT", "tag-hot", "WestJet & Air Canada"),
        ...
    ])
```
Then add to `PAGES` and `FN_MAP`.

---

## Tech Stack

- Python 3.8+ — standard library only, zero dependencies
- Static HTML/CSS — no JavaScript frameworks
- Google Fonts — Epilogue + Inter
- GitHub Pages — free hosting, auto-deploy via Actions

---

## Affiliate Disclosure

CanadaFlightGuide is an independent affiliate partner of FlightHub.
Not operated by or affiliated with FlightHub.

## License

MIT
