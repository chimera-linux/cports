pkgname = "jj"
pkgver = "0.45.1"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
make_check_args = [
    "--",
    "--skip=test_converge::test_find_divergent_changes_two_found",
    "--skip=test_converge::test_find_divergent_changes_exactly_one_found",
]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
checkdepends = ["bash", "git", "openssh"]
pkgdesc = "Git-compatible VCS frontend"
license = "Apache-2.0"
url = "https://www.jj-vcs.dev"
source = f"https://github.com/martinvonz/jj/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "72bf95905a92c592dd0e7316e2cbbad9a8f2ca04ca770cc4f4f7960495a44e15"
# generates completions with host binary
options = ["!cross"]


def post_prepare(self):
    from cbuild.util import cargo, patch

    # done separately because we need to patch lockfile before vendoring :/
    patch.patch(self, [self.files_path / "bser.patch"])

    cargo.clear_vendor_checksums(self, "serde_bser-0.4.0")


def post_build(self):
    from cbuild.util import cargo

    for shell in ["bash", "fish", "nushell", "zsh"]:
        with open(f"{self.cwd}/jj.{shell}", "w") as o:
            self.do(
                cargo.target_path(self, "jj"),
                "util",
                "completion",
                shell,
                stdout=o,
            )


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "jj"))
    self.do(
        cargo.target_path(self, "jj"),
        "util",
        "install-man-pages",
        f"{self.chroot_destdir}/usr/share/man",
    )
    for shell in ["bash", "fish", "nushell", "zsh"]:
        self.install_completion(f"jj.{shell}", shell)
