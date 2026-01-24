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
    "mpd",
]
pkgdesc = "MPD client which submits tracks to a scrobbler"
license = "GPL-2.0-or-later"
url = "https://www.musicpd.org/clients/mpdscribble"
source = f"https://www.musicpd.org/download/mpdscribble/{pkgver}/mpdscribble-{pkgver}.tar.xz"
sha256 = "b9d5829b89c465707256c140000e1a04b1d9d3afe50db46a843cf5ee54bf6309"
hardening = ["vis", "cfi"]
options = ["etcfiles"]


def post_install(self):
    self.install_service(self.files_path / "mpdscribble.user")
    self.install_file("doc/mpdscribble.conf", "usr/share/doc/mpdscribble")
    self.chmod(self.destdir / "etc/mpdscribble.conf", 0o644)
