pkgname = "haproxy-dataplaneapi"
pkgver = "3.3.5"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags="
    + f" -X main.GitTag={pkgver}"
    + " -X main.GitCommit="
    + " -X main.GitDirty= ",
    "./cmd/dataplaneapi",
]
hostmakedepends = ["go"]
pkgdesc = "HAProxy Data Plane API"
license = "Apache-2.0"
url = "https://github.com/haproxytech/dataplaneapi"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7e9d0a97571fba51969cd28efd1fcde28e3757457a62d3f2c6861659060a2877"
