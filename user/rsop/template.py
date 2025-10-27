pkgname = "rsop"
pkgver = "0.10.0"
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
sha256 = "f79b119ac2d88b84301de3e248656153dbed4a5ab9478e0b456d874b64a8eed5"


def post_install(self):
    self.install_completion("clap_artifacts/_rsop", "zsh")
    self.install_completion("clap_artifacts/rsop.bash", "bash")
    self.install_completion("clap_artifacts/rsop.fish", "fish")
    self.install_man("clap_artifacts/*.1", glob=True)
    self.install_license("../LICENSES/MIT.txt")
