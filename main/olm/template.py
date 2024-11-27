pkgname = "olm"
pkgver = "3.2.16"
pkgrel = 0
build_style = "cmake"
make_check_args = ["--test-dir", "tests"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Implementation of the Olm and Megolm cryptographic ratchets"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://gitlab.matrix.org/matrix-org/olm"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "f77032dbdc9a2040879bcc21c3e62cb6656b62e9550a1bb8da5a5b38ba21352a"


@subpackage("olm-devel")
def _(self):
    return self.default_devel()
