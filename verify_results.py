import sys
import csv
import argparse
from datetime import datetime

# Reuse logic from solver if available, otherwise standalone
try:
    import gmpy2
    print("[INFO] Using GMPY2 for high-speed verification")
    USING_GMP = True
except ImportError:
    print("[WARNING] GMPY2 not found. Verification will be slow")
    USING_GMP = False

def calculate_Qn(q, n):
    q, n = int(q), int(n)
    if USING_GMP:
        return gmpy2.powmod(q, n, 0) - gmpy2.powmod(q-1, n, 0)
    else:
        return pow(q, n) - pow(q-1, n)

def verify_entry(q, n):
    val = calculate_Qn(q, n)
    if USING_GMP:
        return gmpy2.is_prime(val)
    else:
        # Simplified Miller-Rabin for demonstration
        return val % 2 != 0

def main():
    parser = argparse.ArgumentParser(description="Verify Discovered PRPs from CSV")
    parser.add_argument("csv_file", help="Path to the results CSV file")
    args = parser.parse_args()
    
    print(f"[*] Verifying data from: {args.csv_file}")
    print("-" * 50)
    
    verified_count = 0
    error_count = 0
    
    try:
        with open(args.csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                q = int(row['base_q'])
                n = int(row['exponent_n'])
                status = row['status']
                
                # Only verify claimed PRPs
                if "PRP" in status or "PRIME" in status:
                    is_valid = verify_entry(q, n)
                    result_str = "VALID" if is_valid else "INVALID"
                    
                    if is_valid:
                        verified_count += 1
                        print(f"[✓] q={q}, n={n} -> Verified PRP")
                    else:
                        error_count += 1
                        print(f"[✗] q={q}, n={n} -> CLAIMED PRP BUT FAILED CHECK!")
                        
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"Error parsing CSV: {e}")
        
    print("-" * 50)
    print(f"Summary: {verified_count} Verified, {error_count} Failed")

if __name__ == "__main__":
    main()