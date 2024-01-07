pkgname = "libvidstab"
pkgver = "1.1.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["orc-devel", "libomp-devel"]
pkgdesc = "Video stabilization library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://public.hronopik.de/vid.stab"
source = f"https://github.com/georgmartius/vid.stab/archive/v{pkgver}.tar.gz"
sha256 = "9001b6df73933555e56deac19a0f225aae152abbc0e97dc70034814a1943f3d4"
# sketchy tests
options = ["!check"]

match self.profile().arch:
    case "x86_64":
        configure_args = ["-DSSE2_FOUND=1"]


@subpackage("libvidstab-devel")
def _devel(self):
    self.depends += ["libomp-devel"]

    return self.default_devel()
