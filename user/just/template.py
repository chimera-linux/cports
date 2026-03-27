pkgname = "just"
pkgver = "1.49.0"
pkgrel = 0
build_style = "cargo"
# skip tests that fail when run outside of git repo
make_check_args = ["--", "--skip", "completions::bash"]
make_check_env = {"XDG_RUNTIME_DIR": "/tmp"}
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
checkdepends = ["bash", "python"]
pkgdesc = "Save and run commands from justfile"
license = "CC0-1.0"
url = "https://github.com/casey/just"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "442406ee14eb9a59414525cf262354fe2e752b22c224ce2a5e42b2c493226e09"
# generates completions and man page with host binary
options = ["!cross"]


def post_build(self):
    with open(self.cwd / "just.1", "w") as f:
        self.do(
            f"./target/{self.profile().triplet}/release/just",
            "--man",
            stdout=f,
        )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/just")
    self.install_man("just.1")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"completions/just.{shell}", shell)
    self.install_completion("completions/just.nu", "nushell")
