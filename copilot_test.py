import subprocess
import platform
from datetime import datetime, timedelta

def get_system_uptime():
    """
    Get and print system uptime.
    Works on Windows, macOS, and Linux.
    """
    system = platform.system()
    
    try:
        if system == "Windows":
            # Get uptime on Windows using wmic
            result = subprocess.run(
                ["wmic", "os", "get", "lastbootuptime"],
                capture_output=True,
                text=True,
                check=True
            )
            boot_time_str = result.stdout.split('\n')[1].strip()
            # Parse Windows boot time format
            boot_time = datetime.strptime(boot_time_str[:14], "%Y%m%d%H%M%S")
            uptime = datetime.now() - boot_time
            
        elif system == "Darwin":
            # Get uptime on macOS
            result = subprocess.run(
                ["uptime"],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"System Uptime (macOS): {result.stdout.strip()}")
            return
            
        else:  # Linux
            # Get uptime on Linux
            result = subprocess.run(
                ["uptime"],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"System Uptime (Linux): {result.stdout.strip()}")
            return
        
        # Format and print uptime
        days = uptime.days
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print(f"System Uptime: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
        print(f"Last Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
    except Exception as e:
        print(f"Error getting system uptime: {e}")
        print("Make sure you have the necessary permissions to run this command.")

if __name__ == "__main__":
    get_system_uptime()
