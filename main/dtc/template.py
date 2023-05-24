pkgname = "dtc"
pkgver = "1.7.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dpython=disabled", "-Ddefault_library=shared"]
hostmakedepends = ["meson", "ninja", "flex", "bison", "pkgconf"]
makedepends = ["libyaml-devel"]
pkgdesc = "Device Tree Compiler"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/utils/dtc/dtc.git"
source = "https://git.kernel.org/pub/scm/utils/dtc/dtc.git/snapshot/dtc-e8364666d5acc985c434fb574e92c5206d9a8d6b.tar.gz"
sha256 = "9871d96b26c495561b64256bef17a749856ab1fb78b1d5e99a27ba9fe6d7bfb0"


@subpackage("dtc-devel")
def _devel(self):
    return self.default_devel()
