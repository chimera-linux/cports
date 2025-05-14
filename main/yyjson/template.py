pkgname = "yyjson"
pkgver = "0.11.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DYYJSON_BUILD_TESTS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "High performance C JSON library"
license = "MIT"
url = "https://ibireme.github.io/yyjson"
source = f"https://github.com/ibireme/yyjson/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "610a38a5e59192063f5f581ce0c3c1869971c458ea11b58dfe00d1c8269e255d"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("yyjson-devel")
def _(self):
    return self.default_devel()
