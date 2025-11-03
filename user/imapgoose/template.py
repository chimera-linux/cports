pkgname = "imapgoose"
pkgver = "0.2.3"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/imapgoose/"]
hostmakedepends = ["go"]
pkgdesc = "Sync maildir directories"
license = "ISC"
url = "https://git.sr.ht/~whynothugo/ImapGoose"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3cf6847596d931e91fd8a3008905946b7aeec91caf1bae0154b32c41052e36e8"


def post_install(self):
    self.install_license("LICENCE")
    self.install_man("imapgoose.1")
    self.install_man("imapgoose.conf.5")
