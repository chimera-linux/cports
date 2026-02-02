pkgname = "rebar3"
pkgver = "3.26.0"
pkgrel = 0
makedepends = ["erlang"]
depends = ["erlang"]
pkgdesc = "Erlang build tool"
license = "Apache-2.0"
url = "https://github.com/erlang/rebar3"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a151dc4a07805490e9f217a099e597ac9774814875f55da2c66545c333fdff64"
# tests require network access
options = ["!check"]


def build(self):
    self.do("./bootstrap", "--offline")


def check(self):
    self.do("./rebar3", "ct")


def install(self):
    self.install_bin("rebar3")
    self.install_man("manpages/rebar3.1")
    self.install_completion(
        "apps/rebar/priv/shell-completion/bash/rebar3", "bash"
    )
    self.install_completion(
        "apps/rebar/priv/shell-completion/fish/rebar3.fish", "fish"
    )
    self.install_completion(
        "apps/rebar/priv/shell-completion/zsh/_rebar3", "zsh"
    )
