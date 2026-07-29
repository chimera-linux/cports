pkgname = "gajim"
pkgver = "2.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gettext-devel",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "cairo",
    "geoclue",
    "glib",
    "gsound",
    "gspell",
    "gst-libav",
    "gst-plugins-base",
    "gst-plugins-good",
    "gstreamer",
    "gtksourceview",
    "gupnp-igd",
    "libadwaita",
    "libsecret",
    "libsoup",
    "pango",
    "python-cairo",
    "python-css-parser",
    "python-emoji",
    "python-gobject",
    "python-httpx",
    "python-keyring",
    "python-nbxmpp",
    "python-omemo-dr",
    "python-openssl",
    "python-packaging",
    "python-pillow",
    "python-precis-i18n",
    "python-qrcode",
    "python-sqlalchemy",
    "sqlite",
]
pkgdesc = "XMPP client"
license = "GPL-3.0-or-later"
url = "https://gajim.org"
source = f"{url}/downloads/{pkgver[: pkgver.rfind('.')]}/gajim-{pkgver}.tar.gz"
sha256 = "342997377463d6655ce9aa4e55cc7617e66ad89ed21a66544e5ba4468079f7e0"
# tests require pysequoia and other dependencies which are not packaged; skip for now
options = ["!check"]


def post_build(self):
    self.do("./make.py", "build", "--dist=unix")


def post_install(self):
    self.do(
        "python",
        "make.py",
        "install",
        "--dist=unix",
        f"--prefix={self.chroot_destdir}/usr",
    )


def check(self):
    self.do("python", "-m", "unittest", "discover", "-s", "test")
