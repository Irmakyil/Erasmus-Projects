# Name: Irmak Yılmaz
# Student Number: E-379
# Programming Language: Python 3

def main():
    print("--- Diffie-Hellman Key Exchange Protocol ---\n")
    
    # Collect inputs from the user (p, g, a, b)
    try:
        p = int(input("Enter the prime number (p): "))
        g = int(input("Enter the base (g): "))
        a = int(input("Enter Alice's secret (a): "))
        b = int(input("Enter Bolek's secret (b): "))
    except ValueError:
        print("Invalid input. Please enter integer values.")
        return

    # Step 1: Alice computes her public value A
    # A = g^a mod p
    # Python's built-in pow(base, exp, mod) is highly optimized for modular exponentiation
    A = pow(g, a, p)
    print(f"\nAlice computes A = {g}^{a} mod {p} = {A}")
    print(f"Alice sends A ({A}) to Bolek.")

    # Step 2: Bolek computes his public value B
    # B = g^b mod p
    B = pow(g, b, p)
    print(f"Bolek computes B = {g}^{b} mod {p} = {B}")
    print(f"Bolek sends B ({B}) to Alice.")

    # Step 3: Alice computes the shared secret s
    # s = B^a mod p
    s_alice = pow(B, a, p)
    print(f"\nAlice computes the shared secret (s) = {B}^{a} mod {p} = {s_alice}")

    # Step 4: Bolek computes the shared secret s
    # s = A^b mod p
    s_bolek = pow(A, b, p)
    print(f"Bolek computes the shared secret (s) = {A}^{b} mod {p} = {s_bolek}")

    # Final Verification
    if s_alice == s_bolek:
        print(f"\nSuccess! Both Alice and Bolek share the exact same secret: {s_alice}")
    else:
        print("\nError: The shared secrets do not match.")

if __name__ == "__main__":
    main()