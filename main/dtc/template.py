pkgname = "dtc"
pkgver = "1.6.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["NO_PYTHON=1"]
make_install_args = make_build_args
hostmakedepends = ["gmake", "flex", "bison", "pkgconf"]
makedepends = ["libyaml-devel"]
pkgdesc = "Device Tree Compiler"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/utils/dtc/dtc.git"
source = f"https://www.kernel.org/pub/software/utils/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "65cec529893659a49a89740bb362f507a3b94fc8cd791e76a8d6a2b6f3203473"

if self.profile().arch == "ppc64le":
    # weird crashes
    options = ["!check"]

@subpackage("dtc-devel")
def _devel(self):
    return self.default_devel()
