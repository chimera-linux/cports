pkgname = "arti"
pkgver = "2.7.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--features=full"]
hostmakedepends = [
    # cargo-auditable bites on tor-async-utils
    "cargo",
    "pkgconf",
]
makedepends = ["rust-std", "openssl3-devel", "sqlite-devel", "zstd-devel"]
pkgdesc = "Modular, reusable and easy to audit tor implementation in Rust"
license = "Apache-2.0 OR MIT"
url = "https://gitlab.torproject.org/tpo/core/arti"
source = (
    f"{url}/-/archive/{pkgname}-v{pkgver}/{pkgname}-{pkgname}-v{pkgver}.tar.bz2"
)
sha256 = "6373d2a3e6c74af148be1228ea41c66eace99c429c52e1c34edb2c7757e264de"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "arti"))

    self.install_file(
        "crates/arti/src/arti-example-config.toml", "usr/share/examples/arti"
    )

    with open(self.cwd / "NOTICE", "w") as fh:
        fh.write("""To comply with LGPL clause 4.a):
arti uses the hashx and equix Rust crates,
which are licensed under LGPL-3.0-only.""")
    # GPL is to fulfil LGPL clause 4.b), despite nothing in the dependency tree using the GPL
    for artifact in ["NOTICE", "GPL-3", "LGPL-3", "LICENSE-MIT"]:
        self.install_license(artifact)
