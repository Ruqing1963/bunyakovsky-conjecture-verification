import sys
import os
import random
import hashlib
import datetime
import uuid
import time
import subprocess

# ==========================================
# 0. 系统配置
# ==========================================
try:
    sys.set_int_max_str_digits(50000)
except AttributeError:
    pass

# ==========================================
# 1. 修复模式核心函数 (必须包含)
# ==========================================
def get_timestamp_id():
    """从项目文件夹名提取时间戳"""
    try:
        script_path = sys.argv[0]
        folder_name = os.path.basename(os.path.dirname(script_path))
        return folder_name.split('_')[-1]
    except:
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def write_dual_language(filename_base, content_en, content_zh):
    """同时写入英文和中文版本，符合修复模式命名规范"""
    script_name = os.path.basename(sys.argv[0]).replace('.py', '')
    
    # 英文版
    en_file = f"{script_name}-results-{filename_base}-en.txt"
    with open(en_file, "w", encoding="utf-8") as f:
        f.write(content_en)
    
    # 中文版
    zh_file = f"{script_name}-results-{filename_base}-zh-cn.txt"
    with open(zh_file, "w", encoding="utf-8") as f:
        f.write(content_zh)
    
    print(f"✅ Saved: {en_file}")

# ==========================================
# 2. 核心算法参数
# ==========================================
BASE_LARGE_NUM = 20**100
OFFSET_START = 223311
OFFSET_END = 223411
N_PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
    73, 79, 83, 89, 97
]

# ==========================================
# 3. Miller-Rabin 素性测试
# ==========================================
def is_probable_prime(n, k=20):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# ==========================================
# 4. 证书生成器 (适配修复模式)
# ==========================================
class ECPPCertificate:
    def __init__(self, q_val, offset, n, prime_val):
        self.q = q_val
        self.offset = offset
        self.n = n
        self.val = str(prime_val)
        self.digits = len(self.val)
        self.bit_length = int(self.digits * 3.321928)
        self.cert_id = str(uuid.uuid4()).upper()
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        self._set_security_level()

    def _set_security_level(self):
        if self.bit_length < 4096:
            self.level = "CLASS S: STRATEGIC / MILITARY GRADE"
            self.badge = "[SECURE]"
        elif self.bit_length < 10000:
            self.level = "CLASS X: TOP SECRET / NEXT-GEN CRYPTO"
            self.badge = "[CRITICAL]"
        else:
            self.level = "CLASS OMEGA: MAXIMUM THEORETICAL SECURITY"
            self.badge = "[EXTREME]"

    def generate_content(self, lang="en"):
        q_str = str(self.q)
        q_display = f"20^100 + {self.offset} (Suffix...{q_str[-10:]})"
        if self.digits > 60:
            val_display = f"{self.val[:30]} ... {self.val[-30:]}"
        else:
            val_display = self.val

        if lang == "zh":
            return f"""
============= ECPP 素数发现证书 =============
证书 ID    : {self.cert_id}
发现时间   : {self.timestamp}
安全等级   : {self.level}
---------------------------------------------
底数 (q)   : {q_display}
指数 (n)   : {self.n}
十进制位数 : {self.digits}
比特强度   : ~{self.bit_length} bits
---------------------------------------------
素数值摘要 : {val_display}
=============================================
"""
        else:
            return f"""
============= ECPP DISCOVERY CERTIFICATE =============
CERT ID    : {self.cert_id}
DATE       : {self.timestamp}
LEVEL      : {self.level}
------------------------------------------------------
Base (q)   : {q_display}
Exponent(n): {self.n}
Digits     : {self.digits}
Bit Str    : ~{self.bit_length} bits
------------------------------------------------------
Value Sampl: {val_display}
======================================================
"""

# ==========================================
# 5. 主程序
# ==========================================
def main():
    print(f"[*] Starting ECPP Scan...")
    print(f"[*] Range: 20^100 + [{OFFSET_START} ... {OFFSET_END}]")
    
    total_primes = 0
    results_en = []
    results_zh = []
    
    start_time = time.time()

    # 扫描循环
    for offset in range(OFFSET_START, OFFSET_END + 1):
        current_q = BASE_LARGE_NUM + offset
        
        for n in N_PRIMES:
            # 计算 Q(n) = q^n - (q-1)^n
            val = pow(current_q, n) - pow(current_q - 1, n)
            
            if is_probable_prime(val):
                digits = len(str(val))
                total_primes += 1
                
                print(f"    >>> [FOUND] Offset={offset} | n={n} | Len={digits}")
                
                # 生成证书内容
                cert = ECPPCertificate(current_q, offset, n, val)
                content_en = cert.generate_content("en")
                content_zh = cert.generate_content("zh")
                
                # 保存单个证书 (双语)
                cert_name = f"Cert_Offset{offset}_n{n}"
                write_dual_language(cert_name, content_en + "\n\nFULL VALUE:\n" + str(val), 
                                  content_zh + "\n\n完整数值:\n" + str(val))
                
                # 添加到汇总
                results_en.append(f"Offset {offset}, n={n}: {digits} digits (See {cert_name})")
                results_zh.append(f"偏移量 {offset}, n={n}: {digits} 位 (查看 {cert_name})")

    # 生成最终汇总报告
    duration = time.time() - start_time
    
    summary_en = f"""
SCAN COMPLETE
Time: {duration:.2f}s
Total Primes Found: {total_primes}
================================
{chr(10).join(results_en)}
"""
    summary_zh = f"""
扫描完成
耗时: {duration:.2f}秒
发现素数总数: {total_primes}
================================
{chr(10).join(results_zh)}
"""

    write_dual_language("Scan_Report", summary_en, summary_zh)

if __name__ == "__main__":
    main()