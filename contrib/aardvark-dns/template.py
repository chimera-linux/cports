pkgname = "aardvark-dns"
pkgver = "1.7.0"
pkgrel = 0
build_style = "cargo"
# FIXME: https://github.com/containers/aardvark-dns/issues/379
make_check_args = [
    "--",
    "--skip=test::test::tests::test_backend_network_scoped_custom_dns_server",
]
hostmakedepends = ["cargo"]
makedepends = ["rust"]
pkgdesc = "Authoritative dns server for A/AAAA container records"
maintainer = "roastveg <louis@hamptonsoftworks.com>"
license = "Apache-2.0"
url = "https://github.com/containers/aardvark-dns"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6ee7dfa8bab8040b917959a2f57f25496ad036a2d933c6225114e2c1e68bab0b"
