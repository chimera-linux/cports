pkgname = "sbctl"
pkgver = "0.14"
pkgrel = 1
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
sha256 = "88ccdf3a87151c1b639be4e43999f4984f238eebffebe1d17d9f30e7039bf6e8"
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
