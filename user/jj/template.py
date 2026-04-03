pkgname = "jj"
pkgver = "0.40.0"
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
sha256 = "ca45f2b866ce2fa25c7fc485e6b168cf055a39b1eab0ea170738c0b7e86d3b33"
# generates completions with host binary
options = ["!cross"]

if self.profile().arch in ["loongarch64"]:
    broken = "outdated nix crate, can't update"


def post_prepare(self):
    from cbuild.util import cargo, patch

    # done separately because we need to patch lockfile before vendoring :/
    patch.patch(self, [self.files_path / "bser.patch"])

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
