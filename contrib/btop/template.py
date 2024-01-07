pkgname = "btop"
pkgver = "1.3.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["OPTFLAGS="]
make_use_env = True
hostmakedepends = ["gmake"]
pkgdesc = "Monitor of resources"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "375e078ce2091969f0cd14030620bd1a94987451cf7a73859127a786006a32cf"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]
