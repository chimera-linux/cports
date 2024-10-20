pkgname = "dinit"
pkgver = "0.19.1"
# temporary so we get our features
_gitrev = "f883bcb2eabe6c2646bc74647a3aeaece09a9875"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--syscontrolsocket=/run/dinitctl"]
configure_gen = []
make_dir = "."
make_check_args = ["check-igr"]  # additional target
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/archive/{_gitrev}.tar.gz"
sha256 = "1dd190e8fb906dfa80316365f0f6fac03113a134763b794fa625183ab8b74878"
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]
