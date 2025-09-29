pkgname = "just"
pkgver = "1.43.0"
pkgrel = 0
build_style = "cargo"
# skip tests that fail when run outside of git repo
make_check_args = ["--", "--skip", "completions::bash"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
checkdepends = ["bash", "python"]
pkgdesc = "Save and run commands from justfile"
license = "CC0-1.0"
url = "https://github.com/casey/just"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "03904d6380344dbe10e25f04cd1677b441b439940257d3cc9d8c5f09d91e3065"
# generates completions and man page with host binary
options = ["!cross"]


def post_build(self):
    with open(self.cwd / "just.1", "w") as f:
        self.do(
            f"./target/{self.profile().triplet}/release/just",
            "--man",
            stdout=f,
        )


def post_install(self):
    self.install_man("just.1")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"completions/just.{shell}", shell)
    self.install_completion("completions/just.nu", "nushell")
