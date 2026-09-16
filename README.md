# Momentum CRM

Momentum CRM is Untrained Momentum's custom business operating system, built as a hybrid on top of **Odoo Community** rather than rebuilding standard CRM/ERP infrastructure from scratch.

## Pilot scope

The first test is intentionally limited to internal brands:

- Mecosta County Kids
- Untrained Matriarch

The existing Untrained Momentum CRM stays in production while this pilot is evaluated.

## What is in this repo now

- Odoo 19 Community Docker baseline
- PostgreSQL 16
- custom `momentum_crm` addon
- `momentum.brand` model
- brand fields added to Contacts, CRM Leads, and Projects
- seeded internal test brands
- architecture and migration guardrails

## Start locally

1. Copy `.env.example` to `.env` and replace the database password.
2. Update the matching database password and admin password in `config/odoo.conf` before anything beyond local testing.
3. Run:

```bash
docker compose up -d
```

4. Open `http://localhost:8069`.
5. Create a test database.
6. In Apps, update the app list and install **Momentum CRM**.

## Repository layout

```text
addons/
  momentum_crm/       Custom Odoo addon
config/
  odoo.conf           Odoo runtime config
docs/
  ARCHITECTURE.md     Product architecture and pilot boundaries
docker-compose.yml    Odoo + PostgreSQL development stack
```

## Product direction

Odoo Community handles commodity business infrastructure. Momentum CRM adds the parts that make the system useful for Untrained Momentum and, eventually, other small businesses: workflow automation, outreach, bookings, social publishing, approvals, operating dashboards, and client-specific processes.

Do not migrate paying clients into this pilot until the internal test brands have passed functional and security testing.
