pkgname = "musl-fts"
pkgver = "1.2.7"
pkgrel = 1
build_style = "makefile"
make_build_args = ["PREFIX=/usr"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Implementation of fts(3) for musl libc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/chimera-linux/musl-fts"
source = f"{url}/archive/refs/tags/v{pkgver}-mk2.tar.gz"
sha256 = "1f65612b523e7040dbd9d5579a2eca97ede79c2ff3f91db7ccc288263e60da50"
# no test suite; also no point in LTOing this
options = ["bootstrap", "!check", "!lto"]


def post_install(self):
    self.install_license("COPYING")
    # single fts.3, the same-named version in man-pages is 97% identical anyway
    self.uninstall("usr/share/man")


@subpackage("musl-fts-devel")
def _devel(self):
    self.options = ["!splitstatic"]
    return self.default_devel()
