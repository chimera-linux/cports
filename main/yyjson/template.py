pkgname = "yyjson"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DYYJSON_BUILD_TESTS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "High performance C JSON library"
license = "MIT"
url = "https://ibireme.github.io/yyjson"
source = f"https://github.com/ibireme/yyjson/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b16246f617b2a136c78d73e5e2647c6f1de1313e46678062985bdcf1f40bb75d"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("yyjson-devel")
def _(self):
    return self.default_devel()
