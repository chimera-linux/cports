pkgname = "mint-themes"
pkgver = "2.4.3"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["bash", "gsed", "libsass-python", "python"]
pkgdesc = "Mint-X and Mint-Y GTK and Cinnamon themes"
license = "GPL-3.0-or-later"
url = "https://github.com/linuxmint/mint-themes"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "bab4d4ca82a3b753ebb30c22f9f059b5543be8e9664472350a017517a6c78bf6"
# no tests
options = ["!check"]
exec_wrappers = [("/usr/bin/gsed", "sed")]


def install(self):
    self.install_files("usr", "")
