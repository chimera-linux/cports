pkgname = "cglm"
pkgver = "0.9.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCGLM_SHARED=ON",
    "-DCGLM_USE_TEST=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Graphics math library for C"
license = "MIT"
url = "https://github.com/recp/cglm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "be5e7d384561eb0fca59724a92b7fb44bf03e588a7eae5123a7d796002928184"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("cglm-devel")
def _(self):
    return self.default_devel()
