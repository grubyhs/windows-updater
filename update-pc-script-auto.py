import sys
from utilities import *
from motherboard import *
from chocolatey import *
from winget import *
from windows_update import *

if __name__ == "__main__":
    if run_as_admin():
        motherboard_launcher()
    # Update Winget
        winget_upgrade()
    # Check if Chocolatey (choco) is installed and perform the necessary actions
        choco_upgrade()
    # Update Windows
        windows_update()
        # End of the script
        print("Script execution completed.")
    else:
        sys.exit(0)  # Exit if user declines admin privileges