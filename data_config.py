# Data Path Configuration for AI-ACE Notebooks
# This file provides standard data paths for all notebooks

import os
from pathlib import Path

# Get the absolute path to the data directory
DATA_DIR = Path(__file__).parent / "data"

# Common data file paths
MPG_DATA = DATA_DIR / "mpg.csv"
TEMP_HUMIDITY_DATA = DATA_DIR / "온습도 관측 데이터.csv"
MARRIAGE_STATS_2024 = DATA_DIR / "2024년_월별_결혼증감률.csv"
MARRIAGE_NATIONAL_2024 = DATA_DIR / "2024년_전국_월별_결혼통계.csv"
MARRIAGE_REGIONAL_2024 = DATA_DIR / "2024년_지역별_결혼통계_상세.csv"

# KOSIS data files
KOSIS_MONTHLY_TREND = DATA_DIR / "KOSIS_월별_혼인통계_추이.csv"
KOSIS_REGIONAL_ANALYSIS = DATA_DIR / "KOSIS_지역별_혼인통계_분석.csv"
KOSIS_ANALYSIS_SUMMARY = DATA_DIR / "KOSIS_혼인통계_분석요약.csv"

def get_data_path(filename):
    """
    Get the full path to a data file.
    
    Args:
        filename (str): Name of the data file
        
    Returns:
        Path: Full path to the data file
    """
    return DATA_DIR / filename

def list_data_files():
    """
    List all available data files.
    
    Returns:
        list: List of data file names
    """
    if DATA_DIR.exists():
        return [f.name for f in DATA_DIR.glob("*.csv")]
    return []

# Example usage:
# import sys
# sys.path.append('../..')  # Add ai-ace to path
# from data_config import MPG_DATA, get_data_path
# 
# df = pd.read_csv(MPG_DATA)
# # or
# df = pd.read_csv(get_data_path("mpg.csv"))