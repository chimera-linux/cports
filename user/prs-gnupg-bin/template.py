# Keep prs-gnupg-bin, prs-gpgme and prs-rpgpie in sync
pkgname = "prs-gnupg-bin"
pkgver = "0.5.7"
pkgrel = 0
build_wrksrc = "cli"
build_style = "cargo"
prepare_after_patch = True
make_build_args = [
    "--no-default-features",
    "--features="
    + ",".join(
        [
            "alias",
            "backend-gnupg-bin",
            "clipboard",
            "notify",
            "select-fzf-bin",
            "select-skim",
            "tomb",
            "totp",
        ]
    ),
]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["gnupg"]
pkgdesc = "Password manager CLI inspired by pass"
subdesc = "GnuPG binary backend"
license = "GPL-3.0-only"
url = "https://timvisee.com/projects/prs"
source = (
    f"https://gitlab.com/timvisee/prs/-/archive/v{pkgver}/prs-v{pkgver}.tar.gz"
)
sha256 = "0ad41003ab48a5309e3f2df0d6fe723babfe66007c980d3d0abf72c0a4d47f59"
# Host binary for completion generation
options = ["!cross"]

if self.profile().arch == "loongarch64":
    broken = "nix crate issues"


def post_build(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        with open(self.cwd / f"prs.{shell}", "w") as f:
            self.do(
                f"../target/{self.profile().triplet}/release/prs",
                "internal",
                "completions",
                shell,
                stdout=f,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        self.install_completion(f"prs.{shell}", shell, name="prs")
