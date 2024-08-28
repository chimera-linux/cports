pkgname = "distrobox"
pkgver = "1.7.2.1"
pkgrel = 0
depends = ["curl", "podman", "polkit"]
pkgdesc = "Use any Linux distribution inside your terminal"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-only"
url = "https://distrobox.it"
source = f"https://github.com/89luca89/distrobox/archive/{pkgver}.tar.gz"
sha256 = "ff2cca0c6334fff6ed577d23f68a6746ad4009f42d8a45eef5ca3850c895a4bb"


def install(self):
    self.do("./install", "--prefix", f"{self.chroot_destdir}/usr")
    self.install_file(self.files_path / "distrobox.conf", "usr/share/distrobox")
    self.install_file("docs/*.md", "usr/share/doc/distrobox", glob=True)
