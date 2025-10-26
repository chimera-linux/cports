pkgname = "haproxy-dataplaneapi"
pkgver = "3.2.4"
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
sha256 = "13a0ef16151837849f9fb91ad6ff869495688a40e627dbf82ffe31101fdbf110"
