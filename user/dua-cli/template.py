pkgname = "dua-cli"
pkgver = "2.31.0"
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
sha256 = "e338d61af692898560851894fae4f26ba1435700b8871ee008e6c5b48bd0e34c"


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
