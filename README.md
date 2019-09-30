# data.gov.pl usage monitor

A proof-of-concept app created during a 24 hour long hackathon. Finds uses of openly accessible data based on phrase monitoring and reverse IP lookup.

Demo: https://horosin.github.io/data-gov-monitor/

## Technology stack

The project was created using:
- Python - reverse IP tracking and data preprocessing
- R - report and data analysis.

## Use the code
The app is not ready for use and is not intended to. If you really want to check it out:

### Report generation
You need to install R.
```
RScript ./render_report.R
```

### Log generation
We didn't have any access to the real log data. We had to generate mock logs in order to showcase the functionality. To generate your own logs, use:

```
python3 ./data-analysis/mock-log-generator.py
```

## Reverse IP lookup

```
python3 ./data-analysis/ip_reverse_scanner.py
```

