pkgname = "miniserve"
pkgver = "0.31.0"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    "--test-threads=1",
    # These tests will run `script -qec`, which is not
    # compatible with chimerautils' script
    "--skip",
    "qrcode_shown_in_tty_when_enabled",
    "--skip",
    "qrcode_hidden_in_tty_when_disabled",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["zstd-devel"]
checkdepends = [
    "curl",  # test case: cant_navigate_up_the_root
    "openssl3-devel",
]
pkgdesc = "CLI tool to serve files and dirs over HTTP"
license = "MIT"
url = "https://github.com/svenstaro/miniserve"
source = f"{url}/archive/refs/tags/v{pkgver}.zip"
sha256 = "df6f4c8adc171c6dd5578264f540d09b47f254641c7d5a91733e3a046f99f25b"
# generates completions and manpage with host binary
options = ["!cross"]


def post_build(self):
    miniserve_exe = f"target/{self.profile().triplet}/release/miniserve"

    with open(self.cwd / "miniserve.1", "w") as outf:
        self.do(
            miniserve_exe,
            "--print-manpage",
            stdout=outf,
        )

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"miniserve.{shell}", "w") as outf:
            self.do(
                miniserve_exe,
                "--print-completions",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/miniserve")
    self.install_license("LICENSE")
    self.install_man("miniserve.1")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"miniserve.{shell}", shell)
