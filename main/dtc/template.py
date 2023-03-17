pkgname = "dtc"
pkgver = "1.7.0"
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
sha256 = "29edce3d302a15563d8663198bbc398c5a0554765c83830d0d4c0409d21a16c4"

if self.profile().arch == "ppc64le":
    # weird crashes
    options = ["!check"]

@subpackage("dtc-devel")
def _devel(self):
    return self.default_devel()
