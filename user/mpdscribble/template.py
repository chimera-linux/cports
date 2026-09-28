pkgname = "mpdscribble"
pkgver = "0.26"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "curl-devel",
    "dinit-chimera",
    "fmt-devel",
    "libgcrypt-devel",
    "libmpdclient-devel",
    "linux-headers",
]
pkgdesc = "Last.fm scrobbler for MPD"
license = "GPL-2.0-or-later"
url = "https://www.musicpd.org/clients/mpdscribble"
source = f"https://www.musicpd.org/download/mpdscribble/{pkgver}/mpdscribble-{pkgver}.tar.xz"
sha256 = "b9d5829b89c465707256c140000e1a04b1d9d3afe50db46a843cf5ee54bf6309"
hardening = ["vis", "cfi"]


def post_install(self):
    # services are set to start after mpd, but not depend (because mpd may be remote)
    self.install_service(self.files_path / "mpdscribble")
    self.install_service(self.files_path / "mpdscribble.user")
    self.install_file("doc/mpdscribble.conf", "usr/share/examples/mpdscribble")
    # the conf file is not useful by itself at all
    self.uninstall("etc")
