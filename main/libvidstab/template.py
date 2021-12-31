pkgname = "libvidstab"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["orc-devel", "libomp-devel"]
pkgdesc = "Video stabilization library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://public.hronopik.de/vid.stab"
source = f"https://github.com/georgmartius/vid.stab/archive/v{pkgver}.tar.gz"
sha256 = "14d2a053e56edad4f397be0cb3ef8eb1ec3150404ce99a426c4eb641861dc0bb"
# sketchy tests
options = ["!check"]

match self.profile().arch:
    case "x86_64":
        configure_args += ["-DSSE2_FOUND=1"]

@subpackage("libvidstab-devel")
def _devel(self):
    self.depends += ["libomp-devel"]

    return self.default_devel()
