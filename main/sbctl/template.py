pkgname = "sbctl"
pkgver = "0.15.4"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/sbctl"]
hostmakedepends = ["asciidoc", "go"]
checkdepends = ["openssl-devel"]
depends = [
    "llvm-binutils",  # required to generate EFI bundles
]
pkgdesc = "Secure Boot key manager"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://github.com/Foxboron/sbctl"
source = f"{url}/releases/download/{pkgver}/sbctl-{pkgver}.tar.gz"
sha256 = "0435097f79fc30c9b3567a50a8beb8d7d71fcea6121533b5da543ca64241cfff"
# fails
options = ["!cross"]

if self.profile().arch in ["ppc64", "ppc64le"]:
    # not supported by go-tpm-tools simulator
    options += ["!check"]


def post_build(self):
    self.do("make", "man")
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
