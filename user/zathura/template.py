pkgname = "zathura"
pkgver = "2026.10.23"
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
sha256 = "29a0931527f63c832f50eeef169d885a5db52a3a9e13b12a3a7beca9aaf63d2d"


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
