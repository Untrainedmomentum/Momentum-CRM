# Momentum CRM Architecture

Momentum CRM is a hybrid operating system built on Odoo Community with Untrained Momentum-specific modules layered on top.

## Phase 1: safe internal pilot

Only internal/test brands are used initially:

- Mecosta County Kids
- Untrained Matriarch

No paying-client migration is part of phase 1.

## Core responsibilities

Odoo Community provides the base for:

- contacts
- CRM leads and opportunities
- projects and tasks
- users and permissions
- core business records

Momentum modules add the pieces specific to Untrained Momentum:

- brand/business-unit context
- outreach workflows
- booking integrations
- social publishing and approvals
- client-specific workflow automation
- reporting and operating dashboards
- migration tooling from the current CRM

## Data model direction

`momentum.brand` is the first custom object. It identifies the internal brand/business unit associated with contacts, leads, and projects.

This is intentionally separate from Odoo's company model. A brand may be an internal property or test tenant without needing to become a separate legal company.

## Deployment direction

GitHub stores source code only. Odoo itself requires an application server and PostgreSQL database; GitHub Pages cannot run Odoo.

The included Docker Compose stack is the development/self-hosting baseline. Production deployment will add:

- managed secrets
- HTTPS/reverse proxy
- database backups
- persistent volumes
- restricted database manager access
- monitoring

## Migration rule

The existing CRM remains production during the pilot. We only migrate a workflow after Momentum CRM proves it works better in testing.
