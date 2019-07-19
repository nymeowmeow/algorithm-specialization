#include <iostream>
#include <fstream>
#include <vector>
#include <tuple>
#include <cmath>
#include <cassert>
#include <algorithm>

using namespace std;

double
calculateDistance(const tuple<double, double>& first, const tuple<double, double>& second) 
{
    double x0 = get<0>(first);
    double x1 = get<0>(second);
    double y0 = get<1>(first);
    double y1 = get<1>(second);
    return sqrt((x0 - x1)*(x0-x1) + (y0 - y1)*(y0-y1));
}

int main()
{
    ifstream fp("tsp.txt");
    int citycount;
    fp >> citycount;
    double x, y;

    vector<tuple<double, double> > cities;
    while (fp >> x >> y)
    {
	cities.push_back(make_tuple(x, y));
    }
    fp.close();
    cout << "number of cities " << citycount << endl;
    assert(citycount == cities.size());
    double distance[citycount][citycount] = { {0} };
    for (int i= 0; i < citycount; ++i)
    {
	for (int j = 0; j <= i; ++j)
        {
	    double d = calculateDistance(cities[i], cities[j]);
	    distance[i][j] = d;
	    distance[j][i] = d;
	}
    }
    /*
    for (int i = 0; i < citycount; ++i)
    {
         for (int j = 0; j < citycount; ++j)
             cout << distance[i][j] << " ";
	 cout << "\n";
    }
    */
    double BIG = 9999999;
    long nsubsets = 1 << citycount; //2^n
    double** A = new double*[nsubsets];
    for (long i = 0; i < nsubsets; ++i)
    {
	A[i] = new double[citycount];
	for (int j = 0; j < citycount; ++j)
	    A[i][j] = BIG;
    }

    A[0][0] = 0;
    for (long m = 2; m <= citycount; ++m)
    {
         string mask(m, 1);
	 mask.resize(citycount, 0);

	 do {
	     if (mask[0]) //for subset that containing 1
	     {
                 long bitmask = 1;
		 for (long i = 1; i < citycount; ++i)
		     if (mask[i])
                         bitmask = (1 << i) | bitmask;

		 for (int j = 1; j < citycount; ++j)
		 {
                     if (((bitmask >> j) & 1) == 1) 
		     {
                         long b = bitmask ^ (1 << j); //remove j from subset
			 for (int k = 0; k < citycount; ++k)
			 {
                             if (((b >> k) & 1) == 1) 
			     {
                                 if (A[b][k] + distance[k][j] < A[bitmask][j])
				     A[bitmask][j] = A[b][k] + distance[k][j];
			     }
			 }
		     }
		 }
	     }
	 } while (prev_permutation(mask.begin(), mask.end()));
    }
    double minDistance = BIG;
    for (long i = 0; i < citycount; ++i)
	    if (A[nsubsets - 1][i] + distance[i][0] < minDistance)
		    minDistance = A[nsubsets-1][i] + distance[i][0];
    cout  << minDistance << endl;
    return 1;
}
