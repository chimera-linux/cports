pkgname = "gajim"
pkgver = "2.3.4"
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
sha256 = "99acd07022575630d94b49ab6d7bef51f64df7dfcabc3d9a71c2641f1e6c5dd3"


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
