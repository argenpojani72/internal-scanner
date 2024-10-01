import os
import psutil

def run_system_scan():
    # Ensure the directory exists
    os.makedirs('data/scanning_reports', exist_ok=True)
    
    # Example scan logic
    scan_result = {
        'cpu_usage': psutil.cpu_percent(),
        'memory': psutil.virtual_memory()._asdict(),
        'disk_usage': psutil.disk_usage('/')._asdict()
    }
    
    # Write the result to a file
    with open('data/scanning_reports/system_scan.json', 'w') as f:
        f.write(str(scan_result))

if __name__ == "__main__":
    run_system_scan()
