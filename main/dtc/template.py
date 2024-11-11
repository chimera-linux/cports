pkgname = "dtc"
pkgver = "1.7.2"
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
sha256 = "04a30bd38b426ed771b8a8b5d9b773e54976d4f5d51a80a9e76a45b20c9a8272"


@subpackage("dtc-devel")
def _(self):
    return self.default_devel()
