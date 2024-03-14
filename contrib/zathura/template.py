pkgname = "zathura"
pkgver = "0.5.4"
pkgrel = 1
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
sha256 = "a3037f7aa94d4096bfd97069f62ffcdca9f06431e8663548c1cd6b945c556f32"


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
