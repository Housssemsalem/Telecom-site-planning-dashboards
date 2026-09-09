# ETL & Monitoring

This folder contains **sanitized portfolio examples** inspired by the monitoring approach used during the internship.

## Example workflow

```text
Incoming batch
      ↓
Schema validation
      ↓
Data Quality checks
      ↓
Comparison with previous batch
      ↓
KPI / change summary
      ↓
Monitoring output
```

The Python example demonstrates generic techniques such as required-column validation, null checks, duplicate detection and batch-to-batch comparison.

### Confidentiality

The original production scripts, SQL queries, internal database structures, credentials, file paths and company-specific business rules are intentionally not published. The code in this repository is a simplified and non-confidential demonstration.
