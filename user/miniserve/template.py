pkgname = "miniserve"
pkgver = "0.35.0"
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
sha256 = "6cccb1ac67fc07002bfb4fafd6b0a75c319279ed162b58a0bf20a4a931ddf5b7"
# generates completions and manpage with host binary
options = ["!cross"]


def post_build(self):
    from cbuild.util import cargo

    with open(self.cwd / "miniserve.1", "w") as outf:
        self.do(
            cargo.target_path(self, "miniserve"),
            "--print-manpage",
            stdout=outf,
        )

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"miniserve.{shell}", "w") as outf:
            self.do(
                cargo.target_path(self, "miniserve"),
                "--print-completions",
                shell,
                stdout=outf,
            )


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "miniserve"))
    self.install_license("LICENSE")
    self.install_man("miniserve.1")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"miniserve.{shell}", shell)
