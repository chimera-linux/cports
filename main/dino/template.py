pkgname = "dino"
pkgver = "0.4.3"
pkgrel = 3
build_style = "cmake"
configure_args = [
    "-DBUILD_TESTS=ON",
    "-DDINO_PLUGIN_ENABLED_notification-sound=ON",
    "-DUSE_SOUP3=ON",
]
hostmakedepends = [
    "cmake",
    "pkgconf",
    "ninja",
    "gettext",
    "unzip",
    "vala",
    "glib-devel",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "glib-devel",
    "libsoup-devel",
    "qrencode-devel",
    "libgee-devel",
    "libgcrypt-devel",
    "sqlite-devel",
    "libcanberra-devel",
    "gspell-devel",
    "libsrtp-devel",
    "libnice-devel",
    "gnutls-devel",
    "libsignal-protocol-c-devel",
    "gst-plugins-base-devel",
    "gpgme-devel",
]
pkgdesc = "Modern XMPP client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/dino/dino"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "432d7c3b5170c595b1b31a8d64d73ded26e32af9f03a2d1a01828c22a8ade3fa"


def do_check(self):
    for test in ["libdino", "signal-protocol-vala", "xmpp-vala"]:
        self.do(f"./build/{test}-test")


def _genmod(pname, pdesc):
    @subpackage(f"dino-plugin-{pname}")
    def _plug(self):
        self.pkgdesc = f"{pkgdesc} ({pdesc} plugin)"
        # this is not normally built with default settings
        if pname != "notification-sound":
            self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
        return [f"usr/lib/dino/plugins/{pname}.so"]


for _plugin, _desc in [
    ("http-files", "file host"),
    ("ice", "ICE"),
    ("notification-sound", "notification sound"),
    ("omemo", "OMEMO"),
    ("openpgp", "OpenPGP"),
    ("rtp", "Jingle RTP"),
]:
    _genmod(_plugin, _desc)
