pkgname = "rclone"
pkgver = "1.68.1"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Rsync for cloud storage"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://rclone.org"
source = f"https://github.com/rclone/rclone/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "26259526855a12499d00e3a3135ee95e7aeb3ecf2f85886d8c837a2e7b236226"
# tests require network
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        self.do(
            self.chroot_cwd / "build/rclone",
            "genautocomplete",
            shell,
            f"rclone.{shell}",
        )


def install(self):
    self.install_bin("build/rclone")
    self.install_link("usr/bin/mount.rclone", "rclone")
    self.install_link("usr/bin/rclonefs", "rclone")

    self.install_man("rclone.1")
    self.install_dir(f"usr/share/doc/{pkgname}")
    self.install_file("MANUAL.html", f"usr/share/doc/{pkgname}", 0o644)
    self.install_file("MANUAL.txt", f"usr/share/doc/{pkgname}", 0o644)

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"rclone.{shell}", shell)

    self.install_license("COPYING")
