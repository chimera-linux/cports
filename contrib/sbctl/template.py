pkgname = "sbctl"
pkgver = "0.13"
pkgrel = 0
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

    # Generate bash completions
    with open(self.cwd / "sbctl.bash", "w") as cf:
        self.do(
            self.make_dir + "/sbctl",
            "completion",
            "bash",
            stdout=cf,
        )

    # Generate zsh completions
    with open(self.cwd / "sbctl.zsh", "w") as cf:
        self.do(
            self.make_dir + "/sbctl",
            "completion",
            "zsh",
            stdout=cf,
        )

    # Generate fish completions
    with open(self.cwd / "sbctl.fish", "w") as cf:
        self.do(
            self.make_dir + "/sbctl",
            "completion",
            "fish",
            stdout=cf,
        )


def post_install(self):
    self.install_man("docs/sbctl.8")

    self.install_completion("sbctl.bash", "bash")
    self.install_completion("sbctl.zsh", "zsh")
    self.install_completion("sbctl.fish", "fish")

    self.install_license("LICENSE")
