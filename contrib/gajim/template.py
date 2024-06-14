pkgname = "gajim"
pkgver = "1.9.1"
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
checkdepends = depends + [
    "python-cryptography",
    "python-pytest",
    "xserver-xorg-xvfb",
]
pkgdesc = "XMPP client"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://gajim.org"
source = f"{url}/downloads/{pkgver[:pkgver.rfind('.')]}/gajim-{pkgver}.tar.gz"
sha256 = "56f5f31a8f062ed90027f6553a960e6e825e46a6640db643bbd0cc8da1ea5aeb"
# XXX: fix or skip the grapheme tests
options = ["!check"]


def post_build(self):
    self.do(
        "python",
        "./pep517build/build_metadata.py",
        "-o",
        "dist/metadata",
    )


def do_check(self):
    self.do("xvfb-run", "--", "python", "-m", "pytest")


def post_install(self):
    self.install_dir("usr/share/man/man1")
    self.install_dir("usr/share/applications")
    self.install_dir("usr/share/icons/hicolor/scalable/apps")
    self.install_dir("usr/share/metainfo")
    self.do(
        "python",
        "./pep517build/install_metadata.py",
        f"--prefix={self.chroot_destdir}/usr",
        "dist/metadata",
    )
