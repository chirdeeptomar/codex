# Private Media Access Design (MVP)

- Evidence files are stored using an S3-compatible backend with `default_acl = "private"`.
- Public APIs never return direct evidence URLs.
- Access should be mediated by authenticated moderator/admin workflows or signed short-lived URLs generated server-side.
- Citizen evidence access is currently controlled by `tracking_id` + secret `tracking_token` and should be extended with one-time tokens + expiry in a later phase.
