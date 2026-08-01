pkgname = "zathura"
pkgver = "2026.07.18"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "appstream-glib",
    "gettext",
    "librsvg-progs",
    "meson",
    "pkgconf",
    "python-sphinx",
]
makedepends = [
    "file-devel",
    "girara-devel",
    "glib-devel",
    "gtk4-devel",
    "json-glib-devel",
    "libseccomp-devel",
    "sqlite-devel",
    "xxhash-devel",
]
checkdepends = [
    "check-devel",
    "desktop-file-utils",
    "xserver-xorg-xvfb",
]
pkgdesc = "Document viewer"
license = "Zlib"
url = "https://pwmt.org/projects/zathura"
source = f"{url}/download/zathura-{pkgver}.tar.xz"
sha256 = "9efc4a92f8b2d03e5a1b80756d3ae4249d8d6efdb10e311795e8cdd8e35a9f87"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("zathura-devel")
def _(self):
    return self.default_devel()


@subpackage("zathura-backends")
def _(self):
    self.subdesc = "backends"
    self.install_if = [self.parent]
    self.depends = [
        "virtual:zathura-pdf-poppler!zathura",
        "virtual:zathura-cb!zathura",
        "virtual:zathura-djvu!zathura",
        "virtual:zathura-ps!zathura",
    ]
    self.options = ["empty"]

    return []
