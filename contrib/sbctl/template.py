pkgname = "sbctl"
pkgver = "0.13"
pkgrel = 2
build_style = "go"
make_build_args = ["./cmd/sbctl"]
hostmakedepends = ["go", "asciidoc", "gmake"]
depends = [
    "llvm-binutils",  # required to generate EFI bundles
]
pkgdesc = "Secure Boot key manager"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://github.com/Foxboron/sbctl"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "efe855ea3de3dcaf5bc8974f724983fee0320a47094f6f4fd5f9e34cfa239456"
options = ["!cross"]


def post_build(self):
    # Generate man page, bmake doesn't work
    self.do("gmake", "man")
    # Generate completions
    for shell in ["bash", "zsh", "fish"]:
        with open(self.cwd / f"sbctl.{shell}", "w") as cf:
            self.do(
                f"{self.make_dir}/sbctl",
                "completion",
                shell,
                stdout=cf,
            )


def post_install(self):
    self.install_man("docs/sbctl.8")

    self.install_completion("sbctl.bash", "bash")
    self.install_completion("sbctl.zsh", "zsh")
    self.install_completion("sbctl.fish", "fish")

    self.install_license("LICENSE")
