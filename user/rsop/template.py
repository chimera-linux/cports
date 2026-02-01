pkgname = "rsop"
pkgver = "0.9.3"
pkgrel = 0
build_wrksrc = "rsop"
build_style = "cargo"
make_build_env = {"CLAP_ARTIFACTS": "clap_artifacts"}
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Stateless OpenPGP CLI tool backed by rpgp"
license = "MIT OR Apache-2.0"
url = "https://codeberg.org/heiko/rsop"
source = f"{url}/archive/rsop/v{pkgver}.tar.gz"
sha256 = "7740f608226a9003ac66dc8717db976b82c4976c4ab39fef13db87302415375c"


def post_install(self):
    self.install_completion("clap_artifacts/_rsop", "zsh")
    self.install_completion("clap_artifacts/rsop.bash", "bash")
    self.install_completion("clap_artifacts/rsop.fish", "fish")
    self.install_man("clap_artifacts/*.1", glob=True)
    self.install_license("../LICENSES/MIT.txt")
