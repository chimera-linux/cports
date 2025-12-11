pkgname = "distrobox"
pkgver = "1.8.2.2"
pkgrel = 0
depends = ["curl", "podman", "polkit"]
pkgdesc = "Use any Linux distribution inside your terminal"
license = "GPL-3.0-only"
url = "https://distrobox.it"
source = f"https://github.com/89luca89/distrobox/archive/{pkgver}.tar.gz"
sha256 = "0c797689c0b8c7c7c9fa53d1f5550657af95e64d8b8bbdc0fe374f341ebf6cd0"
options = ["!lintcomp"]  # zsh _distrobox_running_containers


def install(self):
    self.do("./install", "--prefix", f"{self.chroot_destdir}/usr")
    self.install_file(self.files_path / "distrobox.conf", "usr/share/distrobox")
    self.install_file("docs/*.md", "usr/share/doc/distrobox", glob=True)
