pkgname = "rclone"
pkgver = "1.67.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Rsync for cloud storage"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://rclone.org"
source = f"https://github.com/rclone/rclone/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4ecf2e99eb98c9bb678be5b0cd28550c4a2a2d63b5f2ed66962a4f4b9b36c402"
# tests require network
options = ["!check", "!cross"]


def post_build(self):
    self.do(
        self.chroot_cwd / "build/rclone",
        "genautocomplete",
        "bash",
        "rclone.bash",
    )
    self.do(
        self.chroot_cwd / "build/rclone",
        "genautocomplete",
        "zsh",
        "rclone.zsh",
    )
    self.do(
        self.chroot_cwd / "build/rclone",
        "genautocomplete",
        "fish",
        "rclone.fish",
    )


def do_install(self):
    self.install_bin("build/rclone")
    self.install_link("usr/bin/mount.rclone", "rclone")
    self.install_link("usr/bin/rclonefs", "rclone")

    self.install_man("rclone.1")
    self.install_dir(f"usr/share/doc/{pkgname}")
    self.install_file("MANUAL.html", f"usr/share/doc/{pkgname}", 0o644)
    self.install_file("MANUAL.txt", f"usr/share/doc/{pkgname}", 0o644)

    self.install_completion("rclone.bash", "bash")
    self.install_completion("rclone.zsh", "zsh")
    self.install_completion("rclone.fish", "fish")

    self.install_license("COPYING")
