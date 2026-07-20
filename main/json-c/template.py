pkgname = "json-c"
pkgver = "0.19"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_THREADING=ON",
    "-DBUILD_STATIC_LIBS=ON",
    "-DDISABLE_WERROR=ON",
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "doxygen"]
checkdepends = ["vim-xxd"]
pkgdesc = "JSON implementation in C"
license = "MIT"
url = "https://json-c.github.io/json-c"
source = (
    f"https://s3.amazonaws.com/json-c_releases/releases/json-c-{pkgver}.tar.gz"
)
sha256 = "37ad0249902e301bd9052bf712e511fcc6acff4ecaad4b5900aad9ce564e26de"


def post_install(self):
    self.install_license("COPYING")


@subpackage("json-c-devel-static")
def _(self):
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


# cmake .a references, sigh
@subpackage("json-c-devel")
def _(self):
    self.depends += [self.with_pkgver("json-c-devel-static")]

    return self.default_devel()
