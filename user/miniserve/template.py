pkgname = "miniserve"
pkgver = "0.29.0"
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
    "openssl3-devel",
    "curl",  # test case: cant_navigate_up_the_root
]
pkgdesc = "CLI tool to serve files and dirs over HTTP"
maintainer = "sonata-chen <sonatachen39@gmail.com>"
license = "MIT"
url = "https://github.com/svenstaro/miniserve"
source = f"{url}/archive/refs/tags/v{pkgver}.zip"
sha256 = "e1b65231fe8eb94ecb46680173fa849be0fb64c07b0c9dc1e471cda1529b2e66"
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
