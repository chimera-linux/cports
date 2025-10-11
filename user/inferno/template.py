pkgname = "inferno"
pkgver = "0.12.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Stack trace visualizer"
license = "CDDL-1.0"
url = "https://github.com/jonhoo/inferno"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "46a04074f40bd51cbb0eac0761d28e84152e947372ce79f923974b52b75e3ec2"
# some tests need an actual git checkout of a submodule (not tarball) and i cbf
options = ["!check"]
