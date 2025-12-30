# Computational Verification of the Bunyakovsky Conjecture

[cite_start]**Author:** Ruqing Chen (GUT Geoservice Inc.) [cite: 1]  
[cite_start]**Paper Status:** Submitted (December 2025) [cite: 1]

## 📄 Abstract

This repository contains the source code, datasets, and verification logs for the research paper:  
[cite_start]**"Computational Verification of the Bunyakovsky Conjecture for the Polynomial $Q_{n}(q)=q^{n}-(q-1)^{n}$"**[cite: 1, 33].

[cite_start]Using a high-performance distributed computational framework [cite: 2, 10][cite_start], we conducted a dense scan of bases with 42 decimal digits and targeted searches for bases up to $q \approx 10^{130}$[cite: 2]. [cite_start]We report a dataset of over **4,000 new probable primes (PRPs)** [cite: 3] [cite_start]and the discovery of a "Titanic" prime with 5,987 digits[cite: 5, 28].

## 🏆 Key Discovery: Titanic Prime

[cite_start]We successfully identified a massive candidate at exponent $n=47$, validating the polynomial's capacity to generate Titanic primes[cite: 28, 35].

| Property | Value |
| :--- | :--- |
| **Formula** | [cite_start]$Q_{47}(q)=q^{47}-(q-1)^{47}$ [cite: 28] |
| **Base ($q$)** | [cite_start]$20^{100} + 223343 \approx 1.27 \times 10^{130}$ [cite: 28] |
| **Digit Count** | [cite_start]**5,987** (Titanic Prime) [cite: 5, 28] |
| **Status** | [cite_start]Strong PRP (BPSW: MR-20 + Lucas) [cite: 28] |

## 📂 Repository Structure

* [cite_start]**`src/`**: Source code for the verification engine (`qn_solver.py`)[cite: 33].
* **`data/`**: 
  * [cite_start]`prp_list.csv`: Complete list of 4,000+ discovered PRPs[cite: 33].
  * `titanic_prime.txt`: Full decimal expansion of the $n=47$ prime.
* [cite_start]**`paper/`**: The submission manuscript (PDF/TeX)[cite: 33].

## ⚙️ Requirements

[cite_start]To replicate the verification results, the following dependencies are required[cite: 11]:
* Python 3.8+
* [cite_start]`gmpy2` (GNU Multiple Precision library interface) [cite: 11]

```bash
pip install gmpy2
```

## 🚀 Usage

[cite_start]To run the verification script for a specific exponent and range[cite: 33]:

```bash
# Example: Check bases for exponent n=23 starting from a specific offset
python src/qn_solver.py --n 23 --start 10000 --range 100
```

## 📜 Citation

[cite_start]If you use this code or data in your research, please cite[cite: 33]:

> **Chen, R.** (2025). Computational Verification of the Bunyakovsky Conjecture for the Polynomial $Q_n(q)$. [cite_start]*Submitted*. [cite: 1]

**BibTeX:**

```bibtex
@article{Chen2025_Bunyakovsky,
  author = {Chen, Ruqing},
  title = {Computational Verification of the Bunyakovsky Conjecture for the Polynomial Qn(q)},
  year = {2025},
  note = {Submitted}
}
```

## 📧 Contact

[cite_start]If you have any questions, please contact[cite: 1]:
* [cite_start]**Ruqing Chen**: `ruqing@hotmail.com` [cite: 1]

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
