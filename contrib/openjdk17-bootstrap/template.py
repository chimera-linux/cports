pkgname = "openjdk17-bootstrap"
pkgver = "17.0.7_p5"
pkgrel = 0
# satisfy revdeps
makedepends = [
    "libxrender-devel", "libxtst-devel", "libxt-devel", "libxrandr-devel",
    "giflib-devel", "libjpeg-turbo-devel", "freetype-devel", "lcms2-devel",
    "alsa-lib-devel",
]
depends = ["!openjdk17"]
pkgdesc = "Bootstrap binaries of OpenJDK 17"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only WITH Classpath-exception-2.0"
url = "https://openjdk.org"
source = f"https://repo.chimera-linux.org/distfiles/openjdk-bootstrap-{pkgver}-{self.profile().arch}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = "c158dabf44fb211859910f15e97181827e834edb2e1180b30e2bfba95c851c74"
    case "ppc64le":
        sha256 = "37f5bf35c5b8f95c34710975ec4a2c25677df46a5da9e5e82e643dd5113eca99"
    case "x86_64":
        sha256 = "b0053f81d28e640ad96488d5b19d753a307643b7f7df0a5801cd0353eeb985bb"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_dir("usr/lib/jvm/java-17-openjdk")
    for f in self.cwd.iterdir():
        self.install_files(f, "usr/lib/jvm/java-17-openjdk")
