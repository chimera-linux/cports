pkgname = "rclone"
pkgver = "1.69.3"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Rsync for cloud storage"
license = "MIT"
url = "https://rclone.org"
source = f"https://github.com/rclone/rclone/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ff6d17d187dd23648bfd33f20ff48902f7f08d2d9231f1f11825109903356b21"
# tests require network
options = ["!check", "!cross"]

if self.profile().arch in ["loongarch64"]:
    broken = "saferith@v0.33.0/arith_decl.go:...: missing function body"


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
