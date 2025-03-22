pkgname = "gajim"
pkgver = "2.0.4"
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
sha256 = "7af247b4cfcc3a41e519531e14963ee10d366490c64ca044dab8e3a5ea35f600"


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
