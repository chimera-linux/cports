pkgname = "doasedit"
pkgver = "1.0.8"
pkgrel = 0
depends = ["opendoas"]
pkgdesc = "Shell script to edit files with doas"
license = "MIT"
url = "https://codeberg.org/TotallyLeGIT/doasedit"
source = f"https://codeberg.org/TotallyLeGIT/doasedit/archive/{pkgver}.tar.gz"
sha256 = "de7dfc450568d14f1ff473aa4a50a0d0505e188e117cc12cf3a2b0ea5da8af10"


def install(self):
    self.install_bin("doasedit")
    self.install_license("LICENSE")
