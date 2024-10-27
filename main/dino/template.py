pkgname = "dino"
pkgver = "0.4.4"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DBUILD_TESTS=ON",
    "-DDINO_PLUGIN_ENABLED_notification-sound=ON",
    "-DUSE_SOUP3=ON",
]
hostmakedepends = [
    "cmake",
    "gettext",
    "glib-devel",
    "ninja",
    "pkgconf",
    "unzip",
    "vala",
]
makedepends = [
    "glib-devel",
    "gnutls-devel",
    "gpgme-devel",
    "gspell-devel",
    "gst-plugins-base-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libcanberra-devel",
    "libgcrypt-devel",
    "libgee-devel",
    "libnice-devel",
    "libsignal-protocol-c-devel",
    "libsoup-devel",
    "libsrtp-devel",
    "qrencode-devel",
    "sqlite-devel",
]
pkgdesc = "Modern XMPP client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/dino/dino"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "29f37dc3a54fb123f223964d01de76fcea038ca6d134aa35b75c62b07acb9d03"


def check(self):
    for test in ["libdino", "signal-protocol-vala", "xmpp-vala"]:
        self.do(f"./build/{test}-test")


def _genmod(pname, pdesc):
    @subpackage(f"dino-plugin-{pname}")
    def _(self):
        self.subdesc = f"{pdesc} plugin"
        # this is not normally built with default settings
        if pname != "notification-sound":
            self.install_if = [self.parent]
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


@subpackage("dino-devel")
def _(self):
    return self.default_devel()
