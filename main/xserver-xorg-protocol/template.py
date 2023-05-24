# update when xorg/xwayland update calls for it
pkgname = "xserver-xorg-protocol"
_commit = "85ff1cdbd3286838e512fe7c70af149a8743b6fe"
pkgver = "20180227"
pkgrel = 0
pkgdesc = "X server protocol name registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = (
    f"https://gitlab.freedesktop.org/xorg/xserver/-/raw/{_commit}/dix/protocol.txt",
    False,
)
sha256 = "b8f6921aaf1d88c74b0cd88295bdfe28b84b432200b8d2fb5b40b0d6eef6016d"


def do_install(self):
    from cbuild.core import paths

    self.install_file(
        paths.sources() / f"{pkgname}-{pkgver}/protocol.txt", "usr/lib/xorg"
    )
