pkgname = "libvidstab"
pkgver = "1.1.1"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["orc-devel"]
pkgdesc = "Video stabilization library"
license = "GPL-2.0-or-later"
url = "http://public.hronopik.de/vid.stab"
source = f"https://github.com/georgmartius/vid.stab/archive/v{pkgver}.tar.gz"
sha256 = "9001b6df73933555e56deac19a0f225aae152abbc0e97dc70034814a1943f3d4"
# sketchy tests
options = ["!check"]


_have_omp = self.profile().arch in [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "riscv64",
    "x86_64",
]

if _have_omp:
    makedepends += ["libomp-devel"]

match self.profile().arch:
    case "x86_64":
        configure_args += ["-DSSE2_FOUND=1"]


@subpackage("libvidstab-devel")
def _(self):
    if _have_omp:
        self.depends += ["libomp-devel"]

    return self.default_devel()
