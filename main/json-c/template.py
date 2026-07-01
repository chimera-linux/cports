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
pkgdesc = "JSON implementation in C"
license = "MIT"
url = "https://json-c.github.io/json-c"
source = (
    f"https://s3.amazonaws.com/json-c_releases/releases/json-c-{pkgver}.tar.gz"
)
sha256 = "37ad0249902e301bd9052bf712e511fcc6acff4ecaad4b5900aad9ce564e26de"
tool_flags = {"CFLAGS": ["-Wno-error"]}
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("json-c-devel")
def _(self):
    return self.default_devel()
