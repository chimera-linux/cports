pkgname = "lite-xl"
pkgver = "2.1.7"
pkgrel = 0
build_style = "meson"
configure_args = ["-Duse_system_lua=true"]
hostmakedepends = ["meson", "ninja", "python-pkgconfig"]
makedepends = ["freetype-devel", "lua5.4-devel", "pcre2-devel", "sdl2-devel"]
pkgdesc = "lite-xl Text editor"
license = "MIT AND OFL-1.1"
url = "https://lite-xl.com"
source = (
    f"https://github.com/lite-xl/lite-xl/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "69d1ce4c1d148d382ccb06f45feca2565c5c8fe9d0b1b9bc1cbe014f6826ce6b"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("licenses/licenses.md")
