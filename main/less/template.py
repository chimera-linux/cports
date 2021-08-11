pkgname = "less"
version = "581.2"
revision = 0
build_style = "gnu_configure"
configure_args = ["--with-regex=posix"]
makedepends = ["ncurses-devel"]
short_desc = "Pager program similar to more(1)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "less"
homepage = "http://www.greenwoodsoftware.com/less"
distfiles = [f"http://www.greenwoodsoftware.com/less/less-{version}.tar.gz"]
checksum = ["ce34b47caf20a99740672bf560fc48d5d663c5e78e67bc254e616b9537d5d83b"]
