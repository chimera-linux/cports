pkgname = "musl-bsd-headers"
pkgver = "0.1"
pkgrel = 1
pkgdesc = "BSD compatibility headers for musl"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND BSD-3-Clause"
url = "https://chimera-linux.org"
options = ["bootstrap"]


def install(self):
    for f in ["cdefs", "queue", "tree"]:
        self.install_file(self.files_path / f"{f}.h", "usr/include/sys")

    self.install_file(self.files_path / "error.h", "usr/include")

    self.install_license(self.files_path / "LICENSE.BSD-3-Clause")
    self.install_license(self.files_path / "LICENSE.BSD-2-Clause")
