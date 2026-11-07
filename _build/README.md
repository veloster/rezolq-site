# rezolq.com — how to update the site

The pages at the root of this repository (`index.html`, `privacy.html`, `support.html`, `terms.html`, `legal.html`, `404.html`) and `assets/css/site.css` are **generated**. Do not edit them by hand.

## Change a text, a colour or a page

1. Texts of the home page, the header, the footer and the page titles: `_build/build.py`.
2. Texts of the legal pages and of the support page: `_build/content/<page>.html`.
3. Colours, fonts, spacing, radii: `_build/tokens.json` (a copy of the REZOLQ Design System tokens). Change the Design System first, then copy the values here.
4. Rebuild, from the repository root:

   ```bash
   python3 _build/build.py
   ```

5. Check locally: `python3 -m http.server 8765`, then open http://localhost:8765.
6. Publish: commit and push to `main`. GitHub Pages republishes in about a minute. The hourly “Site monitor” workflow then checks the site.

## When the app is released

- Replace the two “coming soon” buttons in `_build/build.py` (hero and final section) with the official “Download on the App Store” and “Get it on Google Play” badges, linked to the store pages. Use the badges unmodified, from Apple’s and Google’s marketing sites.
- Name the cue-server hosting provider in `_build/content/privacy.html` (section 3 and section 6).

## What is where

- Hosting: GitHub Pages (repository settings → Pages), custom domain `rezolq.com`, HTTPS enforced.
- Domain and DNS: DreamHost. DNS records are listed in the project’s emergency sheet.
- Fonts: Inter and Inter Tight (SIL Open Font License), hosted in `fonts/`.
