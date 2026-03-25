"""
State configuration for this NebraskaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "NE"
STATE_NAME = "Nebraska"
APP_NAME = "NebraskaDischargeWatch"
APP_TAGLINE = "Nebraska Discharge Monitoring"
DOMAIN = "nebraskadischargewatch.org"
DATA_FILE = "ne_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@nebraskadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "CST"
EPA_REGION = 7
