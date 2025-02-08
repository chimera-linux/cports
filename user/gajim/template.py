pkgname = "gajim"
pkgver = "1.9.5"
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
    "gtksourceview4",
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
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://gajim.org"
source = f"{url}/downloads/{pkgver[: pkgver.rfind('.')]}/gajim-{pkgver}.tar.gz"
sha256 = "7fdf4db0eb16a7ebc679c2360f145f64e0abcff0f16913c45f92c8eb8d87563c"


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
