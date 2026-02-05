pkgname = "mpdscribble"
pkgver = "0.25"
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
sha256 = "20f89d945bf517c4d68bf77a77a359fdb13842ab1295e8d21eda79be2b5b35ce"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "mpdscribble.user")
    self.install_file("doc/mpdscribble.conf", "usr/share/doc/mpdscribble")
    self.chmod(self.destdir / "etc/mpdscribble.conf", 0o644)
