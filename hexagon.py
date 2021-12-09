import itertools as it
import matplotlib.pyplot as plt

comps = np.array([i for i in it.product([i/3 for i in range(4)],repeat=3) if sum(i)==1])

cartxs = 1.-comps[:, 0]-comps[:, 1]/2.
cartys = np.sqrt(3) * comps[:, 1] / 2.0

#overlaps
plt.scatter(cartxs,cartys)
plt.scatter(cartxs,-cartys)
plt.scatter(-cartxs,cartys)
plt.scatter(-cartxs,-cartys)
plt.scatter(cartxs-0.5,cartys-np.sqrt(3)/2)
plt.scatter(cartxs-0.5,-(cartys-np.sqrt(3)/2))

cx = [c for c in cartxs]
cy = [c for c in cartys]
cx.extend([c for c in cartxs])
cy.extend([-c for c in cartys])

cx.extend([-c for c in cartxs])
cy.extend([c for c in cartys])

cx.extend([-c for c in cartxs])
cy.extend([-c for c in cartys])

cx.extend([c-0.5 for c in cartxs])
cy.extend([c-np.sqrt(3)/2 for c in cartys])

cx.extend([c-0.5 for c in cartxs])
cy.extend([-(c-np.sqrt(3)/2) for c in cartys])

uni = np.unique(np.array([cx,cy]),axis=1)
