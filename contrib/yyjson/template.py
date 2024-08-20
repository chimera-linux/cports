pkgname = "yyjson"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DYYJSON_BUILD_TESTS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "High performance C JSON library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://ibireme.github.io/yyjson"
source = f"https://github.com/ibireme/yyjson/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0d901cb2c45c5586e3f3a4245e58c2252d6b24bf4b402723f6179523d389b165"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("yyjson-devel")
def _(self):
    return self.default_devel()
