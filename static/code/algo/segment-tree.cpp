#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


#define lint long long int


class SegTree {
    /* Represents integers segments trees, operate the sum on elements */

    public :
        SegTree(int n) {
            /* Create a segment tree with n éléments. */
            m_n = n;
            m_val = vector<lint>(4*n, -1);
            m_sum = vector<lint>(4*n, 0);
        }

        void set(int l, int r, lint x) {
            /* Set all elements of index in [l, r-1] to x */
            sub_set(l, r, x, 0, 0, m_n);
        }

        void set(int i, lint x) {
            /* Set element of index i to x */
            set(i, i+1, x);
        }

        lint get(int l, int r) {
            /* Get the sum of values of elements of [l, r-1] */
            return sub_get(l, r, 0, 0, m_n);
        }

    private :
        // size of the tree
        int m_n;
        // common values of elements descending from the node
        vector<lint> m_val;
        // sum of elements under the node
        vector<lint> m_sum;

        void sub_set(int a, int b, lint x, int v, int l, int r) {
            if (r <= a || b <= l) {
                // nothing to update
            }
            else if (a <= l && r <= b) { // [l, r] in [a, b]
                m_val[v] = x;
                m_sum[v] = x * (r - l);
            }
            else {
                int mid = (l + r) / 2;
                if (m_val[v] != -1) {
                    // push a value to subtrees
                    sub_set(l, mid, m_val[v], 2*v+1, l, mid);
                    sub_set(mid, r, m_val[v], 2*v+2, mid, r);
                    m_val[v] = -1;
                }
                // set new values for appropriate interval in subtree
                sub_set(a, b, x, 2*v+1, l, mid);
                sub_set(a, b, x, 2*v+2, mid, r);
                // update the sum
                m_sum[v] = m_sum[2*v+1] + m_sum[2*v+2];
            }
        }

        lint sub_get(int a, int b, int v, int l, int r) {
            if (r <= a || b <= l) {
                // [r, l-1] and [a, b-1] don't intersect
                return 0;
            }
            else if(a <= l && r <= b) {
                // [l, r-1] is included in [a, b-1]
                return m_sum[v];
            }
            else if(m_val[v] != -1) {
                // all elements of the node share the same value
                return m_val[v] * (min(b, r) - max(a, l));
            }
            else {
                // update the subtrees
                int mid = (l + r) / 2;
                return sub_get(a, b, 2*v+1, l, mid) + sub_get(a, b, 2*v+2, mid, r);
            }
        }
};
