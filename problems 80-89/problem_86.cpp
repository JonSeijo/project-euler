#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef long long ll;

const ll EXPECTED = 1000000;

ll norma_cuad(ll c1, ll c2) {
	return c1*c1 + c2*c2;
}

bool es_cuad_perfecto(ll d) {
	ll a = (ll) sqrt(d);
	return (a * a == d || (a+1) * (a+1) == d);
}

ll cant_mayores(vector<ll> &lista, ll x) {
	ll lo = -1;
	ll hi = lista.size();
	while (lo + 1 < hi) {
		ll m = (lo + hi) / 2;
		if (lista[m] < x)
			lo = m;
		else
			hi = m;
	}
	return lista.size() - hi;
}

ll res(ll M) {
	ll cuboides = 0;
	vector< vector<ll> > perfectos(2*M + 1);

	for (ll base = 1; base <= 2*M; base++) {
		for (ll h = 1; h <= M; h++) {
			if (es_cuad_perfecto( norma_cuad(base, h) ))
				perfectos[base].push_back(h);
		}
	}

	for (ll a = 1; a <= M; a++) {
		for (ll b = a; b <= M; b++) {
			cuboides += cant_mayores(perfectos[a+b], b);
		}
	}

	return cuboides;
}

int main() {
	ll lo = 0;
	ll hi = 2000;
	while (lo + 1 < hi) {
		ll m = (lo + hi) / 2;
		cout << "Probando: " << m << "\n";
		if (res(m) < EXPECTED) 
			lo = m;
		else
			hi = m;
	}

	cout << hi << "\n";
}
