# main.py – DUMMY verzió, amíg a modell még nincs kész

import numpy as np

# -------------------------
# XOR bemeneti adatok
# -------------------------
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
], dtype=float)

y = np.array([
    [0],
    [1],
    [1],
    [0],
], dtype=float)

# -------------------------
# Dummy tanulási eredmények
# (mintha egy háló már megtanulta volna az XOR-t)
# -------------------------

# Hiba alakulása 100 epochon keresztül – csökkenő görbe
epochs = 100
errors = [0.5 * (0.95 ** i) for i in range(epochs)]

# Rejtett réteg dummy aktivációi (4 minta × 2 neuron)
hidden_output = np.array([
    [0.1, 0.9],  # minta: [0, 0]
    [0.8, 0.2],  # minta: [0, 1]
    [0.7, 0.3],  # minta: [1, 0]
    [0.2, 0.8],  # minta: [1, 1]
])

# Végső kimenet dummy értékekkel (közel a [0, 1, 1, 0]-hoz)
final_output = np.array([
    [0.05],  # ~0
    [0.92],  # ~1
    [0.90],  # ~1
    [0.08],  # ~0
])

# -------------------------
# Dummy predict függvény
# (amíg nincs igazi modell)
# -------------------------
def dummy_predict(x1: float, x2: float) -> int:
    """
    Ideiglenes XOR logika – csak teszteléshez.
    Később ezt lecseréljük a valódi model.predict hívásra.
    """
    return int((x1 != x2))


if __name__ == "__main__":
    print("XOR bemenetek (X):")
    print(X)
    print("\nValódi kimenetek (y):")
    print(y)

    print("\nDUMMY végső kimenetek (final_output):")
    print(np.round(final_output, 2))

    # Dummy interaktív rész – ezt a frontend később lecseréli / kibővíti
    try:
        x1 = int(input("\nAdj meg egy x1 értéket (0 vagy 1): "))
        x2 = int(input("Adj meg egy x2 értéket (0 vagy 1): "))
        pred = dummy_predict(x1, x2)
        print(f"A dummy modell kimenete: {pred}")
    except ValueError:
        print("Érvénytelen bemenet, csak 0 vagy 1 legyen.")
