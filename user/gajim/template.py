pkgname = "gajim"
pkgver = "2.0.1"
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
    "dbus",
    "farstream",
    "geoclue",
    "glib",
    "gspell",
    "gst-libav",
    "gst-plugins-base",
    "gst-plugins-ugly",
    "gstreamer",
    "gtk+3",
    "gtksourceview",
    "gupnp-igd",
    "libayatana-appindicator",
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
sha256 = "aa137b6d78fa9bd19c137f87d2f7fdeddb136a67d108b8acb82d1cdadff277de"


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
