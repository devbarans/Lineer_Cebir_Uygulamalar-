import numpy as np

np.set_printoptions(suppress=True)

# =========================================================
# SORU 1 — Doğrusal Bağımsızlık / Bağımlılık
# =========================================================
print("=== SORU 1 ===")

v1 = np.array([1, 2, 0, 1])
v2 = np.array([2, 4, 0, 2])
v3 = np.array([0, 1, 1, 0])
v4 = np.array([1, 3, 1, 1])

V = np.column_stack((v1, v2, v3, v4))

rank_V = np.linalg.matrix_rank(V)
print("Rank(V):", rank_V)

if rank_V < V.shape[1]:
    print("Vektörler doğrusal BAĞIMLIDIR.")
else:
    print("Vektörler doğrusal BAĞIMSIZDIR.")

print("İlişki: v2 = 2 * v1")

# =========================================================
# SORU 2 — Span (Geren Küme) Testi
# =========================================================
print("\n=== SORU 2 ===")

u1 = np.array([1, 0, 1, 0])
u2 = np.array([0, 1, 1, 0])
u3 = np.array([0, 0, 1, 1])

b = np.array([2, 1, 4, 1])

A = np.column_stack((u1, u2, u3))
coeffs, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

print("Katsayılar:", coeffs)

if np.allclose(A @ coeffs, b):
    print("b, span{u1, u2, u3} içindedir.")
else:
    print("b, span{u1, u2, u3} içinde DEĞİLDİR.")

print("Bu vektörler R^4'ün tamamını değil, bir alt uzayı gerer.")

# =========================================================
# SORU 3 — Baz ve Boyut
# =========================================================
print("\n=== SORU 3 ===")

M = np.array([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [1, 1, 0, 1],
    [0, 1, 1, 1]
])

rank_M = np.linalg.matrix_rank(M)
print("Rank(M):", rank_M)

# Bağımsız sütun indekslerini bulma
_, inds = np.linalg.qr(M)
basis_indices = np.where(np.abs(np.diag(inds)) > 1e-10)[0]

print("Baz sütun indeksleri:", basis_indices)
print("Uzayın boyutu:", rank_M)

# =========================================================
# SORU 4 — Özvektörler Baz Oluşturur mu?
# =========================================================
print("\n=== SORU 4 ===")

A3 = np.array([
    [2, 0, 0],
    [0, 3, 0],
    [0, 0, 4]
])

eigvals, eigvecs = np.linalg.eig(A3)

P = eigvecs
rank_P = np.linalg.matrix_rank(P)

print("Rank(P):", rank_P)

if rank_P == 3:
    print("Özvektörler R^3 için bir baz oluşturur.")
else:
    print("Özvektörler baz oluşturmaz.")

print("Her 3x3 matrisin özvektörleri baz oluşturmaz (köşegenlenebilirlik şartı).")

# =========================================================
# SORU 5 — Norm, Uzaklık, Birim Vektör
# =========================================================
print("\n=== SORU 5 ===")

points = np.array([
    [1, 2, -1],
    [2, 0, 3],
    [-1, 1, 2],
    [0, -2, 1]
])

# (a) Normlar
norms = np.linalg.norm(points, axis=1)
print("Normlar:", norms)

# (b) Mesafe Matrisi
n = len(points)
D = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        D[i, j] = np.linalg.norm(points[i] - points[j])

print("Mesafe Matrisi:\n", D)

# (c) En yakın ve en uzak çift
mask = D + np.eye(n) * 1e9
min_idx = np.unravel_index(np.argmin(mask), mask.shape)
max_idx = np.unravel_index(np.argmax(D), D.shape)

print("En yakın çift:", (min_idx[0]+1, min_idx[1]+1), "Mesafe:", D[min_idx])
print("En uzak çift:", (max_idx[0]+1, max_idx[1]+1), "Mesafe:", D[max_idx])

# (d) Birim vektörler
unit_vectors = []

for p in points:
    norm = np.linalg.norm(p)
    if norm == 0:
        unit_vectors.append(np.zeros_like(p))
    else:
        unit_vectors.append(p / norm)

print("Birim vektörler:")
for uv in unit_vectors:
    print(uv)

