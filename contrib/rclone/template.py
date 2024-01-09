pkgname = "rclone"
pkgver = "1.65.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Rsync for cloud storage"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://rclone.org"
source = f"https://github.com/rclone/rclone/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e16f7f6b81865c7f719d4b214ea45a0608ada71d9b9b6f65c6ead21128cbc8fe"
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
    self.ln_s("rclone", self.destdir / "usr/bin/mount.rclone")
    self.ln_s("rclone", self.destdir / "usr/bin/rclonefs")

    self.install_man("rclone.1")
    self.install_dir(f"usr/share/doc/{pkgname}")
    self.install_file("MANUAL.html", f"usr/share/doc/{pkgname}", 0o644)
    self.install_file("MANUAL.txt", f"usr/share/doc/{pkgname}", 0o644)

    self.install_completion("rclone.bash", "bash")
    self.install_completion("rclone.zsh", "zsh")
    self.install_completion("rclone.fish", "fish")

    self.install_license("COPYING")
