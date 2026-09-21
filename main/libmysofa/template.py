pkgname = "libmysofa"
pkgver = "1.3.5"
pkgrel = 0
build_style = "cmake"
# tests fail when run in parallel
make_check_args = ["-j1"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["cunit-devel", "zlib-ng-compat-devel"]
checkdepends = []
pkgdesc = "Reader for AES SOFA files to get better HRTFs"
license = "BSD-3-Clause"
url = "https://github.com/hoene/libmysofa"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f29508c335c83d8703f943ffc9ca783ac39aca84e851357f13a55af0f8143137"
# FIXME: breaks fail-issue-167a test
hardening = ["!int"]
# no nodejs on some platforms
options = []


match self.profile.arch:
    case "aarch64" | "loongarch64" | "ppc64le" | "riscv64" | "x86_64":
        checkdepends += ["nodejs"]
    case _:
        options += ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libmysofa-devel")
def _(self):
    return self.default_devel()
