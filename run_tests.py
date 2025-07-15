from tests.test_login import test_login
from datetime import datetime
import os

def main():
    print("Starting tests...")

    # Run the test
    status, message = test_login()

    print(f"Test result: {status} - {message}")

    # Prepare results dictionary
    results = {'Login Test': (status, message)}

    # Make sure reports folder exists
    os.makedirs("reports", exist_ok=True)

    # Create report filename with timestamp
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"reports/test_report_{now}.txt"

    # Write results to report file
    with open(report_file, "w") as f:
        f.write("Test Report\n")
        f.write("="*50 + "\n")
        for test_name, (status, message) in results.items():
            f.write(f"{test_name}:\n")
            f.write(f"  Status: {status}\n")
            f.write(f"  Message: {message}\n\n")

    print(f"Tests complete! Report saved to {report_file}")

if __name__ == "__main__":
    main()
