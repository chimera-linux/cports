pkgname = "dua-cli"
pkgver = "2.46.0"
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
sha256 = "321e06440a8ba5dd05ecfd78904a127c9ffa556a40d886ab5862a9fe9aa9bd21"
# Generates completions using host binary
options = ["!cross"]


def post_build(self):
    from cbuild.util import cargo

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"dua.{shell}", "w") as outf:
            self.do(
                cargo.target_path(self, "dua"),
                "completions",
                shell,
                stdout=outf,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"dua.{shell}", shell, "dua")
    self.install_license("LICENSE")
