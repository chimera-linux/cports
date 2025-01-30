pkgname = "zathura"
pkgver = "0.5.11"
pkgrel = 2
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
sha256 = "54458a9998af0fb8faef2e934a81127bbe4b790c86dcd2c8b8f32365f3d1b53c"


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
        "virtual:zathura-pdf-default!zathura",
        "virtual:zathura-cb!zathura",
        "virtual:zathura-djvu!zathura",
        "virtual:zathura-ps!zathura",
    ]
    self.options = ["empty"]

    return []


@subpackage("zathura-mupdf-default")
def _(self):
    self.options = ["empty"]
    self.subsec = ["mupdf backend"]
    self.provides = ["zathura-pdf-default"]
    self.provider_priority = 100

    return []


@subpackage("zathura-poppler-default")
def _(self):
    self.options = ["empty"]
    self.subsec = ["poppler backend"]
    self.provides = ["zathura-pdf-default"]
    self.provider_priority = 0

    return []
