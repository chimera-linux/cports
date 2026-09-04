pkgname = "picom"
pkgver = "13"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dunittest=true", "-Dwith_docs=true"]
hostmakedepends = ["asciidoctor", "meson", "pkgconf"]
makedepends = [
    "dbus-devel",
    "libconfig-devel",
    "libepoxy-devel",
    "libev-devel",
    "libx11-devel",
    "libxcb-devel",
    "mesa-devel",
    "pcre2-devel",
    "pixman-devel",
    "uthash",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-renderutil-devel",
]
pkgdesc = "Standalone compositor for X11"
license = "MPL-2.0 AND MIT"
url = "https://github.com/yshui/picom"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "db9791a54255742c924ef82a6a882042636d61de0fa61bc14c5e56279cf5791c"
options = ["etcfiles"]


def post_install(self):
    self.install_license("COPYING")
    self.install_license("LICENSES/MIT")


@subpackage("picom-devel")
def _(self):
    return self.default_devel()
