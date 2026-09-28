pkgname = "glm"
pkgver = "1.0.3"
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
license = "custom:Happy-Bunny-License"
url = "https://github.com/g-truc/glm"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6775e47231a446fd086d660ecc18bcd076531cfedd912fbd66e576b118607001"
hardening = ["!int"]


def post_install(self):
    self.install_license("copying.txt")
