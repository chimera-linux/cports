pkgname = "zathura"
pkgver = "0.5.6"
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
pkgdesc = "Document viewer"
maintainer = "ttyyls <contact@behri.org>"
license = "Zlib"
url = "https://pwmt.org/projects/zathura"
source = f"{url}/download/zathura-{pkgver}.tar.xz"
sha256 = "b478e35e87cce57d651b4112dc8193c4b744a07f121b7b6465229a8f386f10da"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("zathura-devel")
def _devel(self):
    return self.default_devel()


@subpackage("zathura-backends")
def _backends(self):
    self.pkgdesc = f"{pkgdesc} (backends)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        "virtual:zathura-pdf-poppler!zathura",
        "virtual:zathura-cb!zathura",
        "virtual:zathura-djvu!zathura",
        "virtual:zathura-ps!zathura",
    ]
    self.options = ["empty"]

    return []
