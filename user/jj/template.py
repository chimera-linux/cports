pkgname = "jj"
pkgver = "0.32.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
checkdepends = ["git", "openssh"]
pkgdesc = "Git-compatible VCS frontend"
license = "Apache-2.0"
url = "https://martinvonz.github.io/jj"
source = f"https://github.com/martinvonz/jj/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "12b8e65b7950b189d1df7e20cc55e20ff9cc2bd8d520847323b80daa1cddb27b"
# generates completions with host binary
options = ["!cross"]


def post_prepare(self):
    from cbuild.util import cargo, patch

    # done separately because we need to patch lockfile before vendoring :/
    patch.patch_git(self, [self.files_path / "bser.patch"])

    cargo.clear_vendor_checksums(self, "serde_bser")


def post_build(self):
    for shell in ["bash", "fish", "nushell", "zsh"]:
        with open(f"{self.cwd}/jj.{shell}", "w") as o:
            self.do(
                f"target/{self.profile().triplet}/release/jj",
                "util",
                "completion",
                shell,
                stdout=o,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/jj")
    self.do(
        f"target/{self.profile().triplet}/release/jj",
        "util",
        "install-man-pages",
        f"{self.chroot_destdir}/usr/share/man",
    )
    for shell in ["bash", "fish", "nushell", "zsh"]:
        self.install_completion(f"jj.{shell}", shell)
