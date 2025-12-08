pkgname = "haproxy-dataplaneapi"
pkgver = "3.2.6"
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
sha256 = "9ca69ce8c8722f94b2f3de2fa07ccfdccc80147ea3d61cabe24025b296b91b88"
