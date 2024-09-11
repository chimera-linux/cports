pkgname = "openbox"
pkgver = "3.6.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-x",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gtk+3-devel",
    "imlib2-devel",
    "librsvg-devel",
    "libxcursor-devel",
    "libxfixes-devel",
    "libxml2-devel",
    "pango-devel",
    "startup-notification-devel",
]
pkgdesc = "Standards compliant, fast, light-weight, extensible window manager"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-only"
url = "https://openbox.org"
source = f"{url}/dist/openbox/openbox-{pkgver}.tar.gz"
sha256 = "8b4ac0760018c77c0044fab06a4f0c510ba87eae934d9983b10878483bde7ef7"


@subpackage("openbox-devel")
def _(self):
    return self.default_devel()
