pkgname = "x265"
pkgver = "3.5"
pkgrel = 2
build_wrksrc = "source"
_commit = "f0c1022b6be1"
build_style = "cmake"
configure_args = ["-DENABLE_PIC=1", "-DGIT_ARCHETYPE=1"]
hostmakedepends = ["pkgconf", "cmake", "ninja"]
makedepends = ["libnuma-devel", "linux-headers"]
pkgdesc = "Open source H.265/HEVC encoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://x265.org"
source = f"https://bitbucket.org/multicoreware/x265_git/get/{pkgver}.tar.gz"
sha256 = "5ca3403c08de4716719575ec56c686b1eb55b078c0fe50a064dcf1ac20af1618"
# guilty until proven wrong
hardening = ["!int"]
# cannot be reliably tested, testing option is conditional
options = ["!check"]

match self.profile().arch:
    case "x86_64":
        configure_args += [
            "-DENABLE_ASSEMBLY=ON",
            "-DCMAKE_ASM_NASM_FLAGS=-w-macro-params-legacy",
        ]
        hostmakedepends += ["nasm"]
    case "ppc64le":
        configure_args += ["-DENABLE_ALTIVEC=ON", "-DCPU_POWER8=ON"]
    case "ppc64" | "ppc":
        configure_args += ["-DENABLE_ALTIVEC=OFF", "-DCPU_POWER8=OFF"]


@subpackage("x265-devel")
def _devel(self):
    return self.default_devel()
