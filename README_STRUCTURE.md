# AI-ACE Project Structure

This document describes the improved file organization for the AI-ACE project.

## Directory Structure

```
ai-ace/
├── data/                          # Centralized data storage
│   ├── mpg.csv                   # Automotive fuel efficiency data
│   ├── 온습도 관측 데이터.csv        # Temperature & humidity sensor data
│   ├── 2024년_월별_결혼증감률.csv    # Monthly marriage rate changes 2024
│   ├── 2024년_전국_월별_결혼통계.csv  # National monthly marriage statistics 2024
│   ├── 2024년_지역별_결혼통계_상세.csv # Regional marriage statistics details 2024
│   ├── KOSIS_월별_혼인통계_추이.csv   # KOSIS monthly marriage trend
│   ├── KOSIS_지역별_혼인통계_분석.csv # KOSIS regional marriage analysis
│   ├── KOSIS_혼인통계_분석요약.csv    # KOSIS marriage analysis summary
│   └── 혼인건수_시도_시_군_구__*.csv  # Marriage count by administrative region
├── notebooks/                     # (Future) Centralized notebook storage
├── data_config.py                # Data path configuration helper
├── day01/                        # Day 1 exercises and projects
├── day02/                        # Day 2 exercises and projects
└── day03/                        # Day 3 exercises and projects
    ├── mission/                  # Mission exercises
    └── quiz/                     # Quiz exercises
```

## Benefits of New Structure

### 1. Simplified Data Access
- **Before**: Complex relative paths like `../quiz/mpg.csv`, `./온습도 관측 데이터.csv`
- **After**: Consistent paths like `../../data/mpg.csv` from any notebook

### 2. Centralized Data Management
- All CSV files in one location (`ai-ace/data/`)
- Easy to find and manage datasets
- No duplicate files across directories

### 3. Consistent Path Structure
- From any notebook in `day*/mission/` or `day*/quiz/`: use `../../data/filename.csv`
- From any notebook in `day*/`: use `../data/filename.csv`
- From any notebook in `ai-ace/`: use `./data/filename.csv`

### 4. Configuration Helper
Use `data_config.py` for even simpler data access:

```python
import sys
sys.path.append('../..')  # Add ai-ace to path
from data_config import MPG_DATA, get_data_path

# Method 1: Use predefined constants
df = pd.read_csv(MPG_DATA)

# Method 2: Use helper function
df = pd.read_csv(get_data_path("mpg.csv"))

# Method 3: List available files
from data_config import list_data_files
print(list_data_files())
```

## Path Reference Guide

### From notebooks in `day03/mission/` or `day03/quiz/`:
```python
# MPG automotive data
df = pd.read_csv('../../data/mpg.csv')

# Temperature/humidity sensor data
sensor_data = pd.read_csv('../../data/온습도 관측 데이터.csv')

# Marriage statistics
marriage_data = pd.read_csv('../../data/2024년_월별_결혼증감률.csv')
```

### From notebooks in `day03/`:
```python
df = pd.read_csv('../data/mpg.csv')
```

### From notebooks in `ai-ace/`:
```python
df = pd.read_csv('./data/mpg.csv')
```

## Migration Notes

### Updated Notebooks
- ✅ `자연어-이병남-1197(예비).ipynb` - Updated to use `../../data/mpg.csv`
- ✅ `온습도_관측_데이터_분석.ipynb` - Updated to use `../../data/온습도 관측 데이터.csv`

### Data Files Moved
- ✅ `mpg.csv` moved from `day03/quiz/` to `data/`
- ✅ `온습도 관측 데이터.csv` moved from `day03/mission/` to `data/`
- ✅ All marriage statistics CSV files moved from `day03/mission/` to `data/`

## Future Improvements

1. **Centralized Notebooks**: Consider moving frequently used notebooks to `ai-ace/notebooks/`
2. **Data Validation**: Add data validation scripts to ensure CSV file integrity
3. **Documentation**: Add metadata files describing each dataset
4. **Version Control**: Implement data versioning for large datasets

## Best Practices

1. **Always use relative paths** pointing to the central data directory
2. **Use the data_config.py helper** when possible for better maintainability
3. **Document new datasets** when adding them to the data directory
4. **Keep original data files intact** - use copies for experimentation