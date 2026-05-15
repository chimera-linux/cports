pkgname = "dua-cli"
pkgver = "2.34.0"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    "--skip=interactive::app::tests::unit::it_can_handle_ending_traversal_reaching_top_but_skipping_levels",
    "--skip=interactive::app::tests::unit::it_can_handle_ending_traversal_without_reaching_the_top",
]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "TUI disk usage analyzer"
license = "MIT"
url = "https://github.com/Byron/dua-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eaa924f50efb425302c124f170644e95a08f8dad1f627b86f50d033ca5feb0c1"
# Generates completions using host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"dua.{shell}", "w") as outf:
            self.do(
                f"./target/{self.profile().triplet}/release/dua",
                "completions",
                shell,
                stdout=outf,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"dua.{shell}", shell, "dua")
    self.install_license("LICENSE")
