pkgname = "just"
pkgver = "1.42.4"
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
sha256 = "bd604ff72ecd8d8def79d39997499433e22fbffa03260e3a2c5fe5f84cc37f52"
# generates completions and man page with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        with open(self.cwd / f"just.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/just",
                "--completions",
                shell,
                stdout=f,
            )
    with open(self.cwd / "just.1", "w") as f:
        self.do(
            f"./target/{self.profile().triplet}/release/just",
            "--man",
            stdout=f,
        )


def post_install(self):
    self.install_man("just.1")
    for shell in ["bash", "fish", "zsh", "nushell"]:
        self.install_completion(f"just.{shell}", shell)
