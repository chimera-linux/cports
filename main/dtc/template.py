pkgname = "dtc"
pkgver = "1.7.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dpython=disabled", "-Ddefault_library=shared"]
hostmakedepends = ["meson", "ninja", "flex", "bison", "pkgconf"]
makedepends = ["libyaml-devel"]
pkgdesc = "Device Tree Compiler"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/utils/dtc/dtc.git"
source = f"https://git.kernel.org/pub/scm/utils/dtc/dtc.git/snapshot/v{pkgver}.tar.gz"
sha256 = "65e65af7037a10026ec53c9784d07cb451ada5a19e396eb5d6c70d179c45e3a6"


@subpackage("dtc-devel")
def _(self):
    return self.default_devel()
