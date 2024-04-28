pkgname = "mpdc"
pkgver = "0.35"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libmpdclient-devel"]
pkgdesc = "Command line mpd client"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://musicpd.org/clients/mpc"
source = f"https://musicpd.org/download/mpc/0/mpc-{pkgver}.tar.xz"
sha256 = "382959c3bfa2765b5346232438650491b822a16607ff5699178aa1386e3878d4"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_completion("contrib/mpc-completion.bash", "bash", name="mpc")
