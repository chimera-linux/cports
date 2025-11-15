pkgname = "glm"
pkgver = "1.0.2"
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
sha256 = "19edf2e860297efab1c74950e6076bf4dad9de483826bc95e2e0f2c758a43f65"
hardening = ["!int"]


def post_install(self):
    self.install_license("copying.txt")
