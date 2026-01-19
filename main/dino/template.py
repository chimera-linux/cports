pkgname = "dino"
pkgver = "0.5.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dplugin-notification-sound=enabled",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
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
    "libomemo-c-devel",
    "libsoup-devel",
    "libsrtp-devel",
    "qrencode-devel",
    "sqlite-devel",
]
pkgdesc = "Modern XMPP client"
license = "GPL-3.0-or-later"
url = "https://github.com/dino/dino"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4c57f20677f47f41b440b7d6eebb697ee89d5d8c38d334ad47c6b5de19894768"

if self.profile().endian != "big":
    makedepends += ["webrtc-audio-processing-devel"]


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
