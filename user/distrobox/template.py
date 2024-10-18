pkgname = "distrobox"
pkgver = "1.8.0"
pkgrel = 0
depends = ["curl", "podman", "polkit"]
pkgdesc = "Use any Linux distribution inside your terminal"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-only"
url = "https://distrobox.it"
source = f"https://github.com/89luca89/distrobox/archive/{pkgver}.tar.gz"
sha256 = "72d8d825b6aad63e03e0b92376e6ead9c053c1e676acab3c7eaac9be2929d0a2"


def install(self):
    self.do("./install", "--prefix", f"{self.chroot_destdir}/usr")
    self.install_file(self.files_path / "distrobox.conf", "usr/share/distrobox")
    self.install_file("docs/*.md", "usr/share/doc/distrobox", glob=True)
