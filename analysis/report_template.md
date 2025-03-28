---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.7
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python tags=["parameters"]
wd = ""
```

```python
import os
import pandas as pd
```

```python
pd.read_csv(
  os.path.join(wd, "area_by_age_comparison.csv")
).set_index("age").plot()
```

```python
disturbance_comparison = pd.read_csv(
  os.path.join(wd, "disturbance_comparison.csv")
).set_index("year")
```

```python
disturbance_types = set(
  [
    str(col)
    .replace("pre-rollback ", "")
    .replace("post-rollback", "")
    .strip() for col in disturbance_comparison.columns
  ]
)
```

```python
for dist_type in disturbance_types:
    for period in ("pre", "post"):
      key = f"{period}-rollback {dist_type}"
      if key not in disturbance_comparison:
        disturbance_comparison[key] = 0.0

    disturbance_comparison[
      [f"pre-rollback {dist_type}", f"post-rollback {dist_type}"]
    ].plot(figsize=(15,5))
```

```python
    df = pd.read_csv(os.path.join(wd, f"procedure_description.csv"), index_col=0)
    df = df[df.index != "00: No data"]
    df.plot(kind="barh")
```

```python
for data in [
 'deforestation_present',
 'establishment_before_rollback',
 'establishment_sr_disturbance',
 'pre_est_post_rollback_sr_disturbances',
 'pre_rollback_sr_disturbances',
 'procedure_name',
 'rollback_period_sr_disturbances',
 'rollback_period_sr_disturbance_count',
 'sr_disturbance_after_establishment'
]:
    df = pd.read_csv(os.path.join(wd, f"{data}.csv"), index_col=0)
    df.plot(kind="barh")
```
