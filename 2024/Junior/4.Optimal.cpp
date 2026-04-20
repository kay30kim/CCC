#include <iostream>
#include <string>
using namespace std;

string press, disp;
int cnt_press[26], cnt_disp[26];
int len_press, len_disp;
char silly_from, silly_to, quiet;

bool find_silly() {
	for (int i = 0; i < 26; i++) {
		if (quiet == i + 'a') continue;
		if (cnt_press[i] > cnt_disp[i]) {
			for (int j = 0; j < 26; j++) {
				if (cnt_press[j] < cnt_disp[j] && cnt_disp[j] == cnt_press[i]) {
					silly_from = i + 'a';
					silly_to = j + 'a';

					int i_press = 0, i_disp = 0;
					for (; i_press < len_press; i_press++) {
						if (press[i_press] == silly_from) {
							if (disp[i_disp] == silly_to) i_disp++;
							else return false;
						} else if (press[i_press] == quiet) {
							// do nothing
						} else {
							if (press[i_press] != disp[i_disp]) return false;
							i_disp++;
						}
					}
					if (i_press != len_press) return false;
					if (i_disp != len_disp) return false;
					return true;
				}
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> press >> disp;

	len_press = press.length();
	for (int i = 0; i < len_press; i++) {
		cnt_press[press[i] - 'a']++;
	}

	len_disp = disp.length();
	for (int i = 0; i < len_disp; i++) {
		cnt_disp[disp[i] - 'a']++;
	}

	if (len_press == len_disp) {
		quiet = '-';
		find_silly();
	} else {
		for (int i = 0; i < 26; i++) {
			if (len_press - len_disp == cnt_press[i] && cnt_disp[i] == 0) {
				quiet = i + 'a';
				if (find_silly()) break;
			}
		}
	}

	cout << silly_from << ' ' << silly_to << '\n' << quiet << '\n';
}