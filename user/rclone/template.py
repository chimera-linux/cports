pkgname = "rclone"
pkgver = "1.72.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Rsync for cloud storage"
license = "MIT"
url = "https://rclone.org"
source = f"https://github.com/rclone/rclone/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5a2eccbc3519224377c0fbbf4469c6e8125c37616ac28cf3c3ec091ccfbbe0c5"
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
