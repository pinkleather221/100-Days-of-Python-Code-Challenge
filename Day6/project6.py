# a payslip generator using functions

def calculate_nhif(gross):
    if gross < 6000:
        return 150 
    elif gross < 12000:
        return 400 
    elif gross < 25000:
        return 750
    else:
        return 950
    
def calculate_nssf(gross):
    return min((gross * 0.06),2160)


def calculate_paye(gross):
    if gross <= 24000:
        return 0 
    return round((gross - 24000) * 0.16)

def print_payslip(name, gross):
    nhif = calculate_nhif(gross)
    nssf = calculate_nssf(gross)
    paye = calculate_paye(gross)
    deductions = nhif + nssf + paye 
    net = gross - deductions

    print("=" * 40)
    print(f"    PAYSLIP - {name}")
    print("=" * 40)
    print(f"  Gross salary:     Ksh {gross}")
    print(f"   NHIF:            Ksh {nhif}")
    print(f"   NSSF:            Ksh {nssf}")
    print(f"   PAYE:            Ksh {paye}")
    print("=" * 40)
    print(f"   NET PAY:        Ksh {net}")
    print("=" * 40)
    print()


print_payslip("Amina Wanjiku", 85000)
print_payslip("David Mwandairo", 28000)
print_payslip("Brian Kamau", 19000)