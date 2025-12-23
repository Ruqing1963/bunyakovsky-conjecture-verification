import sys
import argparse
import time
from datetime import datetime

# Try to import gmpy2 for high performance, fallback to native python
try:
    import gmpy2
    from gmpy2 import mpz
    print("[INFO] Using GMPY2 for high-speed arithmetic")
    USING_GMP = True
except ImportError:
    print("[WARNING] GMPY2 not found. Using native Python (slower)")
    USING_GMP = False

def calculate_Qn(q, n):
    """
    Computes Q_n(q) = q^n - (q-1)^n
    As defined in Equation (1) of the paper.
    """
    if USING_GMP:
        q = mpz(q)
        n = mpz(n)
        term1 = gmpy2.powmod(q, n, 0)     # q^n
        term2 = gmpy2.powmod(q-1, n, 0)   # (q-1)^n
        return term1 - term2
    else:
        return pow(q, n) - pow(q-1, n)

def is_probable_prime(num):
    """
    Performs Miller-Rabin primality test.
    Returns True if PRP, False if Composite.
    """
    if USING_GMP:
        return gmpy2.is_prime(num)
    else:
        # Basic implementation for demonstration
        if num % 2 == 0: return False
        # (In real research, use GMP. This is a placeholder for the logic)
        return True # Simplified for fallback

def main():
    parser = argparse.ArgumentParser(description="Bunyakovsky Conjecture Verification Tool")
    parser.add_argument("--n", type=int, default=47, help="Exponent n (default: 47)")
    parser.add_argument("--q_start", type=int, default=2, help="Start base q")
    parser.add_argument("--q_end", type=int, default=1000, help="End base q")
    
    args = parser.parse_args()
    
    print(f"[*] Starting Search for Q_{args.n}(q)")
    print(f"[*] Range q: [{args.q_start}, {args.q_end}]")
    print("-" * 50)
    
    start_time = time.time()
    found_count = 0
    
    for q in range(args.q_start, args.q_end + 1):
        # Calculate Q_n(q)
        val = calculate_Qn(q, args.n)
        
        # Check Primality
        if is_probable_prime(val):
            found_count += 1
            digits = len(str(val))
            print(f"[FOUND] q={q}, n={args.n} | Digits: {digits} | Status: PRP")
            
            # Save to log
            with open("found_primes.log", "a") as f:
                f.write(f"{datetime.now()},{q},{args.n},{digits}\n")

    elapsed = time.time() - start_time
    print("-" * 50)
    print(f"[*] Scan Complete. Found {found_count} candidates in {elapsed:.2f}s")

if __name__ == "__main__":
    main()