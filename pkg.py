import glob
import sys
def finfpkg(pkg):
    for fname in glob.glob("*.deb"):
        fname1=fname.split('_')[0]
        if pkg==fname1:
            print(fname)
            break
if __name__ == "__main__":
    for pkg in sys.argv:
        finfpkg(pkg)