pkgname = "lite-xl"
pkgver = "2.1.8"
pkgrel = 0
build_style = "meson"
configure_args = ["-Duse_system_lua=true"]
hostmakedepends = ["meson", "ninja", "python-pkgconfig"]
makedepends = ["freetype-devel", "lua5.4-devel", "pcre2-devel", "sdl3-devel"]
pkgdesc = "Lite-xl Text editor"
license = "MIT AND OFL-1.1"
url = "https://lite-xl.com"
source = (
    f"https://github.com/lite-xl/lite-xl/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "fcaffb946bc60583369cb040d533a4ac18075a6d474d49a2a5ff4bf87e2e9a10"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("licenses/licenses.md")
