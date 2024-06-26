pkgname = "glm"
pkgver = "1.0.1"
pkgrel = 0
build_style = "cmake"
# unversioned library built out of all the headers combined
configure_args = ["-DGLM_BUILD_LIBRARY=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "OpenGL Mathematics"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:Happy-Bunny-License"
url = "https://github.com/g-truc/glm"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9f3174561fd26904b23f0db5e560971cbf9b3cbda0b280f04d5c379d03bf234c"
hardening = ["!int"]


def post_install(self):
    self.install_license("copying.txt")
