pkgname = "zathura"
pkgver = "0.5.10"
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
    "check-devel",
    "file-devel",
    "girara-devel",
    "glib-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libnotify-devel",
    "libseccomp-devel",
    "sqlite-devel",
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "Document viewer"
maintainer = "ttyyls <contact@behri.org>"
license = "Zlib"
url = "https://pwmt.org/projects/zathura"
source = f"{url}/download/zathura-{pkgver}.tar.xz"
sha256 = "fb498ec9724910833f6af3d217da830fcfaa5b7562048be93fe4f74b861ef35d"


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
