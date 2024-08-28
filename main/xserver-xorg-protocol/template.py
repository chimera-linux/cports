# update when xorg/xwayland update calls for it
pkgname = "xserver-xorg-protocol"
_commit = "53a0442b8700ddcb33caa5d1d17ca9a290000283"
pkgver = "20240503"
pkgrel = 0
pkgdesc = "X server protocol name registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"!https://gitlab.freedesktop.org/xorg/xserver/-/raw/{_commit}/dix/protocol.txt"
sha256 = "88b141646fc68627338443a820eeb949149ba73d4ddc925d4717d56a92e7e138"
options = ["!distlicense"]


def install(self):
    self.install_file(self.sources_path / "protocol.txt", "usr/lib/xorg")
