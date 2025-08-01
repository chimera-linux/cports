pkgname = "gajim"
pkgver = "2.3.3"
pkgrel = 1
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
checkdepends = [
    "python-cryptography",
    "python-pytest",
    "xserver-xorg-xvfb",
    *depends,
]
pkgdesc = "XMPP client"
license = "GPL-3.0-or-later"
url = "https://gajim.org"
source = f"{url}/downloads/{pkgver[: pkgver.rfind('.')]}/gajim-{pkgver}.tar.gz"
sha256 = "c32b20fb00561d48dd72e7e60501346c5d1f5073e7d131bcae7ec3781567edc1"


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
