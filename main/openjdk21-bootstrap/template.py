pkgname = "openjdk21-bootstrap"
pkgver = "21.0.3_p9"
pkgrel = 1
# satisfy revdeps
makedepends = [
    "alsa-lib-devel",
    "freetype-devel",
    "giflib-devel",
    "lcms2-devel",
    "libjpeg-turbo-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "libxt-devel",
    "libxtst-devel",
]
pkgdesc = "Bootstrap binaries of OpenJDK 21"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only WITH Classpath-exception-2.0"
url = "https://openjdk.org"
source = f"https://repo.chimera-linux.org/distfiles/openjdk-bootstrap-{pkgver}-{self.profile().arch}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = (
            "bc10a4bf011872647d67f391b8cb9d652ddebd7be67b63f4f6e8a278c31f4ecd"
        )
    case "ppc64":
        sha256 = (
            "99e7de2f490b7686aa76fa08ac2295252bfd39df23202cff9c3378539fca56b4"
        )
    case "ppc64le":
        sha256 = (
            "f3a28eef1bff5a019af63223fdd4319cfe5f8f37008cc868ff6207c1f48efec8"
        )
    case "riscv64":
        sha256 = (
            "faf696996a5a5be389a319b64ff5266362ba870b010b40d9e47896399462537f"
        )
    case "x86_64":
        sha256 = (
            "d0fa05f629fae165ff021a143c08493b7b07ca785c237d0852197f78d28a4c3d"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_dir("usr/lib/jvm/java-21-openjdk")
    for f in self.cwd.iterdir():
        self.install_files(f, "usr/lib/jvm/java-21-openjdk")
