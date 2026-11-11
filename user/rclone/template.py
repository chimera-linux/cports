pkgname = "rclone"
pkgver = "1.76.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Rsync for cloud storage"
license = "MIT"
url = "https://rclone.org"
source = f"https://github.com/rclone/rclone/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8cb7e5d576fe9a3aef8b1a0785e2ffc6c1953f8ed109f42000b0b86718f6628b"
hardening = []
# tests require network
options = ["!check", "!cross"]

match self.profile.arch:
    case "ppc64le" | "ppc64":
        # https://github.com/golang/go/issues/82324
        hardening += ["!pie"]


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
