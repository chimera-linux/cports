pkgname = "sbctl"
pkgver = "0.18"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/sbctl"]
hostmakedepends = ["asciidoc", "go", "pkgconf"]
makedepends = ["pcsc-lite-devel"]
checkdepends = ["openssl3-devel"]
depends = [
    "llvm-binutils",  # required to generate EFI bundles
]
pkgdesc = "Secure Boot key manager"
license = "MIT"
url = "https://github.com/Foxboron/sbctl"
source = f"{url}/releases/download/{pkgver}/sbctl-{pkgver}.tar.gz"
sha256 = "d274451b145b0aaecfdf2d01ad45473b61ab40f3f58e4735cee50aa7573c584d"
# fails
options = ["!cross"]

if self.profile().arch in ["loongarch64", "ppc64", "ppc64le"]:
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
    self.install_man("docs/sbctl.conf.5")

    self.install_completion("sbctl.bash", "bash")
    self.install_completion("sbctl.zsh", "zsh")
    self.install_completion("sbctl.fish", "fish")

    self.install_license("LICENSE")
