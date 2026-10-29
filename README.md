# PersonalPage

Personal website of Aleksei Pshenichnyi, built with Jekyll and the [al-folio](https://github.com/alshedivat/al-folio) theme.

## Edit content

- `_pages/about.md` - home page: bio, profile photo, contacts
- `_data/cv.yml` - CV data (renders the CV page and the PDF via RenderCV on push)
- `_projects/` - project cards
- `_news/` - short news items on the home page
- `_data/socials.yml` - email and social links
- `_config.yml` - site name, URL, SEO

## Run locally

```bash
docker compose up --build
# open http://localhost:8080
```

## Deploy

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and publishes it to the `gh-pages` branch.
In GitHub: Settings -> Pages -> Source: "Deploy from a branch" -> `gh-pages` / root.
